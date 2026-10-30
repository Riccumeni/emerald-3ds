# Checkpoint 8/9 — gruppo 47

Completati: **Tyrogue, Hitmontop, Smoochum, Elekid, Magby, Miltank, Blissey, Raikou**. Totale piano: **378/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint47-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint47-2026-10-30/pokemon.mp4): 230.47s, 6912 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Tyrogue | 236/236 | 0.7m | 117.58%/164.06% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0236_tyrogue/verifica.md) |
| Hitmontop | 237/237 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0237_hitmontop/verifica.md) |
| Smoochum | 238/238 | 0.4m | 93.75%/122.66% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0238_smoochum/verifica.md) |
| Elekid | 239/239 | 0.6m | 100.00%/132.03% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0239_elekid/verifica.md) |
| Magby | 240/240 | 0.7m | 96.09%/132.03% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0240_magby/verifica.md) |
| Miltank | 241/241 | 1.2m | 105.08%/161.72% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0241_miltank/verifica.md) |
| Blissey | 242/242 | 1.5m | 111.33%/161.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0242_blissey/verifica.md) |
| Raikou | 243/243 | 1.9m | 141.41%/189.45% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0243_raikou/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT47_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 384 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
