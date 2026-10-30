# Checkpoint 6/9 — gruppo 45

Completati: **Scizor, Shuckle, Sneasel, Teddiursa, Ursaring, Swinub, Piloswine, Remoraid**. Totale piano: **362/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint45-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint45-2026-10-30/pokemon.mp4): 205.42s, 6159 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Scizor | 212/212 | 1.8m | 139.84%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0212_scizor/verifica.md) |
| Shuckle | 213/213 | 0.6m | 118.36%/165.23% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0213_shuckle/verifica.md) |
| Sneasel | 215/215 | 0.9m | 100.00%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0215_sneasel/verifica.md) |
| Teddiursa | 216/216 | 0.6m | 141.41%/188.67% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0216_teddiursa/verifica.md) |
| Ursaring | 217/217 | 1.8m | 139.84%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0217_ursaring/verifica.md) |
| Swinub | 220/220 | 0.4m | 128.52%/168.36% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0220_swinub/verifica.md) |
| Piloswine | 221/221 | 1.1m | 107.03%/158.59% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0221_piloswine/verifica.md) |
| Remoraid | 223/223 | 0.6m | 135.94%/145.70% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0223_remoraid/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT45_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 368 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
