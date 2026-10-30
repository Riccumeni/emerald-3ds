# Checkpoint 5/5 — gruppo 14

Completati: **Grimer, Muk, Koffing, Weezing, Spoink, Grumpig, Sandshrew, Sandslash**. Totale piano: **114/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint14-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint14-2026-10-28/pokemon.mp4): 214.14s, 6422 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Grimer | 88/88 | 0.9m | 98.05%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0088_grimer/verifica.md) |
| Muk | 89/89 | 1.2m | 154.69%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0089_muk/verifica.md) |
| Koffing | 109/109 | 0.6m | 129.69%/175.00% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0109_koffing/verifica.md) |
| Weezing | 110/110 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0110_weezing/verifica.md) |
| Spoink | 325/351 | 0.7m | 88.28%/123.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0325_spoink/verifica.md) |
| Grumpig | 326/352 | 0.9m | 121.88%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0326_grumpig/verifica.md) |
| Sandshrew | 27/27 | 0.6m | 130.47%/165.62% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0027_sandshrew/verifica.md) |
| Sandslash | 28/28 | 1.0m | 101.56%/154.30% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0028_sandslash/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT14_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 120 dossier verificati; tutti i 317 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`35c62b2e2f40bcd4`, SHA-256 `11ce99dc5a277f4fbc3d58bf36af20d7a140ed201f0e6a90ab426f931cfcf3a0`.

Build Normale:`78ea4c127e93ed58`, SHA-256 `5669769244cfb417882cf953021e219d0250969eff65733dab8e7566047e2eb5`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS10_14_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
