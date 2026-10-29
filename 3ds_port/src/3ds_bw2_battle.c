/* Optional BW2 presentation import. The game still owns battle rules,
 * controllers and actor sprites. Imported animation writes their existing tile
 * buffers, so BG copies, masks, affine effects and stereo/voxel composition use
 * the same pixels. Locally imported, validated scripts use a restricted VM.
 *
 * Binary assets are generated locally from the user's ROM; none are compiled
 * into this file. Native DS camera commands become waits on the fixed Emerald
 * camera. SPL has been projected to indexed frames by gen_bw2_battle.py.
 */
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include "global.h"
#include "battle.h"
#include "battle_anim.h"
#include "battle_gfx_sfx_util.h"
#include "data.h"
#include "main.h"
#include "palette.h"
#include "pokemon.h"
#include "pokedex.h"
#include "sound.h"
#include "sprite.h"
#include "constants/species.h"
#include "constants/moves.h"
#include "constants/songs.h"
#include "constants/rgb.h"
#include "3ds_data.h"
#include "3ds_platform.h"
#include "3ds_sprite_ids.h"
#include "3ds_bw2_battle.h"
#include "3ds_video.h"

/* Shared battle helper has no declaration in the upstream public header. */
u8 GetBattlerElevation(u8 battler, u16 species);

#define BW_TILE_BYTES 2048u
#define BW_CACHE_SIZE 14
#define BW_EFFECTS 4
#define BW_TAG 0xb200
#define BW_MAX_SCRIPT 4096u

typedef struct
{
    u8 *data;
    u32 frames, steps, loop, tick;
    const u16 *timeline;
    const u8 *tiles;
    bool8 tried;
    u8 left, top, right, bottom, floor;
    u16 centerY; // Q8, time-weighted center of opaque pixels in the idle cycle.
    u16 nativeWidth, nativeHeight, nativeFootprint; // Original bounds and shared front/back footprint, Q8.
    u8 *spots; // Sparse animated texture coordinates for procedural Spinda spots.
} BwClip;

typedef struct
{
    BwClip *clip;
    u32 id, tick;
    u16 species;
    bool8 shiny, paused;
} BwActor;

/* Separate from BwActor so capture tools retain its stable 16-byte ABI. */
typedef struct
{
    u16 scale; // Q8, visual size; OAM matrices contain its reciprocal.
    s16 x, y;
    u16 heightDm, targetSpan, sourceFactor; // Q8 correction, 256 without a hint.
} BwPresentation;

typedef struct
{
    BwClip *clip;
    u32 id, tick;
    u8 sprite;
    struct SpriteFrameImage image;
    struct SpriteTemplate template;
} BwEffect;

typedef struct
{
    u32 id;
    s16 x, y;
    u16 tick, duration, scaleTick, scaleDuration;
    s32 dx, dy, sx, sy;
    u8 affineMode, matrixNum, ownMatrix;
    bool8 affinePaused, used;
} BwMotion;

static BwClip sClips[BW_CACHE_SIZE];
static u16 sPokemonKeys[MAX_BATTLERS_COUNT];
static BwActor sActors[MAX_BATTLERS_COUNT];
/* Public diagnostic state; keep the established 16-byte actor/capture ABI. */
u32 gCtrBW2ActorPersonality[MAX_BATTLERS_COUNT];
u8 gCtrBW2ActorForms[MAX_BATTLERS_COUNT];
static u8 sSpindaMask[MAX_BATTLERS_COUNT][4096];
static BwPresentation sPresentation[MAX_BATTLERS_COUNT];
static BwEffect sEffects[BW_EFFECTS];
static BwMotion sMotion[MAX_BATTLERS_COUNT];
static u32 sEffectKeys[BW_CACHE_SIZE - MAX_BATTLERS_COUNT];
static u8 *sScript;
static u32 sScriptSize, sPC, sMoveTick;
static unsigned sCameraWait, sCryWait;
static u16 sMove, sSoundAt[8];
static u8 sAttacker, sTarget, sSoundCount;
static bool8 sRunning, sHadBattle;
static u16 sSavedPalette[PLTT_SIZE / 2];
static u8 sFade, sFadeGoal, sFadeWait, sFadeClock;

static const struct OamData sEffectOam = {
    .shape = SPRITE_SHAPE(64x64), .size = SPRITE_SIZE(64x64), .priority = 1
};

static u32 Read32(const void *ptr)
{
    u32 result;
    memcpy(&result, ptr, sizeof(result));
    return result;
}

static u16 Read16(const void *ptr)
{
    u16 result;
    memcpy(&result, ptr, sizeof(result));
    return result;
}

static bool8 SupportedSpecies(u16 species)
{
    /* Emerald's legacy Unown placeholders are not real species. Actual
     * Unown forms require a separate personality-based import. */
    return (species > SPECIES_NONE && species < 252)
        || (species >= SPECIES_TREECKO && species < NUM_SPECIES);
}

static bool8 HasActorAnimation(const BwActor *actor, const struct Sprite *sprite)
{
    /* Player backs share a table; opponents keep their species' front table.
     * Requiring only gAnims_MonPic leaves every imported front frozen. */
    return sprite->anims == gAnims_MonPic
        || sprite->anims == gMonFrontAnimsPtrTable[actor->species];
}

static unsigned ArgCount(unsigned opcode)
{
    switch (opcode)
    {
    case 0: case 42: return 5;
    case 6: case 56: case 58: return 1;
    case 7: case 9: return 11;
    case 18: case 21: case 67: return 7;
    case 26: return 2;
    case 52: return 9;
    case 59: return 4;
    case 77: return 0;
    default: return 255;
    }
}

static void MeasureClip(BwClip *clip)
{
    u8 floors[512];
    u16 counts[512] = {0};
    u32 sums[512] = {0};
    unsigned histogram[65] = {0};
    clip->left = clip->top = 64;
    for (unsigned f = 0; f < clip->frames; ++f)
    {
        unsigned bottom = 0;
        for (unsigned k = 0; k < BW_TILE_BYTES; ++k)
        {
            unsigned value = clip->tiles[f * BW_TILE_BYTES + k];
            if (!value) continue;
            unsigned x = (k / 32 % 8) * 8 + (k % 4) * 2;
            unsigned y = (k / 256) * 8 + k % 32 / 4;
            for (unsigned n = 0; n < 2; ++n)
            {
                if (!(value >> (n * 4) & 15)) continue;
                ++counts[f];
                sums[f] += y;
                if (x + n < clip->left) clip->left = x + n;
                if (x + n + 1 > clip->right) clip->right = x + n + 1;
                if (y < clip->top) clip->top = y;
                if (y + 1 > clip->bottom) clip->bottom = y + 1;
                if (y + 1 > bottom) bottom = y + 1;
            }
        }
        floors[f] = bottom;
    }
    /* A stable, time-weighted idle floor avoids chasing every bobbing frame
     * or anchoring an entire cycle to one unusually low tail/foot pose. */
    u32 count = 0, sumY = 0;
    for (unsigned t = clip->loop; t < clip->steps; ++t)
    {
        ++histogram[floors[clip->timeline[t]]];
        count += counts[clip->timeline[t]];
        sumY += sums[clip->timeline[t]];
    }
    clip->centerY = count ? (u16)((u64)sumY * 256 / count) : 32 * 256;
    unsigned sum = 0, middle = (clip->steps - clip->loop + 1) / 2;
    for (unsigned y = 0; y <= 64; ++y)
        if ((sum += histogram[y]) >= middle) { clip->floor = y; break; }
}

static unsigned SourceSizeFactor(const BwClip *clip, u16 heightDm)
{
    if (!clip->nativeWidth || !clip->nativeHeight || heightDm >= 40)
        return 256;
    /* Retain the source artist's relative footprint, lost when every clip
     * was fitted to 64x64. Geometric mean avoids treating a long tail/leaf
     * as if the entire body occupied the longest side of its bounding box.
     * The reference is a presentation calibration, not a physical law. */
    unsigned reference = 40 + 3u * heightDm;
    if (reference > 70) reference = 70;
    unsigned footprint = clip->nativeFootprint ? clip->nativeFootprint
        : (unsigned)(sqrtf((float)clip->nativeWidth * clip->nativeHeight) * 256);
    unsigned factor = footprint / reference;
    /* Preserve established sizes when source proportions are already close.
     * A correction is fixed for a clip, never recalculated for each pose. */
    if (factor >= 218 && factor <= 294) return 256;
    if (factor < 205) factor = 205;
    if (factor > 320) factor = 320;
    /* DS art compresses very large species to fit its screen; for giants
     * the bounded Pokedex curve is a better guide than native pixel size. */
    if (heightDm > 20)
        factor = 256 + ((int)factor - 256) * (40 - heightDm) / 20;
    return factor;
}

static BwPresentation PresentationFor(const BwClip *clip, u16 heightDm, bool8 back,
                                      int ground, int nativeCenter)
{
    /* Saturating size curve: meters remain perceptible without a linear
     * ten-meter monster filling the display. Use the whole silhouette's
     * largest extent so long tails/wings also fit, preserving aspect ratio. */
    unsigned target = 36 + 76u * heightDm / (heightDm + 10u);
    if (target > 88) target = 88;
    if (back)
    {
        /* Increase perspective gradually above the small-Pokemon reference.
         * The lower body may sit behind the text, so do not fit its full
         * height into the strip above the message box. */
        unsigned boost = heightDm > 5 ? (heightDm - 5) * 5u : 0;
        unsigned perspective = 130 + (boost > 20 ? 20 : boost);
        target = target * perspective / 100;
        if (target > 112) target = 112;
    }
    unsigned sourceFactor = SourceSizeFactor(clip, heightDm);
    target = target * sourceFactor / 256;
    unsigned limit = back ? 126 : 104;
    if (target > limit) target = limit;
    unsigned w = clip->right > clip->left ? clip->right - clip->left : 1;
    unsigned h = clip->bottom > clip->top ? clip->bottom - clip->top : 1;
    unsigned scale = target * 256 / (w > h ? w : h);
    /* A 64x64 OBJ has a 128x128 affine envelope. Source-driven enlargement
     * may use its transparent padding, but opaque pixels must still fit.
     * Reserve two pixels for reciprocal-matrix rounding. */
    unsigned maxScale = 512;
    if (sourceFactor > 256)
    {
        int radius = abs(32 - (int)clip->left);
        int edges[] = {abs((int)clip->right - 32), abs(32 - (int)clip->top), abs((int)clip->bottom - 32)};
        for (unsigned i = 0; i < ARRAY_COUNT(edges); ++i)
            if (edges[i] > radius) radius = edges[i];
        maxScale = radius ? 126u * 256 / (2 * radius) : 546;
        if (maxScale > 546) maxScale = 546;
    }
    if (scale > maxScale) scale = maxScale;
    if (!back && clip->floor > clip->top)
    {
        /* The scene maps GBA line 112 to screen line GAME_HEIGHT-48.
         * Keep the highest source pose four logical pixels inside the view,
         * including species elevation, without changing its arena floor. */
        float headroom = ground + (CTR_GAME_HEIGHT - 48) / CTR_BATTLE_ZOOM - 116.0f;
        if (headroom > 0)
        {
            unsigned fit = (unsigned)(headroom * 256 / (clip->floor - clip->top));
            if (scale > fit) scale = fit;
        }
    }
    if (scale < 128) scale = 128;
    /* Center the visible body on the arena. Time-weighted pixel mass avoids
     * a long leaf/tail or one extreme pose pulling its bounding-box center.
     * Placement stays fixed through the cycle; the text may cover the body. */
    int anchor = back ? clip->centerY : 256 * clip->floor;
    return (BwPresentation){scale,
        (64 - (int)clip->left - clip->right) * (int)scale / 512,
        ground - nativeCenter - (anchor - 32 * 256) * (int)scale / 65536,
        heightDm, target, sourceFactor};
}

static void LoadNativeLayout(BwClip *clip, const char *path)
{
    char layoutPath[80];
    u32 size;
    snprintf(layoutPath, sizeof(layoutPath), "%s.layout", path);
    if (!CtrData_Size(layoutPath, &size) || size != 12) return;
    u8 *data = CtrData_Load(layoutPath, &size);
    if (!data) return;
    if (size == 12 && memcmp(data, "BWL2", 4) == 0)
    {
        unsigned w = Read16(data + 4), h = Read16(data + 6);
        unsigned otherW = Read16(data + 8), otherH = Read16(data + 10);
        if (w && h && w <= 192 && h <= 192 && otherW && otherH && otherW <= 192 && otherH <= 192)
        {
            clip->nativeWidth = w;
            clip->nativeHeight = h;
            /* One species-wide correction prevents the two camera angles
             * from acquiring different relative proportions. */
            clip->nativeFootprint = (u16)(sqrtf(sqrtf((float)w * h * otherW * otherH)) * 256);
        }
    }
    free(data);
}

static bool8 LoadSpindaMap(BwClip *clip, const char *path)
{
    char name[80];
    u32 size;
    snprintf(name, sizeof(name), "%s.spots", path);
    if (!CtrData_Size(name, &size)) return TRUE;
    if (size < 156 || size > 4 * 1024 * 1024) return FALSE;
    u8 *data = CtrData_Load(name, &size);
    bool8 valid = data && !memcmp(data, "BWS1", 4) && Read32(data + 4) == clip->frames;
    u32 start = 152 + 4 * (clip->frames + 1);
    if (size < start) valid = FALSE;
    for (unsigned i = 0; valid && i <= clip->frames; ++i)
    {
        u32 off = Read32(data + 152 + i * 4);
        if (off < start || off > size || (off - start) % 4
            || (!i && off != start) || (i && off < Read32(data + 148 + i * 4))) valid = FALSE;
    }
    if (valid && Read32(data + 152 + clip->frames * 4) != size) valid = FALSE;
    for (unsigned i = start; valid && i < size; i += 4)
        if (Read16(data + i) >= 4096 || Read16(data + i + 2) >= 32768) valid = FALSE;
    for (unsigned i = 0; valid && i < 4; ++i)
        if (data[8 + i * 36] < 8 || data[9 + i * 36] < 8 - (i == 0)
            || data[8 + i * 36] > 224 || data[9 + i * 36] > 64) valid = FALSE;
    if (!valid) { free(data); return FALSE; }
    clip->spots = data;
    return TRUE;
}

static void SpindaMask(unsigned battler, const BwClip *clip, u32 personality)
{
    u8 *mask = sSpindaMask[battler];
    memset(mask, 0, 4096);
    for (unsigned i = 0; i < 4; ++i, personality >>= 8)
    {
        const u8 *shape = clip->spots + 8 + i * 36;
        int ox = shape[0] + (int)(personality & 15) - 8;
        int oy = shape[1] + (int)(personality >> 4 & 15) - 8;
        for (unsigned y = 0; y < 16; ++y)
        {
            unsigned row = Read16(shape + 4 + y * 2);
            for (unsigned x = 0; x < 16; ++x)
                if (row & (1u << x))
                    for (unsigned pose = 0; pose < 2; ++pose)
                    {
                        int px = ox + (int)x, py = oy + (int)y;
                        if (px < 0 || px >= 256 || py < 0 || py >= 88) continue;
                        unsigned uv = (py + pose * 40) * 256 + px;
                        mask[uv / 8] |= 1u << (uv % 8);
                    }
        }
    }
}

static BwClip *LoadClip(unsigned slot, const char *path)
{
    BwClip *clip = &sClips[slot];
    u32 size;
    if (clip->tried)
        return clip->data ? clip : NULL;
    clip->tried = TRUE;
    if (!CtrData_Size(path, &size) || size < 96 || size > 2 * 1024 * 1024)
        return NULL;
    clip->data = CtrData_Load(path, &size);
    if (clip->data)
    {
        const u8 *data = clip->data;
        u32 frames = Read32(data + 4), steps = Read32(data + 8);
        u32 offset = 92 + ((steps * 2 + 3) & ~3u);
        bool8 valid = memcmp(data, "BWA1", 4) == 0 && frames && frames <= 512
            && steps && steps <= 1024 && Read32(data + 12) < steps
            && Read32(data + 16) == 64 && Read32(data + 20) == 64
            && Read32(data + 24) == 60 && size == offset + frames * BW_TILE_BYTES;
        for (u32 i = 0; valid && i < steps; ++i)
            if (Read16(data + 92 + i * 2) >= frames)
                valid = FALSE;
        if (valid)
        {
            clip->frames = frames;
            clip->steps = steps;
            clip->loop = Read32(data + 12);
            clip->timeline = (const u16 *)(data + 92);
            clip->tiles = data + offset;
            MeasureClip(clip);
            if (slot < MAX_BATTLERS_COUNT)
            {
                LoadNativeLayout(clip, path);
                if (!LoadSpindaMap(clip, path))
                {
                    free(clip->data); memset(clip, 0, sizeof(*clip)); clip->tried = TRUE;
                    return NULL;
                }
            }
            return clip;
        }
        free(clip->data);
        clip->data = NULL;
        CtrLog_Write(CTR_LOG_GAME, "BW2 invalid clip: %s", path);
    }
    return NULL;
}

static BwClip *PokemonFormClip(u16 species, bool8 back, unsigned form)
{
    char path[64];
    if (!SupportedSpecies(species))
        return NULL;
    if (form > 3 || (form && species != SPECIES_CASTFORM
        && !(species == SPECIES_DEOXYS && form == 3))) return NULL;
    if (form) snprintf(path, sizeof(path), "bw2/%u_form%u_%s.bin", species, form, back ? "back" : "front");
    else snprintf(path, sizeof(path), "bw2/%u_%s.bin", species, back ? "back" : "front");
    u16 key = species * 2 + (back ? 1 : 0) + form * 1024;
    for (unsigned slot = 0; slot < MAX_BATTLERS_COUNT; ++slot)
        if (sPokemonKeys[slot] == key)
            return LoadClip(slot, path);
    for (unsigned slot = 0; slot < MAX_BATTLERS_COUNT; ++slot)
    {
        bool8 used = FALSE;
        for (unsigned b = 0; b < MAX_BATTLERS_COUNT; ++b)
            if (sActors[b].clip == &sClips[slot]) used = TRUE;
        if (used) continue;
        /* A switch can reuse the outgoing actor's slot. Never retain the
         * whole national dex, or evict a clip another battler still owns. */
        free(sClips[slot].data);
        free(sClips[slot].spots);
        memset(&sClips[slot], 0, sizeof(sClips[slot]));
        sPokemonKeys[slot] = key;
        return LoadClip(slot, path);
    }
    return NULL;
}

static BwClip *PokemonClip(u16 species, bool8 back)
{
    return PokemonFormClip(species, back, 0);
}

static BwClip *EffectClip(unsigned file, unsigned emitter)
{
    char path[64];
    if (file > 65535 || emitter > 65535) return NULL;
    u32 key = file << 16 | emitter;
    snprintf(path, sizeof(path), "bw2/effect_%u_%u.bin", file, emitter);
    for (unsigned i = MAX_BATTLERS_COUNT; i < BW_CACHE_SIZE; ++i)
        if (sClips[i].tried && sEffectKeys[i - MAX_BATTLERS_COUNT] == key)
            return LoadClip(i, path);
    for (unsigned i = MAX_BATTLERS_COUNT; i < BW_CACHE_SIZE; ++i)
        if (!sClips[i].tried)
        {
            sEffectKeys[i - MAX_BATTLERS_COUNT] = key;
            return LoadClip(i, path);
        }
    return NULL;
}

static void ResetEffectClips(void)
{
    /* No effects are alive when preparing the next move. Keep only its
     * validated dependencies, bounded to ten clips and four live emitters. */
    for (unsigned i = MAX_BATTLERS_COUNT; i < BW_CACHE_SIZE; ++i)
    {
        free(sClips[i].data);
        memset(&sClips[i], 0, sizeof(sClips[i]));
    }
    memset(sEffectKeys, 0, sizeof(sEffectKeys));
}

static const u8 *Frame(BwClip *clip, unsigned tick, bool8 loop)
{
    if (tick >= clip->steps)
        tick = loop ? clip->loop + (tick - clip->loop) % (clip->steps - clip->loop) : clip->steps - 1;
    return clip->tiles + clip->timeline[tick] * BW_TILE_BYTES;
}

static void ActorPixels(unsigned battler)
{
    BwActor *actor = &sActors[battler];
    unsigned position = GetBattlerPosition(battler);
    const u8 *frame = Frame(actor->clip, actor->tick, TRUE);
    u8 patterned[BW_TILE_BYTES];
    if (actor->clip->spots)
    {
        memcpy(patterned, frame, BW_TILE_BYTES);
        unsigned index = (frame - actor->clip->tiles) / BW_TILE_BYTES;
        const u8 *map = actor->clip->spots;
        unsigned end = Read32(map + 156 + index * 4);
        for (unsigned at = Read32(map + 152 + index * 4); at < end; at += 4)
        {
            unsigned pixel = Read16(map + at), uv = Read16(map + at + 2);
            if (!(sSpindaMask[battler][uv / 8] & (1u << (uv % 8)))) continue;
            unsigned shift = (pixel & 1) * 4;
            unsigned color = patterned[pixel / 2] >> shift & 15;
            if (color >= 1 && color <= 3) patterned[pixel / 2] += 5u << shift;
        }
        frame = patterned;
    }
    for (unsigned i = 0; i < 4; ++i)
        memcpy(gMonSpritesGfxPtr->sprites.byte[position] + i * BW_TILE_BYTES, frame, BW_TILE_BYTES);
}

static int ActorDrop(unsigned battler)
{
    return sActors[battler].clip ? sPresentation[battler].y : 0;
}

/* Emerald uses Speed for its own untransformed rear sprite. The opponent,
 * transformed copies and the remote multi-battle partner use Normal.
 * Attack and Defense belong to other games and do not change Emerald rules. */
static unsigned SelectedPokemonForm(u16 species, u8 battler, bool8 back, u16 transformed)
{
    if (species == SPECIES_CASTFORM) return gBattleMonForms[battler];
    if (species != SPECIES_DEOXYS) return 0;
#ifdef CTR_BW2_VALIDATION
    /* Explicit art inventory preview only; absent from production. Ordinary
     * encounters and Transform evidence leave this diagnostic at zero. */
    extern volatile u32 gCtrBw2DeoxysPreview;
    if (gCtrBw2DeoxysPreview) return gCtrBw2DeoxysPreview == 2 ? 3 : 0;
#endif
    return back && transformed == SPECIES_NONE && !ShouldIgnoreDeoxysForm(1, battler) ? 3 : 0;
}

static void RegisterPokemon(struct Pokemon *mon, u8 battler, bool8 back)
{
    BwActor *actor = &sActors[battler];
    u16 species = GetMonData(mon, MON_DATA_SPECIES);
    u16 transformed = gBattleSpritesDataPtr->battlerData[battler].transformSpecies;
    BwClip *clip;
    memset(actor, 0, sizeof(*actor));
    if (transformed != SPECIES_NONE)
        species = transformed;
    unsigned form = SelectedPokemonForm(species, battler, back, transformed);
    clip = form ? PokemonFormClip(species, back, form) : PokemonClip(species, back);
    if (!clip || !gMonSpritesGfxPtr || (species == SPECIES_SPINDA && !back && !clip->spots))
        return;
    actor->species = species;
    gCtrBW2ActorForms[battler] = form;
    actor->clip = clip;
    actor->shiny = IsMonShiny(mon);
    gCtrBW2ActorPersonality[battler] = transformed != SPECIES_NONE ? gTransformedPersonalities[battler]
        : GetMonData(mon, MON_DATA_PERSONALITY);
    if (clip->spots) SpindaMask(battler, clip, gCtrBW2ActorPersonality[battler]);
    u16 height = GetPokedexHeightWeight(SpeciesToNationalPokedexNum(species), 0);
    /* The visible rear arena is centered eight pixels above its lower rim. */
    int ground = GetBattlerSpriteCoord(battler, BATTLER_COORD_Y) + (back ? 24 : 32)
        - GetBattlerElevation(battler, species);
    sPresentation[battler] = PresentationFor(clip, height, back, ground,
        GetBattlerSpriteDefault_Y(battler));
    ActorPixels(battler);
    const void *pal = clip->data + 28 + (actor->shiny ? 32 : 0);
    LoadPalette(pal, OBJ_PLTT_ID(battler), 32);
    LoadPalette(pal, BG_PLTT_ID(8) + BG_PLTT_ID(battler), 32);
    CtrLog_Write(CTR_LOG_GAME, "BW2 actor %u species %u %s, %lu ticks", battler, species,
                 back ? "back" : "front", (unsigned long)clip->steps);
    CtrLog_Write(CTR_LOG_GAME, "BW2 layout %u: height %u dm, scale %u/256, shift %d,%d, target %u, bounds %u,%u,%u,%u floor %u",
        battler, height, sPresentation[battler].scale, sPresentation[battler].x,
        sPresentation[battler].y, sPresentation[battler].targetSpan,
        clip->left, clip->top, clip->right, clip->bottom, clip->floor);
}

void __real_BattleLoadOpponentMonSpriteGfx(struct Pokemon *mon, u8 battler);
void __wrap_BattleLoadOpponentMonSpriteGfx(struct Pokemon *mon, u8 battler)
{
    __real_BattleLoadOpponentMonSpriteGfx(mon, battler);
    RegisterPokemon(mon, battler, FALSE);
}

void __real_BattleLoadPlayerMonSpriteGfx(struct Pokemon *mon, u8 battler);
void __wrap_BattleLoadPlayerMonSpriteGfx(struct Pokemon *mon, u8 battler)
{
    __real_BattleLoadPlayerMonSpriteGfx(mon, battler);
    RegisterPokemon(mon, battler, TRUE);
}

/* The two loaders also have calls inside battle_gfx_sfx_util.c, which GNU
 * --wrap cannot intercept. Restore registration after the outer operation. */
void __real_BattleLoadSubstituteOrMonSpriteGfx(u8 battler, bool8 loadMon);
void __wrap_BattleLoadSubstituteOrMonSpriteGfx(u8 battler, bool8 loadMon)
{
    __real_BattleLoadSubstituteOrMonSpriteGfx(battler, loadMon);
    if (loadMon)
    {
        bool8 back = GetBattlerSide(battler) == B_SIDE_PLAYER;
        RegisterPokemon(back ? &gPlayerParty[gBattlerPartyIndexes[battler]]
                             : &gEnemyParty[gBattlerPartyIndexes[battler]], battler, back);
    }
    else
    {
        sActors[battler].clip = NULL;
    }
}

void __real_LoadBattleMonGfxAndAnimate(u8 battler, bool8 loadMon, u8 spriteId);
void __wrap_LoadBattleMonGfxAndAnimate(u8 battler, bool8 loadMon, u8 spriteId)
{
    __real_LoadBattleMonGfxAndAnimate(battler, loadMon, spriteId);
    if (loadMon)
    {
        bool8 back = GetBattlerSide(battler) == B_SIDE_PLAYER;
        RegisterPokemon(back ? &gPlayerParty[gBattlerPartyIndexes[battler]]
                             : &gEnemyParty[gBattlerPartyIndexes[battler]], battler, back);
    }
    else
    {
        sActors[battler].clip = NULL;
    }
}

static void KillEffect(unsigned index)
{
    BwEffect *effect = &sEffects[index];
    if (!effect->clip)
        return;
    if (effect->sprite < MAX_SPRITES && CtrSprites_Id(effect->sprite) == effect->id)
        DestroySprite(&gSprites[effect->sprite]);
    FreeSpritePaletteByTag(BW_TAG + index);
    memset(effect, 0, sizeof(*effect));
}

static unsigned BattlerForCode(s32 code)
{
    return code == 9 || code == 14 ? sAttacker : sTarget;
}

static void Emit(const s32 *args)
{
    BwClip *clip = EffectClip(args[0], args[1]);
    unsigned b = BattlerForCode(args[2]);
    if (!clip || b >= gBattlersCount)
        return;
    for (unsigned i = 0; i < BW_EFFECTS; ++i)
        if (!sEffects[i].clip)
        {
            BwEffect *effect = &sEffects[i];
            struct SpritePalette palette = { (const u16 *)(clip->data + 28), BW_TAG + i };
            int facing = GetBattlerSide(b) == B_SIDE_PLAYER ? 1 : -1;
            int x = GetBattlerSpriteCoord(b, BATTLER_COORD_X_2)
                + (sActors[b].clip ? sPresentation[b].x : 0) + facing * args[4] * 8 / 4096;
            int y = GetBattlerSpriteDefault_Y(b) + ActorDrop(b)
                - args[5] * 8 / 4096;
            if (LoadSpritePalette(&palette) == 0xff)
                return;
            effect->image.data = Frame(clip, 0, FALSE);
            effect->image.size = BW_TILE_BYTES;
            effect->template = (struct SpriteTemplate) {
                TAG_NONE, BW_TAG + i, &sEffectOam, gDummySpriteAnimTable,
                &effect->image, gDummySpriteAffineAnimTable, SpriteCallbackDummy
            };
            effect->sprite = CreateSprite(&effect->template, x, y, 0);
            if (effect->sprite >= MAX_SPRITES)
            {
                FreeSpritePaletteByTag(BW_TAG + i);
                return;
            }
            effect->id = CtrSprites_Id(effect->sprite);
            effect->clip = clip;
            effect->tick = 0;
            gSprites[effect->sprite].oam.priority = 0;
            return;
        }
}

static BwMotion *Motion(unsigned b)
{
    unsigned id = gBattlerSpriteIds[b];
    BwMotion *motion = &sMotion[b];
    if (id >= MAX_SPRITES || !gSprites[id].inUse)
        return NULL;
    if (!motion->used)
    {
        struct Sprite *sprite = &gSprites[id];
        motion->id = CtrSprites_Id(id);
        motion->x = sprite->x2;
        motion->y = sprite->y2;
        motion->affineMode = sprite->oam.affineMode;
        motion->matrixNum = sprite->oam.matrixNum;
        motion->affinePaused = sprite->affineAnimPaused;
        motion->ownMatrix = 0xff;
        motion->used = TRUE;
    }
    return motion;
}

static void RestoreMotion(unsigned b)
{
    BwMotion *motion = &sMotion[b];
    unsigned id = gBattlerSpriteIds[b];
    if (motion->used)
    {
        if (id < MAX_SPRITES && CtrSprites_Id(id) == motion->id)
        {
            struct Sprite *sprite = &gSprites[id];
            sprite->x2 = motion->x;
            sprite->y2 = motion->y;
            sprite->oam.affineMode = motion->affineMode;
            sprite->oam.matrixNum = motion->matrixNum;
            sprite->affineAnimPaused = motion->affinePaused;
        }
        if (motion->ownMatrix != 0xff)
            FreeOamMatrix(motion->ownMatrix);
        memset(motion, 0, sizeof(*motion));
    }
}

static void FinishMove(void)
{
    for (unsigned i = 0; i < BW_EFFECTS; ++i)
        KillEffect(i);
    for (unsigned b = 0; b < MAX_BATTLERS_COUNT; ++b)
    {
        RestoreMotion(b);
        sActors[b].paused = FALSE;
    }
    memcpy(gPlttBufferFaded, sSavedPalette, sizeof(sSavedPalette));
    sRunning = FALSE;
    gAnimScriptActive = FALSE;
    free(sScript);
    sScript = NULL;
    CtrLog_Write(CTR_LOG_GAME, "BW2 move %u finished at tick %lu", sMove, (unsigned long)sMoveTick);
}

static bool8 Busy(void)
{
    if (sCameraWait || sCryWait || sFade != sFadeGoal)
        return TRUE;
    for (unsigned i = 0; i < BW_EFFECTS; ++i)
        if (sEffects[i].clip)
            return TRUE;
    for (unsigned i = 0; i < MAX_BATTLERS_COUNT; ++i)
        if (sMotion[i].duration || sMotion[i].scaleDuration)
            return TRUE;
    return FALSE;
}

static void PlayMoveSound(void)
{
    u16 sound = sMove == MOVE_POUND ? SE_M_DOUBLE_SLAP : sMove == MOVE_TACKLE ? SE_M_COMET_PUNCH
        : sMove == MOVE_SCRATCH ? SE_M_SCRATCH : sMove == MOVE_LEER ? SE_M_LEER : SE_M_UPROAR;
    PlaySE12WithPanning(sound, GetBattlerSide(sAttacker) == B_SIDE_PLAYER ? -40 : 40);
}

static void AdvanceMove(void)
{
    ++sMoveTick;
    if (sCameraWait) --sCameraWait;
    if (sCryWait) --sCryWait;
    if (sFade != sFadeGoal && ++sFadeClock > sFadeWait)
    {
        sFadeClock = 0;
        sFade += sFade < sFadeGoal ? 1 : -1;
        BlendPalettes(0xffffffff, sFade, RGB_BLACK);
    }
    for (unsigned i = 0; i < sSoundCount; ++i)
        if (sSoundAt[i] && sMoveTick >= sSoundAt[i])
        {
            PlayMoveSound();
            sSoundAt[i] = 0;
        }
    for (unsigned b = 0; b < gBattlersCount; ++b)
    {
        BwMotion *m = &sMotion[b];
        unsigned id = gBattlerSpriteIds[b];
        if (!m->used || id >= MAX_SPRITES || CtrSprites_Id(id) != m->id)
            continue;
        struct Sprite *sprite = &gSprites[id];
        if (m->duration)
        {
            float phase = sinf(6.2831853f * ++m->tick / m->duration);
            int sign = GetBattlerSide(b) == B_SIDE_PLAYER ? 1 : -1;
            sprite->x2 = m->x + (int)(sign * m->dx * phase * 8 / 4096);
            sprite->y2 = m->y - (int)(m->dy * phase * 8 / 4096);
            if (m->tick >= m->duration)
            {
                m->duration = 0;
                sprite->x2 = m->x;
                sprite->y2 = m->y;
            }
        }
        if (m->scaleDuration && m->ownMatrix != 0xff)
        {
            float phase = sinf(6.2831853f * ++m->scaleTick / m->scaleDuration);
            int sx = (int)(256 / (1 + m->sx * phase / 4096));
            int sy = (int)(256 / (1 + m->sy * phase / 4096));
            SetOamMatrix(m->ownMatrix, sx, 0, 0, sy);
            if (m->scaleTick >= m->scaleDuration)
            {
                m->scaleDuration = 0;
                SetOamMatrix(m->ownMatrix, 256, 0, 0, 256);
            }
        }
    }
}

static void MoveCallback(void)
{
    if (!sRunning)
        return;
    AdvanceMove();
    if (sMoveTick > 600)
    {
        CtrLog_Write(CTR_LOG_ERROR, "BW2 move watchdog %u", sMove);
        FinishMove();
        return;
    }
    /* Wait instructions rewind until the effects they started have ended. */
    for (unsigned budget = 0; budget < 64; ++budget)
    {
        u32 start = sPC;
        unsigned op = Read16(sScript + sPC), count = ArgCount(op);
        s32 a[11] = {0};
        sPC += 2;
        for (unsigned i = 0; i < count; ++i, sPC += 4)
            a[i] = (s32)Read32(sScript + sPC);
        switch (op)
        {
        case 0: sCameraWait = a[2]; break;
        case 6: break; /* Preloaded before changing any game state. */
        case 7: case 9: Emit(a); break;
        case 18: case 21:
        {
            unsigned b = BattlerForCode(a[0]);
            BwMotion *m = Motion(b);
            if (!m) break;
            unsigned duration = a[4] * (a[5] + 1) * 2 * a[6];
            if (op == 18)
            {
                m->dx = a[2]; m->dy = a[3]; m->tick = 0;
                m->duration = duration;
            }
            else
            {
                if (m->ownMatrix == 0xff) m->ownMatrix = AllocOamMatrix();
                if (m->ownMatrix == 0xff) break;
                struct Sprite *sprite = &gSprites[gBattlerSpriteIds[b]];
                sprite->oam.affineMode = ST_OAM_AFFINE_NORMAL;
                sprite->oam.matrixNum = m->ownMatrix;
                sprite->affineAnimPaused = TRUE;
                m->sx = a[2]; m->sy = a[3]; m->scaleTick = 0;
                m->scaleDuration = duration;
            }
            break;
        }
        case 26: sActors[BattlerForCode(a[0])].paused = a[1] != 0; break;
        case 42:
            sFade = a[1]; sFadeGoal = a[2]; sFadeWait = a[3]; sFadeClock = 0;
            BlendPalettes(0xffffffff, sFade, RGB_BLACK);
            break;
        case 52:
            if (a[3] == 0) PlayMoveSound();
            else if (sSoundCount < ARRAY_COUNT(sSoundAt)) sSoundAt[sSoundCount++] = sMoveTick + a[3];
            break;
        case 56:
            if (Busy()) sPC = start;
            return;
        case 58: if (a[0]) return; break;
        case 59:
            if ((GetBattlerSide(sAttacker) != B_SIDE_PLAYER) == a[2]) sPC += a[3];
            break;
        case 67:
            PlayCry_Normal(gBattleMons[sAttacker].species, GetBattlerSide(sAttacker) == B_SIDE_PLAYER ? -40 : 40);
            sCryWait = a[3];
            break;
        case 77: FinishMove(); return;
        default: FinishMove(); return;
        }
    }
    FinishMove();
}

static bool8 PrepareMove(u16 move)
{
    char path[64];
    u32 size;
    if (move == 0 || move >= MOVES_COUNT)
        return FALSE;
    if (!sActors[gBattlerAttacker].clip || gBattleTypeFlags & BATTLE_TYPE_LINK)
        return FALSE;
    snprintf(path, sizeof(path), "bw2/move_%u.bin", move);
    if (!CtrData_Size(path, &size) || size < 62 || size > BW_MAX_SCRIPT)
        return FALSE;
    u8 *data = CtrData_Load(path, &size);
    if (!data) return FALSE;
    ResetEffectClips();
    bool8 valid = Read32(data) == 1 && Read32(data + 4) == 60;
    bool8 ended = FALSE;
    bool8 starts[BW_MAX_SCRIPT] = {0};
    for (u32 pc = 60; valid && pc + 2 <= size; )
    {
        unsigned op = Read16(data + pc), count = ArgCount(op);
        starts[pc] = TRUE;
        if (count == 255 || pc + 2 + count * 4 > size) { valid = FALSE; break; }
        if (op == 7 || op == 9)
            valid = EffectClip(Read32(data + pc + 2), Read32(data + pc + 6)) != NULL;
        if (op == 18 || op == 21)
        {
            u32 frames = Read32(data + pc + 18), wait = Read32(data + pc + 22);
            u32 repeat = Read32(data + pc + 26);
            s32 x = (s32)Read32(data + pc + 10), y = (s32)Read32(data + pc + 14);
            s32 limit = op == 21 ? 2048 : 32768;
            if (!frames || frames > 120 || wait > 30 || !repeat || repeat > 10
                || frames * (wait + 1) * 2 * repeat > 600
                || x < -limit || x > limit || y < -limit || y > limit)
                valid = FALSE;
        }
        pc += 2 + count * 4;
        if (op == 77) { ended = TRUE; break; }
    }
    for (u32 pc = 60; valid && ended && pc + 2 <= size; )
    {
        unsigned op = Read16(data + pc), count = ArgCount(op);
        u32 next = pc + 2 + count * 4;
        if (op == 59)
        {
            s32 target = next + (s32)Read32(data + pc + 14);
            if (target < 60 || (u32)target >= size || !starts[target]
                || Read32(data + pc + 2) != 19 || Read32(data + pc + 6) != 0)
                valid = FALSE;
        }
        pc = next;
        if (op == 77) break;
    }
    if (!valid || !ended) { free(data); return FALSE; }
    sScript = data;
    sScriptSize = size;
    return TRUE;
}

void __real_DoMoveAnim(u16 move);
void __wrap_DoMoveAnim(u16 move)
{
    if (sRunning || !PrepareMove(move))
    {
        __real_DoMoveAnim(move);
        return;
    }
    sMove = move;
    sAttacker = gBattlerAttacker;
    sTarget = gBattlerTarget;
    sPC = 60;
    sMoveTick = 0;
    sCameraWait = sCryWait = sSoundCount = 0;
    sFade = sFadeGoal = sFadeClock = 0;
    memset(sSoundAt, 0, sizeof(sSoundAt));
    memcpy(sSavedPalette, gPlttBufferFaded, sizeof(sSavedPalette));
    gBattleAnimAttacker = sAttacker;
    gBattleAnimTarget = sTarget;
    gAnimScriptActive = sRunning = TRUE;
    gAnimScriptCallback = MoveCallback;
    CtrLog_Write(CTR_LOG_GAME, "BW2 move %u %u -> %u (%lu bytes)", move, sAttacker, sTarget,
                 (unsigned long)sScriptSize);
}

void CtrBW2_BeforeSprites(void)
{
    if (!gMain.inBattle)
    {
        if (sHadBattle)
        {
            for (unsigned i = 0; i < BW_CACHE_SIZE; ++i) { free(sClips[i].data); free(sClips[i].spots); }
            free(sScript);
            sScript = NULL;
            memset(sClips, 0, sizeof(sClips));
            memset(sEffectKeys, 0, sizeof(sEffectKeys));
            memset(sPokemonKeys, 0, sizeof(sPokemonKeys));
            memset(sActors, 0, sizeof(sActors));
            memset(sEffects, 0, sizeof(sEffects));
            memset(sMotion, 0, sizeof(sMotion));
            sRunning = FALSE;
        }
        sHadBattle = FALSE;
        return;
    }
    sHadBattle = TRUE;
    if (!gMonSpritesGfxPtr || !gBattleSpritesDataPtr || !gBattleSpritesDataPtr->battlerData)
        return;
    for (unsigned b = 0; b < gBattlersCount; ++b)
    {
        BwActor *actor = &sActors[b];
        unsigned id = gBattlerSpriteIds[b];
        if (!actor->clip || id >= MAX_SPRITES || !gSprites[id].inUse
            || !HasActorAnimation(actor, &gSprites[id]) || gBattleSpritesDataPtr->battlerData[b].behindSubstitute)
            continue;
        u16 species = gBattleSpritesDataPtr->battlerData[b].transformSpecies;
        if (species == SPECIES_NONE) species = gBattleMons[b].species;
        if (species != actor->species)
        {
            actor->id = 0;
            /* Transform changes graphics directly, without the wrapped mon
             * loaders. Let its native mosaic/BG animation finish, then bind
             * the displayed species again and resume the BW2 idle clip. */
            if (gAnimScriptActive) continue;
            bool8 back = GetBattlerSide(b) == B_SIDE_PLAYER;
            struct Pokemon *mon = back ? &gPlayerParty[gBattlerPartyIndexes[b]]
                                       : &gEnemyParty[gBattlerPartyIndexes[b]];
            u16 expected = gBattleSpritesDataPtr->battlerData[b].transformSpecies;
            if (expected == SPECIES_NONE) expected = GetMonData(mon, MON_DATA_SPECIES);
            if (expected != species) continue;
            RegisterPokemon(mon, b, back);
            if (!actor->clip) continue;
        }
        if (species == SPECIES_CASTFORM && gBattleMonForms[b] != gCtrBW2ActorForms[b])
        {
            bool8 back = GetBattlerSide(b) == B_SIDE_PLAYER;
            RegisterPokemon(back ? &gPlayerParty[gBattlerPartyIndexes[b]]
                                 : &gEnemyParty[gBattlerPartyIndexes[b]], b, back);
            if (!actor->clip) continue;
        }
        u32 identity = CtrSprites_Id(id);
        if (actor->id != identity) { actor->tick = 0; actor->id = identity; }
        ActorPixels(b);
        if (!actor->paused) ++actor->tick;
    }
}

void CtrBW2_AfterSprites(void)
{
    if (!gMain.inBattle || !gMonSpritesGfxPtr || !gBattleSpritesDataPtr || !gBattleSpritesDataPtr->battlerData)
        return;
    for (unsigned b = 0; b < gBattlersCount; ++b)
    {
        unsigned id = gBattlerSpriteIds[b];
        BwActor *actor = &sActors[b];
        if (actor->clip && id < MAX_SPRITES && actor->id == CtrSprites_Id(id)
            && HasActorAnimation(actor, &gSprites[id]) && !gBattleSpritesDataPtr->battlerData[b].behindSubstitute)
            RequestSpriteCopy(gMonSpritesGfxPtr->sprites.byte[GetBattlerPosition(b)],
                              (u8 *)OBJ_VRAM0 + gSprites[id].oam.tileNum * 32, BW_TILE_BYTES);
    }
    for (unsigned i = 0; i < BW_EFFECTS; ++i)
    {
        BwEffect *effect = &sEffects[i];
        if (!effect->clip) continue;
        if (effect->tick >= effect->clip->steps || CtrSprites_Id(effect->sprite) != effect->id)
        {
            KillEffect(i);
            continue;
        }
        const u8 *pixels = Frame(effect->clip, effect->tick++, FALSE);
        RequestSpriteCopy(pixels, (u8 *)OBJ_VRAM0 + gSprites[effect->sprite].oam.tileNum * 32, BW_TILE_BYTES);
    }
}

/* Presentation only: keep the game's actor coordinates and affine controller
 * untouched. Compose the extra size into a private matrix after the normal
 * OAM build, including whatever a move/entrance already did to the actor.
 * Double-size OBJ bounds prevent the enlarged 64x64 picture being clipped.
 */
void CtrBW2_AfterOam(void)
{
    u8 matrices[MAX_BATTLERS_COUNT];
    unsigned matrixCount = 0;
    if (!gMain.inBattle)
        return;
    for (unsigned b = 0; b < gBattlersCount; ++b)
    {
        BwActor *actor = &sActors[b];
        unsigned id = gBattlerSpriteIds[b];
        if (!actor->clip || !actor->id
            || id >= MAX_SPRITES || CtrSprites_Id(id) != actor->id
            || gSprites[id].invisible || !HasActorAnimation(actor, &gSprites[id]))
            continue;
        const struct Sprite *sprite = &gSprites[id];
        u8 drawMatrix = 0xff;
        for (unsigned i = 0; i < 128; ++i)
        {
            struct OamData *oam = &gMain.oamBuffer[i];
            if (oam->tileNum != sprite->oam.tileNum || oam->paletteNum != sprite->oam.paletteNum
                || oam->shape != ST_OAM_SQUARE || oam->size != ST_OAM_SIZE_3
                || oam->affineMode == ST_OAM_AFFINE_ERASE)
                continue;
            unsigned oldMode = oam->affineMode, oldMatrix = oam->matrixNum;
            unsigned oldBox = oldMode == ST_OAM_AFFINE_DOUBLE ? 128 : 64;
            CtrVideo_MarkBattleActor(i, i + 1);
            if (drawMatrix == 0xff)
            {
                drawMatrix = AllocOamMatrix();
                if (drawMatrix != 0xff) matrices[matrixCount++] = drawMatrix;
            }
            if (drawMatrix == 0xff)
                continue;
            s16 matrix[4] = {256, 0, 0, 256};
            if (oldMode & ST_OAM_AFFINE_ON_MASK)
                for (unsigned j = 0; j < 4; ++j)
                    matrix[j] = (s16)gMain.oamBuffer[oldMatrix * 4 + j].affineParam;
            else
            {
                if (oldMatrix & ST_OAM_HFLIP) matrix[0] = -256;
                if (oldMatrix & ST_OAM_VFLIP) matrix[3] = -256;
            }
            for (unsigned j = 0; j < 4; ++j)
                gMain.oamBuffer[drawMatrix * 4 + j].affineParam =
                    (s16)(matrix[j] * 256 / sPresentation[b].scale);
            oam->x = (oam->x + oldBox / 2 - 64 + sPresentation[b].x) & 511;
            oam->y = (oam->y + oldBox / 2 - 64 + ActorDrop(b)) & 255;
            oam->affineMode = ST_OAM_AFFINE_DOUBLE;
            oam->matrixNum = drawMatrix;
            int top = sprite->y + sprite->y2 - 64 + ActorDrop(b)
                + (sprite->coordOffsetEnabled ? gSpriteCoordOffsetY : 0);
            CtrVideo_SetOamAnchor(i, i + 1, top);
        }
    }
    /* The completed OAM buffer owns the values for this frame. The game's
     * allocator can reuse these slots on the next frame; nothing is retained
     * across ResetSpriteData, a battle exit, or another actor's lifetime. */
    for (unsigned i = 0; i < matrixCount; ++i) FreeOamMatrix(matrices[i]);
}
