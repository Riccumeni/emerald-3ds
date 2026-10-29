# Checkpoint 3/5 — gruppo 17

Completati: **Crawdaunt, Baltoy, Claydol, Lileep, Cradily, Anorith, Armaldo, Igglybuff**. Totale piano: **138/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint17-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint17-2026-10-29/pokemon.mp4): 245.11s, 7347 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Crawdaunt | 342/327 | 1.1m | 125.00%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0342_crawdaunt/verifica.md) |
| Baltoy | 343/318 | 0.5m | 116.80%/161.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0343_baltoy/verifica.md) |
| Claydol | 344/319 | 1.5m | 133.98%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0344_claydol/verifica.md) |
| Lileep | 345/388 | 1.0m | 100.00%/159.38% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0345_lileep/verifica.md) |
| Cradily | 346/389 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0346_cradily/verifica.md) |
| Anorith | 347/390 | 0.7m | 100.00%/160.55% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0347_anorith/verifica.md) |
| Armaldo | 348/391 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0348_armaldo/verifica.md) |
| Igglybuff | 174/174 | 0.3m | 98.05%/117.19% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0174_igglybuff/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT17_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 144 dossier verificati; tutti i 477 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`4ec0e4edb35bd030`, SHA-256 `6649af886e687646e349fb7f1bdd1d091016df23e0641e2624bc26f8701f007f`.

Build Normale:`93d67843245e6074`, SHA-256 `283a3e68cd54c250f7247800a6223f76dc622d05477ecb8fd29a84b1179a864c`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS15_19_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
