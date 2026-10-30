# Checkpoint 4/10 — gruppo 33

Completati: **Dewgong, Shellder, Cloyster, Gastly, Haunter, Gengar, Onix, Drowzee**. Totale piano: **266/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint33-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint33-2026-10-30/pokemon.mp4): 223.59s, 6706 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Dewgong | 87/87 | 1.7m | 138.28%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0087_dewgong/verifica.md) |
| Shellder | 90/90 | 0.3m | 102.34%/119.14% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0090_shellder/verifica.md) |
| Cloyster | 91/91 | 1.5m | 137.11%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0091_cloyster/verifica.md) |
| Gastly | 92/92 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0092_gastly/verifica.md) |
| Haunter | 93/93 | 1.6m | 136.33%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0093_haunter/verifica.md) |
| Gengar | 94/94 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0094_gengar/verifica.md) |
| Onix | 95/95 | 8.8m | 144.14%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0095_onix/verifica.md) |
| Drowzee | 96/96 | 1.0m | 101.56%/154.30% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0096_drowzee/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT33_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 272 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
