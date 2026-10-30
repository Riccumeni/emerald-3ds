# Preparazione checkpoint 49 — mosse

Questa preparazione non completa o importa nuove mosse: il contatore resta **6/354**, con **348** ancora aperte. L’inventario locale è stato riletto e i 354 script della ROM ricontrollati col decoder corrente: **53 accettati**, di cui **47 non completati**; **301 rifiutati**. Il manifest contiene soltanto le 6 mosse già verificate: Pound, Tackle, Leer, Howl, Scratch e Growl. Gli script accettati non certificano supporto completo del renderer, risorse, rami o prove runtime. [Scansione riproducibile](CHECKPOINT49_MOVE_SCAN.json).

Proposta operativa, da rivedere al primo difetto tecnico: prima contatti a colpo singolo con gli opcode già usati; poi movimento e mosse sul proprio attore.

| Ordine | Mossa | Dipendenze SPL | Prima verifica tecnica |
|---|---|---|---|
| 1 | 2 Karate Chop | 166:0, 166:1 | Emissione figlia presente: implementare o verificare adattamento esplicito |
| 2 | 11 Vice Grip | 175:0, 175:1, 175:2 | Parser SPL rifiuta risorsa: ['Only the selected A5I3 particle textures are supported', 'Only the selected A5I3 particle textures are supported', 'Only the selected A5I3 particle textures are supported'] |
| 3 | 15 Cut | 180:0, 180:1, 180:2 | Emissione figlia presente: implementare o verificare adattamento esplicito |
| 4 | 23 Stomp | 189:0, 189:1, 189:2 | Parser SPL rifiuta risorsa: ['Only the selected A5I3 particle textures are supported', 'Only the selected A5I3 particle textures are supported', 'Only the selected A5I3 particle textures are supported'] |
| 5 | 64 Peck | 229:0, 229:1, 229:2 | Emissione figlia presente: implementare o verificare adattamento esplicito |
| 6 | 21 Slam | 187:0, 187:1 | Emissione figlia presente: implementare o verificare adattamento esplicito |
| 7 | 14 Swords Dance | 179:0, 179:1 | Emissione figlia presente: implementare o verificare adattamento esplicito |
| 8 | 105 Recover | 275:0, 275:1 | Emissione figlia presente: implementare o verificare adattamento esplicito |

Interventi iniziali:

1. Esportare una sola mossa dopo averla segnata in corso; ispezionare tutte le dipendenze SPL, inclusi i bit extra e i limiti di durata riportati nella scansione. L’algoritmo corrente proietta in 2D, omette emissioni figlie e quantizza alpha/palette: una riuscita del parser non basta.
2. Confrontare i parametri di movimento con i limiti runtime di PrepareMove (durata/attesa/ripetizioni/ampiezze), la capacità di 10 clip effetto e 4 emettitori simultanei; allineare decoder e runtime senza accettare un fallback come completamento. Il gate attuale del renderer richiede anche entrypoint 60.
3. Per le nuove mosse audio, sostituire l’attuale associazione pilota di PlayMoveSound con una scelta documentata; verificare separatamente audio/DSP quando disponibile.
4. Configurare scenari reali con bersaglio idoneo: contatti senza immunità e HP sufficienti; Swords Dance con statistiche non massimizzate; Recover con HP realmente mancanti. Le mosse multicolpo Double Slap/Comet Punch/Fury Swipes seguono dopo, con numero di colpi e ripetizioni osservabili. Le mosse Mirror Move, Transform e Nature Power contengono solo fine-script 77: richiedono il comportamento dedicato, non sono importazioni completate.
5. Criteri per ogni direzione: situazione prima dell’uso, turno reale con esecutore giocatore e poi avversario, animazione BW2 effettivamente partita (evento e tick), effetto intero, ripristino attori/matrici/palette/visibilità, ritorno al menu del turno successivo, screenshot e video H.264 nativi 1×, metadati/build/ELF/SHA e revisione visiva. Aggiornare il contatore solo dopo publisher e verifica indipendente.

Mega Punch, Pay Day, Fire Punch, Ice Punch e Thunder Punch sono ancora respinti rispettivamente a opcode 57,54,29,54,57: censire semantica e dipendenze dalla sorgente locale prima di ampliare la VM. Le mosse meteo e Trasformazione usate nei dossier Pokémon restano animazioni Emerald e non aumentano il contatore. Console, audio/DSP, stereo, doppi, link reale e integrazione delle interazioni speciali restano aperti.
