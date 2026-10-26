# Working on the running game

For visual feedback, first inspect Azahar directly rather than asking the
user to attach a screenshot. The installed Computer Use plugin can observe
the window. Prefer native RPC frame capture when its server is enabled:

```text
python 3ds_port/scripts/emu/azahar_rpc.py status
python 3ds_port/scripts/emu/azahar_rpc.py state
python 3ds_port/scripts/emu/azahar_rpc.py capture --output build/live/azahar.png
```

The helper uses the client bundled with the installed emulator at
`D:/Emulators/Azahar/scripting/AzaharRPC.py`, connecting to localhost only.
Before associating an asset with a room, run `state`: it checks the loaded
build ID against the current ELF, then reads the actual map group, map
number and layout ID. Cross-checks with the source map tables reject
inconsistent identifiers. Similar furniture occurs in different houses:
the kitchen visible on 2026-10-26 was Flat2 1F (layout294), not the Cutter's
house (layout98). Visual similarity alone is not a placement identifier.
It reads the process list, performance statistics and a PNG frame directly
from Azahar. It does not depend on foreground window focus. It does not
provide keyboard input, restart or live model reload: those remain separate
operations. The emulator's RPC server must first be enabled in its debug
settings; the helper reports a failed connection rather than pretending a
cached picture is live.

The local connection was verified on 2026-10-26 with Azahar 2126.2:
the RPC server is enabled, process/performance requests succeed and native
PNG frame capture works while the game is running. Use the capture command
for feedback such as "look at the sink"; no user-uploaded image is needed.

The current editable game source is `build/upstream/3ds_port`. Authoritative
port sources and VOX assets live in the top-level `3ds_port`; sync changed
files into the editable source before generating and building. The game the
user opens in Azahar is `D:/Emulators/Azahar/games/emerald3ds.3dsx`. Update
that copy after a successful build and verify its hash matches the built
file. The game must reload the new executable to display embedded changes.

The configured restart shortcut here is F6. It was verified through Computer
Use on 2026-10-26: after copying the build, F6 reloaded it, `state` matched
the new build ID and layout294, and native capture showed the three authored
kitchen props in the running Flat2 room. Verify the loaded build and a live
frame after reloading. The same session then moved to Flat2 2F (layout295):
always query the current map again when the user refers to the current scene.

Use a native frame from the running game to validate the current camera and
map whenever available. Software renders of `buildings.bin` validate the
exported art and geometry; label them as previews, not emulator screenshots.
