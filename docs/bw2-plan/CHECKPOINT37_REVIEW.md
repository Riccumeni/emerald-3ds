# Checkpoint 8/10 — gruppo 37

Completati: **Flareon, Porygon, Omanyte, Omastar, Kabuto, Kabutops, Aerodactyl, Snorlax**. Totale piano: **298/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint37-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint37-2026-10-30/pokemon.mp4): 232.55s, 6974 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Flareon | 136/136 | 0.9m | 119.92%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0136_flareon/verifica.md) |
| Porygon | 137/137 | 0.8m | 118.75%/166.41% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0137_porygon/verifica.md) |
| Omanyte | 138/138 | 0.4m | 129.30%/150.78% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0138_omanyte/verifica.md) |
| Omastar | 139/139 | 1.0m | 123.05%/184.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0139_omastar/verifica.md) |
| Kabuto | 140/140 | 0.5m | 119.92%/146.48% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0140_kabuto/verifica.md) |
| Kabutops | 141/141 | 1.3m | 129.69%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0141_kabutops/verifica.md) |
| Aerodactyl | 142/142 | 1.8m | 173.05%/209.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0142_aerodactyl/verifica.md) |
| Snorlax | 143/143 | 2.1m | 144.92%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0143_snorlax/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT37_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 304 dossier verificati; tutti i 978 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`de509bec1e539760`, SHA-256 `f2ecde88d6d665029ecfcd7e5c335604e31d8bb3c96c4adc7c04f272636d468c`.

Build Normale:`f65244ae7f660a26`, SHA-256 `6b27f2290acfcd48b5813237d5c072fd4b3ea48c63825de7177dbff0f28f25f6`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS30_39_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
