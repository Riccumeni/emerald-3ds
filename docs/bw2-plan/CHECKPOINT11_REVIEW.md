# Checkpoint 2/5 — gruppo 11

Completati: **Minun, Magnemite, Magneton, Voltorb, Electrode, Volbeat, Illumise, Oddish**. Totale piano: **90/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint11-2026-10-28/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint11-2026-10-28/pokemon.mp4): 220.77s, 6621 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Minun | 312/354 | 0.4m | 116.02%/144.92% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0312_minun/verifica.md) |
| Magnemite | 81/81 | 0.3m | 113.28%/150.00% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0081_magnemite/verifica.md) |
| Magneton | 82/82 | 1.0m | 123.05%/187.89% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0082_magneton/verifica.md) |
| Voltorb | 100/100 | 0.5m | 104.30%/136.72% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0100_voltorb/verifica.md) |
| Electrode | 101/101 | 1.2m | 119.53%/174.22% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0101_electrode/verifica.md) |
| Volbeat | 313/386 | 0.7m | 111.33%/154.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0313_volbeat/verifica.md) |
| Illumise | 314/387 | 0.6m | 118.36%/153.52% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0314_illumise/verifica.md) |
| Oddish | 43/43 | 0.5m | 97.66%/125.39% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0043_oddish/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT11_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 96 dossier verificati; tutti i 317 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`35c62b2e2f40bcd4`, SHA-256 `11ce99dc5a277f4fbc3d58bf36af20d7a140ed201f0e6a90ab426f931cfcf3a0`.

Build Normale:`78ea4c127e93ed58`, SHA-256 `5669769244cfb417882cf953021e219d0250969eff65733dab8e7566047e2eb5`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS10_14_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
