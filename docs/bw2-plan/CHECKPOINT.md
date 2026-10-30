# Punto di ripresa — 2026-10-30T11:19:37

Stato: richiesta checkpoint 30–39 conclusa; piano generale da proseguire. Completati **314/386 Pokemon** e **6/354 mosse**, con dossier verificati.

- Piano e registri: `docs/BW2_ANIMATION_PLAN.md`, `docs/bw2-plan/stato.json` e le due checklist.
- Dossier permanenti: `artifacts/bw2-validation/`; i dati grandi restano locali e ignorati da Git.
- Unita' in corso: `null`. Ultima chiusa: `{"tipo": "pokemon", "id": 159, "nome": "Croconaw"}`.
- Prossima unita' da affrontare: `{"tipo": "pokemon", "id": 160, "nome": "Feraligatr", "azione": "Implementare/verificare e chiudere il dossier nelle due direzioni"}`.
- Tutti i dossier pilota sono chiusi; continuare dalla prossima unita' indicata sopra.
- Inventario `docs/bw2-plan/INVENTORY.json`: 772 viste base senza incompatibilita' di formato rilevate; solo 53/354 script accettati dal decoder attuale. Non significa che siano gia' importati/verificati. Forme ancora da censire.
- `3ds_port/scripts/emu/run_bw2_validation.ps1`: avvia solo l'emulatore isolato; `bw2_capture.py` registra fotogrammi nativi via RPC, a 1x, in MP4/H.264 con timestamp reali e verifica la decodifica.
- Dipendenza PyAV locale in `build/bw2-python/`; Python runtime Codex. Acquisizioni native tramite API RPC locale dell’emulatore isolato.
- Banco prova `CTR_BW2_VALIDATION` in `3ds_cycle_test.c`; mailbox esposta via simboli ELF, comando 1 esegue un turno reale, configurazione `bw2-validation.txt` sulla SD isolata.
- Build prova/ELF/ID: `build/bw2-validation/validation.{3dsx,elf}`, `build_id.bin`. Build normale: `build/bw2-validation/Emerald3DS-BW2.3dsx`, `production-build-id.bin`. Le prove usano l'ELF copiato, mai quello sovrascritto da una build successiva.
- Emulatore isolato: `build/bw2-azahar/bw2-test.exe`; PID in `build/bw2-validation/emulator.pid`. Non chiudere l'Azahar originale dell'utente. Durante la registrazione la finestra di prova deve renderizzare: minimizzarla puo' causare timeout.
- Acquisizioni grezze e report: `build/bw2-validation/`. I metadati di ciascun dossier indicano le acquisizioni effettive; quelle precedenti sono storiche. Scala e appoggio: `docs/BW2_POKEMON_LAYOUT.md`.
- Prima di marcare fatto: ispezionare screenshot e fotogrammi QA, assemblare con `bw2_publish_evidence.py --reviewed`, poi `bw2_progress.py --action complete --kind pokemon|mosse --id N`. Il secondo comando controlla hash, direzioni e completamento del turno.
- Correzione aggiuntiva: flush Citro2D durante il ritaglio degli attori, per non ripetere pixel sotto il textbox; verificata nei nuovi video. Non usare le acquisizioni senza `final` precedenti a questa correzione.
- Test dedicati di bridge, esportatore e integrita' dossier passati; build normale verificata con CtrCycle_Frame/Input da 4 byte. Suite generale preesistente bloccata dai test bottom-map: non dichiararla passata.
- ROM sorgente `D:/Projects/pokebw2/black2.nds` solo letta; non resettare lo staging o le modifiche locali preesistenti.

Prima della nuova unita' controllare contesto/budget; salvare processi e sessioni attivi in questo checkpoint se serve interrompere. Non segnare mai completo un dossier parziale.

Nota persistente: Richiesta conclusa: 10/10 checkpoint 30–39, 80 nuove specie; 314/386 Pokémon e 6/354 mosse. Nessuna unità in corso. Audit indipendente AUTONOMOUS30_39_AUDIT.json: 320 dossier; 978 asset precedenti, 345 file locali preesistenti e 129660 file sorgente BW2 invariati; ROM preservata. Bridge e criterio v5/v5.1 invariati, inventario forme Castform/Deoxys e macchie Spinda preservati. Build normale e di prova distinte, con binari/ELF/ID e SHA archiviati nel registro e nei dossier. Emulatore isolato chiuso dopo uscita effettiva; nessuna cattura attiva. Azahar personale preservato. Dieci commit dedicati, nessun push. Prossima unità: Feraligatr, nazionale/Emerald 160. Prove Azahar 1×; audio/DSP, console reale, stereo, doppi, link reale e interazioni speciali restano nella fase d’integrazione. Suite generale bottom-map con problemi preesistenti, non dichiarata superata. Riepilogo e prove: AUTONOMOUS30_39_REVIEW.md.
