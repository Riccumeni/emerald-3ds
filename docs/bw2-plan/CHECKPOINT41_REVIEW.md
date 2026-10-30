# Checkpoint 2/9 â€” gruppo 41

Completati: **Ariados, Cleffa, Togepi, Togetic, Mareep, Flaaffy, Ampharos, Sudowoodo**. Totale piano: **330/386 PokÃ©mon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint41-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint41-2026-10-30/pokemon.mp4): 193.92s, 5815 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400Ã—480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Ariados | 168/168 | 1.1m | 100.00%/158.59% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0168_ariados/verifica.md) |
| Cleffa | 173/173 | 0.3m | 110.16%/138.28% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0173_cleffa/verifica.md) |
| Togepi | 175/175 | 0.3m | 104.69%/141.80% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0175_togepi/verifica.md) |
| Togetic | 176/176 | 0.6m | 106.64%/142.97% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0176_togetic/verifica.md) |
| Mareep | 179/179 | 0.6m | 103.91%/138.67% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0179_mareep/verifica.md) |
| Flaaffy | 180/180 | 0.8m | 105.47%/153.52% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0180_flaaffy/verifica.md) |
| Ampharos | 181/181 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0181_ampharos/verifica.md) |
| Sudowoodo | 185/185 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0185_sudowoodo/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nellâ€™arena indipendente dal testo. [Misure](CHECKPOINT41_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 336 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie giÃ  chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1Ã—; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase dâ€™integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) Â· [Piano](../BW2_ANIMATION_PLAN.md) Â· [Tutte le prove](EVIDENCE.md).
