# Checkpoint 4/9 — gruppo 43

Completati: **Wooper, Quagsire, Espeon, Umbreon, Murkrow, Slowking, Misdreavus, Unown**. Totale piano: **346/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint43-2026-10-30/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint43-2026-10-30/pokemon.mp4): 214.17s, 6423 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Wooper | 194/194 | 0.4m | 104.30%/140.23% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0194_wooper/verifica.md) |
| Quagsire | 195/195 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0195_quagsire/verifica.md) |
| Espeon | 196/196 | 0.9m | 119.92%/179.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0196_espeon/verifica.md) |
| Umbreon | 197/197 | 1.0m | 115.62%/172.27% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0197_umbreon/verifica.md) |
| Murkrow | 198/198 | 0.5m | 106.64%/133.98% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0198_murkrow/verifica.md) |
| Slowking | 199/199 | 2.0m | 114.84%/151.56% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0199_slowking/verifica.md) |
| Misdreavus | 200/200 | 0.7m | 117.19%/154.69% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0200_misdreavus/verifica.md) |
| Unown | 201/201 | 0.5m | 108.98%/153.52% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0201_unown/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT43_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 352 dossier verificati; tutti i 1294 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`5f8ed2ae5815137f`, SHA-256 `f4bbbe0e09bc1ba120d00e78858c70cf2621da876aea8e7c0fc025b1390952a0`.

Build Normale:`c18abb147273c4ca`, SHA-256 `5f1a359e9eb5f188a28110162d93653d4a679207ae2de8de8120710703e6f073`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei nove checkpoint](AUTONOMOUS40_48_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).

## Unown: verifica aggiuntiva obbligatoria

[Tutte le 28 forme normali e shiny, mappatura, personality e più attori](UNOWN_REVIEW.md). La forma A è nel dossier principale; le altre in forms/. Le 56 registrazioni aggiuntive includono ingresso e almeno due cicli; immagini campionate ispezionate prima di registrare la revisione, poi publisher e progress hanno verificato indipendentemente tutti i casi. Le forme non aumentano il contatore delle specie.
