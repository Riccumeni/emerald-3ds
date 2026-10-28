# Acquisizione e avanzamento delle animazioni BW2

Il banco prova usa gli stessi renderer, asset e bridge della build normale.
Solo `3ds_cycle_test.c` aggiunge la configurazione della partita di prova,
l'avanzamento deterministico dei menu e una mailbox per chiedere un turno.
Non modifica le regole delle mosse e non salva la partita.

## Preparazione locale

La copia isolata dell'emulatore è `build/bw2-azahar/bw2-test.exe`, con la
propria configurazione e SD in `build/bw2-azahar/user/`. L'istanza normale
dell'utente e il suo salvataggio non vengono modificati. Il server RPC locale
deve essere attivo solo nell'istanza di prova e la finestra deve renderizzare.
Usare scala interna 1, frame limit 100%, speed=1, pause in background disattiva.

Il recorder usa il client fornito dall'emulatore
`D:/Emulators/Azahar/scripting/AzaharRPC.py`, Pillow, NumPy e PyAV. PyAV è
installato localmente, senza modificare l'ambiente del progetto:

```powershell
python -m pip install --target build/bw2-python av
```

Il launcher locale contiene il percorso del Python runtime di questa macchina;
adattarlo se si usa un altro ambiente.

## Build di prova

Nell'albero di staging già preparato, sincronizzare i soli file interessati;
non eseguire bootstrap/reset di un albero contenente modifiche locali.

```sh
touch src/3ds_cycle_test.c
make -j8 TEST_FLAGS=-DCTR_BW2_VALIDATION
```

Copiare insieme il `.3dsx`, l'ELF e `romfs/engine/build_id.bin` in
`build/bw2-validation/` come `validation.3dsx`, `validation.elf`, `build_id.bin`.
Il recorder confronta l'ID caricato con questo ID prima di leggere i simboli.
Una successiva build normale non deve sovrascrivere questi tre file.

La mailbox `gCtrBw2Validation` è composta da 11 interi a 32 bit:
magic, frame, phase, command, player, enemy, move, shiny, seed, turn, side.
Fasi: 0 avvio; 1 ingresso; 2 stabilizzazione; 3 menu azioni pronto; 4 turno.
Il solo comando previsto, 1, avvia un turno dai controlli ordinari del gioco.
Il recorder non scrive HP, risultati, posizioni o stato dei controller.

La configurazione sulla SD isolata è `3ds/emerald3ds/bw2-validation.txt`:
player/enemy sono ID Emerald, move è l'ID mossa, shiny è 0/1, seed è fisso.
side=0 prova la mossa dal giocatore, side=1 dall'avversario, side=2 da entrambi.
Nelle prove direzionali l'altro Pokémon usa Splash per isolare l'effetto.
La partita pilota usa livello 5 e IV 31; non è uno scenario sufficiente per
tutte le future mosse e forme, che richiederanno configurazioni aggiuntive.

## Acquisizioni

Esempi dalla radice del progetto:

```powershell
./3ds_port/scripts/emu/run_bw2_validation.ps1 -Kind idle -Name idle-example
./3ds_port/scripts/emu/run_bw2_validation.ps1 -Kind move -Move 1 -Side 0 -Name move-0001-player
./3ds_port/scripts/emu/run_bw2_validation.ps1 -Kind palette -Shiny 1 -Name shiny-example
```

Il launcher riavvia soltanto il PID di prova di cui verifica l'eseguibile.
Registra in `build/bw2-validation/<nome>/`, conserva log e report e non
sovrascrive un'acquisizione esistente senza `-Overwrite`. Un report già valido
per la stessa build e gli stessi parametri viene riutilizzato.

`bw2_capture.py` usa RGB nativo, acquisisce a circa 30 fps e mantiene i tempi
reali nel MP4/H.264. Decodifica tutto il file e salva fotogrammi di controllo.
Per i Pokémon registra ingresso e almeno due cicli completi di entrambi gli
attori. Per le mosse registra prima, esecuzione e ritorno al menu dopo un turno.
Le prove shiny confrontano le palette dei battler con quelle degli asset.
Dal 28 ottobre i report contengono anche `presentation`, letta dalla build:
altezza Pokédex, scala Q8, offset e ingombro desiderato di entrambi gli attori.
Con la revisione v5 si registrano inoltre `source_factor_q8`, le dimensioni
originali della vista e `source_footprint_q8`, comune a front/back. Questi
valori provengono dalla clip caricata e dai metadati BWL2, non da un calcolo
applicato dal recorder alle immagini. Le prove `v5-*` sostituiscono i dossier
delle otto specie interessate; i precedenti sono conservati nelle revisioni.
I dossier aggiornati di Grovyle e Sceptile usano `large-back-*`; quelli di
Treecko e Poochyena conservano le prove `arena-center-*`. I metadati indicano
la build di ciascuna prova. La parte inferiore dei back può essere coperta
dal testo; l'algoritmo è descritto in `BW2_POKEMON_LAYOUT.md`.

Gli screenshot dell'effetto possono essere scelti fra i fotogrammi reali
registrati; `bw2_poster.py` estrae un frame senza ritocchi e ne registra
timestamp e hash. Non genera o ricostruisce un effetto assente dal filmato.

La revisione del gruppo Silcoon–Shiftry ha rilevato una riga di pixel della
testa ripetuta nel cielo sopra Lombre e Ludicolo. Le immagini BWA sorgenti
sono pulite: il riempimento del cielo ripete le prime righe della superficie
della scena e lasciava una riga alla giunzione con il passaggio separato
`BattleSkyCompose`. Quel passaggio ora sovrappone una riga logica alla scena,
coprendo la giunzione arrotondata. Scala, appoggio e asset non cambiano.
Le acquisizioni `hoenn3-*` precedenti alla correzione restano diagnostiche;
per il gruppo si usano `hoenn3-final-*` e le palette `hoenn3-shiny-*`.

## Chiusura di un dossier

Controllare visivamente screenshot, frame significativi e fine del video.
Assemblare le due direzioni con `bw2_publish_evidence.py --reviewed`, usando
le quattro opzioni delle sorgenti shiny aggiuntive nel caso dei Pokémon.
Poi eseguire `bw2_progress.py --action complete --kind pokemon|mosse --id N`.
Il numero è nazionale per i Pokémon e ID Emerald per le mosse.

La marcatura controlla presenza, hash, build, direzione e risultato della
cattura; per le mosse anche esecutore e conclusione del turno. Aggiorna
registro, checklist, contatori del piano e checkpoint. Le forme richieste
devono essere dichiarate e verificate prima di chiudere la specie.

Produrre anche una build normale senza TEST_FLAGS, ricompilando
`3ds_cycle_test.c`: `CtrCycle_Frame` e `CtrCycle_Input` devono tornare agli
stub da 4 byte. I dossier distinguono build di prova e build normale.
L'audio non è attestato da questi video: il setup di prova non ha firmware DSP.
