# Checkpoint 5/9 â€” gruppo 44

Completati: **Pineco, Forretress, Dunsparce, Gligar, Steelix, Snubbull, Granbull, Qwilfish**. Totale piano: **354/386 PokÃ©mon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint44-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint44-2026-10-30/pokemon.mp4): 235.94s, 7077 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400Ã—480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Pineco | 204/204 | 0.6m | 96.09%/128.12% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0204_pineco/verifica.md) |
| Forretress | 205/205 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0205_forretress/verifica.md) |
| Dunsparce | 206/206 | 1.5m | 142.19%/150.78% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0206_dunsparce/verifica.md) |
| Gligar | 207/207 | 1.1m | 125.00%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0207_gligar/verifica.md) |
| Steelix | 208/208 | 9.2m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0208_steelix/verifica.md) |
| Snubbull | 209/209 | 0.6m | 121.09%/165.62% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0209_snubbull/verifica.md) |
| Granbull | 210/210 | 1.4m | 106.64%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0210_granbull/verifica.md) |
| Qwilfish | 211/211 | 0.5m | 108.59%/143.36% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0211_qwilfish/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nellâ€™arena indipendente dal testo. [Misure](CHECKPOINT44_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 360 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie giÃ  chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1Ã—; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase dâ€™integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) Â· [Piano](../BW2_ANIMATION_PLAN.md) Â· [Tutte le prove](EVIDENCE.md).
