# Scala e posizione dei Pokémon BW2

Revisione v5 del 28 ottobre 2026, dopo il riscontro su Lombre, Nuzleaf,
Seedot e Shiftry. Il criterio è comune alle specie, senza correzioni per ID.
Le altezze sono già nel Pokédex locale di Emerald: non servono dati dal web.

## Dimensione

La v4 normalizzava il lato più lungo di ogni clip usando solo l’altezza
Pokédex. Questo cancellava parte della proporzione disegnata dagli autori
BW2: uno sprite piccolo poteva diventare troppo grande; chiome o foglie
larghe potevano ridurre troppo il corpo di uno sprite più grande.

La v5 conserva la curva di altezza come base e aggiunge un riferimento
ricavato dai rettangoli originali BW2 **prima** dell’adattamento al canvas
64×64. Usa un fattore comune a front e back, per evitare che un’angolazione
diversa cambi la proporzione relativa della specie.

1. Base frontale, con `h` in decimetri: `min(88, 36 + floor(76*h/(h+10)))`.
2. Base posteriore: prospettiva `130 + min(20, max(0, (h-5)*5))` percento,
   limitata a 112 pixel logici prima della correzione.
3. Impronta nativa: `P = (Wfront*Hfront*Wback*Hback)^(1/4)`, in pixel BW2.
   È la media geometrica degli ingombri delle due viste. Usare entrambe le
   dimensioni riduce il peso di una singola appendice lunga rispetto al solo
   lato maggiore. Non è una segmentazione anatomica del corpo.
4. Riferimento calibrato: `R = min(70, 40 + 3*h)`. Si calcola `q = P/R`.
   Nell’intervallo circa 0,85–1,15 si conserva la scala già stabilita (`q=1`);
   all’esterno si limita la correzione a circa 0,80–1,25. È un criterio di
   presentazione, calibrato sulle specie verificate, non una legge fisica.
5. Sopra 2 m la correzione si attenua linearmente; da 4 m in poi si usa solo
   la curva di altezza. L’arte DS comprime già i Pokémon enormi per la sua
   inquadratura: quell’ingombro nativo non deve annullare il limite dei giganti.
6. Si moltiplica la base per `q`, con limiti finali di 104 pixel frontali e
   126 posteriori. La scala uniforme deriva ancora dall’intera sagoma della
   clip esportata, conservando le proporzioni. Il risultato resta fisso per
   tutto il ciclo.

I calcoli usano Q8 e divisioni intere: la fascia neutra è 218–294 e il fattore
limitato a 205–320 su 256. L’impronta comune è salvata in Q8 dopo il calcolo
sui rettangoli. I limiti sono sul lato maggiore, non su entrambi gli assi.

La scala affine resta normalmente entro 50–200%. Per un ingrandimento
richiesto dall’impronta nativa si può sfruttare il bordo trasparente del
canvas, fino al 213,3% teorico: si limita però la scala affinché tutti i pixel
opachi restino entro 126×126, centrati nel contenitore affine 128×128. Due
pixel sono riservati agli arrotondamenti della matrice reciproca. Non si
tagliano foglie, ali o code per ingrandire il corpo.

Il nuovo riferimento mantiene le scale di Treecko, Poochyena, Grovyle,
Sceptile e dei casi estremi Natu/Wailord. Fra le 26 specie già importate,
otto cambiano scala: i quattro segnalati e Torchic, Silcoon, Cascoon, Lotad.
Per tutti gli otto si rigenerano prove e dossier. Le prove precedenti restano
in `artifacts/bw2-validation/revisions/2026-10-28-before-v5/`.

## Margine superiore della vista frontale (v5.1)

La verifica di Hariyama ha rilevato che una mano alzata raggiungeva la riga
superiore in alcune pose. Dal terzo checkpoint autonomo la scala frontale
ha un ulteriore limite ricavato dal viewport: il pixel più alto dell’intera
sequenza deve restare quattro pixel logici all’interno dello schermo.
La base nell’arena e l’elevazione restano identiche; la scala rimane fissa
per il ciclo, senza spostare o tagliare la mano.

La scena colloca la riga GBA 112 sulla riga schermo 192, con zoom 1,4.
Il limite di salita rispetto alla base è quindi
`ground + (240-48)/1.4 - 116`. Si usa la distanza fra la base idle pesata
e la riga più alta della clip. Questo controllo tiene conto anche dei
Pokémon sospesi. Nessuna delle 50 specie già chiuse nei primi due checkpoint
richiede una riduzione aggiuntiva. Il criterio di proporzione v5 e le viste
posteriori non cambiano. Il confronto video e le misure sono salvati in
`docs/bw2-plan/FRONT_HEADROOM_REVIEW.json`.

## Dati opzionali e compatibilità

L’esportatore scrive, per ogni clip, un file `SPECIES_front.bin.layout` o
`SPECIES_back.bin.layout`: 12 byte, firma `BWL2` e quattro interi little-endian
u16 (larghezza/altezza della vista corrente e della vista opposta). Sono
calcolati da `source_bounds` della ROM, non da una tabella manuale per specie.
L’esportazione incrementale aggiorna anche i metadati dei Pokémon già presenti.
I file BWA, i fotogrammi e le palette non vengono modificati da questa revisione.

I metadati sono caricati una volta insieme alla clip e hanno gli stessi limiti
di cache degli attori. Dati assenti o non validi mantengono la curva v4; non
impediscono il caricamento dello sprite. Effetti delle mosse esclusi da questa
correzione. Il recorder riporta dimensioni sorgenti, impronta e fattore Q8
letti dalla build in esecuzione.

## Posizione

Per le viste frontali, la base stabile è la mediana delle righe inferiori dei fotogrammi del ciclo
idle, pesata con la durata effettiva nella timeline. Un singolo fotogramma
con la coda più in basso non sposta l'intera animazione. L'appoggio è
`BATTLER_COORD_Y + 32`, usando la posizione della relativa arena e sottraendo
l'elevazione prevista da Smeraldo per gli avversari sospesi.

L'offset verticale compensa sia la scala sia l'offset dello sprite originale
GBA: quest'ultimo non deve determinare dove poggia il nuovo disegno BW2.
Il centro nativo usato è `GetBattlerSpriteDefault_Y`, lo stesso con cui il
controller crea lo sprite. Il punto usato per mirare le mosse è diverso
di 8 pixel sul lato del giocatore e non è adatto a questo calcolo.
Il rettangolo complessivo viene anche centrato orizzontalmente. La posizione
resta fissa attraverso il ciclo, preservando le oscillazioni della sorgente.
Per la vista di spalle si allinea invece il **centro della massa dei pixel
opachi** al centro visibile dell'arena (`BATTLER_COORD_Y + 24`, otto pixel
logici sopra il suo riferimento inferiore). Il centro viene calcolato sui
fotogrammi idle, pesando ogni pixel e la durata della posa nella timeline.
Una lunga foglia o un solo fotogramma estremo incidono meno che sul centro
del rettangolo esterno. Il risultato è fisso per tutto il ciclo.

La parte inferiore può finire dietro il riquadro di testo: il riquadro non
influenza il posizionamento. L'offset usa
`arenaY - centroNativo - (centroMassa - 32) * scala`, con precisione Q8.
Le oscillazioni originali restano visibili e non provocano ricentramenti
tra un fotogramma e il successivo.
La base visiva è una stima dalla sagoma: ali, code e Pokémon sospesi richiedono
comunque revisione visiva, senza dichiararli completati automaticamente.

Le trasformazioni si applicano all'OAM dopo la costruzione ordinaria,
componendole con la matrice affine di ingressi e mosse. Le coordinate logiche
del gioco restano intatte. Le particelle BW2 usano il centro visivo corretto.
La clip e le palette sono le stesse per le viste normali e shiny.

## Verifica

I test del bridge controllano curva crescente, limiti dei giganti, fattori
per impronte native piccole/grandi, simmetria scambiando le dimensioni,
compatibilità senza metadati e contenimento dei pixel opachi oltre il 200%.
Restano i test di base frontale pesata, centro di massa posteriore, copertura
inferiore consentita, composizione affine, riflessioni e cache limitata.
I test con gli asset reali eseguono le sei mosse importate dai due lati.
L’esportatore verifica inoltre il formato BWL2, i limiti e la migrazione
incrementale senza cambiare i pixel.

La revisione visiva richiede video nativi di ingresso e almeno due cicli
completi per ogni vista, screenshot e verifica delle palette shiny. Il piano
non segna come fatti i dossier riaperti finché queste prove non sono concluse.

[Indice degli screenshot e video](bw2-plan/EVIDENCE.md).
