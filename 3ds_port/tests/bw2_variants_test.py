"""Reject incomplete or stale procedural species evidence."""
from pathlib import Path
import hashlib,json,sys,tempfile,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import bw2_variants as variants
class VariantsTest(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name);self.folder=self.root/'spinda';self.folder.mkdir();self.item=dict(cartella='spinda',numero_nazionale=327);self.build=dict(build_id='id',sha256='binary');self.manifest=dict(kind='spinda-personality',visual_reviewed=True,cases=[])
  for pid in variants.SPINDA_SEEDS:
   case=dict(personality=pid,visual_reviewed=True,normal={},shiny={})
   for side,b in [('front',1),('back',0)]:
    for shiny in [False,True] if pid in variants.SPINDA_SHINY_SEEDS else [False]:
     relative=f'{pid:08x}/{"shiny-" if shiny else ""}{side}';folder=self.folder/relative;folder.mkdir(parents=True)
     (folder/'screenshot.png').write_bytes(b'png');(folder/'demo.mp4').write_bytes(b'video')
     cap=dict(passed=True,kind='palette' if shiny else 'idle',build_id='id',binary_sha256='binary',scenario=dict(player=308,enemy=308,shiny=int(shiny),personality=pid),screenshot_sha256=hashlib.sha256(b'png').hexdigest(),video=dict(sha256=hashlib.sha256(b'video').hexdigest()),actors=[dict(battler=b,species=308,shiny=1)],spinda_patterns=[dict(battler=b,personality=pid,procedural=bool(b))]);self.write(folder/'capture.json',cap);case['shiny' if shiny else 'normal'][side]=relative
   self.manifest['cases'].append(case)
  self.write(self.folder/'variants.json',self.manifest)
 def write(self,path,value):path.write_text(json.dumps(value))
 def mutate(self,relative,change):
  path=self.folder/relative;value=json.loads(path.read_text());change(value);self.write(path,value)
 def test_complete_extremes_overlap_and_palettes(self):self.assertEqual(variants.check_variants(self.root,self.item,self.build)['personalities'],8)
 def test_missing_seed(self):
  self.mutate('variants.json',lambda m:m['cases'].pop())
  with self.assertRaisesRegex(ValueError,'Missing extreme'):variants.check_variants(self.root,self.item,self.build)
 def test_wrong_personality(self):
  self.mutate('ffffffff/front/capture.json',lambda c:c['scenario'].update(personality=0))
  with self.assertRaisesRegex(ValueError,'personality mismatch'):variants.check_variants(self.root,self.item,self.build)
 def test_changed_video(self):
  (self.folder/'ffffffff/back/demo.mp4').write_bytes(b'changed')
  with self.assertRaisesRegex(ValueError,'video changed'):variants.check_variants(self.root,self.item,self.build)
 def test_stale_build(self):
  self.mutate('ffffffff/front/capture.json',lambda c:c.update(binary_sha256='stale'))
  with self.assertRaisesRegex(ValueError,'build mismatch'):variants.check_variants(self.root,self.item,self.build)
 def test_unreviewed_case(self):
  self.mutate('variants.json',lambda c:c['cases'][0].update(visual_reviewed=False))
  with self.assertRaisesRegex(ValueError,'Unreviewed'):variants.check_variants(self.root,self.item,self.build)
 def test_missing_procedural_check(self):
  self.mutate('ffffffff/front/capture.json',lambda c:c.update(spinda_patterns=[]))
  with self.assertRaisesRegex(ValueError,'Procedural pixels'):variants.check_variants(self.root,self.item,self.build)
class CastformVariantsTest(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name);self.folder=self.root/'castform';self.folder.mkdir();self.item=dict(cartella='castform',numero_nazionale=351);self.build=dict(build_id='id',sha256='binary')
  self.manifest=dict(kind='castform-weather',visual_reviewed=True,cases=[],return_normal_reviewed=True,return_normal={})
  for form in range(4):
   case=dict(form=form,visual_reviewed=True,normal={},shiny={})
   for side in ['front','back']:
    for shiny,key in [(0,'normal'),(1,'shiny')]:
     path=f'{form}/{key}/{side}';self.make_capture(path,form,shiny);case[key][side]=path
   self.manifest['cases'].append(case)
  for side in ['front','back']:
   path=f'return/{side}';self.make_capture(path,1,0,True);self.manifest['return_normal'][side]=path
  self.write(self.folder/'variants.json',self.manifest)
 def write(self,path,value):path.write_text(json.dumps(value))
 def mutate(self,relative,change):
  path=self.folder/relative;value=json.loads(path.read_text());change(value);self.write(path,value)
 def make_capture(self,path,form,shiny,cycle=False):
  p=self.folder/path;p.mkdir(parents=True);(p/'screenshot.png').write_bytes(b'png');(p/'demo.mp4').write_bytes(b'video')
  actors=[dict(battler=b,species=385,shiny=shiny) for b in range(2)]
  cap=dict(passed=True,kind='form' if form else ('palette' if shiny else 'idle'),build_id='id',binary_sha256='binary',scenario=dict(player=385,enemy=385,shiny=shiny,move={0:1,1:241,2:240,3:258}[form],return_normal=cycle),screenshot_sha256=hashlib.sha256(b'png').hexdigest(),video=dict(sha256=hashlib.sha256(b'video').hexdigest()),actors=actors,presentation=[dict(battler=b,form=0,game_form=0) for b in range(2)])
  if form:
   samples=[]
   for value,at in [(form,10)]+([(0,30)] if cycle else []):
    for delta,tick in [(0,0),(5,200)]:samples.append(dict(at=at+delta,phase=3,forms=[value,value],loaded_forms=[value,value],actors=[dict(tick=tick) for b in range(2)]))
   samples+=[dict(at=1,phase=4,chosen_moves=[241,150]),dict(at=20,phase=4,chosen_moves=[150,150])]
   history=[dict(forms=[0,0]),dict(forms=[form,form])]+([dict(forms=[0,0])] if cycle else [])
   cap.update(weather_move_imported=False,turn_completed_at=29,completed_turns=5 if cycle else 1,expected_form=form,final_form=0 if cycle else form,form_history=history,form_ready_at=10,normal_ready_at=30 if cycle else None,target_actor_steps={'0':100,'1':100},normal_actor_steps={'0':100,'1':100},samples=samples)
  self.write(p/'capture.json',cap)
 def check(self):return variants.check_variants(self.root,self.item,self.build)
 def test_all_forms_and_natural_expiry(self):self.assertTrue(self.check()['real_weather_expiry'])
 def test_missing_shiny_form(self):
  self.mutate('3/shiny/front/capture.json',lambda c:c['scenario'].update(shiny=0))
  with self.assertRaisesRegex(ValueError,'scenario mismatch'):self.check()
 def test_wrong_resource_selected(self):
  self.mutate('2/normal/back/capture.json',lambda c:c['samples'][1].update(loaded_forms=[0,0]))
  with self.assertRaisesRegex(ValueError,'Two stable'):self.check()
 def test_one_cycle_is_insufficient(self):
  self.mutate('1/normal/front/capture.json',lambda c:c['samples'][1]['actors'][1].update(tick=199))
  with self.assertRaisesRegex(ValueError,'Two stable'):self.check()
 def test_gameplay_must_really_return(self):
  self.mutate('return/front/capture.json',lambda c:c.update(completed_turns=4))
  with self.assertRaisesRegex(ValueError,'Actual turn'):self.check()
 def test_expiry_cannot_use_repeated_weather_move(self):
  self.mutate('return/front/capture.json',lambda c:c['samples'][-1].update(chosen_moves=[241,150]))
  with self.assertRaisesRegex(ValueError,'Sunny Day then Splash'):self.check()
 def test_reject_move_import_claim(self):
  self.mutate('3/normal/front/capture.json',lambda c:c.update(weather_move_imported=True))
  with self.assertRaisesRegex(ValueError,'pending imports'):self.check()
 def test_hashes_apply_to_shiny_form_videos(self):
  (self.folder/'2/shiny/back/demo.mp4').write_bytes(b'changed')
  with self.assertRaisesRegex(ValueError,'media changed'):self.check()
if __name__=='__main__':unittest.main()
