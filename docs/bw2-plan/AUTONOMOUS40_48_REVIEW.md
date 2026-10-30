# Nove checkpoint autonomi — 40–48

Completati **9/9 checkpoint** richiesti, nell’ordine del piano. Partenza: 314 Pokémon. Obiettivo: 386. Totale corrente: **386/386 Pokémon, 6/354 mosse**. Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi.

| Checkpoint | Specie | Stato | Prove |
|---|---|---|---|
| 1/9 (gruppo 40) | Feraligatr, Sentret, Furret, Hoothoot, Noctowl, Ledyba, Ledian, Spinarak | complete | [Dossier, screenshot e video](CHECKPOINT40_REVIEW.md) |
| 2/9 (gruppo 41) | Ariados, Cleffa, Togepi, Togetic, Mareep, Flaaffy, Ampharos, Sudowoodo | complete | [Dossier, screenshot e video](CHECKPOINT41_REVIEW.md) |
| 3/9 (gruppo 42) | Politoed, Hoppip, Skiploom, Jumpluff, Aipom, Sunkern, Sunflora, Yanma | complete | [Dossier, screenshot e video](CHECKPOINT42_REVIEW.md) |
| 4/9 (gruppo 43) | Wooper, Quagsire, Espeon, Umbreon, Murkrow, Slowking, Misdreavus, Unown | complete | [Dossier, screenshot e video](CHECKPOINT43_REVIEW.md) |
| 5/9 (gruppo 44) | Pineco, Forretress, Dunsparce, Gligar, Steelix, Snubbull, Granbull, Qwilfish | complete | [Dossier, screenshot e video](CHECKPOINT44_REVIEW.md) |
| 6/9 (gruppo 45) | Scizor, Shuckle, Sneasel, Teddiursa, Ursaring, Swinub, Piloswine, Remoraid | complete | [Dossier, screenshot e video](CHECKPOINT45_REVIEW.md) |
| 7/9 (gruppo 46) | Octillery, Delibird, Mantine, Houndour, Houndoom, Porygon2, Stantler, Smeargle | complete | [Dossier, screenshot e video](CHECKPOINT46_REVIEW.md) |
| 8/9 (gruppo 47) | Tyrogue, Hitmontop, Smoochum, Elekid, Magby, Miltank, Blissey, Raikou | complete | [Dossier, screenshot e video](CHECKPOINT47_REVIEW.md) |
| 9/9 (gruppo 48) | Entei, Suicune, Larvitar, Pupitar, Tyranitar, Lugia, Ho Oh, Celebi | complete | [Dossier, screenshot e video](CHECKPOINT48_REVIEW.md) |

Le specie vengono segnate come fatte soltanto dopo prove front/back e shiny, revisione visiva e verifica dei dossier. Ogni gruppo completo è salvato in un commit dedicato; i messaggi Git identificano il numero di checkpoint. ROM, asset e filmati restano locali secondo la politica artifacts.

[Piano](../BW2_ANIMATION_PLAN.md) · [Registro](AUTONOMOUS40_48.json) · [Checkpoint di ripresa](CHECKPOINT.md).

## Audit conclusivo

[Audit indipendente](AUTONOMOUS40_48_AUDIT.json): **392 dossier** (386 Pokémon e 6 mosse), più le varianti richieste. Nuove acquisizioni: 72 scenari ordinari front/back e 56 video aggiuntivi Unown normali/shiny, con ingresso e due cicli, più 72 controlli palette shiny. Totale nuovo: **99934 fotogrammi**, **3330.20 secondi a 1×**. PNG integrali 400×480 e H.264/yuv420p permanenti.

[Unown: tutte le 28 forme e prove](UNOWN_REVIEW.md): mappatura da sorgente e ROM effettive, personality native Emerald, selezione e pixel/palette verificati, due attori Unown diversi negli incontri aggiuntivi e quattro attori nei test host. A nel dossier principale, altre in forms/. Scala, trasparenze, ancoraggio, ingresso e pose dei video normali/shiny ispezionati prima della chiusura indipendente.

Preservati byte per byte 1294 asset precedenti e 345 file locali preesistenti, comprese modifiche UI/bag/voxel, file non tracciati e checklist mosse. Preservati 129660 file BW2, ROM e stato Git sorgente. Criterio v5/v5.1 e macchie Spinda invariati; Castform, Deoxys e riaggancio dopo Trasformazione superano le regressioni.

- **Prova**: ID `5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`. [3DSX](../../artifacts/bw2-validation/builds/5f8ed2ae5815137f_f4bbbe0e09bc/validation.3dsx) · [ELF](../../artifacts/bw2-validation/builds/5f8ed2ae5815137f_a9eb96860bd4/validation.elf) · [ID](../../artifacts/bw2-validation/builds/5f8ed2ae5815137f_34cc04fdffc3/build_id.bin).
- **Normale**: ID `c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`. [3DSX](../../artifacts/bw2-validation/builds/c18abb147273c4ca_5f1a359e9eb5/Emerald3DS-BW2.3dsx) · [ELF](../../artifacts/bw2-validation/builds/c18abb147273c4ca_3fc9f061c443/production.elf) · [ID](../../artifacts/bw2-validation/builds/c18abb147273c4ca_3f6d91c230ee/production-build-id.bin).

Build normale senza automatismi/mailbox, CtrCycle_Frame/Input da 4 byte; comandi reali delle due modalità verificati. Test passati: bridge sintetico/reale, Spinda, Castform, Deoxys normale/diagnostico e Trasformazione; 22 test esportatore, 7 dossier, 24 varianti precedenti, 13 test di integrità Unown e test host Unown su selezione/palette/cache/pixel.

Limiti: Azahar 1×; audio/DSP, console reale, stereo, doppi, link reale e integrazione delle interazioni speciali da verificare. Suite generale bottom-map con problemi preesistenti, non dichiarata superata. Emulatore isolato chiuso dopo uscita effettiva; Azahar personale preservato. Nessun push.

## Commit dedicati

| Checkpoint | Commit |
|---|---|
| 40 | `977a956` |
| 41 | `dfba38c` |
| 42 | `3a36b00` |
| 43 | `513f3ed` |
| 44 | `ff57184` |
| 45 | `e71f7a6` |
| 46 | `e1688a1` |
| 47 | `1fd304f` |
| 48 | Commit finale identificato dal messaggio `Complete autonomous BW2 checkpoint 48: eight Pokemon` (hash in git log) |

Il catalogo Pokémon è chiuso; restano **348 mosse** e le verifiche di integrazione. [Preparazione checkpoint 49](CHECKPOINT49_PREPARATION.md): 53 script accettati dal decoder, 47 ancora non completati, soltanto 6 mosse effettivamente importate e verificate. Proposta iniziale: Karate Chop, Vice Grip, Cut, Stomp, Peck, Slam, Swords Dance, Recover; dipendenze e interventi tecnici documentati. Nessun aumento del contatore mosse.
