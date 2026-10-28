# Checkpoint 2/5 — gruppo 6

Completati: **Alakazam, Nincada, Ninjask, Shedinja, Whismur, Loudred, Exploud, Makuhita**. Totale piano:**50/386 Pokémon,6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint06-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint06-2026-10-28/pokemon.mp4): 233.97s, 7017 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Alakazam | 65/65 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0065_alakazam/verifica.md) |
| Nincada | 290/301 | 0.5m | 93.75%/121.09% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0290_nincada/verifica.md) |
| Ninjask | 291/302 | 0.8m | 98.05%/147.27% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0291_ninjask/verifica.md) |
| Shedinja | 292/303 | 0.8m | 114.45%/159.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0292_shedinja/verifica.md) |
| Whismur | 293/370 | 0.6m | 118.36%/165.62% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0293_whismur/verifica.md) |
| Loudred | 294/371 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0294_loudred/verifica.md) |
| Exploud | 295/372 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0295_exploud/verifica.md) |
| Makuhita | 296/335 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0296_makuhita/verifica.md) |

Algoritmo v5 approvato invariato: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT06_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale:56 dossier verificati; tutti i157file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`15dde47674f650ec`, SHA-256 `54227e749aa5fc2b7ef3fd5a8682ecfbf73cf0f9efdd38412924ca92ed629bb3`.

Build Normale:`2ed791a98434d45b`, SHA-256 `036f89da901d369a80087f5911adc14843ce003b6ecd09ec275da719b1dde19a`.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da4byte. Limiti: prove su emulatore Azahar a1×; audio non acquisito nel setup senza DSP; console,stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS5_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
