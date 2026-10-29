# Cinque checkpoint autonomi â€” 15â€“19

Completati **5/5 checkpoint** richiesti, nellâ€™ordine del piano. Partenza: 114 PokÃ©mon. Obiettivo: 154. Totale corrente: **154/386 PokÃ©mon, 6/354 mosse**. Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi.

| Checkpoint | Specie | Stato | Prove |
|---|---|---|---|
| 1/5 (gruppo 15) | Spinda, Skarmory, Trapinch, Vibrava, Flygon, Cacnea, Cacturne, Swablu | complete | [Dossier, screenshot e video](CHECKPOINT15_REVIEW.md) |
| 2/5 (gruppo 16) | Altaria, Zangoose, Seviper, Lunatone, Solrock, Barboach, Whiscash, Corphish | complete | [Dossier, screenshot e video](CHECKPOINT16_REVIEW.md) |
| 3/5 (gruppo 17) | Crawdaunt, Baltoy, Claydol, Lileep, Cradily, Anorith, Armaldo, Igglybuff | complete | [Dossier, screenshot e video](CHECKPOINT17_REVIEW.md) |
| 4/5 (gruppo 18) | Jigglypuff, Wigglytuff, Feebas, Milotic, Castform, Staryu, Starmie, Kecleon | complete | [Dossier, screenshot e video](CHECKPOINT18_REVIEW.md) |
| 5/5 (gruppo 19) | Shuppet, Banette, Duskull, Dusclops, Tropius, Chimecho, Absol, Vulpix | complete | [Dossier, screenshot e video](CHECKPOINT19_REVIEW.md) |

Le specie vengono segnate come fatte soltanto dopo prove front/back e shiny, revisione visiva e verifica dei dossier. Ogni gruppo completo Ã¨ salvato in un commit dedicato; i messaggi Git identificano il numero di checkpoint. ROM, asset e filmati restano locali secondo la politica artifacts.

[Piano](../BW2_ANIMATION_PLAN.md) Â· [Registro](AUTONOMOUS15_19.json) Â· [Checkpoint di ripresa](CHECKPOINT.md).

Audit finale: **160 dossier**, 477 file degli asset precedenti e 342 file locali estranei preservati byte per byte. ROM sorgente invariata. [Risultati e hash](AUTONOMOUS15_19_AUDIT.json). Nessuna unità lasciata in corso; emulatore isolato chiuso e Azahar personale preservato. Prossima specie: **Ninetales (#38)**.

Sono inclusi [Spinda con otto personality, estremi e sovrapposizioni](SPINDA_REVIEW.md) e [Castform con quattro forme, shiny e transizioni reali](CASTFORM_REVIEW.md). Le mosse meteo restano da importare e il contatore mosse resta 6/354.

Test pertinenti passati: bridge con asset reali/sintetici, oracolo texture Spinda, cambio forme/cache/palette Castform, 18 test esportatore, 7 test dossier e 15 test varianti. Presentazione v5.1 invariata. Audio/DSP, console reale, stereo e doppi restano da validare; la suite generale con problemi bottom-map preesistenti non è dichiarata superata.

Build normale finale: [`b9eafa1bb23e8fcf`](../../artifacts/bw2-validation/builds/b9eafa1bb23e8fcf_ad98f8246237/Emerald3DS-BW2.3dsx). Build di prova finale: [`24b3c6b5fb7206c7`](../../artifacts/bw2-validation/builds/24b3c6b5fb7206c7_d46fe4521249/validation.3dsx). Binari, ELF e ID completi archiviati; i filmati dei gruppi 15–17 usano le build precedenti conservate nel registro. Tutti gli artifact grandi restano locali e ignorati da Git.
