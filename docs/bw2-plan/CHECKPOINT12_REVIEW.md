# Checkpoint 3/5 — gruppo 12

Completati: **Gloom, Vileplume, Bellossom, Doduo, Dodrio, Roselia, Gulpin, Swalot**. Totale piano: **98/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint12-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint12-2026-10-28/pokemon.mp4): 241.39s, 7239 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Gloom | 44/44 | 0.8m | 107.81%/162.89% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0044_gloom/verifica.md) |
| Vileplume | 45/45 | 1.2m | 108.59%/158.59% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0045_vileplume/verifica.md) |
| Bellossom | 182/182 | 0.4m | 101.56%/142.19% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0182_bellossom/verifica.md) |
| Doduo | 84/84 | 1.4m | 108.20%/153.12% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0084_doduo/verifica.md) |
| Dodrio | 85/85 | 1.8m | 139.84%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0085_dodrio/verifica.md) |
| Roselia | 315/363 | 0.3m | 104.69%/134.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0315_roselia/verifica.md) |
| Gulpin | 316/367 | 0.4m | 101.95%/140.23% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0316_gulpin/verifica.md) |
| Swalot | 317/368 | 1.7m | 138.28%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0317_swalot/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT12_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 104 dossier verificati; tutti i 317 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`35c62b2e2f40bcd4`, SHA-256 `11ce99dc5a277f4fbc3d58bf36af20d7a140ed201f0e6a90ab426f931cfcf3a0`.

Build Normale:`78ea4c127e93ed58`, SHA-256 `5669769244cfb417882cf953021e219d0250969eff65733dab8e7566047e2eb5`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS10_14_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
