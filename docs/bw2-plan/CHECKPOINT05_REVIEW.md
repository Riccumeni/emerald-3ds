# Checkpoint 1/5 — gruppo 5

Completati: **Masquerain, Shroomish, Breloom, Slakoth, Vigoroth, Slaking, Abra, Kadabra**. Totale piano:**42/386 Pokémon,6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint05-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint05-2026-10-28/pokemon.mp4): 243.14s, 7292 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Masquerain | 284/312 | 0.8m | 114.84%/166.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0284_masquerain/verifica.md) |
| Shroomish | 285/306 | 0.4m | 118.75%/160.55% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0285_shroomish/verifica.md) |
| Breloom | 286/307 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0286_breloom/verifica.md) |
| Slakoth | 287/364 | 0.8m | 107.81%/156.64% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0287_slakoth/verifica.md) |
| Vigoroth | 288/365 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0288_vigoroth/verifica.md) |
| Slaking | 289/366 | 2.0m | 142.97%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0289_slaking/verifica.md) |
| Abra | 63/63 | 0.9m | 119.92%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0063_abra/verifica.md) |
| Kadabra | 64/64 | 1.3m | 129.69%/189.45% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0064_kadabra/verifica.md) |

Algoritmo v5 approvato invariato: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT05_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale:48 dossier verificati; tutti i157file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`15dde47674f650ec`, SHA-256 `54227e749aa5fc2b7ef3fd5a8682ecfbf73cf0f9efdd38412924ca92ed629bb3`.

Build Normale:`2ed791a98434d45b`, SHA-256 `036f89da901d369a80087f5911adc14843ce003b6ecd09ec275da719b1dde19a`.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da4byte. Limiti: prove su emulatore Azahar a1×; audio non acquisito nel setup senza DSP; console,stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS5_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
