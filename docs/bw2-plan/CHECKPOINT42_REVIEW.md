# Checkpoint 3/9 â€” gruppo 42

Completati: **Politoed, Hoppip, Skiploom, Jumpluff, Aipom, Sunkern, Sunflora, Yanma**. Totale piano: **338/386 PokÃ©mon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint42-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint42-2026-10-30/pokemon.mp4): 193.11s, 5791 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400Ã—480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Politoed | 186/186 | 1.1m | 125.00%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0186_politoed/verifica.md) |
| Hoppip | 187/187 | 0.4m | 117.97%/153.12% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0187_hoppip/verifica.md) |
| Skiploom | 188/188 | 0.6m | 101.56%/120.31% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0188_skiploom/verifica.md) |
| Jumpluff | 189/189 | 0.8m | 114.84%/166.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0189_jumpluff/verifica.md) |
| Aipom | 190/190 | 0.8m | 98.05%/153.52% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0190_aipom/verifica.md) |
| Sunkern | 191/191 | 0.3m | 104.69%/131.64% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0191_sunkern/verifica.md) |
| Sunflora | 192/192 | 0.8m | 107.81%/142.58% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0192_sunflora/verifica.md) |
| Yanma | 193/193 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0193_yanma/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nellâ€™arena indipendente dal testo. [Misure](CHECKPOINT42_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 344 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie giÃ  chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1Ã—; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase dâ€™integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) Â· [Piano](../BW2_ANIMATION_PLAN.md) Â· [Tutte le prove](EVIDENCE.md).
