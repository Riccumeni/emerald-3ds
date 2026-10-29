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

def castform_media(folder,relative,build,side,form,shiny,cycle=False):
 source=(folder/relative).resolve()
 if not source.is_relative_to(folder.resolve()):raise ValueError('Variant evidence escaped its dossier')
 cap=read(source/'capture.json');scenario=cap['scenario']
 if not cap.get('passed') or cap['kind']!='form':raise ValueError('Missing actual weather/form capture')
 if cap['build_id']!=build['build_id'] or cap['binary_sha256']!=build['sha256']:raise ValueError('Variant build mismatch')
 if scenario['player']!=385 or scenario['enemy']!=385 or scenario['shiny']!=shiny:raise ValueError('Castform scenario mismatch')
 if {241:1,240:2,258:3}.get(scenario['move'])!=form or cap['expected_form']!=form:raise ValueError('Wrong weather form')
 if bool(scenario['return_normal'])!=cycle or cap['final_form']!=(0 if cycle else form):raise ValueError('Weather expiry missing')
 if cap.get('weather_move_imported') is not False:raise ValueError('Weather moves must remain pending imports')
 if not cap.get('turn_completed_at') or cap['completed_turns']<(5 if cycle else 1):raise ValueError('Actual turn/menu return missing')
 if not any(a['battler']==side and a['species']==385 and a['shiny']==shiny for a in cap['actors']):raise ValueError('Form shiny selection missing')
 history=[h['forms'][side] for h in cap['form_history']]
 if not history or history[0]!=0 or form not in history or history[-1]!=(0 if cycle else form):raise ValueError('Forecast transition missing')
 if cycle:
  chosen=[s.get('chosen_moves',[0])[0] for s in cap['samples'] if s['phase']==4]
  if 241 not in chosen or 150 not in chosen:raise ValueError('Actual Sunny Day then Splash choices missing')
 for value,ready,step_key in [(form,cap['form_ready_at'],'target_actor_steps')]+([(0,cap['normal_ready_at'],'normal_actor_steps')] if cycle else []):
  samples=[s for s in cap['samples'] if s['at']>=ready and s['phase']==3 and s['forms']==[value,value] and s['loaded_forms']==[value,value]]
  ticks=[s['actors'][side]['tick'] for s in samples]
  if not ticks or max(ticks)-min(ticks)<2*cap[step_key][str(side)]:raise ValueError('Two stable form cycles missing')
 if sha(source/'screenshot.png')!=cap['screenshot_sha256'] or sha(source/'demo.mp4')!=cap['video']['sha256']:raise ValueError('Castform media changed')
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
 if item['numero_nazionale']==351:
  if manifest.get('kind')!='castform-weather':raise ValueError('Castform weather audit missing')
  cases={c['form']:c for c in manifest['cases']}
  if set(cases)!={0,1,2,3}:raise ValueError('Missing Castform form')
  for form,case in cases.items():
   if not case.get('visual_reviewed'):raise ValueError('Unreviewed Castform form')
   for direction,side in [('front',1),('back',0)]:
    for shiny,key in [(0,'normal'),(1,'shiny')]:
     if not form:
      cap=media(folder,case[key][direction],build,385,side,'palette' if shiny else 'idle')
      pose=next(p for p in cap['presentation'] if p['battler']==side)
      if pose.get('form')!=0 or pose.get('game_form')!=0:raise ValueError('Normal Castform selection missing')
     else:castform_media(folder,case[key][direction],build,side,form,shiny)
  if not manifest.get('return_normal_reviewed'):raise ValueError('Normal return is not reviewed')
  for direction,side in [('front',1),('back',0)]:castform_media(folder,manifest['return_normal'][direction],build,side,1,0,True)
  return dict(kind=manifest['kind'],forms=4,shiny_forms=4,front_back=True,real_weather_expiry=True)
 if item['numero_nazionale']==386:
  if manifest.get('kind')!='deoxys-emerald':raise ValueError('Deoxys Emerald audit missing')
  cases={c['form']:c for c in manifest['cases']}
  if set(cases)!={0,3}:raise ValueError('Missing Emerald Deoxys form')
  def selected(cap,side,form):
   pose=next((p for p in cap.get('presentation',[]) if p['battler']==side),None)
   pixels=next((p for p in cap.get('deoxys_pixels',[]) if p['battler']==side),None)
   if not pose or pose.get('form')!=form or not pixels or pixels.get('form')!=form or pixels.get('species')!=410:raise ValueError('Deoxys selected pixels/form mismatch')
   if pixels.get('shiny')!=cap['scenario']['shiny']:raise ValueError('Deoxys shiny pixels selection mismatch')
   if cap['kind']=='idle':
    ticks=[a['tick'] for s in cap['samples'] if s['time']>=cap['ready_at'] and s['phase']==3 for a in s['actors'] if a['battler']==side and a['species']==410]
    if not ticks or max(ticks)-min(ticks)<2*cap['actor_steps'][str(side)]:raise ValueError('Two Deoxys form cycles missing')
  for form,case in cases.items():
   if not case.get('visual_reviewed'):raise ValueError('Unreviewed Deoxys form')
   for direction,side in [('front',1),('back',0)]:
    for shiny,key in [(0,'normal'),(1,'shiny')]:
     cap=media(folder,case[key][direction],build,410,side,'palette' if shiny else 'idle')
     if cap['scenario'].get('deoxys_preview')!=(2 if form else 1):raise ValueError('Deoxys art inventory context missing')
     selected(cap,side,form)
  for direction,side in [('front',1),('back',0)]:
   for shiny,key in [(0,'normal'),(1,'shiny')]:
    cap=media(folder,manifest['default'][key][direction],build,410,side,'palette' if shiny else 'idle')
    if cap['scenario'].get('deoxys_preview')!=0:raise ValueError('Ordinary Deoxys capture cannot use an art preview')
    selected(cap,side,0 if side else 3)
  if not manifest.get('transform_reviewed'):raise ValueError('Real Deoxys Transform not reviewed')
  for shiny,key in [(0,'normal'),(1,'shiny')]:
   source=(folder/manifest['transform'][key]).resolve()
   if not source.is_relative_to(folder.resolve()):raise ValueError('Deoxys transform path escaped dossier')
   cap=read(source/'capture.json');scenario=cap['scenario']
   if not cap.get('passed') or cap['kind']!='transform' or cap['build_id']!=build['build_id'] or cap['binary_sha256']!=build['sha256']:raise ValueError('Deoxys Transform build/capture mismatch')
   if (scenario['player'],scenario['enemy'],scenario['move'],scenario['side'],scenario['shiny'],scenario.get('deoxys_preview'))!=(132,410,144,0,shiny,0):raise ValueError('Deoxys Transform scenario mismatch')
   if not cap.get('turn_completed_at') or not cap.get('ready_at'):raise ValueError('Real Transform turn/menu return missing')
   for side in (0,1):
    selected(cap,side,0)
    ticks=[a['tick'] for s in cap['samples'] if s['time']>=cap['ready_at'] and s['phase']==3 for a in s['actors'] if a['battler']==side and a['species']==410]
    if not ticks or max(ticks)-min(ticks)<2*cap['actor_steps'][str(side)]:raise ValueError('Two transformed Deoxys cycles missing')
   if sha(source/'screenshot.png')!=cap['screenshot_sha256'] or sha(source/'demo.mp4')!=cap['video']['sha256']:raise ValueError('Deoxys Transform media changed')
  if not manifest.get('selection_reviewed'):raise ValueError('Emerald Deoxys selectors not reviewed')
  return dict(kind=manifest['kind'],forms=2,shiny_forms=2,front_back=True,ordinary_player_speed=True,ordinary_opponent_normal=True,real_transform=True,link_selection_host_tested=True,link_runtime_verified=False)
 raise ValueError('No implemented variant audit for this species')
