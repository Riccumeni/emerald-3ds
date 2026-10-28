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
if __name__=='__main__':unittest.main()
