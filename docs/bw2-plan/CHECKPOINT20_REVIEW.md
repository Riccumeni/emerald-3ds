# Checkpoint 1/10 — gruppo 20

Completati: **Ninetales, Pichu, Pikachu, Raichu, Psyduck, Golduck, Wynaut, Wobbuffet**. Totale piano: **162/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint20-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint20-2026-10-29/pokemon.mp4): 222.41s, 6670 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Ninetales | 38/38 | 1.1m | 125.00%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0038_ninetales/verifica.md) |
| Pichu | 172/172 | 0.3m | 107.81%/138.67% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0172_pichu/verifica.md) |
| Pikachu | 25/25 | 0.4m | 113.67%/157.42% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0025_pikachu/verifica.md) |
| Raichu | 26/26 | 0.8m | 114.84%/166.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0026_raichu/verifica.md) |
| Psyduck | 54/54 | 0.8m | 119.53%/177.73% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0054_psyduck/verifica.md) |
| Golduck | 55/55 | 1.7m | 113.28%/161.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0055_golduck/verifica.md) |
| Wynaut | 360/360 | 0.6m | 110.16%/145.70% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0360_wynaut/verifica.md) |
| Wobbuffet | 202/202 | 1.3m | 106.64%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0202_wobbuffet/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT20_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 168 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`78516b1a53c4bfa8`, SHA-256 `5a198041106a73236613d17631667fd1f74774a24837fa8e06a578d2ccb827ca`.

Build Normale:`39b4647bb1f1c442`, SHA-256 `72f680aa46297f31c747341a34e85817e92e86d09e698d344bb11d37422f8ab4`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
