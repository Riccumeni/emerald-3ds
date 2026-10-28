# Checkpoint 5/5 — gruppo 9

Completati: **Crobat, Tentacool, Tentacruel, Sableye, Mawile, Aron, Lairon, Aggron**. Totale piano: **74/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint09-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint09-2026-10-28/pokemon.mp4): 255.94s, 7675 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Crobat | 169/169 | 1.8m | 171.09%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0169_crobat/verifica.md) |
| Tentacool | 72/72 | 0.9m | 119.92%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0072_tentacool/verifica.md) |
| Tentacruel | 73/73 | 1.6m | 157.42%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0073_tentacruel/verifica.md) |
| Sableye | 302/322 | 0.5m | 100.00%/130.47% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0302_sableye/verifica.md) |
| Mawile | 303/355 | 0.6m | 106.64%/142.97% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0303_mawile/verifica.md) |
| Aron | 304/382 | 0.4m | 140.62%/173.44% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0304_aron/verifica.md) |
| Lairon | 305/383 | 0.9m | 100.00%/150.00% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0305_lairon/verifica.md) |
| Aggron | 306/384 | 2.1m | 141.80%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0306_aggron/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 dal terzo gruppo: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT09_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 80 dossier verificati; tutti i 157 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`ab9b0891e3970829`, SHA-256 `6a48c0fdee8fbab7096fbdb29433741e077bde265f99113c1a2362fbe206a0a6`.

Build Normale:`c65648fb2fe7ded3`, SHA-256 `c7ca71c43aee28d283e43f33ac10761708ec28989e6cdccc7083973257117f3c`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS5_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
