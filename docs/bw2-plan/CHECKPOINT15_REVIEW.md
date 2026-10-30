# Checkpoint 1/5 — gruppo 15

Completati: **Spinda, Skarmory, Trapinch, Vibrava, Flygon, Cacnea, Cacturne, Swablu**. Totale piano: **122/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint15-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint15-2026-10-28/pokemon.mp4): 250.44s, 7506 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Spinda | 327/308 | 1.1m | 115.23%/155.86% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0327_spinda/verifica.md) |
| Skarmory | 227/227 | 1.7m | 138.28%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0227_skarmory/verifica.md) |
| Trapinch | 328/332 | 0.7m | 126.17%/164.06% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0328_trapinch/verifica.md) |
| Vibrava | 329/333 | 1.1m | 125.00%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0329_vibrava/verifica.md) |
| Flygon | 330/334 | 2.0m | 132.42%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0330_flygon/verifica.md) |
| Cacnea | 331/344 | 0.4m | 98.05%/127.34% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0331_cacnea/verifica.md) |
| Cacturne | 332/345 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0332_cacturne/verifica.md) |
| Swablu | 333/358 | 0.4m | 109.77%/142.97% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0333_swablu/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT15_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 128 dossier verificati; tutti i 477 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`4ec0e4edb35bd030`, SHA-256 `6649af886e687646e349fb7f1bdd1d091016df23e0641e2624bc26f8701f007f`.

Build Normale:`93d67843245e6074`, SHA-256 `283a3e68cd54c250f7247800a6223f76dc622d05477ecb8fd29a84b1179a864c`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS15_19_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
