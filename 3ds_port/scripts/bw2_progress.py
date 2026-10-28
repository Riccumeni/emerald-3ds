"""Update the persistent BW2 plan; completion requires real, reviewed dossiers."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "docs/bw2-plan"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_dossier(item, kind):
    folder = ROOT / item["cartella"]
    metadata = json.loads((folder / "metadata.json").read_text(encoding="utf-8"))
    if not metadata.get("visual_reviewed"):
        raise ValueError("Review the actual recorded frames before completing the unit")
    if not (folder / "verifica.md").is_file():
        raise ValueError("Missing verification notes")
    directions = ("front", "back") if kind == "pokemon" else ("player", "opponent")
    for direction in directions:
        proof = metadata["directions"][direction]
        report = json.loads((folder / direction / "capture.json").read_text(encoding="utf-8"))
        if not report.get("passed"):
            raise ValueError("Capture failed: " + direction)
        if sha(folder / direction / "screenshot.png") != report["screenshot_sha256"]:
            raise ValueError("Screenshot changed: " + direction)
        if sha(folder / direction / "demo.mp4") != report["video"]["sha256"]:
            raise ValueError("Video changed: " + direction)
        if (proof["screenshot_sha256"] != report["screenshot_sha256"]
                or proof["video_sha256"] != report["video"]["sha256"]):
            raise ValueError("Metadata does not match recorded media: " + direction)
        if report["build_id"] != metadata["test_build"]["build_id"]:
            raise ValueError("Mismatched capture build: " + direction)
        if report.get("binary_sha256") != metadata["test_build"].get("sha256"):
            raise ValueError("Mismatched capture binary: " + direction)
        if kind == "pokemon":
            side = 1 if direction == "front" else 0
            species = report["scenario"]["enemy" if side else "player"]
            if species != item["id_emerald"] or report["kind"] != "idle":
                raise ValueError("Wrong Pokemon/direction")
            palette = json.loads((folder / direction / "shiny-capture.json").read_text(encoding="utf-8"))
            if (not palette["passed"] or palette["build_id"] != metadata["test_build"]["build_id"]
                    or not any(a["species"] == item["id_emerald"] and a["battler"] == side and a["shiny"] for a in palette["actors"])):
                raise ValueError("Shiny verification missing")
            if sha(folder / direction / "shiny.png") != palette["screenshot_sha256"]:
                raise ValueError("Shiny screenshot changed")
            if item["forme_da_verificare"] and not metadata.get("forms_complete"):
                raise ValueError("Forms/personality audit incomplete")
        else:
            side = 0 if direction == "player" else 1
            if report["kind"] != "move" or report["scenario"]["side"] != side or not report["turn_completed_at"]:
                raise ValueError("Wrong direction or turn did not complete")
            if not any(e["move"] == item["id_emerald"] and e["attacker"] == side for e in report["events"]):
                raise ValueError("Requested move not demonstrated")
        item["prove"][direction].update(stato="verificato", build_verificata=report["build_id"],
                                         screenshot_sha256=proof["screenshot_sha256"], video_sha256=proof["video_sha256"])
    if kind=='pokemon' and item['forme_da_verificare']:
        from bw2_variants import check_variants
        check_variants(ROOT,item,metadata['test_build'])
    return metadata


def refresh(state):
    for kind, filename, title, directions in (("pokemon", "POKEMON.md", "Pokémon", "front/back"),
                                               ("mosse", "MOVES.md", "mosse", "giocatore/avversario")):
        items = state[kind]
        done = sum(i["fatto"] for i in items)
        key = "pokemon_fatti" if kind == "pokemon" else "mosse_fatte"
        state["contatori"][key] = done
        text = f"# Checklist {title}\n\nTotale: **{len(items)}**. Fatti con dossier completo: **{done}**.\n\n"
        text += "Ogni casella richiede implementazione, prova nel gioco e screenshot/video nelle due direzioni.\n\n[Piano](../BW2_ANIMATION_PLAN.md) · [Registro](stato.json)\n\n"
        for item in items:
            n = item["numero_nazionale"] if kind == "pokemon" else item["id_emerald"]
            status = "FATTO" if item["fatto"] else item["stato"].replace("_", " ")
            text += f"- [{'x' if item['fatto'] else ' '}] {n:04d} **{item['nome']}** — {status}; {directions}; [prove](../../{item['cartella']}/).\n"
        (PLAN / filename).write_text(text, encoding="utf-8")
    pending_pilots = [(kind, i) for kind in ("pokemon", "mosse") for i in state[kind]
                      if i["implementazione_prototipo"] and not i["fatto"]]
    pending = pending_pilots or [("pokemon", i) for i in state["pokemon"] if not i["fatto"]]
    if not pending:
        pending = [("mosse", i) for i in state["mosse"] if not i["fatto"]]
    if pending:
        kind, item = pending[0]
        state["prossima_unita"] = {"tipo": kind, "id": item["numero_nazionale"] if kind == "pokemon" else item["id_emerald"],
                                   "nome": item["nome"], "azione": "Implementare/verificare e chiudere il dossier nelle due direzioni"}
    else:
        state["prossima_unita"] = None
    state["fase_corrente"] = "0_validazione_pilota" if pending_pilots else "1_catalogo_e_pokemon"
    production = ROOT / "build/bw2-validation/Emerald3DS-BW2.3dsx"
    production_id = ROOT / "build/bw2-validation/production-build-id.bin"
    if production.is_file() and production_id.is_file():
        state["ultima_build_normale"] = {"percorso": production.relative_to(ROOT).as_posix(),
                                        "build_id": production_id.read_bytes()[:8].hex(), "sha256": sha(production)}
    main = ROOT / "docs/BW2_ANIMATION_PLAN.md"
    text = main.read_text(encoding="utf-8")
    text = text.replace("Stato: piano preparato; espansione non iniziata.", "Stato: esecuzione in corso; avanzamento nelle checklist collegate.")
    text = re.sub(r"(\| Pokémon \| 386 \|[^\n]*\| )\d+( \|)",
                  lambda m: m[1] + str(state["contatori"]["pokemon_fatti"]) + m[2], text)
    text = re.sub(r"(\| Mosse \| 354 \|[^\n]*\| )\d+( \|)",
                  lambda m: m[1] + str(state["contatori"]["mosse_fatte"]) + m[2], text)
    main.write_text(text, encoding="utf-8")
    state["aggiornato_il"] = datetime.now().isoformat(timespec="seconds")
    (PLAN / "stato.json").write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    counts = state["contatori"]
    index = "# Prove verificate delle animazioni BW2\n\n"
    index += f"Completati: **{counts['pokemon_fatti']}/386 Pokemon**, **{counts['mosse_fatte']}/354 mosse**.\n\n"
    for kind, label, directions in (("pokemon", "Pokemon", ("front", "back")),
                                     ("mosse", "Mosse", ("player", "opponent"))):
        index += f"## {label}\n\n| Unita' | Prima direzione | Seconda direzione | Verifica |\n|---|---|---|---|\n"
        for item in state[kind]:
            if not item["fatto"]:
                continue
            links = []
            base = "../../" + item["cartella"]
            for direction in directions:
                links.append(f"{direction}: [PNG]({base}/{direction}/screenshot.png), [MP4]({base}/{direction}/demo.mp4)")
            index += f"| {item['nome']} | {links[0]} | {links[1]} | [Note]({base}/verifica.md) |\n"
        index += "\n"
    (PLAN / "EVIDENCE.md").write_text(index.rstrip() + "\n", encoding="utf-8")
    checkpoint = f"# Punto di ripresa — {state['aggiornato_il']}\n\n"
    checkpoint += f"Stato: esecuzione in corso. Completati **{counts['pokemon_fatti']}/386 Pokemon** e **{counts['mosse_fatte']}/354 mosse**, con dossier verificati.\n\n"
    checkpoint += "- Piano e registri: `docs/BW2_ANIMATION_PLAN.md`, `docs/bw2-plan/stato.json` e le due checklist.\n"
    checkpoint += "- Dossier permanenti: `artifacts/bw2-validation/`; i dati grandi restano locali e ignorati da Git.\n"
    checkpoint += f"- Unita' in corso: `{json.dumps(state.get('unita_in_corso'), ensure_ascii=False)}`. Ultima chiusa: `{json.dumps(state.get('ultimo_completato'), ensure_ascii=False)}`.\n"
    checkpoint += f"- Prossima unita' da affrontare: `{json.dumps(state.get('prossima_unita'), ensure_ascii=False)}`.\n"
    checkpoint += ("- Chiudere prima i dossier pilota ancora incompleti, poi seguire l'ordine del piano.\n" if pending_pilots else
                   "- Tutti i dossier pilota sono chiusi; continuare dalla prossima unita' indicata sopra.\n")
    checkpoint += "- Inventario `docs/bw2-plan/INVENTORY.json`: 772 viste base senza incompatibilita' di formato rilevate; solo 53/354 script accettati dal decoder attuale. Non significa che siano gia' importati/verificati. Forme ancora da censire.\n"
    checkpoint += "- `3ds_port/scripts/emu/run_bw2_validation.ps1`: avvia solo l'emulatore isolato; `bw2_capture.py` registra fotogrammi nativi via RPC, a 1x, in MP4/H.264 con timestamp reali e verifica la decodifica.\n"
    checkpoint += "- Dipendenza PyAV locale in `build/bw2-python/`; Python runtime Codex. UI Windows non disponibile in questa sessione (errore kernel assets); usare l'API locale dell'emulatore.\n"
    checkpoint += "- Banco prova `CTR_BW2_VALIDATION` in `3ds_cycle_test.c`; mailbox esposta via simboli ELF, comando 1 esegue un turno reale, configurazione `bw2-validation.txt` sulla SD isolata.\n"
    checkpoint += "- Build prova/ELF/ID: `build/bw2-validation/validation.{3dsx,elf}`, `build_id.bin`. Build normale: `build/bw2-validation/Emerald3DS-BW2.3dsx`, `production-build-id.bin`. Le prove usano l'ELF copiato, mai quello sovrascritto da una build successiva.\n"
    checkpoint += "- Emulatore isolato: `build/bw2-azahar/bw2-test.exe`; PID in `build/bw2-validation/emulator.pid`. Non chiudere l'Azahar originale dell'utente. Durante la registrazione la finestra di prova deve renderizzare: minimizzarla puo' causare timeout.\n"
    checkpoint += "- Acquisizioni grezze e report: `build/bw2-validation/`. I metadati di ciascun dossier indicano le acquisizioni effettive; quelle precedenti sono storiche. Scala e appoggio: `docs/BW2_POKEMON_LAYOUT.md`.\n"
    checkpoint += "- Prima di marcare fatto: ispezionare screenshot e fotogrammi QA, assemblare con `bw2_publish_evidence.py --reviewed`, poi `bw2_progress.py --action complete --kind pokemon|mosse --id N`. Il secondo comando controlla hash, direzioni e completamento del turno.\n"
    checkpoint += "- Correzione aggiuntiva: flush Citro2D durante il ritaglio degli attori, per non ripetere pixel sotto il textbox; verificata nei nuovi video. Non usare le acquisizioni senza `final` precedenti a questa correzione.\n"
    checkpoint += "- Test dedicati di bridge, esportatore e integrita' dossier passati; build normale verificata con CtrCycle_Frame/Input da 4 byte. Suite generale preesistente bloccata dai test bottom-map: non dichiararla passata.\n"
    checkpoint += "- ROM sorgente `D:/Projects/pokebw2/black2.nds` solo letta; non resettare lo staging o le modifiche locali preesistenti.\n"
    checkpoint += "\nPrima della nuova unita' controllare contesto/budget; salvare processi e sessioni attivi in questo checkpoint se serve interrompere. Non segnare mai completo un dossier parziale.\n"
    if state.get("checkpoint_note"):
        checkpoint += "\nNota persistente: " + state["checkpoint_note"] + "\n"
    (PLAN / "CHECKPOINT.md").write_text(checkpoint, encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--kind", choices=("pokemon", "mosse"))
    p.add_argument("--id", type=int)
    p.add_argument("--action", choices=("begin", "complete", "refresh"), default="refresh")
    args = p.parse_args()
    state = json.loads((PLAN / "stato.json").read_text(encoding="utf-8"))
    if args.action != "refresh":
        if args.kind is None or args.id is None:
            p.error("--kind and --id required")
        id_key = "numero_nazionale" if args.kind == "pokemon" else "id_emerald"
        item = next(i for i in state[args.kind] if i[id_key] == args.id)
        if args.action == "begin":
            if item["fatto"]:
                raise ValueError("Unit already completed; invalidate its evidence explicitly before reopening")
            item["stato"] = "in_corso"
            state["unita_in_corso"] = {"tipo": args.kind, "id": args.id, "nome": item["nome"]}
        else:
            metadata = check_dossier(item, args.kind)
            item.update(stato="fatto", fatto=True, completato_il=datetime.now().isoformat(timespec="seconds"),
                        build_verificata=metadata["test_build"]["build_id"])
            state["ultimo_completato"] = {"tipo": args.kind, "id": args.id, "nome": item["nome"]}
            state["unita_in_corso"] = None
            if args.kind=='pokemon' and item.get('forme_da_verificare'):
                special=next(case for case in state['casi_speciali'] if case['numero_nazionale']==args.id)
                special.update(stato='fatto',fatto=True,prove=item['cartella']+'/variants.json')
                variants=PLAN/'VARIANTS.md'
                variants.write_text(variants.read_text(encoding='utf-8').replace('- [ ] **'+item['nome'],'- [x] **'+item['nome']),encoding='utf-8')
    refresh(state)
    print(json.dumps(state["contatori"]))


if __name__ == "__main__":
    main()
