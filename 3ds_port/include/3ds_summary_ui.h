#ifndef CTR_SUMMARY_UI_H
#define CTR_SUMMARY_UI_H

#include <stdbool.h>
#include <stdint.h>

enum { CTR_SUMMARY_STATS, CTR_SUMMARY_MOVES, CTR_SUMMARY_CONTEST };
enum {
    CTR_SUMMARY_TAB, CTR_SUMMARY_SELECT_MOVE, CTR_SUMMARY_SWAP,
    CTR_SUMMARY_PREVIOUS, CTR_SUMMARY_NEXT, CTR_SUMMARY_CLOSE, CTR_SUMMARY_STATS_MODE
};

typedef struct
{
    uint8_t ready, tab, cursor, swapFrom, egg, locked, statsMode, ivsEnabled, level, ribbons;
    uint8_t nickname[12];
    uint16_t species, item, hp, stats[6], moves[4];
    uint8_t pp[4], maxPP[4], ivs[6], evs[6];
    uint32_t exp, expStart, expEnd, nextExp;
} CtrSummaryView;

typedef struct
{
    uint32_t serial;
    uint8_t ready, egg, level, gender, otGender, markings, ability, flip;
    int8_t portraitX, portraitY;
    uint16_t species, dex, otId;
    uint8_t nickname[12], otName[18], abilityName[32], abilityDescription[192], memo[384];
    uint8_t portrait[2048];
    uint16_t palette[16];
    uint8_t ball[128];
    uint16_t ballPalette[16];
} CtrSummaryProfile;

bool CtrSummary_DualShown(void);
void CtrSummary_ReadView(CtrSummaryView *view);
void CtrSummary_ReadProfile(CtrSummaryProfile *profile);
/* A native 400x240 RGB565 canvas, column-major, and its content version. */
const uint16_t *CtrSummary_ProfileCanvas(uint32_t *version);
void CtrSummary_Command(unsigned command, unsigned value);
void CtrSummary_ResetDual(void);

#endif
