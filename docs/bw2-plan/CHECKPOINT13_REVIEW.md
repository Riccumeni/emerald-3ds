# Checkpoint 4/5 — gruppo 13

Completati: **Carvanha, Sharpedo, Wailmer, Numel, Camerupt, Slugma, Magcargo, Torkoal**. Totale piano: **106/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint13-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint13-2026-10-28/pokemon.mp4): 248.33s, 7446 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Carvanha | 318/330 | 0.8m | 118.75%/181.64% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0318_carvanha/verifica.md) |
| Sharpedo | 319/331 | 1.8m | 139.84%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0319_sharpedo/verifica.md) |
| Wailmer | 320/313 | 2.0m | 142.97%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0320_wailmer/verifica.md) |
| Numel | 322/339 | 0.7m | 110.16%/139.45% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0322_numel/verifica.md) |
| Camerupt | 323/340 | 1.9m | 141.41%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0323_camerupt/verifica.md) |
| Slugma | 218/218 | 0.7m | 132.42%/176.17% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0218_slugma/verifica.md) |
| Magcargo | 219/219 | 0.8m | 116.80%/166.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0219_magcargo/verifica.md) |
| Torkoal | 324/321 | 0.5m | 117.97%/153.12% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0324_torkoal/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT13_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 112 dossier verificati; tutti i 317 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`35c62b2e2f40bcd4`, SHA-256 `11ce99dc5a277f4fbc3d58bf36af20d7a140ed201f0e6a90ab426f931cfcf3a0`.

Build Normale:`78ea4c127e93ed58`, SHA-256 `5669769244cfb417882cf953021e219d0250969eff65733dab8e7566047e2eb5`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS10_14_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
