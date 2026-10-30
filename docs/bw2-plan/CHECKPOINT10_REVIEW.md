# Checkpoint 1/5 — gruppo 10

Completati: **Machop, Machoke, Machamp, Meditite, Medicham, Electrike, Manectric, Plusle**. Totale piano: **82/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint10-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint10-2026-10-28/pokemon.mp4): 277.58s, 8325 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Machop | 66/66 | 0.8m | 109.77%/153.52% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0066_machop/verifica.md) |
| Machoke | 67/67 | 1.5m | 134.77%/189.45% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0067_machoke/verifica.md) |
| Machamp | 68/68 | 1.6m | 136.33%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0068_machamp/verifica.md) |
| Meditite | 307/356 | 0.6m | 98.05%/139.06% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0307_meditite/verifica.md) |
| Medicham | 308/357 | 1.3m | 104.69%/151.56% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0308_medicham/verifica.md) |
| Electrike | 309/337 | 0.6m | 101.95%/144.53% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0309_electrike/verifica.md) |
| Manectric | 310/338 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0310_manectric/verifica.md) |
| Plusle | 311/353 | 0.4m | 93.75%/122.27% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0311_plusle/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT10_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 88 dossier verificati; tutti i 317 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`35c62b2e2f40bcd4`, SHA-256 `11ce99dc5a277f4fbc3d58bf36af20d7a140ed201f0e6a90ab426f931cfcf3a0`.

Build Normale:`78ea4c127e93ed58`, SHA-256 `5669769244cfb417882cf953021e219d0250969eff65733dab8e7566047e2eb5`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS10_14_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
