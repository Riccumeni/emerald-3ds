# Checkpoint 8/10 — gruppo 27

Completati: **Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey**. Totale piano: **218/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint27-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint27-2026-10-29/pokemon.mp4): 238.80s, 7153 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Blastoise | 9/9 | 1.6m | 136.33%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0009_blastoise/verifica.md) |
| Caterpie | 10/10 | 0.3m | 113.28%/141.80% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0010_caterpie/verifica.md) |
| Metapod | 11/11 | 0.7m | 142.97%/171.88% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0011_metapod/verifica.md) |
| Butterfree | 12/12 | 1.1m | 125.00%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0012_butterfree/verifica.md) |
| Weedle | 13/13 | 0.3m | 112.50%/147.66% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0013_weedle/verifica.md) |
| Kakuna | 14/14 | 0.6m | 130.47%/165.62% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0014_kakuna/verifica.md) |
| Beedrill | 15/15 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0015_beedrill/verifica.md) |
| Pidgey | 16/16 | 0.3m | 110.16%/147.66% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0016_pidgey/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT27_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 224 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`1441ec92f9e6b9b6`, SHA-256 `aab76a7b3322e46be17cb62dbf3366706d1fa2e7e8105615dbccfb6d50a269ca`.

Build Normale:`3724fc8cdfba9514`, SHA-256 `31a8bb0a85c2d0f4b69be3129b3c2283c9a759e90485e0d15eda5149aca5319a`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
