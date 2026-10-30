# Checkpoint 7/9 â€” gruppo 46

Completati: **Octillery, Delibird, Mantine, Houndour, Houndoom, Porygon2, Stantler, Smeargle**. Totale piano: **370/386 PokÃ©mon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint46-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint46-2026-10-30/pokemon.mp4): 247.06s, 7409 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400Ã—480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Octillery | 224/224 | 0.9m | 119.92%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0224_octillery/verifica.md) |
| Delibird | 225/225 | 0.9m | 109.38%/156.25% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0225_delibird/verifica.md) |
| Mantine | 226/226 | 2.1m | 144.92%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0226_mantine/verifica.md) |
| Houndour | 228/228 | 0.6m | 115.62%/135.94% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0228_houndour/verifica.md) |
| Houndoom | 229/229 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0229_houndoom/verifica.md) |
| Porygon2 | 233/233 | 0.6m | 130.47%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0233_porygon2/verifica.md) |
| Stantler | 234/234 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0234_stantler/verifica.md) |
| Smeargle | 235/235 | 1.2m | 103.12%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0235_smeargle/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nellâ€™arena indipendente dal testo. [Misure](CHECKPOINT46_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 376 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie giÃ  chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1Ã—; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase dâ€™integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) Â· [Piano](../BW2_ANIMATION_PLAN.md) Â· [Tutte le prove](EVIDENCE.md).
