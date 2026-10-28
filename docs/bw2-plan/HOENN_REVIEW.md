# Verifica del gruppo Silcoon–Shiftry

Resoconto della prima chiusura del gruppo con la scala v4. La successiva [revisione v5 delle dimensioni](V5_REVIEW.md) aggiorna Lombre, Nuzleaf, Seedot e Shiftry e le altre specie influenzate dal nuovo criterio. Per le prove correnti usare i dossier e l'[indice](EVIDENCE.md).

Completati **10 nuovi Pokémon**, ciascuno segnato come fatto subito dopo la chiusura del proprio dossier. Totale del piano: **26/386 Pokémon**, **6/354 mosse**. Prossimo Pokémon: **Taillow**.

![Dieci nuovi Pokémon, nelle due direzioni](../../artifacts/bw2-validation/batch3-hoenn-2026-10-28/pokemon.png)

[Filmato completo](../../artifacts/bw2-validation/batch3-hoenn-2026-10-28/pokemon.mp4): dieci incontri con lati invertiti, 325.96 secondi e 9777 fotogrammi. Concatenazione dei video nativi, senza tagli, ricodifica o accelerazione. Gli screenshot della raccolta ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video front/back, oltre a screenshot e controllo delle palette shiny.

| Pokémon | Nazionale / Emerald | Altezza | Scala front / back | Dossier |
|---|---|---:|---:|---|
| Beautifly | 267 / 292 | 1.0 m | 123.05% / 184.77% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0267_beautifly/verifica.md) |
| Silcoon | 266 / 291 | 0.6 m | 127.73% / 178.91% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0266_silcoon/verifica.md) |
| Cascoon | 268 / 293 | 0.7 m | 121.48% / 171.88% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0268_cascoon/verifica.md) |
| Dustox | 269 / 294 | 1.2 m | 128.12% / 186.33% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0269_dustox/verifica.md) |
| Lombre | 271 / 296 | 1.2 m | 148.05% / 200.00% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0271_lombre/verifica.md) |
| Lotad | 270 / 295 | 0.5 m | 135.55% / 175.39% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0270_lotad/verifica.md) |
| Ludicolo | 272 / 297 | 1.5 m | 134.77% / 186.33% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0272_ludicolo/verifica.md) |
| Seedot | 273 / 298 | 0.5 m | 160.16% / 200.00% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0273_seedot/verifica.md) |
| Nuzleaf | 274 / 299 | 1.0 m | 127.34% / 198.05% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0274_nuzleaf/verifica.md) |
| Shiftry | 275 / 300 | 1.3 m | 129.69% / 186.33% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0275_shiftry/verifica.md) |

Le percentuali sono trasformazioni del canvas esportato 64×64, non rapporti fra le stature dei Pokémon. L’algoritmo v4 usa altezza Pokédex di Emerald e ingombro della sequenza; non è stato cambiato per queste specie. Il back mantiene il centro della massa visibile nell’arena e può essere coperto inferiormente dal testo, come richiesto. [Misure lette dalla build](HOENN3_MEASUREMENTS.json).

Durante la revisione sono comparsi frammenti della testa ripetuti sopra Lombre e Ludicolo. Le immagini esportate dalla ROM erano pulite: una riga del riempimento del cielo restava visibile alla giunzione con la scena. `BattleSkyCompose` ora sovrappone una riga logica alla scena, coprendo la giunzione arrotondata senza spostare o ridimensionare il Pokémon. Tutte le prove finali del gruppo sono state registrate dopo questa correzione.

Il controllo della riga 17, colonne 230–319, dopo la stabilizzazione, rilevava pixel scuri in 551/577 frame di Lombre e 783/783 di Ludicolo. Nelle nuove registrazioni il conteggio è 0/577 e 0/783 nella stessa regione. È una verifica mirata della giunzione; la revisione visiva comprende anche pose, ingresso, fotogrammi centrali, finali e screenshot dei dieci incontri. [Confronto Lombre](../../artifacts/bw2-validation/batch3-hoenn-2026-10-28/sky-lotad-lombre.png), [confronto Ludicolo](../../artifacts/bw2-validation/batch3-hoenn-2026-10-28/sky-seedot-ludicolo.png), [misure e hash dei video](../../artifacts/bw2-validation/batch3-hoenn-2026-10-28/sky-review.json).

Le dieci catture finali attestano l’avanzamento di entrambi gli attori per almeno due cicli completi, a velocità 1×, con decodifica integrale degli MP4. Dieci ulteriori scenari verificano le palette shiny su entrambi i lati. I dossier vengono chiusi solo dopo revisione delle immagini e verifica automatica di hash, build e direzioni. Sette test della procedura dossier passati. Nessuna nuova mossa è stata aggiunta in questo gruppo.

Build di prova **225550ffd296ea83** (SHA-256 `ca1c8f4d23198dc9b37941f6081b1f91352444ef213d5a667dde01dfddb69035`); build normale **1fb87fe7b2e7373d** (`888370dbf95b2c508fda4fcb4a0d32a3770dfd7eac473fbde08b57692b41cd6d`). Binari ed ELF di prova archiviati nei percorsi indicati nei metadati. La build normale ha gli stub `CtrCycle_Frame` e `CtrCycle_Input` da quattro byte e non contiene `gCtrBw2Validation`.

Limiti delle prove: emulatore Azahar 2126.2 a risoluzione nativa; audio non acquisito nel setup senza DSP. Console fisica, stereo, doppi e casi speciali restano nella fase d’integrazione.

[Piano](../BW2_ANIMATION_PLAN.md) · [Indice di tutte le prove](EVIDENCE.md) · [Checkpoint](CHECKPOINT.md).
