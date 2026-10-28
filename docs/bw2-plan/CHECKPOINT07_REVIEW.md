# Checkpoint 3/5 — gruppo 7

Completati: **Hariyama, Goldeen, Seaking, Magikarp, Gyarados, Azurill, Marill, Azumarill**. Totale piano: **58/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint07-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint07-2026-10-28/pokemon.mp4): 238.84s, 7162 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Hariyama | 297/336 | 2.3m | 157.42%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0297_hariyama/verifica.md) |
| Goldeen | 118/118 | 0.6m | 108.20%/145.70% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0118_goldeen/verifica.md) |
| Seaking | 119/119 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0119_seaking/verifica.md) |
| Magikarp | 129/129 | 0.9m | 119.92%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0129_magikarp/verifica.md) |
| Gyarados | 130/130 | 6.5m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0130_gyarados/verifica.md) |
| Azurill | 298/350 | 0.2m | 94.92%/121.48% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0298_azurill/verifica.md) |
| Marill | 183/183 | 0.4m | 88.67%/116.80% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0183_marill/verifica.md) |
| Azumarill | 184/184 | 0.8m | 114.84%/166.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0184_azumarill/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 dal terzo gruppo: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT07_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 64 dossier verificati; tutti i 157 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`ab9b0891e3970829`, SHA-256 `6a48c0fdee8fbab7096fbdb29433741e077bde265f99113c1a2362fbe206a0a6`.

Build Normale:`c65648fb2fe7ded3`, SHA-256 `c7ca71c43aee28d283e43f33ac10761708ec28989e6cdccc7083973257117f3c`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS5_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
