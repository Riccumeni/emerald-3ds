# Cinque checkpoint autonomi — 10–14

Completati **5/5 checkpoint** richiesti, nell’ordine del piano. Partenza: 74 Pokémon. Obiettivo: 114. Totale corrente: **114/386 Pokémon, 6/354 mosse**. Criterio v5 conservato; guardia verticale v5.1 per tutti i gruppi.

| Checkpoint | Specie | Stato | Prove |
|---|---|---|---|
| 1/5 (gruppo 10) | Machop, Machoke, Machamp, Meditite, Medicham, Electrike, Manectric, Plusle | complete | [Dossier, screenshot e video](CHECKPOINT10_REVIEW.md) |
| 2/5 (gruppo 11) | Minun, Magnemite, Magneton, Voltorb, Electrode, Volbeat, Illumise, Oddish | complete | [Dossier, screenshot e video](CHECKPOINT11_REVIEW.md) |
| 3/5 (gruppo 12) | Gloom, Vileplume, Bellossom, Doduo, Dodrio, Roselia, Gulpin, Swalot | complete | [Dossier, screenshot e video](CHECKPOINT12_REVIEW.md) |
| 4/5 (gruppo 13) | Carvanha, Sharpedo, Wailmer, Numel, Camerupt, Slugma, Magcargo, Torkoal | complete | [Dossier, screenshot e video](CHECKPOINT13_REVIEW.md) |
| 5/5 (gruppo 14) | Grimer, Muk, Koffing, Weezing, Spoink, Grumpig, Sandshrew, Sandslash | complete | [Dossier, screenshot e video](CHECKPOINT14_REVIEW.md) |

Le specie vengono segnate come fatte soltanto dopo prove front/back e shiny, revisione visiva e verifica dei dossier. Ogni gruppo completo è salvato in un commit dedicato; i messaggi Git identificano il numero di checkpoint. ROM, asset e filmati restano locali secondo la politica artifacts.

[Piano](../BW2_ANIMATION_PLAN.md) · [Registro](AUTONOMOUS10_14.json) · [Checkpoint di ripresa](CHECKPOINT.md).

## Verifica finale

Audit di **120 dossier**: 114 Pokémon e 6 mosse. Le 40 nuove specie hanno prove native front/back, ingresso e almeno due cicli completi, otto pose campionate per scenario e revisione delle palette shiny. Totale dei 40 incontri normali: **1201.42 secondi**, **36053 fotogrammi**, acquisizione tra 29.95 e 29.98 fps, a velocità 1×. Altri 40 scenari verificano lo shiny.

Il criterio v5.1 resta invariato. Verificati gli hash dei 317 asset precedenti, dei 344 file locali estranei al lavoro e della ROM sorgente. Binari, ELF corrispondenti e file ID sono archiviati; le 35 tavole di revisione sono conservate con hash. Nessun processo isolato è rimasto attivo; Azahar personale è preservato. [Audit con misure e hash](AUTONOMOUS10_14_AUDIT.json).

- Build normale: [3DSX](../../artifacts/bw2-validation/builds/78ea4c127e93ed58_5669769244cf/Emerald3DS-BW2.3dsx), [ELF](../../artifacts/bw2-validation/builds/78ea4c127e93ed58_f9142e767ebd/production.elf), [ID](../../artifacts/bw2-validation/builds/78ea4c127e93ed58_5669769244cf/production-build-id.bin); ID `78ea4c127e93ed58`, SHA-256 `5669769244cfb417882cf953021e219d0250969eff65733dab8e7566047e2eb5`.
- Build di prova: [3DSX](../../artifacts/bw2-validation/builds/35c62b2e2f40bcd4_11ce99dc5a27/validation.3dsx), [ELF](../../artifacts/bw2-validation/builds/35c62b2e2f40bcd4_f8cfc596afdd/validation.elf), [ID](../../artifacts/bw2-validation/builds/35c62b2e2f40bcd4_11ce99dc5a27/build_id.bin); ID `35c62b2e2f40bcd4`, SHA-256 `11ce99dc5a277f4fbc3d58bf36af20d7a140ed201f0e6a90ab426f931cfcf3a0`.

Passati: 16 test esportatore, 7 test di integrità dossier, bridge con dati sintetici e asset reali (sei mosse nei due versi, ripristino attori/palette, shiny e pulizia cache). Build normale senza mailbox di validazione e con stub Frame/Input da 4 byte. Log compilazione e bridge archiviati in `artifacts/bw2-validation/checkpoints10-14-2026-10-28/`.

Limiti: prove su Azahar a 1×; audio non acquisito nel setup senza DSP. Console reale, stereo e doppi restano da verificare. La suite generale non è dichiarata superata: restano i problemi bottom-map preesistenti. ROM, asset e media restano locali secondo la politica artifacts; nessun push.

Prossima unità: **Spinda**, nazionale **327**, ID Emerald **308**; verificare macchie procedurali e seed rappresentativi prima di chiuderla. Nessuna unità rimasta in corso. Il prossimo checkpoint è il **15**.
