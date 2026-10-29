# Checkpoint 10/10 — gruppo 29

Completati: **Nidoran F, Nidorina, Nidoqueen, Nidoran M, Nidorino, Nidoking, Clefairy, Clefable**. Totale piano: **234/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint29-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint29-2026-10-29/pokemon.mp4): 231.69s, 6943 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Nidoran F | 29/29 | 0.4m | 128.52%/163.67% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0029_nidoran_f/verifica.md) |
| Nidorina | 30/30 | 0.8m | 105.47%/153.52% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0030_nidorina/verifica.md) |
| Nidoqueen | 31/31 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0031_nidoqueen/verifica.md) |
| Nidoran M | 32/32 | 0.5m | 133.20%/146.48% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0032_nidoran_m/verifica.md) |
| Nidorino | 33/33 | 0.9m | 103.52%/157.03% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0033_nidorino/verifica.md) |
| Nidoking | 34/34 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0034_nidoking/verifica.md) |
| Clefairy | 35/35 | 0.6m | 106.25%/127.73% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0035_clefairy/verifica.md) |
| Clefable | 36/36 | 1.3m | 114.45%/161.72% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0036_clefable/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT29_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 240 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`1441ec92f9e6b9b6`, SHA-256 `aab76a7b3322e46be17cb62dbf3366706d1fa2e7e8105615dbccfb6d50a269ca`.

Build Normale:`3724fc8cdfba9514`, SHA-256 `31a8bb0a85c2d0f4b69be3129b3c2283c9a759e90485e0d15eda5149aca5319a`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
