# Avanzamento: linee iniziali e Percorso 101

Resoconto dei gruppi precedenti: i contatori sotto si riferiscono alla loro chiusura. Per l'avanzamento corrente consultare il [piano](../BW2_ANIMATION_PLAN.md) e il [gruppo Silcoon–Shiftry](HOENN_REVIEW.md).

Completati in questa ripresa **10 Pokémon e 2 mosse**. Totale piano: **16/386 Pokémon e 6/354 mosse**. Il lavoro complessivo resta in corso; prossimo Pokémon: Silcoon (nazionale 266 / Emerald 291).

![Nuovi Pokémon e Graffio](../../artifacts/bw2-validation/progress-2026-10-28/overview.png)

| Gruppo | Anteprima | Filmato completo |
|---|---|---|
| Torchic, Combusken, Blaziken, Mudkip, Marshtomp, Swampert | [PNG](../../artifacts/bw2-validation/batch1-starters-2026-10-28/pokemon.png) | [MP4](../../artifacts/bw2-validation/batch1-starters-2026-10-28/pokemon.mp4) |
| Mightyena, Zigzagoon, Linoone, Wurmple | [PNG](../../artifacts/bw2-validation/batch2-route101-2026-10-28/pokemon.png) | [MP4](../../artifacts/bw2-validation/batch2-route101-2026-10-28/pokemon.mp4) |
| Graffio e Ruggito, da entrambi i lati | [PNG](../../artifacts/bw2-validation/batch1-starters-2026-10-28/mosse.png) | [MP4](../../artifacts/bw2-validation/batch1-starters-2026-10-28/mosse.mp4) |

Le raccolte concatenano i filmati nativi senza ricodifica, tagli o accelerazione. I PNG di confronto ritagliano lo schermo superiore; gli screenshot integrali e i singoli video sono nei dossier. Ogni Pokémon ha ingresso e almeno due cicli front/back, più verifica delle palette shiny. Le mosse sono eseguite in turni reali fino al ritorno al menu azioni; l’altro battler usa Splash per isolare la direzione.

| Nuova unità | Dossier |
|---|---|
| Torchic | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0255_torchic/verifica.md) |
| Combusken | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0256_combusken/verifica.md) |
| Blaziken | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0257_blaziken/verifica.md) |
| Mudkip | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0258_mudkip/verifica.md) |
| Marshtomp | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0259_marshtomp/verifica.md) |
| Swampert | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0260_swampert/verifica.md) |
| Mightyena | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0262_mightyena/verifica.md) |
| Zigzagoon | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0263_zigzagoon/verifica.md) |
| Linoone | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0264_linoone/verifica.md) |
| Wurmple | [Screenshot, video e verifica](../../artifacts/bw2-validation/pokemon/0265_wurmple/verifica.md) |
| Scratch | [Screenshot, video e verifica](../../artifacts/bw2-validation/moves/0010_scratch/verifica.md) |
| Growl | [Screenshot, video e verifica](../../artifacts/bw2-validation/moves/0045_growl/verifica.md) |

Il motore delle mosse usa ora dipendenze dinamiche per coppia risorsa/emettitore: fino a dieci clip per mossa, quattro effetti simultanei. Preparare uno script libera gli effetti della mossa precedente e convalida le nuove dipendenze prima di iniziare. Gli script non presenti o non supportati conservano il comportamento originale. Sei script e quindici clip di effetti sono attualmente importati; il decoder accetta solo un sottoinsieme dei formati BW2. Non significa che le altre mosse siano completate.

L’esportatore dispone di --moves e del catalogo dei 354 ID. L’importazione incrementale conserva le risorse già presenti. Graffio aggiunge tre emettitori da SPL174; Ruggito due da SPL210. Si mantengono gli adattamenti della camera fissa e della proiezione 2D SPL; audio non attestato.

Verifiche: 14 test esportatore (cataloghi e selezione incrementale inclusi), bridge C su dati sintetici e reali con sei mosse in entrambe le direzioni (fine, ripristino di palette/coordinate/matrici e cache limitata), sette test d’integrità dossier. I nuovi video e gli hash delle build vengono controllati dalla procedura di chiusura. Console fisica, stereo e doppi restano nella fase d’integrazione.

Build primo gruppo: prova c5ddbf9e0d011840 / normale 57ab744ae1e5dbde. Secondo gruppo: prova f5eeddca12b8f21a / normale 8684543e6738e401. Tutti i binari/ELF sono conservati negli archivi identificati anche dal digest. La build normale attuale è build/bw2-validation/Emerald3DS-BW2.3dsx e non contiene incontro automatico o mailbox.

[Piano](../BW2_ANIMATION_PLAN.md) · [Tutte le prove](EVIDENCE.md) · [Checkpoint](CHECKPOINT.md).
