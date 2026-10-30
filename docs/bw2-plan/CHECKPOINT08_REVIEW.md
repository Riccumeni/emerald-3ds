# Checkpoint 4/5 — gruppo 8

Completati: **Geodude, Graveler, Golem, Nosepass, Skitty, Delcatty, Zubat, Golbat**. Totale piano: **66/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint08-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint08-2026-10-28/pokemon.mp4): 212.20s, 6363 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Geodude | 74/74 | 0.4m | 94.92%/127.34% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0074_geodude/verifica.md) |
| Graveler | 75/75 | 1.0m | 98.05%/146.48% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0075_graveler/verifica.md) |
| Golem | 76/76 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0076_golem/verifica.md) |
| Nosepass | 299/320 | 1.0m | 128.12%/187.11% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0299_nosepass/verifica.md) |
| Skitty | 300/315 | 0.6m | 116.02%/156.25% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0300_skitty/verifica.md) |
| Delcatty | 301/316 | 1.1m | 104.69%/156.64% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0301_delcatty/verifica.md) |
| Zubat | 41/41 | 0.8m | 105.47%/135.55% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0041_zubat/verifica.md) |
| Golbat | 42/42 | 1.6m | 172.66%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0042_golbat/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 dal terzo gruppo: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT08_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 72 dossier verificati; tutti i 157 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`ab9b0891e3970829`, SHA-256 `6a48c0fdee8fbab7096fbdb29433741e077bde265f99113c1a2362fbe206a0a6`.

Build Normale:`c65648fb2fe7ded3`, SHA-256 `c7ca71c43aee28d283e43f33ac10761708ec28989e6cdccc7083973257117f3c`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS5_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
