# Authored furniture

Flat2's third floor (`LAYOUT_RUSTBORO_CITY_FLAT2_3F`, layout296), verified
from the running game via RPC, replaces its flat green cabinet image with
`green_bookshelf.vox`, at x112..128, z32..40, height16. This is a separate
placement of the same authored model beside the blue bookcase.

Flat2's second floor (`LAYOUT_RUSTBORO_CITY_FLAT2_2F`, layout295), confirmed
from the running game via RPC, uses `yellow_table.vox` at x194..222,
z57..79, height9. Its local origin matches the original yellow table's;
the source image is claimed independently of the floor and nearby chair.

The Cutter's house kitchen (`LAYOUT_RUSTBORO_CITY_CUTTERS_HOUSE`) uses three
local authored props: `kitchen_fridge.vox` (two doors, handles and feet,
x128..144, z32..40, height24), `kitchen_sink.vox` (open basin, raised faucet,
hob and wooden cabinet, x144..176, z32..40, height16), and
`striped_kitchen_table.vox` (four legs and longitudinal gold/cream stripes,
x128..158, z73..95, height9). Their original pixels are claimed as separate
pieces before the room shell; other rooms retain their own kitchen models.
The source-art proof checks that decomposition, and custom-prop tests check
the basin opening, faucet height, handles, feet, stripes and surface coverage.

The same assets also stand in `LAYOUT_RUSTBORO_CITY_FLAT2_1F` (layout294),
the room verified from the running game's map identifiers via RPC. There
the fridge is x176..192, sink x192..224 and table x144..174, z57..79.
The cupboard/tap artwork is decomposed separately from the wall, with the
original tap retaining only floor decals because the authored sink includes
the faucet. Regression tests select the actual Flat2 model names, not just
the visually similar Cutter's house (layout98).

`potted_plant.vox` is a full-volume crown, branched trunk and tapered,
open octagonal pot with soil. Its 24 x 24 x 48 voxels fit a 16 pixel-wide,
31 pixel-high source plant, scaled uniformly to 75% (12 pixels wide,
23.25 pixels high) in the room about the pot's floor anchor, without
moving its base. Leaf clusters use five greens and the pot has thin
grey edging. Its exposed mesh stays below 512 triangles. The two reused
plant placements in `LAYOUT_RUSTBORO_CITY_HOUSE` are split from the original
plant model at export: both corners get this asset, while other rooms keep
their existing model. Tests check the crown, trunk, hollow rim, soil,
surface coverage, bounds, budget and isolation of the two placements.

`purple_display_cabinet.vox` models the east-corner cabinet (x160..192,
z32..40, height20): a pale-yellow top, orange wooden frame, two recessed
purple glass panes with diagonal highlights, and the two lower doors.
`white_console.vox` models the wide white panel and its cream control base
beside the television (x96..127, z32..40, height21), including its four feet,
thin bezel, indicator and three vertical controls. Both replace their own
room pixels only, keep the room's collisions and floor, and are included in
the build dependencies and release-generator payload. Tests cover exposed
surface completeness, palette, recesses, feet, controls and placement.

`green_bookshelf.vox` is the small green bookcase beside the larger blue
bookcase in the same room. Its 24 x 12 x 28 voxel model has a recessed shelf,
four separate yellow books and a lower drawer. It fits x32..48, z32..40,
height16 in room pixels, against the back wall. The frame and shelf edges
use the cabinet's green material: the sprite's dark shadow bands are not
painted onto the 3D model. Both authored props use a thin grey outer
contour and a lighter inner edge, matching the neighbouring bookcase's
edging while retaining their green and gold materials. The original outline owns
only furniture pixels, including the stepped corners; the wall and floor
remain separate. The custom-prop tests check the books' gaps, shelf depth,
palette, exposed surface and placement. The VOX file is bundled with the
release generator, just like the table.

`yellow_table.vox` is the 40 x 32 x 28 voxel table made from the supplied
yellow-table reference. It replaces the flat table in
`LAYOUT_RUSTBORO_CITY_HOUSE`, at cells (5,4) through (6,5).

`voxel_custom_props.py` reads its actual palette and voxels, merges adjacent
exposed faces, and fits it to the existing table's 28 x 22 pixel footprint
and 9 pixel height. Original map collisions are unchanged. The rug decals
remain beneath the model. This replacement is local to this room.

The normal building proof still verifies the original room decomposition,
including removal of the old table image. Export and previews then substitute
the authored mesh. This intentionally changes the original GBA projection;
the original-art pixel proof is not a visual-equivalence test of this asset.
`tests/voxel_custom_props_test.py` verifies its palette, open space between
the four legs, exposed surface coverage, dimensions and mesh budget.
