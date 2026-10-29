#!/usr/bin/env python3
"""Exercise the real BW2 bridge on the host, optionally using ROM-derived data.

python bw2_battle_test.py --assets build/upstream/3ds_port/romfs/bw2
"""
import argparse
import importlib.util
import os
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]

HEADER = r'''
#pragma once
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdarg.h>
typedef uint8_t u8; typedef uint16_t u16; typedef uint32_t u32;
typedef uint64_t u64;
typedef int8_t s8; typedef int16_t s16; typedef int32_t s32; typedef u8 bool8;
#define TRUE 1
#define FALSE 0
#define MAX_BATTLERS_COUNT 4
#define CTR_GAME_HEIGHT 240
#define CTR_BATTLE_ZOOM 1.4f
#define MAX_SPRITES 64
#define PLTT_SIZE 1024
#define SPECIES_NONE 0
#define SPECIES_SPINDA 308
#define SPECIES_CASTFORM 385
#define MON_DATA_PERSONALITY 1
#define SPECIES_TREECKO 277
#define SPECIES_POOCHYENA 286
#define NUM_SPECIES 412
#define MOVE_POUND 1
#define MOVE_SCRATCH 10
#define MOVE_TACKLE 33
#define MOVE_LEER 43
#define MOVE_GROWL 45
#define MOVE_HOWL 336
#define MOVES_COUNT 355
#define SE_M_DOUBLE_SLAP 1
#define SE_M_COMET_PUNCH 2
#define SE_M_LEER 3
#define SE_M_UPROAR 4
#define SE_M_SCRATCH 5
#define MON_DATA_SPECIES 0
#define B_SIDE_PLAYER 0
#define BATTLE_TYPE_LINK 2
#define SPRITE_SHAPE(x) 0
#define SPRITE_SIZE(x) 3
#define TAG_NONE 65535
#define ST_OAM_AFFINE_NORMAL 1
#define ST_OAM_AFFINE_ERASE 2
#define ST_OAM_AFFINE_DOUBLE 3
#define ST_OAM_AFFINE_ON_MASK 1
#define ST_OAM_HFLIP 8
#define ST_OAM_VFLIP 16
#define ST_OAM_SQUARE 0
#define ST_OAM_SIZE_3 3
#define RGB_BLACK 0
#define CTR_LOG_GAME 0
#define CTR_LOG_ERROR 1
#define ARRAY_COUNT(a) (sizeof(a)/sizeof((a)[0]))
#define OBJ_PLTT_ID(b) (256+(b)*16)
#define BG_PLTT_ID(b) ((b)*16)
#define BATTLER_COORD_X_2 0
#define BATTLER_COORD_Y_PIC_OFFSET 1
#define BATTLER_COORD_Y 2
struct OamData { unsigned shape,size,priority,affineMode,matrixNum,tileNum,paletteNum,x,y; u16 affineParam; };
union AnimCmd { int dummy; }; union AffineAnimCmd { int dummy; };
struct SpriteFrameImage { const void *data; u16 size; u32 offset; };
struct Sprite;
struct SpriteTemplate {
    u16 tileTag,paletteTag; const struct OamData *oam;
    const union AnimCmd *const *anims; const struct SpriteFrameImage *images;
    const union AffineAnimCmd *const *affineAnims; void (*callback)(struct Sprite *);
};
struct Sprite {
    bool8 inUse,invisible,affineAnimPaused,coordOffsetEnabled;
    s16 x,y,x2,y2; struct OamData oam; const union AnimCmd *const *anims;
};
struct SpritePalette { const u16 *data; u16 tag; };
struct Pokemon { u16 species; bool8 shiny; u32 personality; };
struct BattleMon { u16 species; };
struct BattleSpriteInfo { bool8 behindSubstitute; u16 transformSpecies; };
struct BattleSpriteData { struct BattleSpriteInfo *battlerData; };
struct MonSpritesGfx { union { void *ptr[4]; u8 *byte[4]; } sprites; };
extern struct Sprite gSprites[64];
extern struct Pokemon gPlayerParty[6],gEnemyParty[6];
extern struct BattleMon gBattleMons[4];
extern struct BattleSpriteData *gBattleSpritesDataPtr;
extern struct MonSpritesGfx *gMonSpritesGfxPtr;
extern u8 gBattlersCount,gBattlerSpriteIds[4],gBattlerPartyIndexes[4],gBattlerAttacker,gBattlerTarget;
extern u8 gBattleAnimAttacker,gBattleAnimTarget,gAnimScriptActive;
extern u32 gBattleTypeFlags, gTransformedPersonalities[4];
extern u8 gBattleMonForms[4];
extern u16 gPlttBufferFaded[512];
extern struct Main { bool8 inBattle; struct OamData oamBuffer[128]; } gMain;
extern s16 gSpriteCoordOffsetY;
extern void (*gAnimScriptCallback)(void);
extern const union AnimCmd *const gAnims_MonPic[],*const gDummySpriteAnimTable[];
extern const union AnimCmd *const *const gMonFrontAnimsPtrTable[];
extern const union AffineAnimCmd *const gDummySpriteAffineAnimTable[];
extern u8 testVram[65536];
#define OBJ_VRAM0 testVram
u32 GetMonData(struct Pokemon *,unsigned);
bool8 IsMonShiny(struct Pokemon *);
u16 SpeciesToNationalPokedexNum(u16);
u16 GetPokedexHeightWeight(u16,u8);
u8 GetBattlerElevation(u8,u16);
u8 GetBattlerPosition(u8);
u8 GetBattlerSide(u8);
s16 GetBattlerSpriteCoord(u8,unsigned);
u8 GetBattlerSpriteDefault_Y(u8);
bool8 CtrData_Size(const char *,u32 *);
void *CtrData_Load(const char *,u32 *);
void CtrLog_Write(int,const char *,...);
u32 CtrSprites_Id(unsigned);
void LoadPalette(const void *,u16,u16);
void DestroySprite(struct Sprite *);
void FreeSpritePaletteByTag(u16);
u8 LoadSpritePalette(const struct SpritePalette *);
u8 CreateSprite(const struct SpriteTemplate *,s16,s16,u8);
void SpriteCallbackDummy(struct Sprite *);
u8 AllocOamMatrix(void);
void FreeOamMatrix(u8);
void SetOamMatrix(u8,s16,s16,s16,s16);
void BlendPalettes(u32,u8,u16);
void PlaySE12WithPanning(u16,s8);
void PlayCry_Normal(u16,s8);
void RequestSpriteCopy(const u8 *,u8 *,u16);
void CtrVideo_SetOamAnchor(unsigned,unsigned,int);
void CtrVideo_MarkBattleActor(unsigned,unsigned);
'''

HARNESS = r'''
#include "global.h"
#include "PRODUCTION"
struct Sprite gSprites[64];
struct Pokemon gPlayerParty[6],gEnemyParty[6];
struct BattleMon gBattleMons[4];
struct Main gMain;
s16 gSpriteCoordOffsetY;
struct BattleSpriteInfo info[4];
struct BattleSpriteData battleData={info},*gBattleSpritesDataPtr=&battleData;
struct MonSpritesGfx gfx,*gMonSpritesGfxPtr=&gfx;
u8 gBattlersCount=2,gBattlerSpriteIds[4]={0,1,2,3},gBattlerPartyIndexes[4];
u8 gBattlerAttacker,gBattlerTarget,gBattleAnimAttacker,gBattleAnimTarget,gAnimScriptActive;
u32 gBattleTypeFlags, gTransformedPersonalities[4];
u8 gBattleMonForms[4];
u16 gPlttBufferFaded[512];
u8 testVram[65536],pixels[4][8192];
void (*gAnimScriptCallback)(void);
const union AnimCmd *const gAnims_MonPic[]={NULL},*const gDummySpriteAnimTable[]={NULL};
static const union AnimCmd frontCommand={1};
static const union AnimCmd *const treeckoFront[]={&frontCommand},*const poochyenaFront[]={&frontCommand};
const union AnimCmd *const *const gMonFrontAnimsPtrTable[412]={
 [SPECIES_TREECKO]=treeckoFront,[SPECIES_POOCHYENA]=poochyenaFront
};
const union AffineAnimCmd *const gDummySpriteAffineAnimTable[]={NULL};
static const char *assetRoot;
static u32 identities[64],serial;
static unsigned fallbacks,watchdogs,emitted,copies,matrixCount;
static bool8 denyTestClip;
static u32 matrixBitmap;
u32 GetMonData(struct Pokemon *m,unsigned field) { return field==MON_DATA_PERSONALITY ? m->personality : m->species; }
bool8 IsMonShiny(struct Pokemon *m) { return m->shiny; }
u16 SpeciesToNationalPokedexNum(u16 s) { return s; }
u16 GetPokedexHeightWeight(u16 s,u8 d) { (void)d;return s==278?9:s==279?17:5; }
u8 GetBattlerElevation(u8 b,u16 s) { (void)b;(void)s;return 0; }
u8 GetBattlerPosition(u8 b) { return b; }
u8 GetBattlerSide(u8 b) { return b&1; }
s16 GetBattlerSpriteCoord(u8 b,unsigned axis) { return axis==BATTLER_COORD_Y_PIC_OFFSET ? 72 : axis ? 64 : 80+(b&1)*80; }
u8 GetBattlerSpriteDefault_Y(u8 b) { (void)b;return 64; }
static FILE *Open(const char *p) { if(denyTestClip&&!strcmp(p,"bw2/1_front.bin"))return NULL;char path[2048]; snprintf(path,sizeof(path),"%s/%s",assetRoot,p); return fopen(path,"rb"); }
bool8 CtrData_Size(const char *p,u32 *n) { FILE *f=Open(p); if(!f)return FALSE; fseek(f,0,SEEK_END);*n=ftell(f);fclose(f);return TRUE; }
void *CtrData_Load(const char *p,u32 *n) { FILE *f=Open(p);if(!f)return NULL;fseek(f,0,SEEK_END);*n=ftell(f);rewind(f);void *b=malloc(*n);assert(fread(b,1,*n,f)==*n);fclose(f);return b; }
void CtrLog_Write(int level,const char *fmt,...) { (void)level; if(strstr(fmt,"watchdog"))++watchdogs; }
u32 CtrSprites_Id(unsigned i) { return i<64&&gSprites[i].inUse ? identities[i] : 0; }
void LoadPalette(const void *p,u16 off,u16 n) { assert(off*2+n<=1024);memcpy(gPlttBufferFaded+off,p,n); }
void DestroySprite(struct Sprite *s) { s->inUse=FALSE; }
void FreeSpritePaletteByTag(u16 tag) { (void)tag; }
u8 LoadSpritePalette(const struct SpritePalette *p) { (void)p; return 5; }
u8 CreateSprite(const struct SpriteTemplate *t,s16 x,s16 y,u8 priority) { (void)priority;
 for(unsigned i=4;i<8;++i) {
  if(!gSprites[i].inUse) { gSprites[i]=(struct Sprite){.inUse=TRUE,.x=x,.y=y,.oam=*t->oam};gSprites[i].oam.tileNum=512+(i-4)*64;identities[i]=++serial;++emitted;return i; }
 }
 return 64;
}
void SpriteCallbackDummy(struct Sprite *s) { (void)s; }
u8 AllocOamMatrix(void) {
 for(unsigned i=0;i<32;++i) if(!(matrixBitmap&(1u<<i))) {matrixBitmap|=1u<<i;++matrixCount;return i;}
 return 255;
}
void FreeOamMatrix(u8 m) { assert(m<32&&(matrixBitmap&(1u<<m))&&matrixCount);matrixBitmap&=~(1u<<m);--matrixCount; }
void SetOamMatrix(u8 m,s16 a,s16 b,s16 c,s16 d) { assert(m<32&&a>0&&d>0&&b==0&&c==0); }
void CtrVideo_SetOamAnchor(unsigned first,unsigned end,int y) { (void)y;assert(first<end&&end<=128); }
void CtrVideo_MarkBattleActor(unsigned first,unsigned end) { assert(first<end&&end<=128); }
void BlendPalettes(u32 mask,u8 fade,u16 color) { (void)mask;(void)color;assert(fade<=16);memset(gPlttBufferFaded,fade,1024); }
void PlaySE12WithPanning(u16 sound,s8 pan) { (void)sound;(void)pan; }
void PlayCry_Normal(u16 species,s8 pan) { (void)species;(void)pan; }
void RequestSpriteCopy(const u8 *p,u8 *dest,u16 n) { assert(dest>=testVram&&dest+n<=testVram+sizeof(testVram));memcpy(dest,p,n);++copies; }
void __real_BattleLoadOpponentMonSpriteGfx(struct Pokemon *m,u8 b) { (void)m;memset(pixels[b],0xaa,8192); }
void __real_BattleLoadPlayerMonSpriteGfx(struct Pokemon *m,u8 b) { __real_BattleLoadOpponentMonSpriteGfx(m,b); }
void __real_BattleLoadSubstituteOrMonSpriteGfx(u8 b,bool8 m) { (void)m;memset(pixels[b],0xaa,8192); }
void __real_LoadBattleMonGfxAndAnimate(u8 b,bool8 m,u8 id) { (void)id;__real_BattleLoadSubstituteOrMonSpriteGfx(b,m); }
void __real_DoMoveAnim(u16 move) { (void)move;++fallbacks; }
static void Start(void) {
 gMain.inBattle=FALSE;CtrBW2_BeforeSprites();gMain.inBattle=TRUE;gBattleTypeFlags=0;
 memset(info,0,sizeof(info));memset(gSprites,0,sizeof(gSprites));
 for(unsigned i=0;i<4;++i) { gfx.sprites.byte[i]=pixels[i];gSprites[i].inUse=TRUE;gSprites[i].anims=gAnims_MonPic;
 gSprites[i].oam.tileNum=i*64;gSprites[i].x2=3;gSprites[i].y2=-2;identities[i]=++serial; }
 gBattleMons[0].species=SPECIES_TREECKO;gBattleMons[1].species=SPECIES_POOCHYENA;
 /* Emerald gives opponents their species' front table, not gAnims_MonPic. */
 gSprites[1].anims=gMonFrontAnimsPtrTable[SPECIES_POOCHYENA];
 gPlayerParty[0]=(struct Pokemon){SPECIES_TREECKO,TRUE};gEnemyParty[0]=(struct Pokemon){SPECIES_POOCHYENA,FALSE};
 __wrap_BattleLoadPlayerMonSpriteGfx(&gPlayerParty[0],0);
 __wrap_BattleLoadOpponentMonSpriteGfx(&gEnemyParty[0],1);
 CtrBW2_BeforeSprites();CtrBW2_AfterSprites();
}
static void PrimeOam(void) {
 for(unsigned i=0;i<128;++i) gMain.oamBuffer[i]=(struct OamData){.affineMode=ST_OAM_AFFINE_ERASE};
 for(unsigned b=0;b<2;++b) {
  gMain.oamBuffer[10+b*10]=(struct OamData){.shape=0,.size=3,.tileNum=b*64,.x=80,.y=60};
 }
}
static void TestActorPresentation(void) {
 u8 tiles[3*BW_TILE_BYTES]={0};u16 timeline[]={0,1,1,1,2};
 static const unsigned rows[]={9,19,59};
 for(unsigned f=0;f<3;++f)tiles[f*BW_TILE_BYTES+(rows[f]/8*8)*32+(rows[f]%8)*4]=1;
 BwClip measured={.frames=3,.steps=5,.loop=1,.timeline=timeline,.tiles=tiles};
 MeasureClip(&measured);
 assert(measured.left==0&&measured.right==1&&measured.top==9&&measured.bottom==60);
 assert(measured.floor==20); // time-weighted idle floor, not the lowest outlier
 assert(measured.centerY==29*256); // pixel mass follows durations, not the union box
 BwClip silhouette={.left=2,.top=2,.right=62,.bottom=62,.floor=58,.centerY=32*256};
 BwPresentation tiny=PresentationFor(&silhouette,1,FALSE,64,40);
 BwPresentation treecko=PresentationFor(&silhouette,5,FALSE,64,40);
 BwPresentation grovyle=PresentationFor(&silhouette,9,FALSE,64,40);
 BwPresentation sceptile=PresentationFor(&silhouette,17,FALSE,64,40);
 BwPresentation giant=PresentationFor(&silhouette,100,FALSE,64,40);
 BwPresentation largest=PresentationFor(&silhouette,145,TRUE,114,83);
 BwPresentation rearSmall=PresentationFor(&silhouette,5,TRUE,114,83);
 BwPresentation rearGrovyle=PresentationFor(&silhouette,9,TRUE,114,83);
 BwPresentation rearSceptile=PresentationFor(&silhouette,17,TRUE,114,83);
 assert(rearSmall.targetSpan==79&&rearSmall.scale==337);
 assert(rearGrovyle.targetSpan==108&&rearGrovyle.scale==460);
 assert(rearSceptile.targetSpan==112&&rearSceptile.scale==477);
 assert(tiny.scale<treecko.scale&&treecko.scale<grovyle.scale&&grovyle.scale<sceptile.scale);
 assert(sceptile.scale<giant.scale&&giant.targetSpan==88&&largest.targetSpan==112);
 assert((60u*giant.scale/256)<=88&&(60u*largest.scale/256)<=112);
 assert(treecko.y+40+(58-32)*treecko.scale/256==64);
 assert(largest.y+83+(2+62-64)*largest.scale/512==114);
 assert(60u*largest.scale/256>80); // lower-body overlap must not shrink large rear views
 assert(largest.y+83+(62-32)*largest.scale/256>114); // lower body can lie behind the text
 silhouette.top=18;silhouette.bottom=62;
 silhouette.centerY=40*256;
 BwPresentation quadruped=PresentationFor(&silhouette,5,TRUE,114,83);
 assert(quadruped.y+83+(18+62-64)*quadruped.scale/512==114);
 silhouette.top=2;
 silhouette.right=62;silhouette.bottom=32; // a long horizontal body must fit too
 BwPresentation wide=PresentationFor(&silhouette,17,FALSE,64,40);
 assert(wide.scale==sceptile.scale);
 silhouette.left=31;silhouette.right=33;silhouette.top=31;silhouette.bottom=33;
 assert(PresentationFor(&silhouette,145,TRUE,114,83).scale==512);
 // The canvas alone cannot distinguish a small native sprite from a large
 // one reduced by the exporter. Source hints must restore that distinction.
 silhouette=(BwClip){.left=2,.top=12,.right=62,.bottom=62,.floor=60,.centerY=35*256};
 BwPresentation unhinted=PresentationFor(&silhouette,10,FALSE,64,40);
 silhouette.nativeWidth=47;silhouette.nativeHeight=58;
 BwPresentation compact=PresentationFor(&silhouette,10,FALSE,64,40);
 silhouette.nativeWidth=100;silhouette.nativeHeight=72;
 BwPresentation broad=PresentationFor(&silhouette,13,FALSE,64,40);
 assert(compact.scale<unhinted.scale&&compact.sourceFactor<256&&broad.sourceFactor>256);
 unsigned hint=SourceSizeFactor(&silhouette,13);
 BwPresentation broadRear=PresentationFor(&silhouette,13,TRUE,114,83);
 assert(broadRear.scale>512&&60u*broadRear.scale/256<=126);
 silhouette.nativeWidth=72;silhouette.nativeHeight=100;
 assert(SourceSizeFactor(&silhouette,13)==hint); // footprint, not longest side
 assert(SourceSizeFactor(&silhouette,145)==256); // giant limit ignores DS framing
 silhouette.nativeWidth=44;silhouette.nativeHeight=63;
 assert(SourceSizeFactor(&silhouette,5)==256); // established Treecko size
 silhouette.nativeWidth=52;silhouette.nativeHeight=44;
 assert(SourceSizeFactor(&silhouette,5)==256); // established Poochyena size
 silhouette.nativeWidth=0;
 assert(SourceSizeFactor(&silhouette,10)==256); // optional old assets still work
 BwClip tall={.left=10,.top=2,.right=54,.bottom=62,.floor=62,.centerY=32*256,
              .nativeWidth=100,.nativeHeight=100};
 BwPresentation high=PresentationFor(&tall,12,FALSE,64,40);
 float pixelTop=(high.y+40+(2-32)*high.scale/256.0f)*CTR_BATTLE_ZOOM
                 +CTR_GAME_HEIGHT-48-112*CTR_BATTLE_ZOOM;
 assert(pixelTop>=4); // highest raised hand stays inside the display
 assert(high.y+40+(62-32)*high.scale/256==64); // same arena floor
 BwPresentation floating=PresentationFor(&tall,12,FALSE,48,24);
 assert(floating.scale<high.scale); // elevation consumes available headroom
 Start();PrimeOam();struct Sprite logical=gSprites[0];
 CtrBW2_AfterOam();struct OamData *tree=&gMain.oamBuffer[10];unsigned matrix=tree->matrixNum;
 unsigned scale=sPresentation[0].scale;
 assert(64+ActorDrop(0)+((int)sActors[0].clip->centerY-32*256)*(int)scale/65536==88);
 assert(tree->affineMode==ST_OAM_AFFINE_DOUBLE&&tree->x==((48+sPresentation[0].x)&511));
 assert(tree->y==((28+ActorDrop(0))&255));
 assert((s16)gMain.oamBuffer[matrix*4].affineParam==(int)(256*256/scale));
 assert(memcmp(&logical,&gSprites[0],sizeof(logical))==0);
 assert(gMain.oamBuffer[20].affineMode==ST_OAM_AFFINE_DOUBLE);
 assert(matrixCount==0&&matrixBitmap==0);
 PrimeOam();gMain.oamBuffer[10].matrixNum=ST_OAM_HFLIP;CtrBW2_AfterOam();matrix=gMain.oamBuffer[10].matrixNum;
 assert((s16)gMain.oamBuffer[matrix*4].affineParam==-(int)(256*256/scale));
 PrimeOam();gMain.oamBuffer[10].affineMode=ST_OAM_AFFINE_NORMAL;gMain.oamBuffer[10].matrixNum=3;
 const s16 original[4]={128,16,-24,384};for(unsigned j=0;j<4;++j)gMain.oamBuffer[12+j].affineParam=original[j];
 matrixBitmap=1u<<3;matrixCount=1;CtrBW2_AfterOam();matrix=gMain.oamBuffer[10].matrixNum;
 for(unsigned j=0;j<4;++j) { assert((s16)gMain.oamBuffer[matrix*4+j].affineParam==original[j]*256/(int)scale);assert((s16)gMain.oamBuffer[12+j].affineParam==original[j]); }
 assert(matrixCount==1&&matrixBitmap==(1u<<3));matrixCount=matrixBitmap=0;
 PrimeOam();CtrBW2_AfterOam();assert(gMain.oamBuffer[10].matrixNum!=gMain.oamBuffer[20].matrixNum);
 assert(matrixCount==0&&matrixBitmap==0);
 PrimeOam();matrixBitmap=0xffffffffu;matrixCount=32;struct OamData unchanged=gMain.oamBuffer[10];
 CtrBW2_AfterOam();assert(memcmp(&unchanged,&gMain.oamBuffer[10],sizeof(unchanged))==0);
 matrixCount=matrixBitmap=0;
 puts("BW2 layout: height curve, giant limits, aspect ratio, stable ground, both views, affine composition and exhaustion passed");
}
static void TestActorPlayback(void) {
 for(unsigned reversed=0;reversed<2;++reversed) {
  Start();
  if(reversed) {
   gBattleMons[0].species=SPECIES_POOCHYENA;gBattleMons[1].species=SPECIES_TREECKO;
   gPlayerParty[0].species=SPECIES_POOCHYENA;gEnemyParty[0].species=SPECIES_TREECKO;
   gSprites[1].anims=gMonFrontAnimsPtrTable[SPECIES_TREECKO];
   __wrap_BattleLoadPlayerMonSpriteGfx(&gPlayerParty[0],0);
   __wrap_BattleLoadOpponentMonSpriteGfx(&gEnemyParty[0],1);
  }
  unsigned changed[2]={0},steps=sActors[0].clip->steps+sActors[1].clip->steps+10;
  for(unsigned b=0;b<2;++b) sActors[b].tick=0;
  for(unsigned tick=0;tick<steps;++tick) {
   u8 previous[2][BW_TILE_BYTES];
   for(unsigned b=0;b<2;++b) memcpy(previous[b],testVram+b*BW_TILE_BYTES,BW_TILE_BYTES);
   CtrBW2_BeforeSprites();CtrBW2_AfterSprites();
   for(unsigned b=0;b<2;++b) {
    assert(sActors[b].tick==tick+1);
    assert(memcmp(testVram+b*BW_TILE_BYTES,Frame(sActors[b].clip,tick,TRUE),BW_TILE_BYTES)==0);
    changed[b]+=memcmp(previous[b],testVram+b*BW_TILE_BYTES,BW_TILE_BYTES)!=0;
   }
  }
  assert(changed[0]>1&&changed[1]>1);
  sActors[1].paused=TRUE;u32 held=sActors[1].tick;
  for(unsigned i=0;i<10;++i) {CtrBW2_BeforeSprites();CtrBW2_AfterSprites();assert(sActors[1].tick==held);}
  sActors[1].paused=FALSE;CtrBW2_BeforeSprites();assert(sActors[1].tick==held+1);
 }
 puts("BW2 playback: both species animate from front/back through loop, pause and resume");
}
static void TestActorCache(void) {
 Start();denyTestClip=TRUE;BwClip *player=sActors[0].clip,*enemy=sActors[1].clip;
 assert(PokemonClip(SPECIES_TREECKO,TRUE)==player);
 sActors[2].clip=PokemonClip(SPECIES_TREECKO,FALSE);assert(sActors[2].clip);
 sActors[3].clip=PokemonClip(SPECIES_POOCHYENA,TRUE);assert(sActors[3].clip);
 const u8 *playerData=player->data,*enemyData=enemy->data;
 assert(!PokemonClip(1,FALSE)); /* All four cache slots are pinned. */
 sActors[3].clip=NULL;assert(!PokemonClip(1,FALSE)); /* Missing asset may reuse only the released slot. */
 assert(player->data==playerData&&enemy->data==enemyData&&sActors[2].clip->data);
 sActors[3].clip=PokemonClip(SPECIES_POOCHYENA,TRUE);assert(sActors[3].clip);
 assert(!PokemonClip(252,FALSE)&&!PokemonClip(NUM_SPECIES,FALSE));
 gMain.inBattle=FALSE;CtrBW2_BeforeSprites();
 for(unsigned i=0;i<4;++i)assert(!sPokemonKeys[i]);
 denyTestClip=FALSE;
 puts("BW2 cache: shared clips, four active battlers, safe switch eviction, missing data and cleanup");
}
int main(int argc,char **argv) {
 assert(argc==2);assetRoot=argv[1];TestActorCache();TestActorPlayback();TestActorPresentation();Start();assert(sActors[0].clip&&sActors[1].clip);
 assert(memcmp(gPlttBufferFaded+256,sActors[0].clip->data+60,32)==0); /* shiny */
 u8 original[8192];memcpy(original,pixels[0],sizeof(original));
 for(unsigned i=0;i<90;++i) { CtrBW2_BeforeSprites();CtrBW2_AfterSprites(); }
 assert(copies>90); /* continuous animation without changing the sprite callback */
 /* A script may reuse dependencies, but cannot silently overrun ten slots. */
 ResetEffectClips();
 static const u16 oldEffects[][2]={{165,0},{165,1},{199,0},{199,1},{208,0},{208,1},{208,2},{510,0},{510,1},{510,2}};
 for(unsigned i=0;i<10;++i)assert(EffectClip(oldEffects[i][0],oldEffects[i][1]));
 assert(!EffectClip(174,0)&&!EffectClip(65536u,0));
 ResetEffectClips();BwClip *fresh=EffectClip(174,0);assert(fresh&&fresh==EffectClip(174,0));
 puts("BW2 effects: dynamic resource keys, deduplication, bounded slots and reset passed");
 for(unsigned side=0;side<2;++side) for(unsigned k=0;k<6;++k) {
  static const u16 moves[]={MOVE_POUND,MOVE_TACKLE,MOVE_LEER,MOVE_HOWL,MOVE_SCRATCH,MOVE_GROWL};
  Start();gBattlerAttacker=side;gBattlerTarget=side^1;u16 saved[512];memcpy(saved,gPlttBufferFaded,sizeof(saved));
  unsigned before=emitted,baseline=fallbacks;__wrap_DoMoveAnim(moves[k]);assert(sRunning&&fallbacks==baseline);
  unsigned frame=0;while(gAnimScriptActive&&frame++<601) {gAnimScriptCallback();CtrBW2_BeforeSprites();CtrBW2_AfterSprites();}
  assert(!gAnimScriptActive&&!sRunning&&frame<600&&watchdogs==0&&emitted>before);
  assert(memcmp(saved,gPlttBufferFaded,sizeof(saved))==0&&matrixCount==0);
  assert(gSprites[0].x2==3&&gSprites[1].x2==3&&gSprites[0].y2==-2&&gSprites[1].y2==-2);
  for(unsigned i=0;i<4;++i) assert(!sActors[i].paused);
  printf("move %u side %u: %u frames, actors/palettes restored\n",moves[k],side,frame);
 }
 Start();unsigned base=fallbacks;__wrap_DoMoveAnim(99);assert(fallbacks==base+1&&!sRunning);
 gBattleTypeFlags=BATTLE_TYPE_LINK;__wrap_DoMoveAnim(MOVE_POUND);assert(fallbacks==base+2&&!sRunning);
 __wrap_BattleLoadSubstituteOrMonSpriteGfx(0,FALSE);assert(!sActors[0].clip);
 __wrap_LoadBattleMonGfxAndAnimate(0,TRUE,0);assert(sActors[0].clip);
 gBattleMons[0].species=1;CtrBW2_BeforeSprites();assert(sActors[0].id==0);
 unsigned writes=copies;CtrBW2_AfterSprites();assert(copies==writes+1); /* opponent only */
 gMain.inBattle=FALSE;CtrBW2_BeforeSprites();for(unsigned i=0;i<14;++i)assert(!sClips[i].data);
 /* Missing optional assets leave the original loader and move intact. */
 assetRoot="directory-that-does-not-exist";Start();assert(!sActors[0].clip&&!sActors[1].clip);
 base=fallbacks;__wrap_DoMoveAnim(MOVE_POUND);assert(fallbacks==base+1&&!sRunning);
 puts("BW2 bridge: fallback, substitute restoration, identity, shiny and cleanup passed");return 0;
}
'''


def synthetic_assets(path):
    path.mkdir(parents=True)
    clip = struct.pack('<4s6I',b'BWA1',2,4,1,64,64,60)+bytes(64)+struct.pack('<4H',0,1,0,1)+bytes(2048)+bytes([17])*2048
    for sp in (277,286):
        for side in ('front','back'):(path/f'{sp}_{side}.bin').write_bytes(clip)
    for fid,indices in ((165,range(2)),(199,range(2)),(208,range(3)),(510,range(3)),(174,range(3)),(210,range(2))):
        for i in indices:(path/f'effect_{fid}_{i}.bin').write_bytes(clip)
    for move,fid in ((1,165),(33,199),(43,208),(336,510),(10,174),(45,210)):
        body=struct.pack('<H11i',7,fid,0,11,8,0,0,0,4096,4096,4096,4096)
        body+=struct.pack('<HiH',56,0,77)
        (path/f'move_{move}.bin').write_bytes(struct.pack('<15I',1,*([60]*14))+body)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets',type=Path)
    parser.add_argument('--cc',default=shutil.which('gcc'))
    args=parser.parse_args()
    if not args.cc:raise SystemExit('Host C compiler is required')
    with tempfile.TemporaryDirectory(prefix='bw2-test-') as folder:
        temp=Path(folder)
        (temp/'global.h').write_text(HEADER)
        for name in ('battle','battle_anim','battle_gfx_sfx_util','data','main','palette','pokemon','pokedex','sound','sprite',
                     'constants/species','constants/moves','constants/songs','constants/rgb',
                     '3ds_data','3ds_platform','3ds_sprite_ids','3ds_bw2_battle','3ds_video'):
            p=temp/(name+'.h');p.parent.mkdir(exist_ok=True);p.write_text('#include "global.h"\n')
        source=ROOT/'3ds_port/src/3ds_bw2_battle.c'
        (temp/'test.c').write_text(HARNESS.replace('PRODUCTION',source.as_posix()))
        assets=args.assets
        if not assets:
            assets=temp/'assets/bw2';synthetic_assets(assets)
        exe=temp/'test.exe'
        subprocess.run([args.cc,'-std=gnu99','-Wall','-Wextra','-Werror','-Wno-missing-field-initializers',
                        '-I',str(temp),str(temp/'test.c'),'-o',str(exe),'-lm'],check=True)
        env=os.environ.copy();env['PATH']=str(Path(args.cc).parent)+os.pathsep+env.get('PATH','')
        subprocess.run([str(exe),str(assets.resolve().parent)],env=env,check=True)


if __name__=='__main__':main()
