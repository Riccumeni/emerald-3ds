# Checkpoint 3/10 — gruppo 32

Completati: **Weepinbell, Victreebel, Ponyta, Rapidash, Slowpoke, Slowbro, Farfetchd, Seel**. Totale piano: **258/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint32-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint32-2026-10-30/pokemon.mp4): 206.44s, 6191 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Weepinbell | 70/70 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0070_weepinbell/verifica.md) |
| Victreebel | 71/71 | 1.7m | 138.28%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0071_victreebel/verifica.md) |
| Ponyta | 77/77 | 1.0m | 105.08%/153.91% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0077_ponyta/verifica.md) |
| Rapidash | 78/78 | 1.7m | 138.28%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0078_rapidash/verifica.md) |
| Slowpoke | 79/79 | 1.2m | 106.64%/156.64% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0079_slowpoke/verifica.md) |
| Slowbro | 80/80 | 1.6m | 136.33%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0080_slowbro/verifica.md) |
| Farfetchd | 83/83 | 0.8m | 112.11%/159.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0083_farfetchd/verifica.md) |
| Seel | 86/86 | 1.1m | 100.00%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0086_seel/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT32_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 264 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
