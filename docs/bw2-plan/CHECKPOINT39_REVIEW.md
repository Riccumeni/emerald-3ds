# Checkpoint 10/10 — gruppo 39

Completati: **Chikorita, Bayleef, Meganium, Cyndaquil, Quilava, Typhlosion, Totodile, Croconaw**. Totale piano: **314/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint39-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint39-2026-10-30/pokemon.mp4): 223.31s, 6697 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Chikorita | 152/152 | 0.9m | 100.00%/145.70% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0152_chikorita/verifica.md) |
| Bayleef | 153/153 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0153_bayleef/verifica.md) |
| Meganium | 154/154 | 1.8m | 139.84%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0154_meganium/verifica.md) |
| Cyndaquil | 155/155 | 0.5m | 106.64%/136.72% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0155_cyndaquil/verifica.md) |
| Quilava | 156/156 | 0.9m | 119.92%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0156_quilava/verifica.md) |
| Typhlosion | 157/157 | 1.7m | 138.28%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0157_typhlosion/verifica.md) |
| Totodile | 158/158 | 0.6m | 108.20%/142.97% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0158_totodile/verifica.md) |
| Croconaw | 159/159 | 1.1m | 103.12%/153.12% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0159_croconaw/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT39_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 320 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
