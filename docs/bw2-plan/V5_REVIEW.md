# Revisione v5 delle dimensioni

Lombre, Nuzleaf e Seedot sono stati ridotti; Shiftry è stato ingrandito in
entrambe le viste. La revisione riguarda il criterio generale e non contiene
eccezioni per ID di specie. Il centraggio nell’arena e la base frontale
seguono lo stesso algoritmo di posizione già approvato.

| Pokémon | Variazione front | Variazione back | Confronto prima/dopo |
|---|---:|---:|---|
| Lombre | -20.8% | -16.2% | [PNG](../../artifacts/bw2-validation/v5-size-2026-10-28/comparison-lombre.png) |
| Nuzleaf | -20.2% | -20.7% | [PNG](../../artifacts/bw2-validation/v5-size-2026-10-28/comparison-nuzleaf.png) |
| Seedot | -21.2% | -15.0% | [PNG](../../artifacts/bw2-validation/v5-size-2026-10-28/comparison-seedot.png) |
| Shiftry | +19.3% | +12.6% | [PNG](../../artifacts/bw2-validation/v5-size-2026-10-28/comparison-shiftry.png) |

Le variazioni sono rapporti fra le scale Q8 precedenti e nuove, non variazioni
di area. Le pose nei confronti possono differire: tutti i fotogrammi provengono
dal gioco, senza ridimensionare i soggetti nelle immagini. I PNG di confronto
ritagliano lo schermo superiore; gli screenshot integrali sono nei dossier.
[Misure effettive lette dalla build](V5_MEASUREMENTS.json).

![Nuove proporzioni](../../artifacts/bw2-validation/v5-size-2026-10-28/pokemon.png)

[Video delle quattro specie segnalate](../../artifacts/bw2-validation/v5-size-2026-10-28/pokemon.mp4): 148.80 secondi, 4463 frame. Concatenazione di quattro incontri con lati invertiti, senza tagli, ricodifica o accelerazione.

Il problema della v4 era la normalizzazione di ogni sagoma: il solo lato
maggiore cancellava parte delle proporzioni originali. La v5 usa l’altezza
Pokédex e un’impronta ricavata dai rettangoli originali BW2 prima della
conversione a 64×64. La media geometrica delle due viste produce una
correzione comune a front/back, limitata all’80–125%, con fascia neutra del
15% e attenuazione per i giganti. È una calibrazione di presentazione;
non riconosce semanticamente ogni parte anatomica e richiede revisione visiva.

Il back di Shiftry può usare il bordo trasparente oltre il limite conservativo
del 200%: 537/256 = 209,77%. L’intera sagoma opaca resta entro 126×126 nel
contenitore affine 128×128, riservando margine agli arrotondamenti. La chioma
e le foglie non sono tagliate per ingrandire il corpo. [Algoritmo e formato BWL2](../BW2_POKEMON_LAYOUT.md).

Il controllo con il codice C reale ha caricato tutte le 52 clip e i relativi
metadati. Diciotto specie mantengono le scale precedenti, inclusi Treecko,
Poochyena, Grovyle, Sceptile, Natu e Wailord. La nuova curva influisce anche
su Torchic, Silcoon, Cascoon e Lotad: sono stati riaperti e riverificati con
nuovi video e palette shiny, insieme ai quattro segnalati.
[Audit delle 52 viste](V5_PROFILE_AUDIT.json).

Per tutti gli otto Pokémon sono stati revisionati otto incontri nativi,
ingresso e almeno due cicli completi, screenshot e frame iniziali/centrali/
finali. Otto ulteriori scenari verificano le palette shiny su entrambi i lati.
Ogni dossier è stato chiuso individualmente dopo la verifica delle prove.

| Pokémon riverificato | Dossier front/back e shiny |
|---|---|
| Torchic | [Screenshot, video e metadati](../../artifacts/bw2-validation/pokemon/0255_torchic/verifica.md) |
| Silcoon | [Screenshot, video e metadati](../../artifacts/bw2-validation/pokemon/0266_silcoon/verifica.md) |
| Cascoon | [Screenshot, video e metadati](../../artifacts/bw2-validation/pokemon/0268_cascoon/verifica.md) |
| Lotad | [Screenshot, video e metadati](../../artifacts/bw2-validation/pokemon/0270_lotad/verifica.md) |
| Lombre | [Screenshot, video e metadati](../../artifacts/bw2-validation/pokemon/0271_lombre/verifica.md) |
| Seedot | [Screenshot, video e metadati](../../artifacts/bw2-validation/pokemon/0273_seedot/verifica.md) |
| Nuzleaf | [Screenshot, video e metadati](../../artifacts/bw2-validation/pokemon/0274_nuzleaf/verifica.md) |
| Shiftry | [Screenshot, video e metadati](../../artifacts/bw2-validation/pokemon/0275_shiftry/verifica.md) |

I BWA, i fotogrammi, le palette e la ROM sorgente sono invariati. I nuovi
file BWL2 contengono soltanto dimensioni ricavate da `source_bounds` della
ROM. I dossier precedenti sono conservati in
`artifacts/bw2-validation/revisions/2026-10-28-before-v5/`.

Verifiche: 16 test esportatore, bridge C con dati sintetici e reali, sei
mosse nelle due direzioni, sette test d’integrità dossier e audit delle prove.
La build normale ha gli stub `CtrCycle_Frame/Input` da quattro byte e non
contiene la mailbox di prova. Console fisica, stereo e doppi restano nella
fase d’integrazione; audio non acquisito nel setup senza DSP.

Build di prova: `f4d71104098af506`, SHA-256 `d98ad34610150829fc165ba4d59a855188d15205d030478a4679de6351738c46`.

Build normale: `7f2a20de7ba65da2`, SHA-256 `f9dc6ca9e595b0c3708109adf88122257639ba6fb47fcb4ee8fdf0710603b362`.

Totale invariato dopo la riverifica: **26/386 Pokémon e 6/354 mosse**. Nessuna nuova specie o mossa aggiunta in questa revisione.

[Piano](../BW2_ANIMATION_PLAN.md) · [Prove](EVIDENCE.md) · [Checkpoint](CHECKPOINT.md).
