"""Validate additional native evidence for species with procedural/weather forms."""
import hashlib
import json
from pathlib import Path

SPINDA_SEEDS=(0,0xffffffff,0x88888888,0x77777777,0x0f0f0f0f,0xf0f0f0f0,0x87654321,0x808f8888)
SPINDA_SHINY_SEEDS=(0,0xffffffff,0x808f8888)
def read(path):return json.loads(path.read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def media(folder, relative, build, species, side, kind, personality=None):
 source=(folder/relative).resolve()
 if not source.is_relative_to(folder.resolve()):raise ValueError('Variant evidence escaped its dossier')
 cap=read(source/'capture.json');scenario=cap['scenario']
 if not cap.get('passed') or cap['kind']!=kind:raise ValueError('Variant capture failed/wrong kind')
 if cap['build_id']!=build['build_id'] or cap['binary_sha256']!=build['sha256']:raise ValueError('Variant build mismatch')
 if scenario['enemy' if side else 'player']!=species:raise ValueError('Variant species/direction mismatch')
 if personality is not None:
  if scenario.get('personality')!=personality:raise ValueError('Variant personality mismatch')
  pattern=next((p for p in cap.get('spinda_patterns',[]) if p['battler']==side),None)
  if pattern is None or pattern['personality']!=personality or pattern['procedural']!=bool(side):raise ValueError('Procedural pixels were not verified')
 if sha(source/'screenshot.png')!=cap['screenshot_sha256']:raise ValueError('Variant screenshot changed')
 if kind=='idle':
  if scenario['shiny']!=0 or sha(source/'demo.mp4')!=cap['video']['sha256']:raise ValueError('Variant video changed')
 else:
  if scenario['shiny']!=1 or not any(a['battler']==side and a['species']==species and a['shiny'] for a in cap['actors']):raise ValueError('Variant shiny selection mismatch')
 return cap

def check_variants(root,item,build):
 folder=Path(root)/item['cartella'];manifest=read(folder/'variants.json')
 if not manifest.get('visual_reviewed'):raise ValueError('Variants require visual review')
 if item['numero_nazionale']==327:
  if manifest.get('kind')!='spinda-personality':raise ValueError('Spinda personality audit missing')
  cases={c['personality']:c for c in manifest['cases']}
  if set(cases)!=set(SPINDA_SEEDS):raise ValueError('Missing extreme/overlap Spinda seed')
  for seed,c in cases.items():
   if not c.get('visual_reviewed'):raise ValueError('Unreviewed Spinda seed')
   for direction,side in [('front',1),('back',0)]:
    media(folder,c['normal'][direction],build,308,side,'idle',seed)
    if seed in SPINDA_SHINY_SEEDS:media(folder,c['shiny'][direction],build,308,side,'palette',seed)
  return dict(kind=manifest['kind'],personalities=len(cases),shiny_personalities=len(SPINDA_SHINY_SEEDS),front_back=True)
 raise ValueError('No implemented variant audit for this species')
