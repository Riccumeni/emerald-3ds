# Checkpoint 1/9 — gruppo 40

Completati: **Feraligatr, Sentret, Furret, Hoothoot, Noctowl, Ledyba, Ledian, Spinarak**. Totale piano: **322/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint40-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint40-2026-10-30/pokemon.mp4): 218.88s, 6564 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Feraligatr | 160/160 | 2.3m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0160_feraligatr/verifica.md) |
| Sentret | 161/161 | 0.8m | 114.84%/166.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0161_sentret/verifica.md) |
| Furret | 162/162 | 1.8m | 118.36%/156.64% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0162_furret/verifica.md) |
| Hoothoot | 163/163 | 0.7m | 113.28%/160.16% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0163_hoothoot/verifica.md) |
| Noctowl | 164/164 | 1.6m | 108.20%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0164_noctowl/verifica.md) |
| Ledyba | 165/165 | 1.0m | 115.62%/187.11% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0165_ledyba/verifica.md) |
| Ledian | 166/166 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0166_ledian/verifica.md) |
| Spinarak | 167/167 | 0.5m | 111.33%/139.84% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0167_spinarak/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT40_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 328 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
