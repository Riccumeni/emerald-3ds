# Punto di ripresa — 2026-10-28T18:02:49

Stato: esecuzione in corso. Completati **50/386 Pokemon** e **6/354 mosse**, con dossier verificati.

- Piano e registri: `docs/BW2_ANIMATION_PLAN.md`, `docs/bw2-plan/stato.json` e le due checklist.
- Dossier permanenti: `artifacts/bw2-validation/`; i dati grandi restano locali e ignorati da Git.
- Unita' in corso: `null`. Ultima chiusa: `{"tipo": "pokemon", "id": 296, "nome": "Makuhita"}`.
- Prossima unita' da affrontare: `{"tipo": "pokemon", "id": 297, "nome": "Hariyama", "azione": "Implementare/verificare e chiudere il dossier nelle due direzioni"}`.
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

Nota persistente: Richiesta esplicita: completare5checkpoint consecutivi in autonomia, non terminare prima di5/5. AUTONOMOUS5.json è il registro esatto: 2/5 chiusi, target34->74Pokemon,6mosse. Gruppo corrente/riferimento 6 (Alakazam,Nincada,Ninjask,Shedinja,Whismur,Loudred,Exploud,Makuhita). Gruppo6 concluso con prove e audit; commit dedicato identificabile da git log. Prossimo gruppo: 7. Build e processi in AUTONOMOUS5.json. Tutte40specie già esportate in una build comune;148viste candidate/74specie,6mosse15effetti,157assetprecedenti invariati. Algoritmo v5 approvato invariato; source/BWL2/hash sono nelle prove. Parent capture:build/bw2-auto5-capture.ps1, logbuild/bw2-auto5-captures.log,80scenari8idle+8shiny pergruppo,prefixcp05..cp09. Controllare processi o sessioni inAUTONOMOUS5.json; non avviare un secondo emulatore simultaneo. Helperbuild/bw2-auto5.py:render(n),palette(n),mark(normal/shiny dopo ispezione),publish(ids),finish(n),commit(n),start(n+1),status. Non sovrascrivere validation.3dsx/ELF/ID e normale comuni durante le prove. Ogni Pokemon completo solo dopo QA e shiny; ogni gruppo richiede report,misure,audit e commitBW2. Proseguire fino al quinto gruppo, senza fermarsi a un checkpoint intermedio. Salvare checkpoint prima di nuovo gruppo se contesto scarso; no reset/bootstrap/push, noROMpokebw2 oAzaharutente.
