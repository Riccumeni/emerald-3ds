# Gruppo Taillow–Surskit

Completati otto nuovi Pokémon: Taillow, Swellow, Wingull, Pelipper, Ralts,
Kirlia, Gardevoir e Surskit. Ogni specie è stata segnata come fatta soltanto
dopo la revisione delle due viste e delle palette shiny.

Totale: **34/386 Pokémon e 6/354 mosse**. Prossima specie: **Masquerain**.

![Otto nuove specie nelle due direzioni](../../artifacts/bw2-validation/batch4-taillow-surskit-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/batch4-taillow-surskit-2026-10-28/pokemon.mp4): 272.66 secondi, 8178 fotogrammi. Otto incontri con i lati invertiti, concatenati senza tagli, ricodifica o accelerazione. Gli screenshot nella raccolta ritagliano lo schermo superiore; ogni dossier conserva PNG integrali 400×480, video front/back e prove shiny.

| Pokémon | Nazionale / Emerald | Altezza | Scala front / back | Dossier |
|---|---|---:|---:|---|
| Taillow | 276 / 304 | 0.3 m | 97.66% / 114.06% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0276_taillow/verifica.md) |
| Swellow | 277 / 305 | 0.7 m | 111.33% / 154.69% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0277_swellow/verifica.md) |
| Wingull | 278 / 309 | 0.6 m | 106.64% / 142.97% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0278_wingull/verifica.md) |
| Pelipper | 279 / 310 | 1.2 m | 150.00% / 209.77% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0279_pelipper/verifica.md) |
| Ralts | 280 / 392 | 0.4 m | 115.23% / 140.23% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0280_ralts/verifica.md) |
| Kirlia | 281 / 393 | 0.8 m | 91.41% / 133.20% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0281_kirlia/verifica.md) |
| Gardevoir | 282 / 394 | 1.6 m | 136.33% / 186.33% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0282_gardevoir/verifica.md) |
| Surskit | 283 / 311 | 0.5 m | 101.56% / 131.64% | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0283_surskit/verifica.md) |

Le percentuali sono trasformazioni del canvas esportato, non proporzioni
metriche fra specie. L’algoritmo v5 approvato è invariato: altezza Emerald e
impronta nativa BW2 condivisa tra front/back; stessa base frontale e centro
di massa posteriore nell’arena. Il testo può coprire la parte inferiore dei
back. [Algoritmo](../BW2_POKEMON_LAYOUT.md) · [Misure lette dalla build](BATCH4_MEASUREMENTS.json).

Revisione visiva: ingresso, otto pose distribuite nel ciclo, screenshot e
fotogrammi iniziali/centrali/finali degli otto incontri. Controllati ali e
code di Taillow/Swellow/Wingull/Pelipper, pose di Ralts/Kirlia, abito e braccia
di Gardevoir e movimento delle zampe di Surskit. I video attestano almeno due
cicli completi di entrambi gli attori. Otto ulteriori scenari confrontano le
palette shiny con quelle esportate dalla ROM.

L’esportazione incrementale ha aggiunto 16 viste e i relativi BWL2: totale
68 viste di 34 specie, sei mosse e quindici clip di effetti. I 125 file degli
asset precedenti sono rimasti identici, verificati tramite SHA-256. Nessuna
nuova mossa aggiunta in questo gruppo. La ROM è stata soltanto letta.

Build di prova `f2ecf4d5e40cf598`, SHA-256
`8f0bbf00cc6618af733f2a60b1cbab3908d83696ce72372dc80d761fccbf1616`.
Build normale `c4d710a45a166c54`, SHA-256
`2e04cc3c8fc17d3aff9eaa92f5f3ecbc0a738532e744b83be81d29beae2b8303`.
Binari ed ELF di prova archiviati; i metadati dei dossier indicano i percorsi.
La build normale ha gli stub Frame/Input da quattro byte e non contiene la
mailbox di prova. Le copie di distribuzione locali sono aggiornate.

Verifiche concluse: build di prova e normale, decodifica integrale dei video,
audit di 40 dossier (34 Pokémon e sei mosse), sette test della procedura prove.
Console fisica, stereo e doppi restano nella fase d’integrazione; audio non
acquisito nel setup senza DSP.

Il codice BW2 e la revisione approvata sono salvati nel commit `3f239cf`.
Gli asset ROM e i filmati restano locali, secondo il criterio della cartella
artifacts. Nessuna modifica alle altre attività UI/voxel del checkout.

[Piano](../BW2_ANIMATION_PLAN.md) · [Prove](EVIDENCE.md) · [Checkpoint](CHECKPOINT.md).
