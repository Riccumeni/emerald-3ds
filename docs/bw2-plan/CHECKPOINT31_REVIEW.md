# Checkpoint 2/10 — gruppo 31

Completati: **Mankey, Primeape, Growlithe, Arcanine, Poliwag, Poliwhirl, Poliwrath, Bellsprout**. Totale piano: **250/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint31-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint31-2026-10-30/pokemon.mp4): 237.34s, 7117 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Mankey | 56/56 | 0.5m | 101.56%/131.64% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0056_mankey/verifica.md) |
| Primeape | 57/57 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0057_primeape/verifica.md) |
| Growlithe | 58/58 | 0.7m | 119.53%/160.16% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0058_growlithe/verifica.md) |
| Arcanine | 59/59 | 1.9m | 141.41%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0059_arcanine/verifica.md) |
| Poliwag | 60/60 | 0.6m | 94.14%/123.44% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0060_poliwag/verifica.md) |
| Poliwhirl | 61/61 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0061_poliwhirl/verifica.md) |
| Poliwrath | 62/62 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0062_poliwrath/verifica.md) |
| Bellsprout | 69/69 | 0.7m | 120.31%/142.19% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0069_bellsprout/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT31_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 256 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
