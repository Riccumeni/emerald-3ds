# Checkpoint 1/10 — gruppo 30

Completati: **Paras, Parasect, Venonat, Venomoth, Diglett, Dugtrio, Meowth, Persian**. Totale piano: **242/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint30-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint30-2026-10-30/pokemon.mp4): 226.16s, 6783 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Paras | 46/46 | 0.3m | 89.45%/116.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0046_paras/verifica.md) |
| Parasect | 47/47 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0047_parasect/verifica.md) |
| Venonat | 48/48 | 1.0m | 110.94%/166.02% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0048_venonat/verifica.md) |
| Venomoth | 49/49 | 1.5m | 164.84%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0049_venomoth/verifica.md) |
| Diglett | 50/50 | 0.2m | 100.00%/128.91% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0050_diglett/verifica.md) |
| Dugtrio | 51/51 | 0.7m | 101.56%/142.19% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0051_dugtrio/verifica.md) |
| Meowth | 52/52 | 0.4m | 94.92%/123.05% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0052_meowth/verifica.md) |
| Persian | 53/53 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0053_persian/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT30_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 248 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
