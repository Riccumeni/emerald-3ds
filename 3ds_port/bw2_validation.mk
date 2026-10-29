# Optional overlay for the BW2 validation build:
# make -f Makefile -f bw2_validation.mk TEST_FLAGS=-DCTR_BW2_VALIDATION
# The ordinary build leaves TEST_FLAGS empty. Touch both bridge and cycle
# sources when switching modes: the parent makefile scopes these test flags.
build/bridge/3ds_bw2_battle.o: FULLCFLAGS += $(TEST_FLAGS)
