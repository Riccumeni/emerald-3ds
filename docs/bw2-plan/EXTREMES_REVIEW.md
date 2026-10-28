# Due estremi di statura: Natu e Wailord

Aggiunti due nuovi Pokémon BW2 al progetto e chiusi i rispettivi dossier. Natu misura 0,2 m: è al minimo del Pokédex di Smeraldo, insieme a Diglett e Azurill. Wailord misura 14,5 m: è il massimo del gioco. Le misure provengono dal campo height delle voci locali in build/upstream/src/data/pokemon/pokedex_entries.h.

![Le due orientazioni della battaglia](../../artifacts/bw2-validation/extremes-2026-10-28/panoramica.png)

[Filmato completo](../../artifacts/bw2-validation/extremes-2026-10-28/dimostrazione-completa.mp4): prima Natu back/Wailord front, poi Wailord back/Natu front. Video nativi 400×480 a circa 30 fps, concatenati senza ricodifica o accelerazione: 58,11 secondi, 1.743 fotogrammi decodificati e verificati.

| Pokémon | Altezza Pokédex | Frontale | Di spalle |
|---|---:|---|---|
| Wailord | 14,5 m | [PNG](../../artifacts/bw2-validation/pokemon/0321_wailord/front/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0321_wailord/front/demo.mp4) | [PNG](../../artifacts/bw2-validation/pokemon/0321_wailord/back/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0321_wailord/back/demo.mp4) |
| Natu | 0,2 m | [PNG](../../artifacts/bw2-validation/pokemon/0177_natu/front/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0177_natu/front/demo.mp4) | [PNG](../../artifacts/bw2-validation/pokemon/0177_natu/back/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0177_natu/back/demo.mp4) |

È stato applicato lo stesso algoritmo v4 dei Pokémon precedenti, senza eccezioni per Natu o Wailord. Si conserva la proporzione delle sagome: il valore descrive il lato più lungo, non forza ogni corpo ad avere la stessa forma. La compressione delle dimensioni mantiene leggibile il piccolo e limita il gigante.

| Pokémon | Ingombro front/back, pixel logici | Scala Q8 front/back | Durata ciclo front/back |
|---|---|---|---|
| Natu | 48 / 62 | 299 / 369 | 408 / 408 tick |
| Wailord | 88 / 112 | 375 / 477 | 336 / 336 tick |

Wailord raggiunge i limiti di ingombro previsti; nessuna dimensione viene derivata linearmente dai 14,5 metri. Nel back il corpo resta centrato nell’arena e la parte inferiore può essere coperta dal testo. Le due scene includono l’ingresso e almeno due cicli completi per entrambi gli attori; i report controllano anche l’avanzamento dei tick. Occhi, parti, trasparenza, oscillazioni e sovrapposizioni sono stati ispezionati nei fotogrammi distribuiti lungo i cicli. Le palette shiny sono confrontate con gli asset per tutte e quattro le viste.

Build di prova 8c0f9eae3f9ed8e0, SHA-256 31058dc7d55b75a38fc99a21c21084cc8cf1df75f6226fe0b6262869ed67dd34. Build normale ada3679491ddb126, SHA-256 2fff83c3ff709f37f04dbb2bc8a227e616ed829e621212fd66e35b293ce2fa81. La build normale contiene i sei Pokémon importati e non contiene incontro automatico o mailbox del banco prova.

[Misure e report](EXTREMES_MEASUREMENTS.json) · [Algoritmo](../BW2_POKEMON_LAYOUT.md) · [Indice di tutte le prove](EVIDENCE.md). I metadati dei singoli dossier conservano hash degli asset, della ROM, delle build e dei media. Gli asset dei quattro Pokémon precedenti sono rimasti identici durante l’esportazione incrementale.

Prova su Azahar isolato a velocità 1×: audio, console fisica, stereo e doppi non attestati. Questi sono i due estremi del campo statura; forme particolari, corpi sottili e mosse complesse richiedono le proprie prove nel piano generale.
