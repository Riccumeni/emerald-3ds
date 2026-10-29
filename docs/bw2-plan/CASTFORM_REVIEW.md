# Castform — quattro forme e Forecast

Castform (#351, ID Emerald 385) usa quattro coppie front/back BW2: normale, Sole, Pioggia e Neve. Il bridge legge `gBattleMonForms` e ricollega la clip quando Forecast cambia la forma. Meteo, abilità, tipi, turni e animazione della trasformazione restano quelli di Emerald.

Le risorse sono individuate dalla tabella personal BW2 `a/0/1/6`, voce 351: offset sprite 27, quattro forme. I blocchi aggiuntivi nell'archivio grafico `a/0/0/4` iniziano alle risorse 14240, 14260 e 14280. Ciascuno conserva timeline, parti trasformate, palette normale/shiny e impronta delle due viste. L'export incrementale conserva anche l'inventario delle forme già esportate.

La presentazione applica il criterio generale v5.1 a ogni coppia di viste; nessuna correzione di scala o posizione specifica per Castform. Il back resta centrato nell'arena e può essere parzialmente coperto dal testo.

| Caso | Prove native del gioco | Pose campionate |
|---|---|---|
| Normale | [Front](../../artifacts/bw2-validation/pokemon/0351_castform/front/demo.mp4), [back](../../artifacts/bw2-validation/pokemon/0351_castform/back/demo.mp4) | [Gruppo 18](CHECKPOINT18_REVIEW.md) |
| Sole | [Video](../../artifacts/bw2-validation/pokemon/0351_castform/forms/sunny/front/demo.mp4) | [Pose e trasformazione](../../artifacts/bw2-validation/castform-weather-2026-10-29/castform-sunny-review.png) |
| Pioggia | [Video](../../artifacts/bw2-validation/pokemon/0351_castform/forms/rainy/front/demo.mp4) | [Pose e trasformazione](../../artifacts/bw2-validation/castform-weather-2026-10-29/castform-rainy-review.png) |
| Neve | [Video](../../artifacts/bw2-validation/pokemon/0351_castform/forms/snowy/front/demo.mp4) | [Pose e trasformazione](../../artifacts/bw2-validation/castform-weather-2026-10-29/castform-snowy-review.png) |
| Shiny Sole | [Video](../../artifacts/bw2-validation/pokemon/0351_castform/forms/sunny/shiny-front/demo.mp4) | [Pose](../../artifacts/bw2-validation/castform-weather-2026-10-29/castform-shiny-sunny-review.png) |
| Shiny Pioggia | [Video](../../artifacts/bw2-validation/pokemon/0351_castform/forms/rainy/shiny-front/demo.mp4) | [Pose](../../artifacts/bw2-validation/castform-weather-2026-10-29/castform-shiny-rainy-review.png) |
| Shiny Neve | [Video](../../artifacts/bw2-validation/pokemon/0351_castform/forms/snowy/shiny-front/demo.mp4) | [Pose](../../artifacts/bw2-validation/castform-weather-2026-10-29/castform-shiny-snowy-review.png) |
| Sole → normale | [Cinque turni reali e scadenza del meteo](../../artifacts/bw2-validation/pokemon/0351_castform/forms/return-normal/front/demo.mp4) | [Prima/dopo](../../artifacts/bw2-validation/castform-weather-2026-10-29/castform-return-normal-review.png) |

Gli incontri meteo mostrano due Castform contemporaneamente: battler 0 posteriore, battler 1 frontale. Ogni filmato integrale è conservato nei due percorsi del dossier. Sono registrati ingresso, turno reale con ritorno al menu, cambio forma e almeno due cicli completi stabili per entrambe le viste. La prova di scadenza usa Giornodisole seguito da Splash realmente selezionato dal menu: il recorder legge le mosse scelte, senza scrivere meteo o forme. Il ritorno alla forma normale avviene al quinto turno e conserva altri due cicli.

La variante shiny viene verificata mediante flag dell'attore e confronto dei 32 byte della palette OBJ con la risorsa BW2. Sole e Neve hanno palette normale/shiny identiche nella ROM fornita. Pioggia differisce soltanto nell'indice 0 trasparente: i colori visibili coincidono. La forma normale ha colori shiny diversi. Non si introducono nuove colorazioni.

I report conservano cronologia `gBattleMonForms`, forma caricata, meteo, tick degli attori, tempi di ritorno al menu, SHA di asset, screenshot, video, binario ed ELF. Il gate `bw2_variants.py` ricontrolla indipendentemente tutte le forme, shiny e cicli; rifiuta media alterati, build diverse, forma caricata errata e scadenza senza turni e mosse reali. [Manifest delle varianti](../../artifacts/bw2-validation/pokemon/0351_castform/variants.json).

Il test host `bw2_castform_test.py` esercita le otto clip effettive, le palette, forme indipendenti per attore, cambi ripetuti e liberazione della cache. Sono passati anche bridge con asset reali e sintetici, esportatore, gate dei dossier/varianti e regressione Spinda. La build normale è separata da quella con mailbox di acquisizione; percorsi, ID e SHA sono nel [registro](AUTONOMOUS15_19.json).

Le mosse Giornodisole, Pioggiadanza e Grandine conservano qui le animazioni native Emerald e **non** vengono segnate come importazioni BW2 completate: il contatore mosse resta 6/354. Limiti delle prove: Azahar a 1×; audio/DSP, console reale, stereo, doppi e interazioni speciali restano da validare nelle rispettive fasi del piano.
