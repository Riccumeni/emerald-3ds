# Punto di ripresa — 2026-10-28T17:20:13

Stato: esecuzione in corso. Completati **34/386 Pokemon** e **6/354 mosse**, con dossier verificati.

- Piano e registri: `docs/BW2_ANIMATION_PLAN.md`, `docs/bw2-plan/stato.json` e le due checklist.
- Dossier permanenti: `artifacts/bw2-validation/`; i dati grandi restano locali e ignorati da Git.
- Unita' in corso: `null`. Ultima chiusa: `{"tipo": "pokemon", "id": 283, "nome": "Surskit"}`.
- Prossima unita' da affrontare: `{"tipo": "pokemon", "id": 284, "nome": "Masquerain", "azione": "Implementare/verificare e chiudere il dossier nelle due direzioni"}`.
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

Nota persistente: Commit3f239cf salvato: motore e strumenti BW2, piano completo e algoritmo v5 approvato; selezionati solo45file/hunk pertinenti, altre modifiche UI/voxel e conversioni EOL conservate. Nuovo gruppo276–283 completato singolarmente: Taillow304,Swellow305,Wingull309,Pelipper310,Ralts392,Kirlia393,Gardevoir394,Surskit311. Totale34/386Pokemon e6/354mosse. Algoritmo v5 invariato;125assetprecedenti invariati (SHA-256). Export68viste/34specie,6mosse15effetti. Report docs/bw2-plan/BATCH4_REVIEW.md, misure BATCH4_MEASUREMENTS.json. Acquisizioni batch4-* e batch4-shiny-* concluse (job74155 completato); revisionati8pose/ciclo più QAstart/mid/end/poster per8scenari e8shiny. Raccolta artifacts/bw2-validation/batch4-taillow-surskit-2026-10-28/pokemon.mp4:272.657s,8178frame, concat nativa senza tagli/ricodifica/accelerazione. Buildtest f2ecf4d5e40cf598 SHA8f0bbf00cc6618af733f2a60b1cbab3908d83696ce72372dc80d761fccbf1616 e normale c4d710a45a166c54 SHA2e04cc3c8fc17d3aff9eaa92f5f3ecbc0a738532e744b83be81d29beae2b8303 archiviate conELF; buildnormale e copieprototype aggiornate, Frame/Input4byte, mailbox assente. Audit40dossier passati e7testdossier passati. Nessun nuovo codice runtime o nuova mossa in questo gruppo. Commit dell’avanzamento: consultare git log; include soltanto i file BW2. ProssimoPokemon Masquerain284. Emulatoreisolato chiuso, nessuna registrazione o build pendente; non toccareAzaharutente/pokebw2/ROM. Non bootstrap/reset/push. Prima di un nuovo gruppo verificare contesto e salvarecheckpoint.
