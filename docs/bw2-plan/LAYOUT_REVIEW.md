# Grovyle e Sceptile: back ingranditi — 28 ottobre 2026

Grovyle di spalle è circa il 35% più grande e Sceptile circa il 40%, rispetto alla precedente build. Il centro della massa del corpo resta sulla stessa arena; il testo può coprire la parte inferiore.

![Prima e dopo](../../artifacts/bw2-validation/large-back-2026-10-28/confronto.png)

[Nuovo filmato completo](../../artifacts/bw2-validation/large-back-2026-10-28/dimostrazione-completa.mp4): Grovyle back/Sceptile front, poi Sceptile back/Grovyle front. Concatenazione senza ricodifica o accelerazione, 73,79 secondi e 2.213 fotogrammi interamente decodificati.

| Pokémon | Frontale | Di spalle |
|---|---|---|
| Treecko | [PNG](../../artifacts/bw2-validation/pokemon/0252_treecko/front/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0252_treecko/front/demo.mp4) | [PNG](../../artifacts/bw2-validation/pokemon/0252_treecko/back/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0252_treecko/back/demo.mp4) |
| Poochyena | [PNG](../../artifacts/bw2-validation/pokemon/0261_poochyena/front/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0261_poochyena/front/demo.mp4) | [PNG](../../artifacts/bw2-validation/pokemon/0261_poochyena/back/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0261_poochyena/back/demo.mp4) |
| Grovyle | [PNG](../../artifacts/bw2-validation/pokemon/0253_grovyle/front/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0253_grovyle/front/demo.mp4) | [PNG](../../artifacts/bw2-validation/pokemon/0253_grovyle/back/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0253_grovyle/back/demo.mp4) |
| Sceptile | [PNG](../../artifacts/bw2-validation/pokemon/0254_sceptile/front/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0254_sceptile/front/demo.mp4) | [PNG](../../artifacts/bw2-validation/pokemon/0254_sceptile/back/screenshot.png) · [MP4](../../artifacts/bw2-validation/pokemon/0254_sceptile/back/demo.mp4) |

Grovyle: scala Q8 341 → 460, cioè 133,2% → 179,7%. Sceptile: 341 → 477, cioè 133,2% → 186,3%. I valori sono riferiti al canvas normalizzato; gli incrementi relativi sono 34,9% e 39,9%. Il precedente limite posteriore di 80 pixel è rimosso; la prospettiva varia dal 130 al 150% in base all’altezza Pokédex, con ingombro massimo 112 pixel logici e scala massima 200%. [Algoritmo](../BW2_POKEMON_LAYOUT.md).

Le nuove acquisizioni sono large-back-*, build di prova bda058839521ce0d. Treecko e Poochyena conservano le prove arena-center-* e il medesimo comportamento. Ogni specie ha prove front/back e shiny coerenti con la build indicata nei propri metadati.

Build normale 3387017fec479c42, SHA-256 6d30893415c592ae926a35ff96936383f51c37524895874642ddb82189e80db4, senza incontro automatico o mailbox.

Test dedicati: 12 test esportatore, bridge C con dati sintetici e reali incluse le quattro mosse pilota sui due lati, 7 test integrità prove. Nuovi video con ingresso e almeno due cicli completi per vista, palette shiny verificate. Acquisizione Azahar isolato a velocità 1× e circa 30 fps; audio, console fisica e stereo non attestati. Vecchi dossier di Grovyle/Sceptile conservati in revisions/2026-10-28-before-large-back.
