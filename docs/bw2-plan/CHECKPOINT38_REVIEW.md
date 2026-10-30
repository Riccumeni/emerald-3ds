# Checkpoint 9/10 — gruppo 38

Completati: **Articuno, Zapdos, Moltres, Dratini, Dragonair, Dragonite, Mewtwo, Mew**. Totale piano: **306/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint38-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint38-2026-10-30/pokemon.mp4): 199.42s, 5979 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Articuno | 144/144 | 1.7m | 131.64%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0144_articuno/verifica.md) |
| Zapdos | 145/145 | 1.6m | 138.67%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0145_zapdos/verifica.md) |
| Moltres | 146/146 | 2.0m | 173.05%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0146_moltres/verifica.md) |
| Dratini | 147/147 | 1.8m | 131.25%/161.72% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0147_dratini/verifica.md) |
| Dragonair | 148/148 | 4.0m | 144.14%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0148_dragonair/verifica.md) |
| Dragonite | 149/149 | 2.2m | 131.64%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0149_dragonite/verifica.md) |
| Mewtwo | 150/150 | 2.0m | 142.97%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0150_mewtwo/verifica.md) |
| Mew | 151/151 | 0.4m | 113.28%/146.48% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0151_mew/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT38_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 312 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
