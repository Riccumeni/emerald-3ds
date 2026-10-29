# Checkpoint 4/10 — gruppo 23

Completati: **Relicanth, Corsola, Chinchou, Lanturn, Luvdisc, Horsea, Seadra, Kingdra**. Totale piano: **186/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint23-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint23-2026-10-29/pokemon.mp4): 203.05s, 6090 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Relicanth | 369/381 | 1.0m | 101.56%/154.30% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0369_relicanth/verifica.md) |
| Corsola | 222/222 | 0.6m | 101.56%/128.91% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0222_corsola/verifica.md) |
| Chinchou | 170/170 | 0.5m | 101.56%/131.64% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0170_chinchou/verifica.md) |
| Lanturn | 171/171 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0171_lanturn/verifica.md) |
| Luvdisc | 370/325 | 0.6m | 137.50%/183.59% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0370_luvdisc/verifica.md) |
| Horsea | 116/116 | 0.4m | 107.03%/147.27% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0116_horsea/verifica.md) |
| Seadra | 117/117 | 1.2m | 110.16%/154.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0117_seadra/verifica.md) |
| Kingdra | 230/230 | 1.8m | 139.84%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0230_kingdra/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT23_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 192 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`78516b1a53c4bfa8`, SHA-256 `5a198041106a73236613d17631667fd1f74774a24837fa8e06a578d2ccb827ca`.

Build Normale:`39b4647bb1f1c442`, SHA-256 `72f680aa46297f31c747341a34e85817e92e86d09e698d344bb11d37422f8ab4`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
