"""Compare the production Spinda bridge against BW2 texture-first rendering.

Run locally with --rom PATH --assets build/upstream/3ds_port/romfs/bw2.
The ROM is only read. All compiler outputs and oracle frames are temporary.
"""
from pathlib import Path
import argparse,importlib.util,os,struct,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'3ds_port/scripts'))
import gen_bw2_battle as export
spec=importlib.util.spec_from_file_location('bridge_test',ROOT/'3ds_port/tests/bw2_battle_test.py')
bridge=importlib.util.module_from_spec(spec);spec.loader.exec_module(bridge)
SEEDS=[0,0xffffffff,0x88888888,0x77777777,0x0f0f0f0f,0xf0f0f0f0,0x87654321,0x808f8888]
MAIN=r'''
#undef main
int main(int argc,char **argv) {
 assert(argc==3);assetRoot=argv[1];FILE *oracle=fopen(argv[2],"rb");assert(oracle);
 for(unsigned b=0;b<4;++b)gfx.sprites.byte[b]=pixels[b];
 u32 count,steps;assert(fread(&count,4,1,oracle)==1);assert(fread(&steps,4,1,oracle)==1);
 u8 expected[2048];BwClip *shared=NULL;
 for(unsigned n=0;n<count;++n) {
  u32 pid;assert(fread(&pid,4,1,oracle)==1);
  struct Pokemon mon={.species=SPECIES_SPINDA,.personality=pid};
  RegisterPokemon(&mon,1,FALSE);assert(sActors[1].clip&&sActors[1].clip->spots);
  if(shared)assert(shared==sActors[1].clip);shared=sActors[1].clip;
  info[3].transformSpecies=SPECIES_SPINDA;gTransformedPersonalities[3]=pid;
  struct Pokemon ditto={.species=132,.personality=pid^0xffffffff};RegisterPokemon(&ditto,3,FALSE);
  assert(sActors[3].clip==shared&&gCtrBW2ActorPersonality[3]==pid);
  for(unsigned tick=0;tick<steps;++tick) {
   assert(fread(expected,2048,1,oracle)==1);sActors[1].tick=sActors[3].tick=tick;ActorPixels(1);ActorPixels(3);
   assert(!memcmp(pixels[1],expected,2048)&&!memcmp(pixels[3],expected,2048));
   for(unsigned k=1;k<4;++k)assert(!memcmp(pixels[1],pixels[1]+k*2048,2048));
  }
  RegisterPokemon(&mon,0,TRUE);assert(sActors[0].clip&&!sActors[0].clip->spots);
  ActorPixels(0);assert(!memcmp(pixels[0],Frame(sActors[0].clip,0,TRUE),2048));
 }
 assert(fgetc(oracle)==EOF);fclose(oracle);
 gMain.inBattle=FALSE;sHadBattle=TRUE;CtrBW2_BeforeSprites();
 for(unsigned i=0;i<14;++i)assert(!sClips[i].data&&!sClips[i].spots);
 puts("Spinda: all animated pixels match BW2 texture-first oracle; extremes, overlaps, transforms, shared cache, rear invariance and cleanup passed");
 return 0;
}
'''
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--rom',type=Path,required=True);p.add_argument('--assets',type=Path,required=True);p.add_argument('--cc',required=True);a=p.parse_args()
 members=export.Nds(a.rom).archive('a/0/0/4')
 with tempfile.TemporaryDirectory(prefix='bw2-spinda-') as directory:
  folder=Path(directory);oracle=folder/'expected.bin';frames=None
  with oracle.open('wb') as out:
   for index,pid in enumerate(SEEDS):
    images,loop,bounds=export.pokemon_frames(members,327,'front',personality=pid)
    if not index:out.write(struct.pack('<II',len(SEEDS),len(images)))
    out.write(struct.pack('<I',pid))
    for im in images:out.write(export.tiles(im))
  (folder/'global.h').write_text(bridge.HEADER)
  for name in ('battle','battle_anim','battle_gfx_sfx_util','data','main','palette','pokemon','pokedex','sound','sprite','constants/species','constants/moves','constants/songs','constants/rgb','3ds_data','3ds_platform','3ds_sprite_ids','3ds_bw2_battle','3ds_video'):
   f=folder/(name+'.h');f.parent.mkdir(exist_ok=True);f.write_text('#include "global.h"\n')
  source=bridge.HARNESS.replace('PRODUCTION',(ROOT/'3ds_port/src/3ds_bw2_battle.c').as_posix()).replace('int main(int argc,char **argv)','int BridgeRegressionMain(int argc,char **argv)')
  (folder/'test.c').write_text(source+MAIN)
  exe=folder/'test.exe';subprocess.run([a.cc,'-std=gnu99','-Wall','-Wextra','-Werror','-Wno-missing-field-initializers','-Wno-misleading-indentation','-I',str(folder),str(folder/'test.c'),'-o',str(exe),'-lm'],check=True)
  env=os.environ.copy();env['PATH']=str(Path(a.cc).parent)+os.pathsep+env.get('PATH','')
  subprocess.run([str(exe),str(a.assets.resolve().parent),str(oracle)],env=env,check=True)
if __name__=='__main__':main()
