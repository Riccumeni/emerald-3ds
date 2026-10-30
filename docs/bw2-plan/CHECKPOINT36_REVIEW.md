# Checkpoint 7/10 — gruppo 36

Completati: **Electabuzz, Magmar, Tauros, Lapras, Ditto, Eevee, Vaporeon, Jolteon**. Totale piano: **290/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint36-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint36-2026-10-30/pokemon.mp4): 229.39s, 6878 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Electabuzz | 125/125 | 1.1m | 125.00%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0125_electabuzz/verifica.md) |
| Magmar | 126/126 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0126_magmar/verifica.md) |
| Tauros | 128/128 | 1.4m | 135.55%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0128_tauros/verifica.md) |
| Lapras | 131/131 | 2.5m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0131_lapras/verifica.md) |
| Ditto | 132/132 | 0.3m | 89.06%/117.19% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0132_ditto/verifica.md) |
| Eevee | 133/133 | 0.3m | 107.81%/135.94% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0133_eevee/verifica.md) |
| Vaporeon | 134/134 | 1.0m | 100.00%/157.03% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0134_vaporeon/verifica.md) |
| Jolteon | 135/135 | 0.8m | 112.11%/166.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0135_jolteon/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT36_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 296 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
