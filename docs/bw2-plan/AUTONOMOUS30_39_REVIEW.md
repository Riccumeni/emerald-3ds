# Dieci checkpoint autonomi — 30–39

Completati **10/10 checkpoint** richiesti, nell’ordine del piano. Partenza: 234 Pokémon. Obiettivo: 314. Totale corrente: **314/386 Pokémon, 6/354 mosse**. Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi.

| Checkpoint | Specie | Stato | Prove |
|---|---|---|---|
| 1/10 (gruppo 30) | Paras, Parasect, Venonat, Venomoth, Diglett, Dugtrio, Meowth, Persian | complete | [Dossier, screenshot e video](CHECKPOINT30_REVIEW.md) |
| 2/10 (gruppo 31) | Mankey, Primeape, Growlithe, Arcanine, Poliwag, Poliwhirl, Poliwrath, Bellsprout | complete | [Dossier, screenshot e video](CHECKPOINT31_REVIEW.md) |
| 3/10 (gruppo 32) | Weepinbell, Victreebel, Ponyta, Rapidash, Slowpoke, Slowbro, Farfetchd, Seel | complete | [Dossier, screenshot e video](CHECKPOINT32_REVIEW.md) |
| 4/10 (gruppo 33) | Dewgong, Shellder, Cloyster, Gastly, Haunter, Gengar, Onix, Drowzee | complete | [Dossier, screenshot e video](CHECKPOINT33_REVIEW.md) |
| 5/10 (gruppo 34) | Hypno, Krabby, Kingler, Exeggcute, Exeggutor, Cubone, Marowak, Hitmonlee | complete | [Dossier, screenshot e video](CHECKPOINT34_REVIEW.md) |
| 6/10 (gruppo 35) | Hitmonchan, Lickitung, Chansey, Tangela, Kangaskhan, Mr Mime, Scyther, Jynx | complete | [Dossier, screenshot e video](CHECKPOINT35_REVIEW.md) |
| 7/10 (gruppo 36) | Electabuzz, Magmar, Tauros, Lapras, Ditto, Eevee, Vaporeon, Jolteon | complete | [Dossier, screenshot e video](CHECKPOINT36_REVIEW.md) |
| 8/10 (gruppo 37) | Flareon, Porygon, Omanyte, Omastar, Kabuto, Kabutops, Aerodactyl, Snorlax | complete | [Dossier, screenshot e video](CHECKPOINT37_REVIEW.md) |
| 9/10 (gruppo 38) | Articuno, Zapdos, Moltres, Dratini, Dragonair, Dragonite, Mewtwo, Mew | complete | [Dossier, screenshot e video](CHECKPOINT38_REVIEW.md) |
| 10/10 (gruppo 39) | Chikorita, Bayleef, Meganium, Cyndaquil, Quilava, Typhlosion, Totodile, Croconaw | complete | [Dossier, screenshot e video](CHECKPOINT39_REVIEW.md) |

Le specie vengono segnate come fatte soltanto dopo prove front/back e shiny, revisione visiva e verifica dei dossier. Ogni gruppo completo è salvato in un commit dedicato; i messaggi Git identificano il numero di checkpoint. ROM, asset e filmati restano locali secondo la politica artifacts.

[Piano](../BW2_ANIMATION_PLAN.md) · [Registro](AUTONOMOUS30_39.json) · [Checkpoint di ripresa](CHECKPOINT.md).

## Audit conclusivo

[Audit indipendente](AUTONOMOUS30_39_AUDIT.json): **320 dossier** (314 Pokémon e 6 mosse), 80 nuovi scenari front/back e 80 shiny. 67572 fotogrammi nativi, 2251.86 secondi a 1×; intervallo acquisizione 29.978–30.037 fps. Ogni video include ingresso e almeno due cicli; screenshot PNG integrali 400×480 e H.264/yuv420p permanenti.

Preservati byte per byte 978 asset già presenti e 345 file locali preesistenti, incluse modifiche UI/bag/voxel, file non tracciati e checklist mosse. 129660 file BW2 e ROM preservati; stato Git sorgente invariato. Nessun reset, clean, stash, bootstrap o push. Bridge completo invariato rispetto alla baseline; forme Castform/Deoxys e sidecar Spinda mantenuti.

- **Prova**: ID `de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`. [3DSX](../../artifacts/bw2-validation/builds/de509bec1e539760_f2ecde88d6d6/validation.3dsx) · [ELF](../../artifacts/bw2-validation/builds/de509bec1e539760_84f94a734784/validation.elf) · [ID](../../artifacts/bw2-validation/builds/de509bec1e539760_59fb21cf6a34/build_id.bin).
- **Normale**: ID `f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`. [3DSX](../../artifacts/bw2-validation/builds/f65244ae7f660a26_6b27f2290acf/Emerald3DS-BW2.3dsx) · [ELF](../../artifacts/bw2-validation/builds/f65244ae7f660a26_a4ef3f5f2b4c/production.elf) · [ID](../../artifacts/bw2-validation/builds/f65244ae7f660a26_d673eb861184/production-build-id.bin).

Normale senza mailbox di validazione, `CtrCycle_Frame/Input` da 4 byte. Test pertinenti passati: bridge sintetico e reale, oracolo Spinda (otto personality), Castform, Deoxys normale e diagnostico, riaggancio Trasformazione; 20 test esportatore, 7 dossier e 24 varianti. I dettagli e i log sono nel registro.

Limiti: Azahar a 1×; audio/DSP non acquisito; console, stereo, doppi, link reale e integrazione delle interazioni speciali restano da validare. La suite generale bottom-map ha problemi preesistenti e non è dichiarata superata. Le mosse restano **6/354**. Emulatore isolato chiuso; Azahar personale preservato.

## Commit dedicati

| Checkpoint | Commit |
|---|---|
| 30 | `36d7783` |
| 31 | `53c13f9` |
| 32 | `951f3da` |
| 33 | `192b12f` |
| 34 | `be5a257` |
| 35 | `be4afa8` |
| 36 | `1861fdd` |
| 37 | `427092c` |
| 38 | `27a3dd6` |
| 39 | Commit finale identificato dal messaggio `Complete autonomous BW2 checkpoint 39: eight Pokemon` (hash in `git log`) |

Prossima unità del piano: **Feraligatr**, nazionale/Emerald 160.
