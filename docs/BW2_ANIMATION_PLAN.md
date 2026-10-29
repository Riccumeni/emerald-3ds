# Piano: animazioni BW2 per tutte le battaglie di Emerald 3DS

Data iniziale: 27 ottobre 2026. Stato: esecuzione in corso; avanzamento nelle checklist collegate.

## Obiettivo e perimetro

Portare in Emerald 3DS le animazioni di battaglia di tutte le **386 specie**
del Pokédex nazionale di Smeraldo e di tutte le **354 mosse** del gioco,
partendo dal prototipo BW2 di Treecko e Poochyena. Il limite iniziale del
livello 5 non si applica più all'obiettivo di questo piano.

Il censimento deriva dalle costanti dell'albero locale
`build/upstream/include/constants/{species,pokedex,moves}.h`. Si includono
anche i Pokémon non catturabili normalmente in una singola partita.
`SPECIES_NONE`, i vecchi segnaposto Unown, l'Uovo e `MOVE_NONE` non sono
unità di battaglia da importare. Struggle è incluso fra le 354 mosse.

Le forme e le personalizzazioni usate dal motore hanno verifiche aggiuntive:
Unown, Castform, Deoxys e macchie di Spinda. Le palette shiny fanno parte
della verifica di ogni specie. L'inventario delle forme deve essere chiuso
prima di dichiarare completate le specie interessate. Non si aggiungono
nuove forme, specie, mosse, statistiche o regole di BW2 al gameplay di Smeraldo.

La sorgente è `D:/Projects/pokebw2/black2.nds`, letta senza modificarla.
La presentazione segue l'adattamento del prototipo: camera di Emerald,
sprite animati BW2, effetti delle mosse adattati al renderer disponibile.
Ogni differenza visibile rispetto alla sorgente va descritta nella scheda
della singola mossa; uno script non supportato o il ritorno silenzioso
all'animazione originale non valgono come lavoro completato.

## Registro e avanzamento

- [Checkpoint autonomi 15–19](bw2-plan/AUTONOMOUS15_19_REVIEW.md): cinque gruppi consecutivi con prove e commit individuali.

- [Checkpoint autonomi 10–14](bw2-plan/AUTONOMOUS10_14_REVIEW.md): cinque gruppi consecutivi con prove e commit individuali.

- [Cinque checkpoint autonomi](bw2-plan/AUTONOMOUS5_REVIEW.md): cinque gruppi consecutivi con prove e commit individuali.

- [Checklist Pokémon](bw2-plan/POKEMON.md): una riga per ogni specie.
- [Checklist mosse](bw2-plan/MOVES.md): una riga per ogni mossa.
- [Forme e casi speciali](bw2-plan/VARIANTS.md).
- [Registro strutturato](bw2-plan/stato.json): ID, stati, percorsi e prove.
- [Punto di ripresa](bw2-plan/CHECKPOINT.md): ultimo lavoro e prossima unità.
- [Indice delle prove verificate](bw2-plan/EVIDENCE.md): collegamenti a PNG e MP4.
- [Gruppo Taillow–Surskit](bw2-plan/BATCH4_REVIEW.md): Taillow, Swellow, Wingull, Pelipper, Ralts, Kirlia, Gardevoir e Surskit, con prove front/back e shiny.
- [Gruppo Silcoon–Shiftry](bw2-plan/HOENN_REVIEW.md): Silcoon, Beautifly, Cascoon, Dustox e linee Lotad/Seedot.
- [Revisione delle dimensioni v5](bw2-plan/V5_REVIEW.md): Lombre, Nuzleaf e Seedot ridotti, Shiftry ingrandito; otto specie riverificate e diciotto scale invariate.
- [Gruppi precedenti](bw2-plan/BATCHES_REVIEW.md): linee Torchic/Mudkip, primi incontri e nuove mosse.
- [Scala e appoggio automatici](BW2_POKEMON_LAYOUT.md): altezza Pokédex, ingombro, limiti e prospettiva.

`stato.json` è la fonte degli stati; checklist e contatori devono essere
aggiornati nella stessa operazione di chiusura di un'unità. Le caselle
**Fatto** nelle checklist corrispondono al completamento dell'intero criterio
di accettazione, comprese le prove video. Non basta che l'esportazione riesca.

Stati ammessi: `da_fare`, `in_corso`, `implementato_prototipo`,
`da_verificare`, `bloccato`, `fatto`. Per ogni blocco si annotano causa e
passo necessario per risolverlo; non viene trasformato in un completamento.

Avanzamento corrente (aggiornato insieme alle checklist):

| Ambito | Totale | Prototipo implementato | Fatto con tutte le prove |
|---|---:|---:|---:|
| Pokémon | 386 | 2: Treecko, Poochyena | 130 |
| Mosse | 354 | 4: Pound, Tackle, Leer, Howl | 6 |

Dal 28 ottobre 2026 le correzioni fisse di Treecko e Poochyena sono sostituite
dall'[algoritmo di scala e appoggio](BW2_POKEMON_LAYOUT.md), basato su altezza
Pokédex, ingombro dell'animazione e spazio disponibile sullo schermo. Treecko,
Poochyena, Grovyle e Sceptile hanno nuovi dossier completi front/back.
Sono stati aggiunti anche [Natu e Wailord come casi estremi di statura](bw2-plan/EXTREMES_REVIEW.md), con prove front/back e shiny.
Per il back si centra la sagoma nell'arena: il testo può coprire la parte
inferiore del corpo e non determina l'altezza del Pokémon.
Le vecchie prove del prototipo sono utili per la diagnosi; i nuovi dossier
completi sono indicati singolarmente nelle checklist e nei relativi metadati.
`build/bw2-prototype/battle-preview.png` è una vecchia anteprima precedente
alle correzioni e non va usata come prova finale.

## Cartelle e prove richieste

Radice locale, esterna alle cartelle cancellabili della compilazione:
`D:/Projects/emerald-3ds/artifacts/bw2-validation/`.
Sono predisposte 386 cartelle Pokémon e 354 cartelle mosse con le rispettive
sottocartelle. Le cartelle vuote indicano soltanto che la struttura esiste.
Le prove effettivamente acquisite e verificate sono indicate nel registro.

Esempio Pokémon, denominato tramite numero nazionale e nome:

```text
pokemon/0252_treecko/
  front/screenshot.png
  front/demo.mp4
  back/screenshot.png
  back/demo.mp4
  metadata.json
  verifica.md
  forms/<forma>/front/...
  forms/<forma>/back/...
```

Esempio mossa, denominata tramite ID di Smeraldo e nome:

```text
moves/0033_tackle/
  player/screenshot.png
  player/demo.mp4
  opponent/screenshot.png
  opponent/demo.mp4
  metadata.json
  verifica.md
  cases/<variante-rilevante>/...
```

Per ogni specie servono almeno **uno screenshot e un video frontale**, più
**uno screenshot e un video posteriore**. Per ogni mossa servono almeno
**uno screenshot e un video con esecutore del giocatore**, più
**uno screenshot e un video con esecutore avversario**. Per le sole unità
base sono almeno 1.480 screenshot e 1.480 video; le varianti si aggiungono.

Le prove provengono dal gioco realmente in esecuzione e dalla stessa build
indicata nei metadati. Una GIF dell'esportatore, un montaggio di pose o
un cambiamento del contatore in memoria sono controlli ausiliari: non
sostituiscono il video dimostrativo del funzionamento sullo schermo.

Requisiti delle acquisizioni:

1. Screenshot PNG del gioco, con Pokémon o effetto riconoscibile, HUD e arena
   visibili. Per le mosse scegliere una fase significativa dell'effetto.
2. Video MP4 riproducibile, preferibilmente H.264/yuv420p, almeno 30 fps di
   acquisizione ove disponibili; riportare fps effettivi e prestazioni del gioco.
   Registrare a velocità di gioco 1x, senza accelerare i tempi per mascherare
   attese o rallentamenti. Verificare apertura, durata e fotogrammi del file.
3. Per i Pokémon: ingresso completo e almeno due cicli dell'animazione a riposo,
   senza tagliare testa, piedi o coda. Per le mosse: situazione prima dell'uso,
   esecuzione completa, conclusione e ritorno al turno successivo. Le mosse
   a più turni richiedono anche i turni pertinenti.
4. `metadata.json` registra ID/nome, direzione, forma, shiny/personality quando
   rilevanti, scenario e seed riproducibile, build ID e SHA-256 del binario,
   impronta degli asset/sorgente, emulatore/dispositivo, impostazioni di
   velocità e rendering, data, risoluzione, durata/fps e impronte dei media.
5. `verifica.md` descrive controlli svolti, differenze BW2/Emerald accettate,
   problemi residui e risultato. Una revisione della posa statica non prova
   l'animazione: guardare anche inizio, centro e fine del video.

Le prove restano locali, con un indice consultabile. Una modifica successiva
che cambia il risultato visivo invalida le prove interessate: lo stato torna
`da_verificare` e i nuovi media sostituiscono quelli della build precedente.
Misurare lo spazio occupato dal primo dossier completo prima di stimare lo
spazio necessario per l'intero progetto. Non pubblicare automaticamente ROM,
asset estratti, salvataggi o registrazioni.

## Fase 0 — Inventario e sistema di verifica

- [x] Censire 386 specie e 354 mosse dalle costanti locali.
- [x] Preparare checklist, registro e cartelle delle prove.
- [ ] Mappare ID Emerald -> numero nazionale -> risorsa BW2, compresi forme,
  eccezioni, palette e personalizzazioni. Non assumere che gli ID coincidano.
- [ ] Inventariare sequenze, modalità di playback, quad, script, opcode,
  effetti SPL e dipendenze di tutte le risorse; registrare le risorse mancanti.
  Prima scansione in `bw2-plan/INVENTORY.json`: 772 viste base leggibili e
  53/354 script accettati dal decoder limitato; dipendenze e forme ancora da chiudere.
- [x] Predisporre il banco di prova deterministico per specie sui due lati e
  mossa forzata da ciascun lato (`CTR_BW2_VALIDATION`, solo build di prova).
- [ ] Estendere gli scenari a tutte le forme e ai rami particolari delle mosse:
  mossa forzata da ciascun lato, bersagli idonei, HP e stati controllati.
  Usare SD/salvataggi isolati e flag demo esclusi dalle build consegnate.
- [x] Acquisire screenshot e MP4 dai fotogrammi reali del renderer tramite RPC
  locale, con timestamp e controllo di decodifica. La finestra isolata deve
  renderizzare: minimizzarla può sospendere l'acquisizione.
- [x] Associare automaticamente media, build e scenario e produrre un indice
  delle prove. Segnalare cartelle incomplete o video vuoti/non riproducibili.
- [x] Registrare dimensioni, tempi video/fps e diagnostica memoria del pilota
  in `bw2-plan/PILOT_MEASUREMENTS.json` (misure emulatore, console ancora da provare).
- [x] Completare per primi i dossier Treecko, Poochyena, Pound, Tackle, Leer,
  Howl. Solo allora marcarli `fatto` e procedere a nuove unità.

## Fase 1 — Generalizzare l'importazione dei Pokémon

- [x] Sostituire gli elenchi fissi di due specie con un catalogo di risorse
  per le 386 specie base e importazione incrementale.
- [ ] Gestire tutte le sequenze/modalità realmente presenti, durata e loop;
  verificare le limitazioni attuali di 512 frame unici e 1.024 tick per clip.
  Non troncare animazioni per farle rientrare nel formato.
- [ ] Verificare scala e ancoraggio per tutte le specie e forme. L'algoritmo
  basato su altezza e sagoma è introdotto e verificato sui primi quattro
  Pokémon, con limiti di spazio e prospettiva diversi per front/back.
  Controllare piedi/arena, clipping, occhi, arti e sovrapposizioni per ogni unità.
- [ ] Adeguare cache e caricamenti al lavoro su larga scala: il prototipo ha
  14 slot totali, selezione statica degli effetti e quattro effetti simultanei.
  Definire limiti misurati e caricare le sole risorse necessarie alla battaglia.
  La cache degli attori è ora limitata ai quattro battler, con condivisione e
  riuso degli slot non più attivi. Gli effetti ora usano chiavi dinamiche per
  risorsa/emettitore e dieci slot per mossa; formati e capacità restano da
  verificare sulle dipendenze delle altre mosse.
- [ ] Garantire palette/shiny, trasparenze, matrici, cambio sprite, copie su BG,
  ingresso/uscita, KO, trasformazione, sostituto e cambi di forma.
- [ ] Controllare percorsi frontali e posteriori distinti: il precedente errore
  di confronto con la sola tabella posteriore non deve ricomparire.

La fase tecnica si chiude con il pilota completo; non si dichiara già
compatibile l'intero catalogo solo perché il catalogo viene caricato.

## Fase 2 — Completare i Pokémon uno alla volta

Ordine: chiudere i due piloti, poi restanti specie del Pokédex di Hoenn
nell'ordine del gioco; infine le altre specie in ordine nazionale. Il registro
contiene l'ordine operativo. I casi speciali si affrontano insieme alla specie
interessata, senza rimandarli dopo la sua marcatura `fatto`.

Per ogni Pokémon:

1. Leggere checkpoint e voce nel registro; verificare di avere contesto e
   budget sufficienti per l'unità. Segnare `in_corso` prima di iniziare.
2. Importare front/back e forme applicabili, conservando palette e ciclo BW2.
3. Correggere profilo di posa, scala e ancoraggio sulla rispettiva arena.
4. Provare entrambi i lati nel gioco, almeno due loop, shiny e interazioni
   rilevanti; controllare che gameplay e salvataggio rimangano coerenti.
5. Acquisire e verificare screenshot/video front e back e le prove aggiuntive
   delle forme; compilare metadati e differenze note.
6. Eseguire i controlli pertinenti e una build pulita dagli automatismi demo.
   Segnare **fatto** soltanto quando codice, esecuzione e dossier sono completi.
7. Aggiornare subito registro, casella della specie, contatori e checkpoint.
   Comunicare Pokémon completato, percorso delle prove e prossimo elemento.

## Fase 3 — Generalizzare il motore delle mosse

- [ ] Analizzare i 354 script e raggrupparli per dipendenze reali; il prototipo
  interpreta soltanto gli opcode delle quattro mosse iniziali.
- [ ] Implementare progressivamente controllo del flusso, parametri, attese,
  sincronizzazione, posizionamento, trasformazioni, maschere, palette e sfondi
  richiesti dagli script incontrati. Mantenere validazione e protezione dai blocchi.
- [ ] Ampliare gli effetti SPL per le caratteristiche necessarie, inclusi
  emissioni figlie, orientamento e trasparenze dove visibili; registrare gli
  adattamenti alla camera di Emerald. Non limitarsi a riutilizzare gli attuali
  dieci emettitori per mosse con effetti differenti.
- [ ] Gestire direzione, bersaglio, effetti su entrambi i lati, mosse sul proprio
  Pokémon e mosse globali. Provare con specie di dimensioni diverse.
- [ ] Gestire animazioni con più colpi/turni, carica/scarica, meteo, recupero,
  trasformazioni e dipendenze dallo stato realmente presenti nelle mosse.
- [ ] Decidere per ogni dipendenza sonora l'adattamento coerente al prototipo;
  dichiarare separatamente la verifica audio quando il setup emulato la consente.
- [ ] Eliminare il vincolo del prototipo che abilita le mosse importate solo
  quando l'attaccante è una delle due specie supportate.

## Fase 4 — Completare le mosse una alla volta

Chiudere prima le quattro mosse pilota. Poi, dall'inventario degli script,
ordinare le restanti per dipendenze condivise: contatto, proiettili/particelle,
stato e palette, sfondi/maschere, effetti globali e casi speciali. Una famiglia
condivisa riduce lavoro duplicato, ma ogni mossa mantiene la propria voce
e le proprie prove. Gli ID crescenti sono soltanto l'ordine iniziale provvisorio.

Per ogni mossa:

1. Segnare `in_corso`, elencare risorse/opcode e scenario significativo.
2. Implementare l'effetto completo e gli adattamenti necessari mantenendo
   calcolo danni, bersagli, PP, probabilità e turni di Emerald.
3. Eseguire dal giocatore e dall'avversario; entrambe le esecuzioni devono
   terminare e ripristinare attori, palette, visibilità e controlli.
4. Provare i rami visivi pertinenti: più colpi, più turni, meteo, esito e
   bersagli multipli quando previsti. I casi senza effetto visivo vanno
   documentati con il comportamento reale, senza inventare un'animazione.
5. Registrare screenshot/video nelle cartelle `player/` e `opponent/`, più
   gli eventuali `cases/`; verificare i file e aggiornare metadati e relazione.
6. Eseguire controlli e build pertinenti; marcare **fatto** e aggiornare
   immediatamente registro, checklist, contatori e checkpoint.

## Fase 5 — Integrazione e consegna

- [ ] Verificare catalogo completo: nessuna specie/mossa dimenticata,
  nessuna risorsa non supportata nascosta da fallback durante la validazione.
- [ ] Verificare forme e personalizzazioni e tutte le cartelle delle prove.
- [ ] Eseguire regressioni su battaglie singole/doppie, mosse richiamate,
  trasformazione/sostituto, KO, cambi Pokémon e combattimenti ripetuti.
- [ ] Verificare composizione normale, voxel e stereo, HUD e menu di battaglia.
- [ ] Misurare memoria, I/O e fluidità su emulatore e su console quando
  disponibile. La sola prova in Azahar non dimostra le prestazioni hardware.
- [ ] Risolvere eventuali regressioni introdotte. I problemi preesistenti della
  suite generale vanno distinti e riportati; non dichiararla passata se bloccata.
- [ ] Produrre build senza flag demo, indice navigabile dei dossier e rapporto
  finale con contatori, build ID, limiti e risultati verificati.

## Contesto, budget e ripresa del lavoro

L'unità di avanzamento è un Pokémon o una mossa; evitare di avviare più unità
senza chiuderne lo stato. Prima di iniziarne una nuova controllare lo spazio
di contesto e il budget disponibili. Non avviare un'unità se il margine è
insufficiente per implementazione, verifica e registrazione dei risultati.

Quando si avvicina il limite, aggiornare prima `CHECKPOINT.md` e `stato.json`
con: ultima unità completata, unità aperta, file modificati, build corrente,
comandi e risultati verificati, media mancanti, problemi e prossimo passo.
Conservare anche ID delle sessioni/processi ancora attivi per non duplicarli.
Chiudere questo punto di salvataggio prima del successivo Pokémon/mossa.

La compattazione del contesto è gestita dalla piattaforma; non si presume di
poterla forzare con uno strumento non disponibile. Alla compattazione o alla
nuova sessione riprendere dal checkpoint senza ricominciare e senza riutilizzare
prove di una build diversa. Compattare non rinnova i limiti di token/uso della
sessione: se il budget non basta, fermarsi al checkpoint e indicare come
riprendere, senza segnare come fatto il lavoro incompleto.

Non annullare modifiche locali estranee e non ricreare/reset dell'albero
`build/upstream` per sincronizzare pochi file. Il registro distingue le
animazioni implementate dai dossier chiusi e dall'integrazione ancora da fare.
