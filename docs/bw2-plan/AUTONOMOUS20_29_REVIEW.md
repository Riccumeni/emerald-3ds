# Dieci checkpoint autonomi — 20–29

Completati **10/10 checkpoint** richiesti, nell’ordine del piano. Partenza: 154 Pokémon. Obiettivo: 234. Totale corrente: **234/386 Pokémon, 6/354 mosse**. Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi.

| Checkpoint | Specie | Stato | Prove |
|---|---|---|---|
| 1/10 (gruppo 20) | Ninetales, Pichu, Pikachu, Raichu, Psyduck, Golduck, Wynaut, Wobbuffet | complete | [Dossier, screenshot e video](CHECKPOINT20_REVIEW.md) |
| 2/10 (gruppo 21) | Xatu, Girafarig, Phanpy, Donphan, Pinsir, Heracross, Rhyhorn, Rhydon | complete | [Dossier, screenshot e video](CHECKPOINT21_REVIEW.md) |
| 3/10 (gruppo 22) | Snorunt, Glalie, Spheal, Sealeo, Walrein, Clamperl, Huntail, Gorebyss | complete | [Dossier, screenshot e video](CHECKPOINT22_REVIEW.md) |
| 4/10 (gruppo 23) | Relicanth, Corsola, Chinchou, Lanturn, Luvdisc, Horsea, Seadra, Kingdra | complete | [Dossier, screenshot e video](CHECKPOINT23_REVIEW.md) |
| 5/10 (gruppo 24) | Bagon, Shelgon, Salamence, Beldum, Metang, Metagross, Regirock, Regice | complete | [Dossier, screenshot e video](CHECKPOINT24_REVIEW.md) |
| 6/10 (gruppo 25) | Registeel, Latias, Latios, Kyogre, Groudon, Rayquaza, Jirachi, Deoxys | complete | [Dossier, screenshot e video](CHECKPOINT25_REVIEW.md) |
| 7/10 (gruppo 26) | Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle | complete | [Dossier, screenshot e video](CHECKPOINT26_REVIEW.md) |
| 8/10 (gruppo 27) | Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey | complete | [Dossier, screenshot e video](CHECKPOINT27_REVIEW.md) |
| 9/10 (gruppo 28) | Pidgeotto, Pidgeot, Rattata, Raticate, Spearow, Fearow, Ekans, Arbok | complete | [Dossier, screenshot e video](CHECKPOINT28_REVIEW.md) |
| 10/10 (gruppo 29) | Nidoran F, Nidorina, Nidoqueen, Nidoran M, Nidorino, Nidoking, Clefairy, Clefable | complete | [Dossier, screenshot e video](CHECKPOINT29_REVIEW.md) |

Le specie vengono segnate come fatte soltanto dopo prove front/back e shiny, revisione visiva e verifica dei dossier. Ogni gruppo completo è salvato in un commit dedicato; i messaggi Git identificano il numero di checkpoint. ROM, asset e filmati restano locali secondo la politica artifacts.

[Piano](../BW2_ANIMATION_PLAN.md) · [Registro](AUTONOMOUS20_29.json) · [Checkpoint di ripresa](CHECKPOINT.md).

## Audit conclusivo e modifiche

[Audit indipendente](AUTONOMOUS20_29_AUDIT.json): **240 dossier**, 80 scenari ordinari e 80 verifiche shiny per le 80 nuove specie. I video ordinari conservano ingresso e almeno due cicli completi per vista; screenshot integrali e video nativi restano nei dossier. Sono stati ispezionati ingresso, otto pose per scenario, frame QA e palette shiny. I 650 file degli asset precedenti e i 330 file locali estranei al lavoro conservano gli hash iniziali. ROM e repository sorgente BW2 invariati. L'algoritmo di presentazione v5 con margine v5.1 è identico a quello approvato.

[Deoxys: forme e Trasformazione](DEOXYS_REVIEW.md): Normale e Velocità front/back e shiny, selezione ordinaria Emerald, turni reali Ditto→Deoxys normale/shiny, ritorno al menu e ripresa dei cicli BW2. La correzione generale del riaggancio dell'attore dopo Trasformazione è coperta anche da una regressione reale Ditto→Spinda e dall'oracolo delle macchie procedurali. Ditto resta una risorsa ausiliaria, non una specie completata; Trasformazione e le altre mosse di supporto restano animazioni Emerald.

Test pertinenti superati: **20 esportatore, 7 integrità dossier, 24 varianti**; bridge con asset sintetici/reali, oracolo Spinda su otto personality, Castform, Deoxys e riaggancio/ripristino dopo Trasformazione. La build normale esclude mailbox e selettore diagnostico Deoxys, con `CtrCycle_Frame/Input` da quattro byte. Le prove precedenti e le catture diagnostiche fallite sono conservate nella cronologia ed escluse dai completamenti.

## Prove e build

- Ultimo gruppo: [screenshot](../../artifacts/bw2-validation/checkpoint29-2026-10-29/pokemon.png), [video nativo completo](../../artifacts/bw2-validation/checkpoint29-2026-10-29/pokemon.mp4), [dossier e misure](CHECKPOINT29_REVIEW.md).
- Build normale finale: [`3724fc8cdfba9514`](../../artifacts/bw2-validation/builds/3724fc8cdfba9514_31a8bb0a85c2/Emerald3DS-BW2.3dsx), SHA-256 `31a8bb0a85c2d0f4b69be3129b3c2283c9a759e90485e0d15eda5149aca5319a`.
- Build di prova finale: [`1441ec92f9e6b9b6`](../../artifacts/bw2-validation/builds/1441ec92f9e6b9b6_aab76a7b3322/validation.3dsx), SHA-256 `aab76a7b3322e46be17cb62dbf3366706d1fa2e7e8105615dbccfb6d50a269ca`.
- Binari, ELF e ID delle diverse coppie usate sono distinti e archiviati: i metadati di ogni dossier indicano la build effettiva e il relativo SHA, compreso il checkpoint 25 con build diverse. [Registro e cronologia](AUTONOMOUS20_29.json).

ROM, asset, build e filmati grandi sono locali e ignorati da Git; un clone del solo repository non li contiene necessariamente.

## Chiusura e ripresa

Emulatore isolato uscito effettivamente e assente dal controllo finale; nessuna acquisizione attiva. Azahar personale preservato e ancora attivo al controllo finale (PID 2460, percorso `D:/Emulators/Azahar/azahar.exe`). Nessun push. Nessuna unità lasciata in corso. Prossima specie: **Paras, nazionale/Emerald 46**.

Limiti: prove Azahar a 1×; audio non registrato nel setup senza DSP. Console reale, stereo, doppi, esecuzione link reale e integrazione completa delle interazioni speciali restano da validare. La suite generale conserva i problemi preesistenti bottom-map e non viene dichiarata superata.

## Commit dedicati

| Checkpoint | Commit |
|---|---|
| 20 | `38483c1` |
| 21 | `8a22db5` |
| 22 | `36ba026` |
| 23 | `0771fd6` |
| 24 | `0d0cd92` |
| 25 | `13c9048` |
| 26 | `51b5dd3` |
| 27 | `9978b56` |
| 28 | `9f2e1fd` |
| 29 | Commit finale identificato dal messaggio `Complete autonomous BW2 checkpoint 29: eight Pokemon` (hash in `git log`) |
