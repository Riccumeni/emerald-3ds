"""Native Emerald Unown selection and bounded multi-actor cache against real clips."""
from pathlib import Path
import argparse,importlib.util,os,re,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('bridge',ROOT/'3ds_port/tests/bw2_battle_test.py');bridge=importlib.util.module_from_spec(spec);spec.loader.exec_module(bridge)
MAIN=r'''
static u32 PersonalityFor(unsigned n) {
 return (n&3)|((n&12)<<6)|((n&48)<<12)|((n&192)<<18);
}
int main(int argc,char **argv) {
 assert(argc==2);assetRoot=argv[1];gMain.inBattle=TRUE;
 for(unsigned b=0;b<4;++b)gfx.sprites.byte[b]=pixels[b];
 for(unsigned value=0;value<256;++value) {
  u32 p=PersonalityFor(value);assert(GET_UNOWN_LETTER(p)==value%28);
  assert(GET_UNOWN_LETTER(p|0xfcfcfcfc)==value%28);
 }
 for(unsigned form=0;form<28;++form) {
  for(unsigned b=0;b<4;++b)sActors[b].clip=NULL;
  for(unsigned b=0;b<4;++b) {
   unsigned f=(form+b)%28;struct Pokemon mon={SPECIES_UNOWN,b%2,PersonalityFor(f)};
   RegisterPokemon(&mon,b,b<2);assert(sActors[b].clip&&sActors[b].species==SPECIES_UNOWN);
   assert(gCtrBW2ActorForms[b]==f&&gCtrBW2ActorPersonality[b]==mon.personality);
   assert(!memcmp(pixels[b],Frame(sActors[b].clip,0,TRUE),2048));
   assert(!memcmp(gPlttBufferFaded+256+b*16,sActors[b].clip->data+(mon.shiny?60:28),32));
   for(unsigned j=0;j<b;++j)assert(sActors[b].clip!=sActors[j].clip);
  }
  assert(!PokemonFormClip(SPECIES_UNOWN,FALSE,28));
  BwClip *old=sActors[0].clip;
  struct Pokemon same={SPECIES_UNOWN,TRUE,PersonalityFor(form)};
  RegisterPokemon(&same,0,TRUE);assert(sActors[0].clip==old);
  assert(sActors[1].clip->data&&sActors[2].clip->data&&sActors[3].clip->data);
 }
 for(unsigned b=0;b<4;++b)sActors[b].clip=NULL;
 struct Pokemon ditto={132,FALSE,0};info[0].transformSpecies=SPECIES_UNOWN;
 gTransformedPersonalities[0]=PersonalityFor(27);RegisterPokemon(&ditto,0,TRUE);
 assert(sActors[0].clip&&gCtrBW2ActorForms[0]==27);
 info[0].transformSpecies=0;
 gMain.inBattle=FALSE;sHadBattle=TRUE;CtrBW2_BeforeSprites();
 for(unsigned i=0;i<14;++i)assert(!sClips[i].data);
 puts("Unown: all 28 forms, actual Emerald macro (256 values and ignored bits), shiny palettes, pixels, four distinct simultaneous actors, cache reuse/eviction, transformed personality and cleanup passed");
}
'''
def main():
 p=argparse.ArgumentParser();p.add_argument('--cc',required=True);p.add_argument('--assets',type=Path,required=True);a=p.parse_args()
 header=bridge.HEADER
 native=(ROOT/'build/upstream/include/pokemon.h').read_text()
 macro=native.split('#define GET_UNOWN_LETTER',1)[1].split('\n\n',1)[0]
 header=re.sub(r'#define GET_UNOWN_LETTER[^\n]*',lambda _: '#define GET_UNOWN_LETTER'+macro,header)
 with tempfile.TemporaryDirectory(prefix='bw2-unown-') as directory:
  folder=Path(directory);(folder/'global.h').write_text(header)
  for name in ('battle','battle_anim','battle_gfx_sfx_util','data','main','palette','pokemon','pokedex','sound','sprite','constants/species','constants/moves','constants/songs','constants/rgb','3ds_data','3ds_platform','3ds_sprite_ids','3ds_bw2_battle','3ds_video'):
   f=folder/(name+'.h');f.parent.mkdir(exist_ok=True);f.write_text('#include "global.h"\n')
  source=bridge.HARNESS.replace('PRODUCTION',(ROOT/'3ds_port/src/3ds_bw2_battle.c').as_posix()).replace('int main(int argc,char **argv)','int BridgeRegressionMain(int argc,char **argv)')
  (folder/'test.c').write_text(source+MAIN);exe=folder/'test.exe'
  subprocess.run([a.cc,'-std=gnu99','-Wall','-Wextra','-Werror','-Wno-missing-field-initializers','-I',str(folder),str(folder/'test.c'),'-o',str(exe),'-lm'],check=True)
  env=os.environ.copy();env['PATH']=str(Path(a.cc).parent)+os.pathsep+env.get('PATH','');subprocess.run([str(exe),str(a.assets.resolve().parent)],env=env,check=True)
if __name__=='__main__':main()
