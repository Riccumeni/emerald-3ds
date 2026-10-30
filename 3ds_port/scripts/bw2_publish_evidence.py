"""Assemble reviewed local captures into one Pokemon/move dossier.

This does not mark work complete. bw2_progress.py independently validates the
result before changing the persistent checklist.
"""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def archive_build(source, build_id):
    # Optional BW2 data is intentionally outside the engine ABI/build ID.
    # Distinguish binaries carrying different optional data by their hash too.
    target = ROOT / "artifacts/bw2-validation/builds" / (build_id + "_" + sha(source)[:12]) / source.name
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if sha(target) != sha(source):
            raise ValueError("Archived build ID collision")
    else:
        shutil.copy2(source, target)
    return target.relative_to(ROOT).as_posix()


def publish(args):
    state = json.loads((ROOT / "docs/bw2-plan/stato.json").read_text(encoding="utf-8"))
    key = "numero_nazionale" if args.kind == "pokemon" else "id_emerald"
    item = next(i for i in state[args.kind] if i[key] == args.id)
    folder = ROOT / item["cartella"]
    directions = ("front", "back") if args.kind == "pokemon" else ("player", "opponent")
    sources = (args.first.resolve(), args.second.resolve())
    palette_sources = tuple(p.resolve() if p else None for p in (args.shiny_first, args.shiny_second))
    reports = []
    metadata = dict(kind=args.kind, id=args.id, nome=item["nome"], id_emerald=item["id_emerald"] if args.kind == "pokemon" else args.id,
                    date=datetime.now().isoformat(timespec="seconds"), visual_reviewed=args.reviewed,
                    directions={}, forms_complete=not item.get("forme_da_verificare", False),
                    emulator="Azahar, isolated workspace executable and copied SD",
                    settings={"speed": 1, "resolution_scale": 1, "voxel": 1, "voxel_battle": 0, "stereo": False},
                    hardware_verified=False, audio_verified=False,
                    source_hashes={name: sha(ROOT / name) for name in (
                        "3ds_port/src/3ds_bw2_battle.c", "3ds_port/src/3ds_video.c",
                        "3ds_port/src/3ds_cycle_test.c", "3ds_port/scripts/gen_bw2_battle.py")})
    emulator = ROOT / "build/bw2-azahar/bw2-test.exe"
    emulator_log = ROOT / "build/bw2-azahar/user/log/azahar_log.txt"
    version = re.search(r"Azahar Version: (.+)", emulator_log.read_text(encoding="utf-8", errors="replace"))
    metadata["emulator_details"] = dict(version=version.group(1) if version else "unknown",
        executable_sha256=sha(emulator), client_sha256=sha(Path("D:/Emulators/Azahar/scripting/AzaharRPC.py")))
    for direction, source, palette_source in zip(directions, sources, palette_sources):
        report = json.loads((source / "capture.json").read_text(encoding="utf-8"))
        if not report["passed"]:
            raise ValueError("Failed capture " + str(source))
        target = folder / direction
        for name in ("screenshot.png", "demo.mp4", "capture.json", "qa-start.png", "qa-middle.png", "qa-end.png"):
            shutil.copy2(source / name, target / name)
        metadata["directions"][direction] = dict(scenario=report["scenario"],
            source_capture=source.relative_to(ROOT).as_posix(), screenshot_sha256=sha(target / "screenshot.png"),
            video_sha256=sha(target / "demo.mp4"), video=report["video"],
            visual_review_frames=[direction + "/" + name for name in ("qa-start.png", "qa-middle.png", "qa-end.png", "screenshot.png")])
        if args.kind == "pokemon":
            if palette_source is None:
                raise ValueError("Shiny capture required for both views")
            shutil.copy2(palette_source / "screenshot.png", target / "shiny.png")
            shutil.copy2(palette_source / "capture.json", target / "shiny-capture.json")
        reports.append(report)
    if (reports[0]["build_id"] != reports[1]["build_id"]
            or reports[0]["binary_sha256"] != reports[1]["binary_sha256"]):
        raise ValueError("Directions were captured from different validation builds")
    metadata["test_build"] = {"build_id": reports[0]["build_id"], "sha256": reports[0]["binary_sha256"],
                              "path": "build/bw2-validation/validation.3dsx", "flags": "CTR_BW2_VALIDATION"}
    validation = ROOT / metadata["test_build"]["path"]
    if sha(validation) != metadata["test_build"]["sha256"]:
        raise ValueError("Keep the matching validation binary before publishing")
    metadata["test_build"]["path"] = archive_build(validation, reports[0]["build_id"])
    metadata["test_build"]["elf_path"] = archive_build(validation.with_suffix(".elf"), reports[0]["build_id"])
    production = ROOT / "build/bw2-validation/Emerald3DS-BW2.3dsx"
    metadata["production_build"] = {"build_id": (ROOT / "build/bw2-validation/production-build-id.bin").read_bytes()[:8].hex(),
                                    "sha256": sha(production), "path": production.relative_to(ROOT).as_posix(),
                                    "validation_flags_present": False}
    metadata["production_build"]["path"] = archive_build(production, metadata["production_build"]["build_id"])
    assets = ROOT / "build/upstream/3ds_port/romfs/bw2"
    manifest = json.loads((assets / "manifest.json").read_text(encoding="utf-8"))
    metadata["rom_sha256"] = manifest["rom_sha256"]
    metadata["rom_code"] = manifest["rom_code"]
    if args.kind == "pokemon":
        metadata["asset_hashes"] = {f"{item['id_emerald']}_{side}{ext}": sha(assets / f"{item['id_emerald']}_{side}{ext}") for side in directions for ext in ('.bin', '.bin.layout')}
        metadata["presentation_algorithm"] = "height-source-footprint-v5.1-front-headroom"
        metadata["adaptations"] = ["64x64 indexed source canvas; bounded height-based scale; front silhouette floor, back time-weighted opaque pixel mass centered on its visible arena; rear-view perspective 130-150% according to height",
                                    "Height from Emerald Pokedex plus shared front/back BW2 footprint; bounded correction 80-125%, 15% dead band, fades out for giants; front extent <=104, back extent <=126 logical pixels; source enlargement may exceed 200% only if opaque bounds fit the 128x128 affine envelope, with a two-pixel margin",
                                    "Rear-view placement independent of the message box: lower body may be covered by the text; native default sprite center instead of move aiming coordinate"]
        metadata["adaptations"].append("Front highest pose remains four logical pixels inside the viewport, accounting for elevation while preserving its arena floor")
        metadata["presentation"] = {direction: report.get("presentation", []) for direction, report in zip(directions, reports)}
        checks = "Ingresso e almeno due cicli completi front/back registrati; palette shiny confrontate con gli asset; pose e copertura inferiore da parte del testo controllate."
    else:
        metadata["asset_hashes"] = {f"move_{args.id}.bin": sha(assets / f"move_{args.id}.bin")}
        metadata["adaptations"] = manifest["adaptations"]
        checks = "Mossa eseguita dal giocatore e dall'avversario con un solo turno reale per scenario; ritorno al menu verificato. L'altro battler usa Splash per isolare la direzione."
    if item.get('forme_da_verificare',False):
        from bw2_variants import check_variants
        metadata['variants_audit']=check_variants(ROOT,item,metadata['test_build'])
        metadata['forms_complete']=True
    if args.kind=='pokemon' and args.id==327:
        metadata['asset_hashes']['308_front.bin.spots']=sha(assets/'308_front.bin.spots')
    if args.kind=='pokemon' and args.id==201:
        for form in range(1,28):
            for side in directions:
                for ext in ('.bin','.bin.layout'):
                    name=f'201_form{form}_{side}{ext}'
                    metadata['asset_hashes'][name]=sha(assets/name)
        metadata['adaptations'].append('All 28 Unown forms selected by the native Emerald personality macro; BW2 alternate resources mapped through the ROM personal-table sprite offset. Separate form/view cache keys; no new species or gameplay rules.')
    if args.kind=='pokemon' and args.id==351:
        for form in range(1,4):
            for side in directions:
                for ext in ('.bin','.bin.layout'):
                    name=f'385_form{form}_{side}{ext}'
                    metadata['asset_hashes'][name]=sha(assets/name)
    if args.kind=='pokemon' and args.id==386:
        for side in directions:
            for ext in ('.bin','.bin.layout'):
                name=f'410_form3_{side}{ext}'
                metadata['asset_hashes'][name]=sha(assets/name)
        metadata['adaptations'].append('Emerald Deoxys selection: own untransformed back Speed; opponent, transformed copies and remote multi partner Normal. Normal and Speed have separate native front/back art inventories; Attack/Defense excluded by Emerald rules. Actual link runtime remains pending.')
    (folder / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    text = f"# Verifica: {item['nome']}\n\n{checks}\n\n"
    text += f"Build di prova: `{metadata['test_build']['build_id']}`. Build normale senza automatismi: `{metadata['production_build']['build_id']}`.\n\n"
    text += "Gli screenshot e i video sono fotogrammi nativi del gioco in esecuzione, acquisiti via RPC locale a velocita' 1x. Ogni MP4 e' stato decodificato interamente per controllare durata e variazione dei frame.\n\n"
    text += "Revisione visiva: ingresso, fotogramma centrale, finale e screenshot significativo. Impostazioni e hash sono in `metadata.json`; andamento dei frame/scenario nei rispettivi `capture.json`.\n\n"
    for direction, report in zip(directions, reports):
        text += f"- {direction}: {report['video']['duration']:.2f} secondi, {report['video']['decoded_frames']} frame, {report['video']['average_fps']:.2f} fps; [screenshot]({direction}/screenshot.png), [video]({direction}/demo.mp4).\n"
    text += "\nAdattamenti dichiarati:\n\n" + "\n".join("- " + a for a in metadata["adaptations"]) + "\n"
    text += "\nLimiti: camera Emerald e presentazione adattata; audio non registrato (DSP firmware assente nel setup di prova); prestazioni su console, stereo e doppi ancora da validare nella fase di integrazione.\n"
    if metadata.get('variants_audit'):
        text+='\nVerifiche aggiuntive delle forme/personality: [registro con percorsi e seed](variants.json). Tutti i casi richiesti sono stati controllati indipendentemente prima della chiusura.\n'
    (folder / "verifica.md").write_text(text, encoding="utf-8")
    print(folder)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--kind", choices=("pokemon", "mosse"), required=True)
    p.add_argument("--id", type=int, required=True)
    p.add_argument("--first", type=Path, required=True, help="Front or player capture directory")
    p.add_argument("--second", type=Path, required=True, help="Back or opponent capture directory")
    p.add_argument("--shiny-first", type=Path)
    p.add_argument("--shiny-second", type=Path)
    p.add_argument("--reviewed", action="store_true", required=True)
    publish(p.parse_args())
