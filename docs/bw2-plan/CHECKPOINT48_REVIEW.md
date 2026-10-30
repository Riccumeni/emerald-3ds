# Checkpoint 9/9 — gruppo 48

Completati: **Entei, Suicune, Larvitar, Pupitar, Tyranitar, Lugia, Ho Oh, Celebi**. Totale piano: **386/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint48-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint48-2026-10-30/pokemon.mp4): 239.38s, 7179 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Entei | 244/244 | 2.1m | 144.92%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0244_entei/verifica.md) |
| Suicune | 245/245 | 2.0m | 142.97%/189.45% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0245_suicune/verifica.md) |
| Larvitar | 246/246 | 0.6m | 98.05%/125.78% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0246_larvitar/verifica.md) |
| Pupitar | 247/247 | 1.2m | 112.89%/167.58% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0247_pupitar/verifica.md) |
| Tyranitar | 248/248 | 2.0m | 142.97%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0248_tyranitar/verifica.md) |
| Lugia | 249/249 | 5.2m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0249_lugia/verifica.md) |
| Ho Oh | 250/250 | 3.8m | 150.00%/189.84% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0250_ho_oh/verifica.md) |
| Celebi | 251/251 | 0.6m | 88.28%/119.92% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0251_celebi/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT48_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 392 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
