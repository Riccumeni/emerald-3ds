# Checkpoint 7/10 — gruppo 26

Completati: **Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle**. Totale piano: **210/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint26-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint26-2026-10-29/pokemon.mp4): 227.92s, 6830 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Bulbasaur | 1/1 | 0.7m | 139.45%/200.00% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0001_bulbasaur/verifica.md) |
| Ivysaur | 2/2 | 1.0m | 101.56%/154.30% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0002_ivysaur/verifica.md) |
| Venusaur | 3/3 | 2.0m | 142.97%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0003_venusaur/verifica.md) |
| Charmander | 4/4 | 0.6m | 121.09%/154.30% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0004_charmander/verifica.md) |
| Charmeleon | 5/5 | 1.1m | 129.30%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0005_charmeleon/verifica.md) |
| Charizard | 6/6 | 1.7m | 141.80%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0006_charizard/verifica.md) |
| Squirtle | 7/7 | 0.5m | 111.33%/139.84% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0007_squirtle/verifica.md) |
| Wartortle | 8/8 | 1.0m | 103.12%/154.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0008_wartortle/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT26_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 216 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`1441ec92f9e6b9b6`, SHA-256 `aab76a7b3322e46be17cb62dbf3366706d1fa2e7e8105615dbccfb6d50a269ca`.

Build Normale:`3724fc8cdfba9514`, SHA-256 `31a8bb0a85c2d0f4b69be3129b3c2283c9a759e90485e0d15eda5149aca5319a`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
