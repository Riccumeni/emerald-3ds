"""Inventory Emerald's BW2 source resources without changing/exporting them.

The move scan reports compatibility with the current restricted decoder;
unsupported scripts are explicitly unresolved, never counted as implemented.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("bw2_export", Path(__file__).with_name("gen_bw2_battle.py"))
bw = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = bw
spec.loader.exec_module(bw)


def tracks(data):
    b = bw.block(data, b"KNBA")
    count, _, sequences, frames, _ = struct.unpack_from("<HHIII", b)
    result = []
    for i in range(count):
        n, loop, kind, mode, off = struct.unpack_from("<HHIII", b, sequences + i * 16)
        duration = sum(bw.u16(b, frames + off + j * 8 + 4) for j in range(n))
        result.append(dict(frames=n, loop_start=loop, kind=kind, mode=mode, duration=duration))
    return result


def inventory(args):
    state = json.loads((ROOT / "docs/bw2-plan/stato.json").read_text(encoding="utf-8"))
    nds = bw.Nds(args.rom)
    mons = nds.archive("a/0/0/4")
    scripts = nds.archive("a/0/6/5")
    pokemon = []
    for item in sorted(state["pokemon"], key=lambda x: x["numero_nazionale"]):
        n = item["numero_nazionale"]
        result = dict(numero_nazionale=n, id_emerald=item["id_emerald"], nome=item["nome"], views={})
        for side, offset in (("front", 0), ("back", 9)):
            base = n * 20 + offset
            try:
                chars = bw.block(mons[base + 2], b"RAHC")
                cells = tracks(mons[base + 5])
                multi = tracks(mons[base + 7])
                issues = []
                if bw.u32(chars, 16) != 16384:
                    issues.append("texture_size_not_supported")
                if any(t["mode"] not in (1, 2) or t["kind"] & 255 not in (0, 1, 2) for t in cells + multi):
                    issues.append("animation_mode_or_kind_not_supported")
                if multi and multi[0]["duration"] > 1024:
                    issues.append("idle_exceeds_current_tick_limit")
                result["views"][side] = dict(resource_base=base, texture_bytes=bw.u32(chars, 16),
                                             cell_tracks=cells, multi_tracks=multi, format_issues=issues,
                                             rendered_and_verified=False)
            except (ValueError, IndexError, struct.error) as error:
                result["views"][side] = dict(error=str(error), rendered_and_verified=False)
        pokemon.append(result)
    moves = []
    first_errors = Counter()
    for item in sorted(state["mosse"], key=lambda x: x["id_emerald"]):
        n = item["id_emerald"]
        data = scripts[n]
        result = dict(id_emerald=n, nome=item["nome"], bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                      header_entries=sorted(set(struct.unpack_from("<14I", data, 4))) if len(data) >= 60 else [],
                      rendered_and_verified=False)
        try:
            commands = bw.decode_script(data)
            result.update(current_decoder_accepts=True, opcodes=sorted(set(op for _, op, _ in commands)),
                          particle_dependencies=sorted(set((a[0], a[1]) for _, op, a in commands if op in (7, 9))))
        except (ValueError, struct.error) as error:
            result.update(current_decoder_accepts=False, first_unresolved=str(error))
            first_errors[str(error).split(" at ")[0]] += 1
        moves.append(result)
    summary = dict(pokemon=len(pokemon), views=len(pokemon) * 2, moves=len(moves),
                   views_with_format_issues=sum(bool(v.get("format_issues") or v.get("error"))
                                               for p in pokemon for v in p["views"].values()),
                   moves_accepted_by_current_decoder=sum(m["current_decoder_accepts"] for m in moves),
                   first_unresolved_errors=dict(first_errors),
                   note="Format scan only: accepted decoding does not imply complete renderer/runtime support; alternative forms still need mapping.")
    report = dict(rom_code=nds.code, rom_sha256=hashlib.sha256(nds.data).hexdigest(),
                  summary=summary, pokemon=pokemon, mosse=moves)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rom", type=Path, required=True)
    p.add_argument("--output", type=Path, default=ROOT / "docs/bw2-plan/INVENTORY.json")
    inventory(p.parse_args())
