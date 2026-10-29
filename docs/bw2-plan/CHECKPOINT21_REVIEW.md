# Checkpoint 2/10 — gruppo 21

Completati: **Xatu, Girafarig, Phanpy, Donphan, Pinsir, Heracross, Rhyhorn, Rhydon**. Totale piano: **170/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint21-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint21-2026-10-29/pokemon.mp4): 241.25s, 7234 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Xatu | 178/178 | 1.5m | 109.77%/151.56% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0178_xatu/verifica.md) |
| Girafarig | 203/203 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0203_girafarig/verifica.md) |
| Phanpy | 231/231 | 0.5m | 101.95%/131.25% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0231_phanpy/verifica.md) |
| Donphan | 232/232 | 1.1m | 126.95%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0232_donphan/verifica.md) |
| Pinsir | 127/127 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0127_pinsir/verifica.md) |
| Heracross | 214/214 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0214_heracross/verifica.md) |
| Rhyhorn | 111/111 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0111_rhyhorn/verifica.md) |
| Rhydon | 112/112 | 1.9m | 141.41%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0112_rhydon/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT21_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 176 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`78516b1a53c4bfa8`, SHA-256 `5a198041106a73236613d17631667fd1f74774a24837fa8e06a578d2ccb827ca`.

Build Normale:`39b4647bb1f1c442`, SHA-256 `72f680aa46297f31c747341a34e85817e92e86d09e698d344bb11d37422f8ab4`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
