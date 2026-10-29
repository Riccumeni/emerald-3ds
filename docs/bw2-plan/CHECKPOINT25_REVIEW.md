# Checkpoint 6/10 — gruppo 25

Completati: **Registeel, Latias, Latios, Kyogre, Groudon, Rayquaza, Jirachi, Deoxys**. Totale piano: **202/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint25-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint25-2026-10-29/pokemon.mp4): 286.77s, 8601 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Registeel | 379/403 | 1.9m | 141.41%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0379_registeel/verifica.md) |
| Latias | 380/407 | 1.4m | 135.55%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0380_latias/verifica.md) |
| Latios | 381/408 | 2.0m | 155.08%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0381_latios/verifica.md) |
| Kyogre | 382/404 | 4.5m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0382_kyogre/verifica.md) |
| Groudon | 383/405 | 3.5m | 151.56%/192.97% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0383_groudon/verifica.md) |
| Rayquaza | 384/406 | 7.0m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0384_rayquaza/verifica.md) |
| Jirachi | 385/409 | 0.3m | 98.05%/141.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0385_jirachi/verifica.md) |
| Deoxys | 386/410 | 1.7m | 128.52%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0386_deoxys/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT25_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 208 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`41d32c7d95a1d171`, SHA-256 `24cd0dd6f7badd662c5f1b1d615a0c93279321370936d58f49e46566c9e08b1f`.

Build Normale:`a7578461a1177544`, SHA-256 `b4c867aef84895c9b663b312b4a4da09193483e5d2f351b2cf3fa105721ef7e2`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).

[Deoxys: due forme, shiny, turni reali di Trasformazione e regressione Spinda](DEOXYS_REVIEW.md). Le build corrispondenti a ciascun dossier sono distinte nei metadati e conservate nella cronologia; nessuna mossa aggiunta.
