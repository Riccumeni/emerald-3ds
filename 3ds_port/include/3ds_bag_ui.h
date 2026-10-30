#ifndef CTR_BAG_UI_H
#define CTR_BAG_UI_H

#include <stdbool.h>
#include <stdint.h>

enum { CTR_BAG_LIST, CTR_BAG_SWAP, CTR_BAG_CONTEXT, CTR_BAG_QUANTITY,
       CTR_BAG_YESNO, CTR_BAG_MESSAGE, CTR_BAG_BUSY };
enum { CTR_BAG_POCKET, CTR_BAG_SELECT, CTR_BAG_PAGE, CTR_BAG_ACTION,
       CTR_BAG_ADJUST, CTR_BAG_CONFIRM, CTR_BAG_BACK };
#define CTR_BAG_ROWS 6

typedef struct
{
    uint8_t ready, pocket, locked, mode, count, selected, first, cursor;
    uint8_t actionCount, actionValid[6], actions[6][32];
    uint16_t items[CTR_BAG_ROWS], quantities[CTR_BAG_ROWS], registered;
    uint16_t quantity, maximum;
    uint8_t names[CTR_BAG_ROWS][32], message[384];
} CtrBagView;

typedef struct
{
    uint32_t serial;
    uint8_t ready, pocket, description[384];
    int16_t x, y, pa, pb, pc, pd;
    uint8_t tiles[2048];
    uint16_t palette[16];
} CtrBagTop;

bool CtrBag_DualShown(void);
void CtrBag_ReadView(CtrBagView *view);
void CtrBag_ReadTop(CtrBagTop *top);
void CtrBag_Command(unsigned command, int value);
const uint16_t *CtrBag_TopCanvas(uint32_t *version);

#endif
