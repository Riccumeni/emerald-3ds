# Checkpoint 3/10 — gruppo 22

Completati: **Snorunt, Glalie, Spheal, Sealeo, Walrein, Clamperl, Huntail, Gorebyss**. Totale piano: **178/386 Pokémon, 6/354 mosse**.

![Viste front/back](../../artifacts/bw2-validation/checkpoint22-2026-10-29/pokemon.png)

[Video completo](../../artifacts/bw2-validation/checkpoint22-2026-10-29/pokemon.mp4): 217.22s, 6514 fotogrammi, concatenazione nativa senza tagli, ricodifica o accelerazione. Le raccolte PNG ritagliano lo schermo superiore; ogni dossier conserva screenshot integrali 400×480 e video delle due viste.

| Specie | Nazionale/Emerald | Altezza | Scala front/back | Dossier |
|---|---|---:|---:|---|
| Snorunt | 361/346 | 0.7m | 135.55%/194.53% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0361_snorunt/verifica.md) |
| Glalie | 362/347 | 1.5m | 130.47%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0362_glalie/verifica.md) |
| Spheal | 363/341 | 0.8m | 130.86%/200.00% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0363_spheal/verifica.md) |
| Sealeo | 364/342 | 1.1m | 100.00%/150.00% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0364_sealeo/verifica.md) |
| Walrein | 365/343 | 1.4m | 133.20%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0365_walrein/verifica.md) |
| Clamperl | 366/373 | 0.4m | 104.30%/134.77% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0366_clamperl/verifica.md) |
| Huntail | 367/374 | 1.7m | 138.28%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0367_huntail/verifica.md) |
| Gorebyss | 368/375 | 1.8m | 139.84%/186.33% | [PNG,MP4,shiny e metadati](../../artifacts/bw2-validation/pokemon/0368_gorebyss/verifica.md) |

Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi: altezza Emerald e impronta nativa BW2 condivisa tra le due viste, centro posteriore nell’arena indipendente dal testo. [Misure](CHECKPOINT22_MEASUREMENTS.json).

Verificati otto incontri con almeno due cicli completi per attore, otto pose campionate per scenario, screenshot e frame QA iniziali/centrali/finali. Otto altri scenari confrontano le palette shiny con gli asset. I dossier sono stati chiusi singolarmente dopo la revisione. Audit attuale: 184 dossier verificati; tutti i 650 file degli asset precedenti invariati. Nessuna nuova mossa in questo gruppo.

Build Prova:`78516b1a53c4bfa8`, SHA-256 `5a198041106a73236613d17631667fd1f74774a24837fa8e06a578d2ccb827ca`.

Build Normale:`39b4647bb1f1c442`, SHA-256 `72f680aa46297f31c747341a34e85817e92e86d09e698d344bb11d37422f8ab4`.

[Verifica del margine superiore v5.1](FRONT_HEADROOM_REVIEW.json): confronto prima/dopo su Hariyama; nessuna scala cambiata per le 50 specie già chiuse.

Build ed ELF di prova archiviati secondo i metadati; normale senza mailbox/automatismi, con Frame/Input da 4 byte. Limiti: prove su emulatore Azahar a 1×; audio non acquisito nel setup senza DSP; console, stereo e doppi restano nella fase d’integrazione.

[Riepilogo dei dieci checkpoint](AUTONOMOUS20_29_REVIEW.md) · [Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md).
