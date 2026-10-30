# Cinque checkpoint autonomi

Completati **5/5 checkpoint** richiesti, nell’ordine del piano. Partenza: 34 Pokémon. Obiettivo: 74. Totale corrente: **74/386 Pokémon, 6/354 mosse**. Criterio v5 conservato; guardia verticale v5.1 dal terzo gruppo.

| Checkpoint | Specie | Stato | Prove |
|---|---|---|---|
| 1/5 (gruppo 5) | Masquerain, Shroomish, Breloom, Slakoth, Vigoroth, Slaking, Abra, Kadabra | complete | [Dossier, screenshot e video](CHECKPOINT05_REVIEW.md) |
| 2/5 (gruppo 6) | Alakazam, Nincada, Ninjask, Shedinja, Whismur, Loudred, Exploud, Makuhita | complete | [Dossier, screenshot e video](CHECKPOINT06_REVIEW.md) |
| 3/5 (gruppo 7) | Hariyama, Goldeen, Seaking, Magikarp, Gyarados, Azurill, Marill, Azumarill | complete | [Dossier, screenshot e video](CHECKPOINT07_REVIEW.md) |
| 4/5 (gruppo 8) | Geodude, Graveler, Golem, Nosepass, Skitty, Delcatty, Zubat, Golbat | complete | [Dossier, screenshot e video](CHECKPOINT08_REVIEW.md) |
| 5/5 (gruppo 9) | Crobat, Tentacool, Tentacruel, Sableye, Mawile, Aron, Lairon, Aggron | complete | [Dossier, screenshot e video](CHECKPOINT09_REVIEW.md) |

Le specie vengono segnate come fatte soltanto dopo prove front/back e shiny, revisione visiva e verifica dei dossier. Ogni gruppo completo è salvato in un commit dedicato; i messaggi Git identificano il numero di checkpoint. ROM, asset e filmati restano locali secondo la politica artifacts.

[Piano](../BW2_ANIMATION_PLAN.md) · [Registro](AUTONOMOUS5.json) · [Checkpoint di ripresa](CHECKPOINT.md).

Verifica finale: 80 dossier (74 Pokémon e 6 mosse), 80 viste dei nuovi Pokémon con asset e prove coerenti; i 157 file degli asset precedenti conservano gli hash iniziali. Le palette shiny sono verificate nelle due viste. Acquisizioni concluse ed emulatore isolato chiuso. Prove su Azahar a 1×: audio e console reale restano da verificare.

Build normale aggiornata: `build/bw2-validation/Emerald3DS-BW2.3dsx` (ID `c65648fb2fe7ded3`). Il [margine superiore v5.1](../BW2_POKEMON_LAYOUT.md) evita il taglio delle pose alte senza cambiare l’appoggio nell’arena; il [confronto Hariyama](FRONT_HEADROOM_REVIEW.json) passa da 30 a 0 fotogrammi a contatto col bordo, su 444 esaminati. Nessuna delle 50 specie già chiuse cambia scala.
