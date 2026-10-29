# Checkpoint 5/5 — gruppo 19

Completati: **Shuppet, Banette, Duskull, Dusclops, Tropius, Chimecho, Absol, Vulpix**. Totale piano: **154/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint19-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint19-2026-10-29/pokemon.mp4): 222.46s, 6665 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Shuppet | 353/377 | 0.6m | 92.97%/119.92% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0353_shuppet/verifica.md) |
| Banette | 354/378 | 1.1m | 108.98%/158.59% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0354_banette/verifica.md) |
| Duskull | 355/361 | 0.8m | 105.47%/137.89% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0355_duskull/verifica.md) |
| Dusclops | 356/362 | 1.6m | 136.33%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0356_dusclops/verifica.md) |
| Tropius | 357/369 | 2.0m | 166.80%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0357_tropius/verifica.md) |
| Chimecho | 358/411 | 0.6m | 86.33%/116.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0358_chimecho/verifica.md) |
| Absol | 359/376 | 1.2m | 128.12%/189.45% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0359_absol/verifica.md) |
| Vulpix | 37/37 | 0.6m | 106.64%/142.97% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0037_vulpix/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT19_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 160 dossier verificati; tutti i 477 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`24b3c6b5fb7206c7`, SHA-256 `d46fe452124971b1f853041140908d6e566c0fd7df0e1ce5dd5400aebf5c9594`.

Build Normale:`b9eafa1bb23e8fcf`, SHA-256 `ad98f8246237ba4a1998bdcf5dd50a3cafd8688784a2347cc3a04923506d7c6b`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS15_19_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
