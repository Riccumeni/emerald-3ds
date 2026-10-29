"""Capture real weather turns, Forecast form changes and two idle cycles.

Uses only the validation mailbox's controller commands. No weather, HP, form,
result or sprite pixels are written by the recorder. Weather moves retain the
ordinary Emerald animation and are not marked imported by this evidence.
"""
from pathlib import Path
from fractions import Fraction
import argparse,hashlib,importlib.util,json,struct,time
import bw2_capture as base
import av
import numpy as np
from PIL import Image
ROOT=base.ROOT

def capture(args):
 module_spec=importlib.util.spec_from_file_location('azahar_client',args.client);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
 rpc=module.AzaharRPC(address='127.0.0.1',timeout=2,retries=0);sym=base.symbols(args.elf,args.nm);expected=args.build_id.read_bytes()[:8]
 for name in ['gCtrBW2ActorForms','gBattleMonForms','gBattleWeather','gChosenMoveByBattler']:
  if name not in sym:raise ValueError('Missing form diagnostic '+name)
 args.output.mkdir(parents=True,exist_ok=True);video=args.output/'demo.mp4'
 if video.exists() and not args.overwrite:raise FileExistsError(video)
 movie=None
 try:
  deadline=time.monotonic()+90
  while True:
   try:
    processes=rpc.process_list()
    if len(processes)!=1:raise ValueError('Expected one isolated game')
    rpc.set_process(next(iter(processes)))
    if rpc.read_memory(sym['sBuildId'],8)==expected:
     initial=base.mailbox(rpc,sym['gCtrBw2Validation'])
     if initial['phase']==1:break
     if initial['phase']>1:raise ValueError('Entrance already passed; restart')
   except (OSError,TimeoutError):pass
   if time.monotonic()>deadline:raise TimeoutError('Form capture startup')
   time.sleep(.03)
  if (initial['player'],initial['enemy'])!=(385,385):raise ValueError('Form scenario requires two Castform')
  target={241:1,240:2,258:3}[initial['move']]
  if args.return_normal and target!=1:raise ValueError('The expiry audit uses Sunny Day')
  initial['return_normal']=bool(args.return_normal);initial['personality']=struct.unpack('<I',rpc.read_memory(sym['gCtrBw2Personality'],4))[0]
  movie=av.open(str(video),'w',options={'movflags':'+faststart'});encoder=None;start=time.monotonic();frames=0;last_pts=-1
  perf_start=rpc.perf_stats();samples=[];history=[];ready=None;first_completed=None;last_completed=None;stable=None;normal=None
  first_ticks={};normal_ticks={};target_steps={};normal_steps={};steps={};last_cmd_turn=-1;started=False;poster=False;observed_target=False;proved_target=False;last_snapshot=None;last_turn_seen=0
  while True:
   now=time.monotonic()-start;state=base.mailbox(rpc,sym['gCtrBw2Validation'])
   if any(state[k]!=initial[k] for k in ['player','enemy','move','shiny','seed','side']):raise ValueError('Form scenario changed')
   if frames%3==0 or last_snapshot is None:
    game=list(rpc.read_memory(sym['gBattleMonForms'],2));loaded=list(rpc.read_memory(sym['gCtrBW2ActorForms'],2));actors=rpc.read_memory(sym['sActors'],32);actor_info=[]
    for b in range(2):
     clip,identity,tick,species,shiny,paused=struct.unpack_from('<IIIHBB',actors,b*16)
     if clip:steps[b]=struct.unpack('<I',rpc.read_memory(clip+8,4))[0]
     actor_info.append(dict(battler=b,species=species,tick=tick,clip=clip,shiny=shiny))
    weather=struct.unpack('<H',rpc.read_memory(sym['gBattleWeather'],2))[0]
    chosen=list(struct.unpack('<2H',rpc.read_memory(sym['gChosenMoveByBattler'],4)))
    last_snapshot=dict(at=now,phase=state['phase'],turn=state['turn'],forms=game,loaded_forms=loaded,weather=weather,chosen_moves=chosen,actors=actor_info);samples.append(last_snapshot)
    if not history or history[-1]['forms']!=game:history.append(dict(at=now,turn=state['turn'],forms=game,loaded_forms=loaded,weather=weather))
   snap=last_snapshot
   if state['phase']==3 and not started:
    ready=now;rpc.write_memory(sym['gCtrBw2Validation']+12,struct.pack('<I',1));started=True;last_cmd_turn=state['turn']
   if started and state['phase']==3 and state['turn']>last_turn_seen:
    last_turn_seen=state['turn'];last_completed=now
    if first_completed is None:first_completed=now
   if first_completed is not None and state['phase']==3:
    if snap['forms']==[target,target] and snap['loaded_forms']==[target,target] and stable is None:
     if not all(a['clip'] and a['species']==385 for a in snap['actors']):raise ValueError('Missing imported form actor')
     stable=now;first_ticks={a['battler']:a['tick'] for a in snap['actors']};target_steps=dict(steps);observed_target=True
    if stable is not None:
     span=2*max(steps.values())/60+1
     if now>=stable+span and not proved_target:
      proved_target=all(a['tick']-first_ticks[a['battler']]>=2*steps[a['battler']] for a in snap['actors'])
      if not proved_target:raise ValueError('Target form did not complete two cycles')
     if proved_target:
      if not args.return_normal:break
      if snap['forms']==[0,0] and snap['loaded_forms']==[0,0]:
       if normal is None:normal=now;normal_ticks={a['battler']:a['tick'] for a in snap['actors']};normal_steps=dict(steps)
       if now>=normal+2*max(steps.values())/60+1:
        if not all(a['tick']-normal_ticks[a['battler']]>=2*steps[a['battler']] for a in snap['actors']):raise ValueError('Returned form did not complete two cycles')
        break
      elif state['turn']>last_cmd_turn and now-last_completed>.5:
       if state['turn']>7:raise ValueError('Weather did not expire through ordinary turns')
       rpc.write_memory(sym['gCtrBw2Validation']+12,struct.pack('<I',2));last_cmd_turn=state['turn']
   width,height,pixels=rpc.screenshot_raw(res_scale=1)
   if encoder is None:
    encoder=movie.add_stream('libx264',rate=30);encoder.width=width;encoder.height=height;encoder.pix_fmt='yuv420p';encoder.options={'crf':'18','preset':'veryfast','tune':'zerolatency'};encoder.time_base=encoder.codec_context.time_base=Fraction(1,90000)
   array=np.frombuffer(pixels,dtype=np.uint8).reshape(height,width,3);frame=av.VideoFrame.from_ndarray(array,format='rgb24');frame.pts=max(last_pts+1,round((time.monotonic()-start)*90000));last_pts=frame.pts;frame.time_base=Fraction(1,90000)
   for packet in encoder.encode(frame):movie.mux(packet)
   frames+=1
   if stable is not None and not poster and now>=stable+1:
    Image.fromarray(array).save(args.output/'screenshot.png');poster=True
   if now>180:raise TimeoutError('Weather/form capture exceeded 180 seconds')
   next_frame=start+frames/30
   if next_frame>time.monotonic():time.sleep(next_frame-time.monotonic())
  for packet in encoder.encode():movie.mux(packet)
  movie.close();movie=None
  if not poster or not observed_target or not proved_target:raise ValueError('Form evidence incomplete')
  if args.return_normal and (normal is None or state['turn']<5):raise ValueError('Normal return was not a real weather expiry')
  if args.return_normal:
   selected=[s['chosen_moves'][0] for s in samples if s['phase']==4]
   if 241 not in selected or 150 not in selected:raise ValueError('Actual Sunny Day then Splash choices missing')
  actor_bytes=rpc.read_memory(sym['sActors'],32);actors=[];asset_hashes={}
  for b in range(2):
   clip,identity,tick,species,shiny,paused=struct.unpack_from('<IIIHBB',actor_bytes,b*16);data=struct.unpack('<I',rpc.read_memory(clip,4))[0];expected_palette=rpc.read_memory(data+(60 if shiny else 28),32);actual_palette=rpc.read_memory(sym['gPlttBufferFaded']+(256+b*16)*2,32)
   if species!=385 or shiny!=initial['shiny'] or expected_palette!=actual_palette:raise ValueError('Active form/shiny palette mismatch')
   actors.append(dict(battler=b,species=species,shiny=shiny,palette_sha256=hashlib.sha256(actual_palette).hexdigest()))
   for form in set([0,target]):
    name=f'385_{"form"+str(form)+"_" if form else ""}{"front" if b else "back"}.bin'
    for ext in ['', '.layout']:asset_hashes[name+ext]=base.sha(ROOT/'build/upstream/3ds_port/romfs/bw2'/(name+ext))
  report=dict(passed=True,kind='form',scenario=initial,build_id=expected.hex(),binary_sha256=base.sha(args.binary),elf_sha256=base.sha(args.elf),actual_capture_fps=frames/(time.monotonic()-start),emulator_performance_start=perf_start,emulator_performance_end=rpc.perf_stats(),ready_at=ready,form_ready_at=stable,normal_ready_at=normal,turn_completed_at=last_completed,completed_turns=state['turn'],expected_form=target,final_form=0 if args.return_normal else target,form_history=history,actors=actors,actor_steps=steps,target_actor_steps=target_steps,normal_actor_steps=normal_steps,samples=samples,presentation=base.presentation(rpc,sym),screenshot_sha256=base.sha(args.output/'screenshot.png'),video=base.verify_video(video,args.output),asset_hashes=asset_hashes,weather_move_imported=False,acquisition='Native Azahar RGB at 1x; real Emerald weather moves, Forecast and menu return; two cycles for each demonstrated stable form',audio='Not captured; no DSP firmware in test setup')
  (args.output/'capture.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:report[k] for k in ['passed','expected_form','final_form','completed_turns','video']}),flush=True)
 finally:
  if movie is not None:movie.close()
  rpc.socket.close()
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kind',choices=['form'],required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--return-normal',action='store_true');p.add_argument('--overwrite',action='store_true')
 p.add_argument('--elf',type=Path,default=ROOT/'build/bw2-validation/validation.elf');p.add_argument('--binary',type=Path,default=ROOT/'build/bw2-validation/validation.3dsx');p.add_argument('--build-id',type=Path,default=ROOT/'build/bw2-validation/build_id.bin');p.add_argument('--client',type=Path,default=Path('D:/Emulators/Azahar/scripting/AzaharRPC.py'));p.add_argument('--nm',type=Path,default=Path('D:/Emulators/DevelopmentFiles/devkitPro/devkitARM/bin/arm-none-eabi-nm.exe'));capture(p.parse_args())
