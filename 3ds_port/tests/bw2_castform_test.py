"""Exercise actual Castform clips and form-driven cache rebinding in the bridge."""
from pathlib import Path
import argparse,importlib.util,os,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('bridge',ROOT/'3ds_port/tests/bw2_battle_test.py');bridge=importlib.util.module_from_spec(spec);spec.loader.exec_module(bridge)
MAIN=r'''
int main(int argc,char **argv) {
 assert(argc==2);assetRoot=argv[1];gMain.inBattle=TRUE;
 for(unsigned b=0;b<4;++b)gfx.sprites.byte[b]=pixels[b];
 for(unsigned b=0;b<2;++b) {
  gPlayerParty[0].species=gEnemyParty[0].species=SPECIES_CASTFORM;gEnemyParty[0].shiny=TRUE;
  gBattleMons[b].species=SPECIES_CASTFORM;gSprites[b].inUse=TRUE;gSprites[b].anims=gAnims_MonPic;identities[b]=b+1;
  RegisterPokemon(b?gEnemyParty:gPlayerParty,b,!b);assert(sActors[b].clip);
 }
 static const u8 forms[]={1,2,3,0,2,1,0};
 for(unsigned k=0;k<sizeof(forms);++k) {
  for(unsigned b=0;b<2;++b)gBattleMonForms[b]=forms[k];
  CtrBW2_BeforeSprites();
  for(unsigned b=0;b<2;++b) {
   assert(gCtrBW2ActorForms[b]==forms[k]&&sActors[b].clip);
   BwClip *clip=PokemonFormClip(SPECIES_CASTFORM,!b,forms[k]);assert(clip==sActors[b].clip);
   assert(!memcmp(pixels[b],Frame(clip,sActors[b].tick-1,TRUE),2048));
   assert(!memcmp(gPlttBufferFaded+256+b*16,clip->data+(b?60:28),32));
  }
 }
 gBattleMonForms[0]=3;CtrBW2_BeforeSprites();assert(gCtrBW2ActorForms[0]==3&&gCtrBW2ActorForms[1]==0);
 assert(!PokemonFormClip(SPECIES_TREECKO,FALSE,1)&&!PokemonFormClip(SPECIES_CASTFORM,FALSE,4));
 gMain.inBattle=FALSE;CtrBW2_BeforeSprites();for(unsigned i=0;i<14;++i)assert(!sClips[i].data&&!sClips[i].spots);
 puts("Castform: all four front/back clips, independent forms, shiny palettes, repeated switches, bounded cache and cleanup passed");return 0;
}
'''
def main():
 p=argparse.ArgumentParser();p.add_argument('--cc',required=True);p.add_argument('--assets',type=Path,required=True);a=p.parse_args()
 with tempfile.TemporaryDirectory(prefix='bw2-castform-') as directory:
  folder=Path(directory);(folder/'global.h').write_text(bridge.HEADER)
  for name in ('battle','battle_anim','battle_gfx_sfx_util','data','main','palette','pokemon','pokedex','sound','sprite','constants/species','constants/moves','constants/songs','constants/rgb','3ds_data','3ds_platform','3ds_sprite_ids','3ds_bw2_battle','3ds_video'):
   f=folder/(name+'.h');f.parent.mkdir(exist_ok=True);f.write_text('#include "global.h"\n')
  source=bridge.HARNESS.replace('PRODUCTION',(ROOT/'3ds_port/src/3ds_bw2_battle.c').as_posix()).replace('int main(int argc,char **argv)','int BridgeRegressionMain(int argc,char **argv)');(folder/'test.c').write_text(source+MAIN)
  exe=folder/'test.exe';subprocess.run([a.cc,'-std=gnu99','-Wall','-Wextra','-Werror','-Wno-missing-field-initializers','-I',str(folder),str(folder/'test.c'),'-o',str(exe),'-lm'],check=True)
  env=os.environ.copy();env['PATH']=str(Path(a.cc).parent)+os.pathsep+env.get('PATH','');subprocess.run([str(exe),str(a.assets.resolve().parent)],env=env,check=True)
if __name__=='__main__':main()
