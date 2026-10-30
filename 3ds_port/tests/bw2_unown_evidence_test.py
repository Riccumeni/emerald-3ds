"""Independent rejection tests for the mandatory 28-form native Unown dossier."""
from pathlib import Path
import copy,hashlib,json,sys,tempfile,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import bw2_variants as variants
def pid(n):return (n&3)|((n&12)<<6)|((n&48)<<12)|((n&192)<<18)
class UnownEvidenceTest(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name);self.folder=self.root/'unown';self.folder.mkdir();self.item=dict(cartella='unown',numero_nazionale=201);self.build=dict(build_id='id',sha256='binary')
  self.manifest=dict(kind='unown-personality',visual_reviewed=True,cache_reviewed=True,multi_actor='1/normal/back',cases=[])
  for f in range(28):
   case=dict(form=f,visual_reviewed=True,normal={},shiny={})
   for key,shiny in [('normal',0),('shiny',1)]:
    for direction,b in [('front',1),('back',0)]:
     rel=f'{f}/{key}/{direction}';p=self.folder/rel;p.mkdir(parents=True);(p/'screenshot.png').write_bytes(b'png');(p/'demo.mp4').write_bytes(b'video')
     forms=[f,(f+1)%28] if b==0 else [(f+1)%28,f]
     checks=[dict(battler=i,form=ff,personality=pid(ff),species=201,shiny=shiny,native_selection=True,clip_sha256='clip',palette_sha256='palette') for i,ff in enumerate(forms)]
     cap=dict(passed=True,kind='idle',build_id='id',binary_sha256='binary',scenario=dict(player=201,enemy=201,shiny=shiny,personality=pid(forms[0]),enemy_personality=pid(forms[1]),deoxys_preview=0),unown_pixels=checks,presentation=[dict(battler=i,form=ff,source_factor_q8=256) for i,ff in enumerate(forms)],ready_at=4,actor_steps={'0':100,'1':100},samples=[dict(phase=3,time=t,actors=[dict(battler=i,species=201,shiny=shiny,tick=tick) for i in range(2)]) for t,tick in [(4,0),(8,200)]],screenshot_sha256=hashlib.sha256(b'png').hexdigest(),video=dict(sha256=hashlib.sha256(b'video').hexdigest(),codec='h264',decoded_frames=240))
     self.write(p/'capture.json',cap);case[key][direction]=rel
   self.manifest['cases'].append(case)
  self.write(self.folder/'variants.json',self.manifest)
 def write(self,p,v):p.write_text(json.dumps(v))
 def mutate(self,relative,change):
  p=self.folder/relative;v=json.loads(p.read_text());change(v);self.write(p,v)
 def check(self):return variants.check_variants(self.root,self.item,self.build)
 def test_complete(self):self.assertEqual(self.check()['forms'],28)
 def test_missing_form(self):
  self.mutate('variants.json',lambda c:c['cases'].pop())
  with self.assertRaisesRegex(ValueError,'Missing or duplicate'):self.check()
 def test_duplicate_form(self):
  self.mutate('variants.json',lambda c:c['cases'][-1].update(form=0))
  with self.assertRaisesRegex(ValueError,'Missing or duplicate'):self.check()
 def test_unreviewed(self):
  self.mutate('variants.json',lambda c:c['cases'][27].update(visual_reviewed=False))
  with self.assertRaisesRegex(ValueError,'Unreviewed'):self.check()
 def test_personality(self):
  self.mutate('27/normal/back/capture.json',lambda c:c['scenario'].update(personality=0))
  with self.assertRaisesRegex(ValueError,'native pixels/personality'):self.check()
 def test_shiny_pixels(self):
  self.mutate('26/shiny/front/capture.json',lambda c:c['unown_pixels'][1].update(shiny=0))
  with self.assertRaisesRegex(ValueError,'native pixels/personality'):self.check()
 def test_short_cycle(self):
  self.mutate('12/normal/back/capture.json',lambda c:c['samples'][-1]['actors'][0].update(tick=199))
  with self.assertRaisesRegex(ValueError,'two cycles'):self.check()
 def test_missing_entrance(self):
  self.mutate('0/normal/front/capture.json',lambda c:c.update(ready_at=0))
  with self.assertRaisesRegex(ValueError,'entrance missing'):self.check()
 def test_changed_shiny_video(self):
  (self.folder/'27/shiny/back/demo.mp4').write_bytes(b'changed')
  with self.assertRaisesRegex(ValueError,'media changed'):self.check()
 def test_wrong_build(self):
  self.mutate('4/normal/back/capture.json',lambda c:c.update(binary_sha256='old'))
  with self.assertRaisesRegex(ValueError,'build mismatch'):self.check()
 def test_diagnostic_rejected(self):
  self.mutate('4/normal/back/capture.json',lambda c:c['scenario'].update(deoxys_preview=1))
  with self.assertRaisesRegex(ValueError,'native scenario'):self.check()
 def test_incomplete_cache_proof(self):
  self.mutate('variants.json',lambda c:c.update(cache_reviewed=False))
  with self.assertRaisesRegex(ValueError,'multi-actor'):self.check()
 def test_path_escape(self):
  self.mutate('variants.json',lambda c:c['cases'][1]['normal'].update(back='../elsewhere'))
  with self.assertRaisesRegex(ValueError,'escaped'):self.check()
if __name__=='__main__':unittest.main()
