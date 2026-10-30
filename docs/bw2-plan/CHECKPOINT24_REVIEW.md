# Checkpoint 5/10 — gruppo 24

Completati: **Bagon, Shelgon, Salamence, Beldum, Metang, Metagross, Regirock, Regice**. Totale piano: **194/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint24-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint24-2026-10-29/pokemon.mp4): 262.44s, 7869 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Bagon | 371/395 | 0.6m | 100.00%/135.94% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0371_bagon/verifica.md) |
| Shelgon | 372/396 | 1.1m | 122.27%/177.73% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0372_shelgon/verifica.md) |
| Salamence | 373/397 | 1.5m | 156.64%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0373_salamence/verifica.md) |
| Beldum | 374/398 | 0.6m | 108.20%/150.78% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0374_beldum/verifica.md) |
| Metang | 375/399 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0375_metang/verifica.md) |
| Metagross | 376/400 | 1.6m | 136.33%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0376_metagross/verifica.md) |
| Regirock | 377/401 | 1.7m | 138.28%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0377_regirock/verifica.md) |
| Regice | 378/402 | 1.8m | 139.84%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0378_regice/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT24_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 200 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`78516b1a53c4bfa8`, SHA-256 `5a198041106a73236613d17631667fd1f74774a24837fa8e06a578d2ccb827ca`.

Build Normale:`39b4647bb1f1c442`, SHA-256 `72f680aa46297f31c747341a34e85817e92e86d09e698d344bb11d37422f8ab4`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
