# Checkpoint 2/5 — gruppo 16

Completati: **Altaria, Zangoose, Seviper, Lunatone, Solrock, Barboach, Whiscash, Corphish**. Totale piano: **130/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint16-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint16-2026-10-29/pokemon.mp4): 327.64s, 9822 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Altaria | 334/359 | 1.1m | 125.00%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0334_altaria/verifica.md) |
| Zangoose | 335/380 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0335_zangoose/verifica.md) |
| Seviper | 336/379 | 2.7m | 163.28%/208.20% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0336_seviper/verifica.md) |
| Lunatone | 337/348 | 1.0m | 100.00%/148.83% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0337_lunatone/verifica.md) |
| Solrock | 338/349 | 1.2m | 130.47%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0338_solrock/verifica.md) |
| Barboach | 339/323 | 0.4m | 93.75%/122.66% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0339_barboach/verifica.md) |
| Whiscash | 340/324 | 0.9m | 119.92%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0340_whiscash/verifica.md) |
| Corphish | 341/326 | 0.6m | 106.64%/150.78% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0341_corphish/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT16_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 136 dossier verificati; tutti i 477 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`4ec0e4edb35bd030`, SHA-256 `6649af886e687646e349fb7f1bdd1d091016df23e0641e2624bc26f8701f007f`.

Build Normale:`93d67843245e6074`, SHA-256 `283a3e68cd54c250f7247800a6223f76dc622d05477ecb8fd29a84b1179a864c`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei cinque checkpoint](AUTONOMOUS15_19_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
