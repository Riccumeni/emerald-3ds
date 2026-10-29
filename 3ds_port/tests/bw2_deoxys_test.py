"""Test the BW2 bridge against Emerald's actual Deoxys selector function."""
from pathlib import Path
import argparse,importlib.util,os,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('bridge',ROOT/'3ds_port/tests/bw2_battle_test.py');bridge=importlib.util.module_from_spec(spec);spec.loader.exec_module(bridge)
MAIN=r'''
volatile u32 gCtrBw2DeoxysPreview;
int main(int argc,char **argv) {
 assert(argc==2);assetRoot=argv[1];gMain.inBattle=TRUE;
 for(unsigned b=0;b<4;++b)gfx.sprites.byte[b]=pixels[b];
 struct Pokemon mon={SPECIES_DEOXYS,FALSE,0};
 RegisterPokemon(&mon,0,TRUE);assert(sActors[0].clip&&gCtrBW2ActorForms[0]==3);
 RegisterPokemon(&mon,1,FALSE);assert(sActors[1].clip&&gCtrBW2ActorForms[1]==0);
 assert(sActors[0].clip==PokemonFormClip(SPECIES_DEOXYS,TRUE,3));
 assert(sActors[1].clip==PokemonFormClip(SPECIES_DEOXYS,FALSE,0));
 assert(!PokemonFormClip(SPECIES_DEOXYS,FALSE,1)&&!PokemonFormClip(SPECIES_DEOXYS,FALSE,2));
 assert(!PokemonFormClip(SPECIES_TREECKO,FALSE,3));
#ifdef CTR_BW2_VALIDATION
 for(unsigned preview=1;preview<=2;++preview) {
  gCtrBw2DeoxysPreview=preview;
  for(unsigned b=0;b<4;++b)
   assert(SelectedPokemonForm(SPECIES_DEOXYS,b,b%2==0,0)==(preview==2?3:0));
 }
 gCtrBw2DeoxysPreview=0;
#endif
 /* Compile and exercise the original upstream predicate, including multi
  * ownership and temporary front/back copies used by move animations. */
 for(unsigned flags=0;flags<4;++flags) {
  gBattleTypeFlags=(flags&1?BATTLE_TYPE_LINK:0)|(flags&2?BATTLE_TYPE_MULTI:0);
  for(unsigned owner=0;owner<4;owner+=2) {
   gLinkPlayers[0].id=owner;
   for(unsigned b=0;b<4;++b) {
    unsigned expected=(b%2==0&&(!(flags&2)||b==owner))?3:0;
    assert(SelectedPokemonForm(SPECIES_DEOXYS,b,b%2==0,0)==expected);
    assert(SelectedPokemonForm(SPECIES_DEOXYS,b,b%2==0,SPECIES_DEOXYS)==0);
    assert(ShouldIgnoreDeoxysForm(5,b)==!(b%2==0&&(!(flags&1)||!(flags&2)||b==owner)));
   }
  }
 }
 gBattleTypeFlags=0;
 /* Native Transform bypasses the wrapped gfx loaders. Keep its mosaic/BG
  * effect intact, then rebind the actor automatically at animation end. */
 gPlayerParty[0]=(struct Pokemon){132,FALSE,0};gBattleMons[0].species=132;
 gSprites[0].inUse=TRUE;gSprites[0].anims=gAnims_MonPic;identities[0]=99;
 RegisterPokemon(&gPlayerParty[0],0,TRUE);assert(sActors[0].species==132);
 info[0].transformSpecies=SPECIES_DEOXYS;gAnimScriptActive=TRUE;
 CtrBW2_BeforeSprites();assert(sActors[0].species==132&&sActors[0].id==0);
 gAnimScriptActive=FALSE;CtrBW2_BeforeSprites();
 assert(sActors[0].species==SPECIES_DEOXYS&&gCtrBW2ActorForms[0]==0&&sActors[0].id==99);
 unsigned tick=sActors[0].tick;CtrBW2_BeforeSprites();assert(sActors[0].tick==tick+1);
 info[0].transformSpecies=0;CtrBW2_BeforeSprites();assert(sActors[0].species==132);
 for(unsigned i=0;i<20;++i) {
  mon.shiny=i%2;info[0].transformSpecies=i%3?SPECIES_NONE:SPECIES_DEOXYS;
  RegisterPokemon(&mon,0,TRUE);unsigned f=info[0].transformSpecies?0:3;
  assert(sActors[0].clip&&gCtrBW2ActorForms[0]==f);
  assert(sActors[0].clip==PokemonFormClip(SPECIES_DEOXYS,TRUE,f));
  assert(!memcmp(pixels[0],Frame(sActors[0].clip,0,TRUE),2048));
  assert(!memcmp(gPlttBufferFaded+256,sActors[0].clip->data+(mon.shiny?60:28),32));
 }
 for(unsigned b=0;b<4;++b)sActors[b].clip=NULL;
 for(unsigned f=0;f<4;f+=3)for(unsigned back=0;back<2;++back) {
  BwClip *c=PokemonFormClip(SPECIES_DEOXYS,back,f);assert(c&&c->steps&&c->nativeWidth&&c->nativeHeight);
 }
 gMain.inBattle=FALSE;sHadBattle=TRUE;CtrBW2_BeforeSprites();
 for(unsigned i=0;i<14;++i)assert(!sClips[i].data&&!sClips[i].spots);
 puts("Deoxys: actual Emerald ownership/link/copy predicates, Normal/Speed front/back, Transform selection, palettes, cache rebinding and cleanup passed");return 0;
}
'''
def main():
 p=argparse.ArgumentParser();p.add_argument('--cc',required=True);p.add_argument('--assets',type=Path,required=True);p.add_argument('--validation',action='store_true');a=p.parse_args()
 original=(ROOT/'build/upstream/src/pokemon.c').read_text();selector='bool8 ShouldIgnoreDeoxysForm'+original.split('bool8 ShouldIgnoreDeoxysForm',1)[1].split('static u16 GetDeoxysStat',1)[0]
 context='#define BATTLE_TYPE_MULTI 4\nstruct {u8 id;} gLinkPlayers[4];\nu8 GetMultiplayerId(void){return 0;}\n'
 with tempfile.TemporaryDirectory(prefix='bw2-deoxys-') as directory:
  folder=Path(directory);(folder/'global.h').write_text(bridge.HEADER)
  for name in ('battle','battle_anim','battle_gfx_sfx_util','data','main','palette','pokemon','pokedex','sound','sprite','constants/species','constants/moves','constants/songs','constants/rgb','3ds_data','3ds_platform','3ds_sprite_ids','3ds_bw2_battle','3ds_video'):
   f=folder/(name+'.h');f.parent.mkdir(exist_ok=True);f.write_text('#include "global.h"\n')
  source=bridge.HARNESS.replace('PRODUCTION',(ROOT/'3ds_port/src/3ds_bw2_battle.c').as_posix()).replace('int main(int argc,char **argv)','int BridgeRegressionMain(int argc,char **argv)')
  source=source.replace('bool8 ShouldIgnoreDeoxysForm(u8 c,u8 b) { (void)c; (void)b; return FALSE; }',context+selector)
  (folder/'test.c').write_text(source+MAIN);exe=folder/'test.exe'
  subprocess.run([a.cc,*(['-DCTR_BW2_VALIDATION'] if a.validation else []),'-std=gnu99','-Wall','-Wextra','-Werror','-Wno-missing-field-initializers','-I',str(folder),str(folder/'test.c'),'-o',str(exe),'-lm'],check=True)
  env=os.environ.copy();env['PATH']=str(Path(a.cc).parent)+os.pathsep+env.get('PATH','');subprocess.run([str(exe),str(a.assets.resolve().parent)],env=env,check=True)
if __name__=='__main__':main()
