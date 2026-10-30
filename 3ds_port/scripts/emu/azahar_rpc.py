"""Read Azahar's running game directly through its bundled local RPC client.

Examples:
  python azahar_rpc.py status
  python azahar_rpc.py capture --output build/live/azahar.png

Enable the emulator's RPC server once in its debug settings. This helper
uses process listing, performance reads and native frame capture. The
state command reads only Emerald's map/build identifiers through ELF
symbols. It does not send desktop input or write game memory.
"""

import argparse
import importlib.util
import json
from pathlib import Path
import struct
import subprocess
import sys


def load_client(path):
    spec = importlib.util.spec_from_file_location("installed_azahar_rpc", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load Azahar's bundled RPC client")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.AzaharRPC


def game_state(rpc, processes, root, nm):
    stage = root / "build/upstream"
    elf = stage / "3ds_port/emerald3ds.elf"
    output = subprocess.check_output([str(nm), "--defined-only", "-n", str(elf)], text=True)
    names = {"gMapHeader", "gSaveBlock1Ptr", "sBuildId", "sBackend"}
    symbols = {}
    for line in output.splitlines():
        fields = line.split()
        if len(fields) == 3 and fields[2] in names:
            if fields[2] in symbols:
                raise RuntimeError("Ambiguous ELF symbol: " + fields[2])
            symbols[fields[2]] = int(fields[0], 16)
    if set(symbols) != names:
        raise RuntimeError("Required Emerald symbols are missing")
    games = [pid for pid, (_, name) in processes.items() if name.startswith("emerald")]
    if len(games) != 1:
        raise RuntimeError("Expected exactly one running Emerald process")
    rpc.set_process(games[0])
    expected = (stage / "3ds_port/romfs/engine/build_id.bin").read_bytes()[:8]
    loaded = rpc.read_memory(symbols["sBuildId"], 8)
    if loaded is None:
        raise RuntimeError("Cannot read running build ID")
    result = {"loaded_build": loaded.hex(), "built_build": expected.hex(),
              "symbols_match": loaded == expected}
    if loaded != expected:
        result["next_step"] = "Reload the built game before reading map state with these ELF symbols."
        return result
    header = rpc.read_memory(symbols["gMapHeader"], 28)
    pointer = rpc.read_memory(symbols["gSaveBlock1Ptr"], 4)
    if header is None or pointer is None:
        raise RuntimeError("Cannot read map identifiers")
    save, = struct.unpack("<I", pointer)
    if not 0x100000 <= save < 0x40000000:
        raise RuntimeError("Invalid save-block pointer")
    location = rpc.read_memory(save + 4, 2)
    if location is None:
        raise RuntimeError("Cannot read map location")
    group, number = location
    layout_id, = struct.unpack_from("<H", header, 18)
    groups = json.loads((stage / "data/maps/map_groups.json").read_text())
    layouts = json.loads((stage / "data/layouts/layouts.json").read_text())["layouts"]
    map_name = groups[groups["group_order"][group]][number]
    layout = layouts[layout_id - 1]
    declared = json.loads((stage / "data/maps" / map_name / "map.json").read_text())["layout"]
    if declared != layout["id"]:
        raise RuntimeError("Runtime map and layout identifiers disagree")
    backend = rpc.read_memory(symbols["sBackend"], 4)
    backend = struct.unpack("<I", backend)[0] if backend else 0
    result.update(map=map_name, group=group, number=number, layout=layout["id"],
                  layout_id=layout_id, size=[layout["width"], layout["height"]],
                  data_backend={1: "romfs", 2: "loose", 3: "pak"}.get(backend, "unknown"))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("status", "capture", "state"))
    parser.add_argument("--client", type=Path,
                        default=Path("D:/Emulators/Azahar/scripting/AzaharRPC.py"))
    parser.add_argument("--output", type=Path, default=Path("build/live/azahar.png"))
    parser.add_argument("--scale", type=int, default=0)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--nm", type=Path, default=Path(
        "D:/Emulators/DevelopmentFiles/devkitPro/devkitARM/bin/arm-none-eabi-nm.exe"))
    args = parser.parse_args()
    rpc = None
    try:
        client = load_client(args.client)
        rpc = client(address="127.0.0.1", timeout=1, retries=0)
        processes = rpc.process_list()
        result = {"connected": True, "endpoint": "127.0.0.1:45987", "processes": processes}
        if args.command == "state":
            result["game"] = game_state(rpc, processes, args.root, args.nm)
        elif args.command == "capture":
            if not hasattr(rpc, "screenshot"):
                raise RuntimeError("This bundled client does not support native screenshots")
            png = rpc.screenshot(res_scale=args.scale)
            if not png.startswith(b"\x89PNG\r\n\x1a\n"):
                raise RuntimeError("Emulator returned an invalid PNG")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(png)
            result["image"] = str(args.output.resolve())
        else:
            result["performance"] = rpc.perf_stats() if hasattr(rpc, "perf_stats") else None
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, TimeoutError, RuntimeError, ValueError) as exc:
        print(json.dumps({"connected": False, "error": str(exc),
                          "next_step": "Enable Azahar's RPC server in its debug settings, then retry."}))
        return 1
    finally:
        if rpc is not None:
            rpc.socket.close()


if __name__ == "__main__":
    sys.exit(main())
