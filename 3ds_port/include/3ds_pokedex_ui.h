#ifndef CTR_POKEDEX_UI_H
#define CTR_POKEDEX_UI_H

#include <stdbool.h>
#include <stdint.h>

#define CTR_DEX_ROWS 5
typedef struct
{
    uint16_t number, species;
    uint8_t seen, caught;
} CtrDexRow;

typedef struct
{
    uint16_t selected, count, seen, caught;
    uint8_t cursorRow;
    CtrDexRow rows[CTR_DEX_ROWS];
} CtrDexList;

bool CtrPokedex_ListShown(void);
void CtrPokedex_ReadList(CtrDexList *view);

#endif
