# BW2 battle prototype

Private, optional presentation import, initially built for Treecko and Poochyena. Emerald's
species data, learnsets, damage calculations and save format are unchanged.
The national species catalog now permits incremental imports of other actors
(Grovyle and Sceptile were added during the plan's execution). Species without
imported data and all remaining moves retain their existing presentation. The imported
move scripts run only when the attacker uses a successfully imported actor;
link battles retain Emerald's original move scripts.

| Pokemon | Emerald ID | BW2 ID | Emerald moves learned through level 5 |
|---|---:|---:|---|
| Treecko | 277 | 252 | Pound (Botta), Leer (Fulmisguardo) |
| Poochyena | 286 | 261 | Tackle (Azione), Howl (Gridodilotta) |

## Generate and build

From a bootstrapped tree's `3ds_port/`, using Python with Pillow:

```sh
python scripts/gen_bw2_battle.py --rom /path/to/black2.nds --out romfs/bw2 --previews build/bw2-preview
make -j8
```

Alternatively pass `BW2_ROM=/path/to/black2.nds` to make to generate the data.
To regenerate after changing the ROM or exporter, rerun the export explicitly.
The root repository's exporter may target `build/upstream/3ds_port/romfs/bw2`.
Use `--species 253` to add Grovyle or another selected national dex number;
`--catalog data/bw2_species.json` maps the national IDs to Emerald IDs.
Use `--moves 10 45` to add Scratch and Growl; `data/bw2_moves.json` contains
the 354 Emerald move IDs. Selection retains earlier imports. Unsupported
opcodes and particle resources still fail export and are not completed units.
Incremental exports retain prior manifest entries and refuse a different ROM.
Do not reset or bootstrap a checkout containing unrelated local changes just
to synchronize these port files.

The ROM is read, never modified. The exporter supports the Black 2 filesystem
and validates the selected scripts/resources; the supplied Italian ROM (IREI)
was used for development. The generated `manifest.json` records the ROM hash,
source commands and output sizes. This is not a ROM authenticity check.

Outputs under `romfs/bw2/` are optional game data, like follower sprites: they
are excluded from the engine ABI, release RomFS and ROM reconstruction recipe,
and included by the pack/devdata staging commands. No Nintendo image, particle
texture, palette or script is stored in tracked source files. The ordinary
Emerald-only builder does not acquire or regenerate the BW2 data.

## Presentation and limits

The exporter samples the Nitro cell and multi-cell animation tracks, including
their per-part positions, rotations, scale and layer order. It renders the
front and back animation into a stable 64x64 indexed canvas, retaining the
normal/shiny palette. Frames are deduplicated and replayed at 60 game ticks per
second. They share Emerald's existing actor tile buffers, including their BG
copies, rather than introducing a second native overlay.

The four move scripts come from `a/0/6/5`. Their referenced SPL resources from
`a/0/0/6` provide the particle textures and lifetime curves. A restricted VM
supports only the opcodes needed by these four scripts and validates the
entire script and effect data before replacing a move. Missing, unsupported or
invalid data leaves Emerald's original move available.

This is an adaptation to Emerald's battle composition, not pixel-identical DS
rendering. The camera stays fixed; camera commands preserve their waits.
Particle emission is projected into a 2D plane and alpha is quantized to a
15-color palette; child-particle emission and DS-specific depth/orientation
are omitted. Sounds and cries use Emerald's audio system. Pokemon motion and
scale curves are adapted to Emerald's coordinates. These choices also retain
the existing voxel/stereo compositor without consuming native GPU textures.

The quad rasterizer preserves DS depth priority: earlier MCSS quads cover
later ones. Shared cell controllers are initialized by their first node.
This keeps Poochyena's eyes, head and limbs visible in the correct order.
As of 28 October 2026, presentation uses the Pokemon's Emerald Pokedex height
and the measured animation silhouette. The saturating size curve, rear-view
perspective and screen limits replace the fixed Treecko/Poochyena adjustments.
See [the layout algorithm](BW2_POKEMON_LAYOUT.md) for formulas and anchoring.
This transform is composed after the normal sprite build, with double-size bounds;
it does not crop the imported frames or change the battle's logical actor
coordinates. Existing move transforms and horizontal/vertical flips are kept.
The temporary presentation matrices are released each frame.
Stable front-view floors and back-view time-weighted opaque pixel centers align imported
actors to their circular arena. The text may cover the lower rear-view body;
BW2 move effect origins follow the resulting visual center.
Enlarged actors are clipped before the scenery's repeated edge row when the
message box is present, so their feet cannot reappear below the text box.

The bridge restores actor positions, matrices, pause state and faded palettes
when a move ends. A watchdog prevents a stalled move from holding the battle
controller indefinitely. Assets are cached only for the current battle.
Substitute removal/restoration has explicit hooks. Pokemon clips share four
slots, pinned by active battlers and reused safely after switches; the whole
catalog is never loaded into RAM. Forms and personalization need their separate
import/validation work in the plan.

Move dependencies now use dynamic `(resource, emitter)` keys rather than a
fixed list of ten emitter identities. Preparing an imported script clears the
previous move's effect clips and validates all referenced resources before
playback. The limits remain ten cached clips per move and four live effect
sprites; missing dependencies or excess resources select the original move.
Only locally present scripts that pass the restricted VM validation run.
Scratch and Growl add five emitter clips, with the same documented SPL
projection limits. Scratch uses Emerald's Scratch sound; Growl uses the
scripted actor cry commands. Audio is not attested by the silent capture setup.

## Validation

```sh
python 3ds_port/tests/bw2_export_test.py
python 3ds_port/tests/bw2_battle_test.py
python 3ds_port/tests/bw2_battle_test.py --assets build/upstream/3ds_port/romfs/bw2
```

The host test compiles and executes the actual bridge with mocked game APIs.
With the ROM-derived assets it runs every selected script from both sides,
checks termination and particle creation, and verifies restoration of position,
scale allocation, palette and pause state. It also checks shiny selection,
substitute restoration, actor identity changes, battle cleanup, missing assets,
unsupported moves and the link-battle fallback. Format tests cover decompression,
tile order, frame deduplication and invalid/unsupported scripts.
Regression tests also cover overlapping body/eye layers, shared controllers,
height-dependent sizing and saturation, silhouette bounds and weighted floors,
rear-view headroom, flip and affine composition, and matrix exhaustion/release.
Playback tests use Emerald's distinct opponent front-animation tables and
verify tile changes through full loops for both species from both sides,
including pause/resume. The bridge accepts both those front tables and the
shared player back table; checking only the latter froze front-facing actors.

`CTR_BATTLE_TEST=SPECIES_POOCHYENA`, `CTR_BATTLE_TEST_LEVEL=5` and
`CTR_BW2_DEMO` together enable an emulator-only test encounter with a temporary
level-5 Treecko party. These flags are not part of the normal build. Run the
test build on a separate emulator SD directory; the demo does not save the game.
The newer `CTR_BW2_VALIDATION` harness and real video acquisition workflow are
documented in [BW2_VALIDATION.md](BW2_VALIDATION.md). The maintained checklists
and evidence index are in [BW2_ANIMATION_PLAN.md](BW2_ANIMATION_PLAN.md).
Hardware performance, doubles, and exhaustive interactions with Emerald's
remaining move animations still need console validation.

The development build was also run in Azahar on an isolated copy of the SD
directory. The corrected front playback was verified through local read-only
RPC against the matching demo ELF/build ID: both actor clocks advanced and
their actual displayed OBJ VRAM tiles changed (16 distinct Poochyena frames
in the sampling window). The report is
`build/bw2-prototype/idle-runtime-verification.json`.
Pound/Tackle/Howl ended normally in repeated level-5 battles (59/59/138 game
ticks). Leer was exercised by the host test from both sides (131 ticks).
`build/bw2-prototype/battle-preview.png` is the initial prototype screenshot,
before the sprite composition and playback corrections.
The supplied save and its isolated copy retained the same SHA-256 after the
run. The emulator test had no DSP firmware, so audio playback was not verified.
The general `make verify` suite is currently blocked by existing bottom-map
test assumptions about `ViewState.party` and `PARTY_CARD_X/Y`; the dedicated
BW2 tests and game build pass independently.
