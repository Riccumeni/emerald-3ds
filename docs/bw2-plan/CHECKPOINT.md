# Punto di ripresa — 2026-10-28T21:16:26

Stato: esecuzione in corso. Completati **114/386 Pokemon** e **6/354 mosse**, con dossier verificati.

- Piano e registri: `docs/BW2_ANIMATION_PLAN.md`, `docs/bw2-plan/stato.json` e le due checklist.
- Dossier permanenti: `artifacts/bw2-validation/`; i dati grandi restano locali e ignorati da Git.
- Unita' in corso: `null`. Ultima chiusa: `{"tipo": "pokemon", "id": 28, "nome": "Sandslash"}`.
- Prossima unita' da affrontare: `{"tipo": "pokemon", "id": 327, "nome": "Spinda", "azione": "Implementare/verificare e chiudere il dossier nelle due direzioni"}`.
- Tutti i dossier pilota sono chiusi; continuare dalla prossima unita' indicata sopra.
- Inventario `docs/bw2-plan/INVENTORY.json`: 772 viste base senza incompatibilita' di formato rilevate; solo 53/354 script accettati dal decoder attuale. Non significa che siano gia' importati/verificati. Forme ancora da censire.
- `3ds_port/scripts/emu/run_bw2_validation.ps1`: avvia solo l'emulatore isolato; `bw2_capture.py` registra fotogrammi nativi via RPC, a 1x, in MP4/H.264 con timestamp reali e verifica la decodifica.
- Dipendenza PyAV locale in `build/bw2-python/`; Python runtime Codex. UI Windows non disponibile in questa sessione (errore kernel assets); usare l'API locale dell'emulatore.
- Banco prova `CTR_BW2_VALIDATION` in `3ds_cycle_test.c`; mailbox esposta via simboli ELF, comando 1 esegue un turno reale, configurazione `bw2-validation.txt` sulla SD isolata.
- Build prova/ELF/ID: `build/bw2-validation/validation.{3dsx,elf}`, `build_id.bin`. Build normale: `build/bw2-validation/Emerald3DS-BW2.3dsx`, `production-build-id.bin`. Le prove usano l'ELF copiato, mai quello sovrascritto da una build successiva.
- Emulatore isolato: `build/bw2-azahar/bw2-test.exe`; PID in `build/bw2-validation/emulator.pid`. Non chiudere l'Azahar originale dell'utente. Durante la registrazione la finestra di prova deve renderizzare: minimizzarla puo' causare timeout.
- Acquisizioni grezze e report: `build/bw2-validation/`. I metadati di ciascun dossier indicano le acquisizioni effettive; quelle precedenti sono storiche. Scala e appoggio: `docs/BW2_POKEMON_LAYOUT.md`.
- Prima di marcare fatto: ispezionare screenshot e fotogrammi QA, assemblare con `bw2_publish_evidence.py --reviewed`, poi `bw2_progress.py --action complete --kind pokemon|mosse --id N`. Il secondo comando controlla hash, direzioni e completamento del turno.
- Correzione aggiuntiva: flush Citro2D durante il ritaglio degli attori, per non ripetere pixel sotto il textbox; verificata nei nuovi video. Non usare le acquisizioni senza `final` precedenti a questa correzione.
- Test dedicati di bridge, esportatore e integrita' dossier passati; build normale verificata con CtrCycle_Frame/Input da 4 byte. Suite generale preesistente bloccata dai test bottom-map: non dichiararla passata.
- ROM sorgente `D:/Projects/pokebw2/black2.nds` solo letta; non resettare lo staging o le modifiche locali preesistenti.

Prima della nuova unita' controllare contesto/budget; salvare processi e sessioni attivi in questo checkpoint se serve interrompere. Non segnare mai completo un dossier parziale.

Nota persistente: Richiesta conclusa: 5/5 checkpoint (10–14), 40 nuovi Pokémon, da 74 a 114/386; mosse 6/354. Ogni specie chiusa singolarmente dopo prove native front/back, ingresso e due cicli, palette shiny e revisione visiva. Criterio v5.1 invariato. Audit finale: 120 dossier, 317 asset precedenti e 344 file locali estranei invariati; SHA-256 ROM sorgente verificato. Riepilogo: AUTONOMOUS10_14_REVIEW.md; audit: AUTONOMOUS10_14_AUDIT.json. Build prova 35c62b2e2f40bcd4 e normale 78ea4c127e93ed58 archiviate con ELF, ID e SHA-256; normale senza mailbox e con stub Frame/Input da 4 byte. Acquisizioni terminate; nessun processo isolato attivo, Azahar personale preservato. Prossima unità: Spinda (nazionale 327, ID Emerald 308), con macchie procedurali da verificare; prossimo gruppo 15. AUTONOMOUS5.json e AUTONOMOUS10_14.json sono registri conclusi: non riaprirli. Cinque commit dedicati, nessun push. Audio, console reale, stereo e doppi restano da verificare.
