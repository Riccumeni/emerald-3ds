# Checkpoint 4/5 — gruppo 18

Completati: **Jigglypuff, Wigglytuff, Feebas, Milotic, Castform, Staryu, Starmie, Kecleon**. Totale piano: **146/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint18-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint18-2026-10-29/pokemon.mp4): 241.24s, 7228 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Jigglypuff | 39/39 | 0.5m | 106.25%/140.23% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0039_jigglypuff/verifica.md) |
| Wigglytuff | 40/40 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0040_wigglytuff/verifica.md) |
| Feebas | 349/328 | 0.6m | 98.05%/133.20% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0349_feebas/verifica.md) |
| Milotic | 350/329 | 6.2m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0350_milotic/verifica.md) |
| Castform | 351/385 | 0.3m | 112.50%/138.67% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0351_castform/verifica.md) |
| Staryu | 120/120 | 0.8m | 98.05%/150.00% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0120_staryu/verifica.md) |
| Starmie | 121/121 | 1.1m | 103.12%/168.75% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0121_starmie/verifica.md) |
| Kecleon | 352/317 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0352_kecleon/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT18_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 152 dossier verificati; tutti i 477 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`24b3c6b5fb7206c7`, SHA-256 `d46fe452124971b1f853041140908d6e566c0fd7df0e1ce5dd5400aebf5c9594`.

Build Normale:`b9eafa1bb23e8fcf`, SHA-256 `ad98f8246237ba4a1998bdcf5dd50a3cafd8688784a2347cc3a04923506d7c6b`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS15_19_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).

[Castform: quattro forme, shiny, Forecast e ritorno naturale al normale](CASTFORM_REVIEW.md). Le mosse meteo di prova mantengono le animazioni Emerald e restano in attesa di importazione BW2.
