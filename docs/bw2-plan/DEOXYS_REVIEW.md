# Deoxys: selezione Emerald, forma Normale e Velocità

Chiusa una sola specie, nazionale **386 / Emerald 410**. Le due forme selezionate dai percorsi battaglia di Emerald hanno risorse BW2 distinte. Nessuna regola, statistica o mossa è stata sostituita con quelle di BW2.

| Contesto | Forma | Verifica |
|---|---|---|
| Pokémon proprio, back, non trasformato | Velocità | Incontro ordinario, ingresso, due cicli e shiny |
| Avversario, front | Normale | Incontro ordinario, ingresso, due cicli e shiny |
| Copia trasformata | Normale | Due turni reali separati di Trasformazione, normale e shiny, ritorno al menu e due cicli |
| Compagno remoto in lotta multi | Normale | Predicato originale Emerald compilato nel test host; esecuzione link reale ancora da verificare |
| Copie temporanee delle mosse | Secondo ShouldIgnoreDeoxysForm(5, battler) | Rami del predicato verificati sul host; integrazione visiva delle relative mosse ancora nella loro fase |

La selezione segue `BattleLoadPlayerMonSpriteGfx`, `BattleLoadOpponentMonSpriteGfx`, `ShouldIgnoreDeoxysForm` e il campo `transformSpecies` dell'albero locale. La forma Velocità è il secondo fotogramma delle risorse originali Emerald, scelto da `DuplicateDeoxysTiles`; il normale resta nel primo. Le forme Attacco e Difesa appartengono agli altri giochi e non vengono introdotte.

Il censimento BW2 legge `a/0/1/6[386]`: offset sprite 30, quattro forme, flag 0. La base normale è `386*20=7720`; Velocità usa `0x3584+(30+2)*20=14340`. Palette normali e shiny vengono lette dalle risorse della forma. L'inventario incrementale conserva anche Castform.

## Prove native e anteprime diagnostiche delle forme

Il dossier principale registra il comportamento ordinario di Emerald: front Normale e back Velocità. Per verificare anche l'arte delle angolazioni alternative, il banco di prova espone esplicitamente `deoxys_preview=1|2`: è un'anteprima diagnostica dei disegni, esclusa dalla build normale. Non viene presentata come una transizione di gameplay. Ogni forma ha un video nativo con ingresso e due cicli nelle due viste, PNG integrali e controllo shiny.

- **Normale**: [front PNG](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/normal/front/screenshot.png), [front MP4](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/normal/front/demo.mp4), [back PNG](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/normal/back/screenshot.png), [back MP4](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/normal/back/demo.mp4), [shiny front](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/normal/front/shiny.png), [shiny back](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/normal/back/shiny.png).
- **Velocità**: [front PNG](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/speed/front/screenshot.png), [front MP4](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/speed/front/demo.mp4), [back PNG](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/speed/back/screenshot.png), [back MP4](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/speed/back/demo.mp4), [shiny front](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/speed/front/shiny.png), [shiny back](../../artifacts/bw2-validation/pokemon/0386_deoxys/forms/speed/back/shiny.png).

![Palette delle due forme](../../artifacts/bw2-validation/pokemon/0386_deoxys/cp25-deoxys-palettes.png)

[Rassegna di otto pose per scenario](../../artifacts/bw2-validation/pokemon/0386_deoxys/cp25-deoxys-review.png).

## Trasformazione e integrità

Ditto è una risorsa ausiliaria di prova e resta da completare nel piano. Il recorder chiede al vero controller di eseguire la mossa 144 una sola volta, con Splash dall'altro lato. Attende il completamento reale del turno e il ritorno al menu, poi registra almeno due cicli della copia Normale. La versione shiny ripete il turno in un incontro separato. Il recorder non scrive specie, forma, statistiche, risultato o palette nella memoria del gioco. Trasformazione mantiene l'animazione Emerald e non viene contata fra le mosse BW2 importate.

- **normal**: [PNG](../../artifacts/bw2-validation/pokemon/0386_deoxys/interactions/transform-normal/screenshot.png), [MP4](../../artifacts/bw2-validation/pokemon/0386_deoxys/interactions/transform-normal/demo.mp4), [rapporto](../../artifacts/bw2-validation/pokemon/0386_deoxys/interactions/transform-normal/capture.json); 38.47s, 1154 fotogrammi, turno completato a 27.03s.
- **shiny**: [PNG](../../artifacts/bw2-validation/pokemon/0386_deoxys/interactions/transform-shiny/screenshot.png), [MP4](../../artifacts/bw2-validation/pokemon/0386_deoxys/interactions/transform-shiny/demo.mp4), [rapporto](../../artifacts/bw2-validation/pokemon/0386_deoxys/interactions/transform-shiny/capture.json); 38.96s, 1169 fotogrammi, turno completato a 27.50s.

L'oracolo legge i pixel effettivi dei battler e le palette dal processo isolato: devono coincidere con il fotogramma della clip BW2 selezionata. La verifica indipendente dei dossier rifiuta forma errata, preview usata al posto dell'incontro ordinario, actor non shiny, un solo ciclo, turno mancante, build diversa o media alterati.

I test host compilano la funzione originale Emerald, controllano proprietà del battler locale/remoto e rami link/multi, selezione normale/trasformata, tutte le clip front/back, cache condivisa e riuso, palette e rilascio. Le equazioni di presentazione v5.1 restano identiche: l'impronta front/back è condivisa entro ciascuna forma; le due viste del dossier principale raffigurano forme diverse.

Build **Prova**: [`1441ec92f9e6b9b6`](../../artifacts/bw2-validation/builds/1441ec92f9e6b9b6_aab76a7b3322/validation.3dsx), SHA-256 `aab76a7b3322e46be17cb62dbf3366706d1fa2e7e8105615dbccfb6d50a269ca`.

Build **Normale**: [`3724fc8cdfba9514`](../../artifacts/bw2-validation/builds/3724fc8cdfba9514_31a8bb0a85c2/Emerald3DS-BW2.3dsx), SHA-256 `31a8bb0a85c2d0f4b69be3129b3c2283c9a759e90485e0d15eda5149aca5319a`.

La build normale esclude mailbox, input di validazione e selettore diagnostico; Frame/Input restano stub da quattro byte. Test pertinenti: 20 esportatore, 7 dossier, 24 varianti, bridge sintetico e reale, oracolo Spinda, Castform e Deoxys. Restano da verificare esecuzione link reale, console, audio/DSP, stereo, doppi e l'integrazione completa delle interazioni speciali nella rispettiva fase.

[Inventario e hash delle prove](../../artifacts/bw2-validation/pokemon/0386_deoxys/variants.json) · [Metadati principali](../../artifacts/bw2-validation/pokemon/0386_deoxys/metadata.json) · [Checkpoint 25](CHECKPOINT25_REVIEW.md).

## Correzione del ripristino dopo Trasformazione

La prova reale ha trovato che `AnimTask_TransformMon` modifica direttamente la grafica, saltando i loader intercettati: al termine del turno restava una copia GBA statica e il vecchio attore Ditto era disabilitato. Il bridge ora attende la conclusione dell'animazione nativa, controlla che specie trasformata/party e specie visualizzata coincidano, poi registra nuovamente l'attore e riprende i cicli BW2. La correzione gestisce anche il ripristino della specie originale; il test conserva il blocco delle incoerenze di specie non spiegate.

Il nuovo test host verifica attesa durante l'effetto, riaggancio, avanzamento e ripristino. Sono ripassati bridge sintetico/reale, Castform e oracolo Spinda. Una ulteriore [Trasformazione reale verso Spinda](../../artifacts/bw2-validation/regressions/2026-10-29-deoxys-transform/spinda/demo.mp4), con [rapporto e oracolo texture](../../artifacts/bw2-validation/regressions/2026-10-29-deoxys-transform/spinda/capture.json), verifica il comportamento con una specie già completata senza sostituire le sue macchie procedurali.

![Prima e dopo il turno e regressione Spinda](../../artifacts/bw2-validation/pokemon/0386_deoxys/cp25-native-transform-review.png)

Il file Make aggiuntivo `3ds_port/bw2_validation.mk` applica il flag di prova anche al bridge: `make -f Makefile -f bw2_validation.mk TEST_FLAGS=-DCTR_BW2_VALIDATION`. La build normale lascia il flag vuoto. Entrambi i sorgenti bridge/cycle sono ricompilati al cambio di modalità; il comando del compilatore e l'assenza dei simboli di prova nel normale sono verificati. I file Make preesistenti restano intatti.

Le sette altre specie del checkpoint25 conservano la prima coppia di build valida. Deoxys usa la coppia finale corretta per tutte le sue prove. Acquisizioni e build precedenti sono conservate nella cronologia, comprese le prove diagnostiche non superate; non vengono conteggiate come completamenti.
