# Checkpoint 5/10 — gruppo 34

Completati: **Hypno, Krabby, Kingler, Exeggcute, Exeggutor, Cubone, Marowak, Hitmonlee**. Totale piano: **274/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint34-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint34-2026-10-30/pokemon.mp4): 229.11s, 6870 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Hypno | 97/97 | 1.6m | 136.33%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0097_hypno/verifica.md) |
| Krabby | 98/98 | 0.4m | 101.56%/134.38% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0098_krabby/verifica.md) |
| Kingler | 99/99 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0099_kingler/verifica.md) |
| Exeggcute | 102/102 | 0.4m | 105.47%/136.72% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0102_exeggcute/verifica.md) |
| Exeggutor | 103/103 | 2.0m | 142.97%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0103_exeggutor/verifica.md) |
| Cubone | 104/104 | 0.4m | 113.67%/139.45% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0104_cubone/verifica.md) |
| Marowak | 105/105 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0105_marowak/verifica.md) |
| Hitmonlee | 106/106 | 1.5m | 134.77%/189.45% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0106_hitmonlee/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT34_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 280 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
