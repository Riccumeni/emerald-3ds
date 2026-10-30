# Checkpoint 6/10 — gruppo 35

Completati: **Hitmonchan, Lickitung, Chansey, Tangela, Kangaskhan, Mr Mime, Scyther, Jynx**. Totale piano: **282/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint35-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint35-2026-10-30/pokemon.mp4): 246.02s, 7377 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Hitmonchan | 107/107 | 1.4m | 108.20%/158.59% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0107_hitmonchan/verifica.md) |
| Lickitung | 108/108 | 1.2m | 128.12%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0108_lickitung/verifica.md) |
| Chansey | 113/113 | 1.1m | 100.00%/148.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0113_chansey/verifica.md) |
| Tangela | 114/114 | 1.0m | 120.31%/175.78% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0114_tangela/verifica.md) |
| Kangaskhan | 115/115 | 2.2m | 146.48%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0115_kangaskhan/verifica.md) |
| Mr Mime | 122/122 | 1.3m | 110.55%/161.72% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0122_mr_mime/verifica.md) |
| Scyther | 123/123 | 1.5m | 134.77%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0123_scyther/verifica.md) |
| Jynx | 124/124 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0124_jynx/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT35_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 288 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
