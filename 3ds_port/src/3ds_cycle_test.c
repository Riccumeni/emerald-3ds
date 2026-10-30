/*
 * Scene cycling for the GPU memory gate of phase F2 (-DCTR_CYCLE_TEST=cycles):
 * "100 scene cycles and a long session without a failure, corruption or loss
 * of 3D". Built only for that test; an ordinary build has none of it.
 *
 * From the player's save it presses A until the field is up, then cycles: the
 * voxel world on or off, the battle over it on or off and the 3D slider at 0
 * or 1 (the eight combinations in turn), a few seconds of field, a wild
 * battle, out of it by RUN (the action cursor set to it, A pressed), and back
 * to the field. Each cycle is logged; the frame profile's segments say how
 * much 3D each scene showed and GPUMEM what failed. The settings it changes
 * are not saved, and the game is never saved.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "global.h"
#include "main.h"
#include "battle.h"
#include "battle_setup.h"
#include "script_pokemon_util.h"
#include "overworld.h"
#include "constants/species.h"
#include "constants/opponents.h"
#include "trainer_see.h"
#include "3ds_platform.h"
#if defined(CTR_BW2_DEMO) || defined(CTR_BW2_VALIDATION)
#include "pokemon.h"
#endif

#ifdef CTR_BW2_VALIDATION
#include "battle_controllers.h"
#include "random.h"
#include "constants/moves.h"

/* Test-only mailbox, exposed by ELF symbols to the local emulator recorder.
 * No game-memory patch is needed: command=1 asks the real controller to play
 * one turn. A normal build contains neither this mailbox nor the encounter. */
volatile struct
{
    u32 magic, frame, phase, command;
    u32 player, enemy, move, shiny, seed, turn, side;
} gCtrBw2Validation = {0x32565742, 0, 0, 0, SPECIES_TREECKO, SPECIES_POOCHYENA,
                       MOVE_POUND, 0, 4660, 0, 2};
static u32 sValidationField, sValidationReady;
static bool8 sValidationInitialized;
static u32 sValidationPersonality;
static u32 sValidationEnemyPersonality;
static bool8 sValidationEnemyPersonalitySet;
volatile u32 gCtrBw2Personality;
volatile u32 gCtrBw2EnemyPersonality;
volatile u32 gCtrBw2DeoxysPreview;

static bool8 ValidationActionMenu(void)
{
    return (gBattleControllerExecFlags & 1)
        && gBattleBufferA[0][0] == CONTROLLER_CHOOSEACTION;
}

static void ValidationInit(void)
{
    FILE *file = fopen("sdmc:/3ds/emerald3ds/bw2-validation.txt", "r");
    char line[96], key[32];
    unsigned value;
    if (file)
    {
        while (fgets(line, sizeof(line), file))
        {
            if (sscanf(line, "%31[^=]=%u", key, &value) != 2)
                continue;
            if (!strcmp(key, "player") && value && value < NUM_SPECIES)
                gCtrBw2Validation.player = value;
            else if (!strcmp(key, "enemy") && value && value < NUM_SPECIES)
                gCtrBw2Validation.enemy = value;
            else if (!strcmp(key, "move") && value && value < MOVES_COUNT)
                gCtrBw2Validation.move = value;
            else if (!strcmp(key, "shiny")) gCtrBw2Validation.shiny = value != 0;
            else if (!strcmp(key, "seed")) gCtrBw2Validation.seed = value;
            else if (!strcmp(key, "personality")) sValidationPersonality = value;
            else if (!strcmp(key, "enemy_personality"))
            {
                sValidationEnemyPersonality = value;
                sValidationEnemyPersonalitySet = TRUE;
            }
            else if (!strcmp(key, "deoxys_preview") && value <= 2) gCtrBw2DeoxysPreview = value;
            else if (!strcmp(key, "side") && value <= 2) gCtrBw2Validation.side = value;
        }
        fclose(file);
    }
    CtrSettings_Freeze();
    CtrSettings_ApplyLine("speed=1");
    CtrSettings_ApplyLine("fps=0");
    CtrSettings_ApplyLine("voxel=1");
    CtrSettings_ApplyLine("voxel_battle=0");
    CtrLog_Write(CTR_LOG_GAME, "BW2 VALIDATE player=%lu enemy=%lu move=%lu shiny=%lu seed=%lu",
                 (unsigned long)gCtrBw2Validation.player, (unsigned long)gCtrBw2Validation.enemy,
                 (unsigned long)gCtrBw2Validation.move, (unsigned long)gCtrBw2Validation.shiny,
                 (unsigned long)gCtrBw2Validation.seed);
}

void CtrCycle_Frame(void)
{
    ++gCtrBw2Validation.frame;
    if (!sValidationInitialized)
    {
        ValidationInit();
        sValidationInitialized = TRUE;
    }
    if (!gMain.inBattle)
    {
        if (gMain.callback2 != CB2_Overworld || gCtrBw2Validation.phase)
            return;
        if (!sValidationField) sValidationField = gCtrBw2Validation.frame;
        if (gCtrBw2Validation.frame - sValidationField < 90)
            return;
        SeedRng(gCtrBw2Validation.seed);
        SeedRng2(gCtrBw2Validation.seed);
        ZeroPlayerPartyMons();
        ZeroEnemyPartyMons();
        u32 ot = sValidationPersonality ^ (gCtrBw2Validation.shiny ? 0 : 0x12345678);
        u32 enemyPersonality = sValidationEnemyPersonalitySet ? sValidationEnemyPersonality : sValidationPersonality;
        u32 enemyOt = enemyPersonality ^ (gCtrBw2Validation.shiny ? 0 : 0x12345678);
        gCtrBw2Personality = sValidationPersonality;
        gCtrBw2EnemyPersonality = enemyPersonality;
        CreateMon(&gPlayerParty[0], gCtrBw2Validation.player, 5, 31, TRUE, sValidationPersonality, OT_ID_PRESET, ot);
        CreateMon(&gEnemyParty[0], gCtrBw2Validation.enemy, 5, 31, TRUE, enemyPersonality, OT_ID_PRESET, enemyOt);
        for (unsigned i = 0; i < MAX_MON_MOVES; ++i)
        {
            u16 move = !i ? gCtrBw2Validation.move : i == 1 ? MOVE_SPLASH : MOVE_NONE;
            SetMonMoveSlot(&gPlayerParty[0], !i && gCtrBw2Validation.side == 1 ? MOVE_SPLASH : move, i);
            SetMonMoveSlot(&gEnemyParty[0], !i && gCtrBw2Validation.side == 0 ? MOVE_SPLASH : move, i);
        }
        gPlayerPartyCount = 1;
        gSaveBlock2Ptr->optionsBattleSceneOff = FALSE;
        gCtrBw2Validation.phase = 1;
        BattleSetup_StartScriptedWildBattle();
        return;
    }
    if (gCtrBw2Validation.phase == 1 && ValidationActionMenu())
    {
        sValidationReady = gCtrBw2Validation.frame;
        gCtrBw2Validation.phase = 2;
    }
    if (gCtrBw2Validation.phase == 2 && gCtrBw2Validation.frame - sValidationReady >= 60)
        gCtrBw2Validation.phase = 3;
    if (gCtrBw2Validation.phase == 3 && (gCtrBw2Validation.command == 1 || gCtrBw2Validation.command == 2))
    {
        /* Command 2 selects the existing Splash slot through the real menu.
         * Weather expiry still follows ordinary Emerald turns and Forecast. */
        gMoveSelectionCursor[0] = gCtrBw2Validation.command == 2 ? 1 : 0;
        gCtrBw2Validation.command = 0;
        gCtrBw2Validation.turn = gBattleResults.battleTurnCounter;
        gCtrBw2Validation.phase = 4;
    }
    if (gCtrBw2Validation.phase == 4 && ValidationActionMenu()
        && gBattleResults.battleTurnCounter != gCtrBw2Validation.turn)
    {
        gCtrBw2Validation.turn = gBattleResults.battleTurnCounter;
        gCtrBw2Validation.phase = 3;
    }
}

void CtrCycle_Input(CtrInputSample *sample)
{
    if ((!gCtrBw2Validation.phase && gCtrBw2Validation.frame % 40 < 2)
        || ((gCtrBw2Validation.phase == 1 || gCtrBw2Validation.phase == 4)
            && gCtrBw2Validation.frame % 30 < 2))
        sample->buttons |= 1;
}

#elif defined(CTR_CYCLE_TEST)

extern u8 gActionSelectionCursor[MAX_BATTLERS_COUNT];

#define CYCLE_FIELD_FRAMES 300
#define CYCLE_PRESS_EVERY 20

static u32 sFrame, sFieldSince, sCycle, sBattles;
static bool8 sStarted, sInBattle, sPress;

void CtrCycle_Frame(void)
{
    bool8 field = gMain.callback2 == CB2_Overworld && !gMain.inBattle;

    ++sFrame;
    if (!sStarted)
    {
        sStarted = TRUE;
        CtrSettings_Freeze();
        CtrSettings_ApplyLine("speed=1");
        CtrLog_Write(CTR_LOG_GAME, "CYCLE test: %u cycles", (unsigned)CTR_CYCLE_TEST);
    }
    sPress = FALSE;
    if (gMain.inBattle)
    {
        if (!sInBattle)
            ++sBattles;
        sInBattle = TRUE;
        for (unsigned i = 0; i < MAX_BATTLERS_COUNT; ++i)
            gActionSelectionCursor[i] = 3;
        sPress = (sFrame % CYCLE_PRESS_EVERY) < 2;
        sFieldSince = 0;
        return;
    }
    sInBattle = FALSE;
    if (!field)
    {
        /* The title and the main menu: CONTINUE is the default. */
        sPress = sCycle == 0 && (sFrame % 40) < 2;
        sFieldSince = 0;
        return;
    }
    if (!sFieldSince)
    {
        unsigned k = sCycle;
        char line[32];

        if (sCycle == CTR_CYCLE_TEST)
        {
            CtrLog_Write(CTR_LOG_GAME, "CYCLE test done: %lu cycles, %lu battles", (unsigned long)sCycle,
                         (unsigned long)sBattles);
            CtrPlatform_RequestExit();
            sFieldSince = sFrame;
            return;
        }
        snprintf(line, sizeof(line), "voxel=%u", k & 1);
        CtrSettings_ApplyLine(line);
        snprintf(line, sizeof(line), "voxel_battle=%u", (k >> 1) & 1);
        CtrSettings_ApplyLine(line);
        CtrScenario_ForceSlider((k >> 2) & 1 ? 1.0f : 0.0f);
        CtrLog_Write(CTR_LOG_GAME, "CYCLE %u voxel=%u battle3d=%u slider=%u at frame %lu", k, k & 1, (k >> 1) & 1,
                     (k >> 2) & 1, (unsigned long)sFrame);
        sFieldSince = sFrame;
        return;
    }
    if (sCycle < CTR_CYCLE_TEST && sFrame - sFieldSince == CYCLE_FIELD_FRAMES)
    {
        ++sCycle;
        CreateScriptedWildMon(SPECIES_ZIGZAGOON, 5, 0);
        BattleSetup_StartScriptedWildBattle();
    }
}

void CtrCycle_Input(CtrInputSample *sample)
{
    if (sPress)
        sample->buttons |= 1;
}

#elif defined(CTR_BATTLE_TEST)

/*
 * A battle on demand, for looking at the battle screen in an emulator
 * (-DCTR_BATTLE_TEST=SPECIES_x, optionally -DCTR_BATTLE_TEST_LEVEL=n, or
 * -DCTR_BATTLE_TEST_TRAINER=TRAINER_x for that trainer's battle - a double
 * one for a doubles trainer): a second and a half after the field is up,
 * every time it is; in battle A is pressed every 12 frames, so that its
 * turns play (FIGHT, the first move, the messages).
 */
#ifndef CTR_BATTLE_TEST_LEVEL
#define CTR_BATTLE_TEST_LEVEL 50
#endif
static u32 sFrame, sFieldSince;

void CtrCycle_Frame(void)
{
    ++sFrame;
    if (gMain.callback2 != CB2_Overworld || gMain.inBattle)
    {
        sFieldSince = 0;
        return;
    }
    if (!sFieldSince)
        sFieldSince = sFrame;
    if (sFrame - sFieldSince == 90)
    {
#ifdef CTR_BATTLE_TEST_TRAINER
        gNoOfApproachingTrainers = 1;
        gTrainerBattleOpponent_A = CTR_BATTLE_TEST_TRAINER;
        BattleSetup_StartTrainerBattle();
#else
#ifdef CTR_BW2_DEMO
        /* Isolated emulator validation only; this build never saves the party. */
        ZeroPlayerPartyMons();
        CreateMon(&gPlayerParty[0], SPECIES_TREECKO, 5, 31, TRUE, 0, OT_ID_PLAYER_ID, 0);
        gPlayerPartyCount = 1;
#endif
        CreateScriptedWildMon(CTR_BATTLE_TEST, CTR_BATTLE_TEST_LEVEL, 0);
        BattleSetup_StartScriptedWildBattle();
#endif
    }
}

void CtrCycle_Input(CtrInputSample *sample)
{
    /* In battle, A every 12 frames: FIGHT, the first move, the messages. */
    if (gMain.inBattle && sFrame % 12 < 2)
        sample->buttons |= 1;
#ifdef CTR_BW2_DEMO
    /* Boot and CONTINUE in the isolated demo without desktop key injection. */
    if (!gMain.inBattle && sFrame % 40 < 2)
        sample->buttons |= 1;
#endif
}

#else

void CtrCycle_Frame(void) {}
void CtrCycle_Input(CtrInputSample *sample) { (void)sample; }

#endif
