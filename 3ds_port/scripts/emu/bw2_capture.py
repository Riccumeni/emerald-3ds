"""Record real Azahar frames from the test-only BW2 validation encounter.

Requires PyAV (may be installed locally in build/bw2-python), Pillow and
Azahar's bundled RPC client. Never drives desktop input or patches gameplay.
The only write is command=1 in the validation build's explicit test mailbox.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "build/bw2-python"))
import av
import numpy as np
from PIL import Image


def symbols(elf, nm):
    result = {}
    for line in subprocess.check_output([str(nm), "--defined-only", str(elf)], text=True).splitlines():
        fields = line.split()
        if len(fields) == 3:
            result[fields[2]] = int(fields[0], 16)
    for name in ("gCtrBw2Validation", "sBuildId", "sActors", "sRunning", "sMove", "sMoveTick", "sAttacker"):
        if name not in result:
            raise ValueError("Not a BW2 validation ELF: missing " + name)
    return result


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def mailbox(rpc, address):
    values = struct.unpack("<11I", rpc.read_memory(address, 44))
    if values[0] != 0x32565742:
        raise ValueError("Invalid validation mailbox")
    return dict(zip(("magic", "frame", "phase", "command", "player", "enemy", "move",
                     "shiny", "seed", "turn", "side"), values))


def presentation(rpc, sym):
    if "sPresentation" not in sym:
        return []
    data = rpc.read_memory(sym["sPresentation"], 24)
    actors = rpc.read_memory(sym["sActors"], 32)
    result = []
    for b in range(2):
        scale, x, y, height, target, source_factor = struct.unpack_from("<HhhHHH", data, b * 12)
        item = dict(battler=b, scale_q8=scale, scale_percent=round(scale * 100 / 256, 2),
                    shift_x=x, shift_y=y, height_dm=height, target_span=target,
                    source_factor_q8=source_factor)
        clip = struct.unpack_from("<I", actors, b * 16)[0]
        if clip:
            left, top, right, bottom, floor, center = struct.unpack("<5BH", rpc.read_memory(clip + 29, 7))
            item.update(silhouette_bounds=[left, top, right, bottom], idle_floor=floor, body_center_y_q8=center)
            if source_factor:
                w, h, footprint = struct.unpack('<3H', rpc.read_memory(clip + 36, 6))
                item.update(source_width=w, source_height=h, source_footprint_q8=footprint)
        if 'gCtrBW2ActorForms' in sym:
            item['form']=rpc.read_memory(sym['gCtrBW2ActorForms']+b,1)[0]
            item['game_form']=rpc.read_memory(sym['gBattleMonForms']+b,1)[0]
        result.append(item)
    return result


def verify_spinda_pixels(rpc, sym, scenario):
    actors=rpc.read_memory(sym['sActors'],32)
    if not any(struct.unpack_from('<H',actors,b*16+12)[0]==308 for b in range(2)):return []
    personalities=struct.unpack('<2I',rpc.read_memory(sym['gCtrBW2ActorPersonality'],8))
    if personalities != (scenario.get('personality',0),)*2:raise ValueError('Actor personality mismatch')
    gfx=struct.unpack('<I',rpc.read_memory(sym['gMonSpritesGfxPtr'],4))[0]
    checks=[]
    for b in range(2):
        clip,identity,tick,species,shiny,paused=struct.unpack_from('<IIIHBB',actors,b*16)
        if species!=308:continue
        path=ROOT/f'build/upstream/3ds_port/romfs/bw2/308_{"front" if b else "back"}.bin'
        raw=path.read_bytes();frames,steps,loop=struct.unpack_from('<3I',raw,4);offset=92+((steps*2+3)&~3)
        mask=bytearray(4096);mapping=None
        if b:
            mapping=path.with_suffix('.bin.spots').read_bytes()
            pid=personalities[b]
            for i in range(4):
                x0,y0,_=struct.unpack_from('<BBH',mapping,8+i*36)
                dx=(pid&15)-8;dy=((pid>>4)&15)-8;pid>>=8
                for y,row in enumerate(struct.unpack_from('<16H',mapping,12+i*36)):
                    for x in range(16):
                        if not row&(1<<x):continue
                        px,py=x0+x+dx,y0+y+dy
                        if not (0<=px<256 and 0<=py<88):continue
                        for shift in (0,40):
                            uv=(py+shift)*256+px;mask[uv//8]|=1<<(uv%8)
            if rpc.read_memory(sym['sSpindaMask']+b*4096,4096)!=bytes(mask):raise ValueError('Spinda personality mask mismatch')
        pointer=struct.unpack('<I',rpc.read_memory(gfx+4+b*4,4))[0]
        matched=None
        for attempt in range(5):
            before=struct.unpack('<I',rpc.read_memory(sym['sActors']+b*16+8,4))[0]
            actual=rpc.read_memory(pointer,2048)
            after=struct.unpack('<I',rpc.read_memory(sym['sActors']+b*16+8,4))[0]
            for t in range(max(0,before-2),after+2):
                at=t if t<steps else loop+(t-loop)%(steps-loop)
                frame=struct.unpack_from('<H',raw,92+2*at)[0];expected=bytearray(raw[offset+frame*2048:offset+(frame+1)*2048])
                if mapping:
                    start,end=struct.unpack_from('<2I',mapping,152+4*frame)
                    for cursor in range(start,end,4):
                        pixel,uv=struct.unpack_from('<HH',mapping,cursor);shift=(pixel&1)*4;color=expected[pixel//2]>>shift&15
                        if mask[uv//8]&(1<<(uv%8)) and 1<=color<=3:expected[pixel//2]+=5<<shift
                if bytes(expected)==actual:matched=t;break
            if matched is not None:break
        if matched is None:raise ValueError('Rendered Spinda pixels differ from procedural source')
        checks.append(dict(battler=b,personality=personalities[b],procedural=bool(mapping),matched_tick=matched,pixels_sha256=hashlib.sha256(actual).hexdigest(),clip_sha256=sha(path),map_sha256=sha(path.with_suffix('.bin.spots')) if mapping else None))
    return checks


def verify_video(path, qa):
    container = av.open(str(path))
    stream = container.streams.video[0]
    info = {"codec": stream.codec_context.name, "width": stream.width, "height": stream.height,
            "pixel_format": stream.codec_context.format.name,
            "duration": float(stream.duration * stream.time_base),
            "average_fps": float(stream.average_rate)}
    count = 0
    unique = set()
    frames = []
    for frame in container.decode(video=0):
        unique.add(hashlib.sha256(frame.to_ndarray(format="rgb24").tobytes()).digest())
        if count == 0:
            frames.append(frame.to_image())
        if frame.time is not None and frame.time >= info["duration"] / 2 and len(frames) == 1:
            frames.append(frame.to_image())
        last = frame.to_image()
        count += 1
    container.close()
    if count < 30 or len(unique) < 3:
        raise ValueError("Video is empty, too short or frozen")
    frames.append(last)
    for name, im in zip(("start", "middle", "end"), frames):
        im.save(qa / ("qa-" + name + ".png"))
    info.update(decoded_frames=count, distinct_decoded_frames=len(unique), sha256=sha(path))
    return info


def verify_deoxys_pixels(rpc, sym):
    """Compare the actual battler tiles with the selected ROM-derived clip."""
    actors=rpc.read_memory(sym['sActors'],32);checks=[]
    if not any(struct.unpack_from('<H',actors,b*16+12)[0]==410 for b in range(2)):return checks
    gfx=struct.unpack('<I',rpc.read_memory(sym['gMonSpritesGfxPtr'],4))[0]
    for b in range(2):
        clip,identity,tick,species,shiny,paused=struct.unpack_from('<IIIHBB',actors,b*16)
        if species!=410:continue
        form=rpc.read_memory(sym['gCtrBW2ActorForms']+b,1)[0]
        if form not in (0,3):raise ValueError('Non-Emerald Deoxys form')
        suffix=f'_form{form}' if form else ''
        path=ROOT/f'build/upstream/3ds_port/romfs/bw2/410{suffix}_{"front" if b else "back"}.bin'
        raw=path.read_bytes();frames,steps,loop=struct.unpack_from('<3I',raw,4);offset=92+((steps*2+3)&~3)
        pointer=struct.unpack('<I',rpc.read_memory(gfx+4+b*4,4))[0];matched=None
        for attempt in range(5):
            before=struct.unpack('<I',rpc.read_memory(sym['sActors']+b*16+8,4))[0]
            actual=rpc.read_memory(pointer,2048)
            after=struct.unpack('<I',rpc.read_memory(sym['sActors']+b*16+8,4))[0]
            for t in range(max(0,before-2),after+2):
                at=t if t<steps else loop+(t-loop)%(steps-loop)
                frame=struct.unpack_from('<H',raw,92+2*at)[0]
                if raw[offset+frame*2048:offset+(frame+1)*2048]==actual:matched=t;break
            if matched is not None:break
        if matched is None:raise ValueError('Rendered Deoxys pixels differ from selected BW2 form')
        actual_palette=rpc.read_memory(sym['gPlttBufferFaded']+(256+b*16)*2,32)
        if actual_palette!=raw[60 if shiny else 28:92 if shiny else 60]:raise ValueError('Deoxys rendered palette differs from selected BW2 form')
        checks.append(dict(battler=b,form=form,species=410,shiny=shiny,matched_tick=matched,clip_sha256=sha(path),pixels_sha256=hashlib.sha256(actual).hexdigest(),palette_sha256=hashlib.sha256(actual_palette).hexdigest()))
    return checks


def capture(args):
    spec = importlib.util.spec_from_file_location("azahar_client", args.client)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rpc = module.AzaharRPC(address="127.0.0.1", timeout=2, retries=0)
    sym = symbols(args.elf, args.nm)
    expected = args.build_id.read_bytes()[:8]
    args.output.mkdir(parents=True, exist_ok=True)
    video = args.output / "demo.mp4"
    if video.exists() and not args.overwrite:
        raise FileExistsError(video)
    movie = None
    try:
        deadline = time.monotonic() + 90
        while True:
            try:
                processes = rpc.process_list()
                if len(processes) != 1:
                    raise RuntimeError("Expected one game in isolated emulator")
                rpc.set_process(next(iter(processes)))
                loaded = rpc.read_memory(sym["sBuildId"], 8)
                if loaded == expected:
                    state = mailbox(rpc, sym["gCtrBw2Validation"])
                    if (args.kind in ("idle", "transform") and state["phase"] == 1
                            or args.kind in ("move", "palette") and state["phase"] == 3):
                        break
                    if args.kind in ("idle", "transform") and state["phase"] > 1:
                        raise ValueError("Entrance already passed; restart the isolated encounter")
            except (OSError, TimeoutError):
                pass
            if time.monotonic() > deadline:
                raise TimeoutError("Validation encounter did not reach capture phase")
            time.sleep(.03)
        print("capture start " + json.dumps(state), flush=True)
        initial = state.copy()
        if 'gCtrBw2Personality' in sym:
            initial['personality']=struct.unpack('<I',rpc.read_memory(sym['gCtrBw2Personality'],4))[0]

        if "gCtrBw2DeoxysPreview" in sym:
            initial["deoxys_preview"]=struct.unpack("<I",rpc.read_memory(sym["gCtrBw2DeoxysPreview"],4))[0]

        if args.kind == "palette":
            actors = rpc.read_memory(sym["sActors"], 64)
            checked = []
            for b in range(2):
                clip, identity, tick, species, shiny, paused = struct.unpack_from("<IIIHBB", actors, b * 16)
                if not clip or not identity or shiny != state["shiny"]:
                    raise ValueError("Actor shiny selection mismatch")
                data = struct.unpack("<I", rpc.read_memory(clip, 4))[0]
                expected_palette = rpc.read_memory(data + (60 if shiny else 28), 32)
                actual_palette = rpc.read_memory(sym["gPlttBufferFaded"] + (256 + b * 16) * 2, 32)
                if expected_palette != actual_palette:
                    raise ValueError("Rendered actor palette mismatch")
                checked.append({"battler": b, "species": species, "shiny": shiny,
                                "palette_sha256": hashlib.sha256(actual_palette).hexdigest()})
            (args.output / "screenshot.png").write_bytes(rpc.screenshot(res_scale=1))
            report = {"passed": True, "kind": "palette", "scenario": initial,
                      "build_id": expected.hex(), "binary_sha256": sha(args.binary), "actors": checked,
                      "screenshot_sha256": sha(args.output / "screenshot.png"),
                      "presentation": presentation(rpc, sym)}
            report["spinda_patterns"]=verify_spinda_pixels(rpc,sym,initial)
            report["deoxys_pixels"]=verify_deoxys_pixels(rpc,sym)
            (args.output / "capture.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            print(json.dumps(report), flush=True)
            return
        movie = av.open(str(video), "w", options={"movflags": "+faststart"})
        encoder = None
        start = time.monotonic()
        ready_at = None
        command_sent = False
        turn_seen = False
        completed_at = None
        snapshot = False
        effect_snapshots = set()
        frames = 0
        last_pts = -1
        samples = []
        events = []
        active = None
        first_tick = {}
        last_tick = {}
        clip_steps = {}
        perf_start = rpc.perf_stats()
        while True:
            now = time.monotonic() - start
            state = mailbox(rpc, sym["gCtrBw2Validation"])
            if (state["player"], state["enemy"], state["move"], state["shiny"], state["seed"], state["side"]) != tuple(
                    initial[n] for n in ("player", "enemy", "move", "shiny", "seed", "side")):
                raise ValueError("Scenario changed during recording")
            if state["phase"] == 3 and ready_at is None and args.kind != "transform":
                ready_at = now
                print("actors ready at %.2fs" % now, flush=True)
            if (args.kind == "move" or args.kind == "transform" and state["phase"] == 3) and not command_sent and now >= 2:
                rpc.write_memory(sym["gCtrBw2Validation"] + 12, struct.pack("<I", 1))
                command_sent = True
            if state["phase"] == 4:
                turn_seen = True
            if args.kind in ("move", "transform") and turn_seen and state["phase"] == 3 and completed_at is None:
                completed_at = now
                print("turn completed at %.2fs" % now, flush=True)
                if args.kind == "transform":
                    ready_at=now;first_tick.clear();last_tick.clear();clip_steps.clear()
            running = bool(rpc.read_memory(sym["sRunning"], 1)[0])
            event = None
            if running:
                move = struct.unpack("<H", rpc.read_memory(sym["sMove"], 2))[0]
                attacker = rpc.read_memory(sym["sAttacker"], 1)[0]
                tick = struct.unpack("<I", rpc.read_memory(sym["sMoveTick"], 4))[0]
                event = (move, attacker)
                if active != event:
                    events.append({"move": move, "attacker": attacker, "start": now, "last_tick": tick})
                events[-1].update(end=now, last_tick=tick)
            active = event
            if frames % 6 == 0:
                actors = rpc.read_memory(sym["sActors"], 64)
                sample = {"time": now, "frame": state["frame"], "phase": state["phase"], "actors": []}
                for b in range(2):
                    clip, identity, tick, species, shiny, paused = struct.unpack_from("<IIIHBB", actors, b * 16)
                    if clip and identity:
                        clip_steps[b] = struct.unpack("<I", rpc.read_memory(clip + 8, 4))[0]
                        sample["actors"].append({"battler": b, "species": species, "tick": tick,
                                                  "identity": identity, "shiny": shiny, "paused": paused})
                        first_tick.setdefault(b, tick)
                        last_tick[b] = tick
                samples.append(sample)
            width, height, pixels = rpc.screenshot_raw(res_scale=1)
            if encoder is None:
                encoder = movie.add_stream("libx264", rate=30)
                encoder.width, encoder.height = width, height
                encoder.pix_fmt = "yuv420p"
                encoder.options = {"crf": "18", "preset": "veryfast", "tune": "zerolatency"}
                encoder.time_base = encoder.codec_context.time_base = Fraction(1, 90000)
            array = np.frombuffer(pixels, dtype=np.uint8).reshape(height, width, 3)
            frame = av.VideoFrame.from_ndarray(array, format="rgb24")
            frame.pts = max(last_pts + 1, round((time.monotonic() - start) * 90000))
            last_pts = frame.pts
            frame.time_base = Fraction(1, 90000)
            for packet in encoder.encode(frame):
                try:
                    movie.mux(packet)
                except av.error.FFmpegError:
                    print("mux error", frames, packet.pts, packet.dts, packet.time_base,
                          encoder.time_base, encoder.codec_context.time_base, flush=True)
                    raise
            frames += 1
            want_snapshot = (args.kind in ("idle", "transform") and ready_at is not None and now > ready_at + 1
                             or args.kind == "move" and running and 32 <= tick <= 44)
            if want_snapshot and not snapshot:
                Image.fromarray(array).save(args.output / "screenshot.png")
                snapshot = True
            if args.kind == "move" and running:
                for moment in (20, 32, 48, 64, 96, 128):
                    if tick >= moment and moment not in effect_snapshots:
                        Image.fromarray(array).save(args.output / ("effect-%04d.png" % moment))
                        effect_snapshots.add(moment)
            duration = max(clip_steps.values(), default=472) * 2 / 60 + 1
            if (args.kind in ("idle", "transform") and ready_at is not None and now >= ready_at + duration
                    or args.kind == "move" and completed_at is not None and now >= completed_at + 2):
                break
            if now > 70:
                raise TimeoutError("Capture did not complete within 70 seconds")
            target = start + frames / 30
            if target > time.monotonic():
                time.sleep(target - time.monotonic())
        for packet in encoder.encode():
            movie.mux(packet)
        movie.close()
        movie = None
        if not snapshot:
            raise ValueError("No meaningful screenshot captured")
        if args.kind in ("idle", "transform"):
            for b in range(2):
                if last_tick.get(b, 0) - first_tick.get(b, 0) < 2 * clip_steps.get(b, 1024):
                    raise ValueError("Actor did not advance through two complete loops")
        elif not any(e["move"] == initial["move"] and e["attacker"] == initial["side"] for e in events):
            raise ValueError("Requested move was not executed by the requested side")
        report = {"passed": True, "kind": args.kind, "scenario": initial,
                  "build_id": expected.hex(), "binary_sha256": sha(args.binary),
                  "elf_sha256": sha(args.elf), "actual_capture_fps": frames / (time.monotonic() - start),
                  "emulator_performance_start": perf_start, "emulator_performance_end": rpc.perf_stats(),
                  "ready_at": ready_at, "turn_completed_at": completed_at, "events": events,
                  "actor_steps": clip_steps, "samples": samples,
                  "presentation": presentation(rpc, sym),
                  "screenshot_sha256": sha(args.output / "screenshot.png"),
                  "video": verify_video(video, args.output),
                  "acquisition": "Native rendered RGB frames over Azahar local RPC, timestamped in real time",
                  "audio": "Not captured; test emulator has no DSP firmware"}
        report["spinda_patterns"]=verify_spinda_pixels(rpc,sym,initial)
        report["deoxys_pixels"]=verify_deoxys_pixels(rpc,sym)
        (args.output / "capture.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({k: report[k] for k in ("passed", "kind", "build_id", "actual_capture_fps", "video")}), flush=True)
    finally:
        if movie is not None:
            movie.close()
        rpc.socket.close()


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--kind", choices=("idle", "move", "palette", "transform"), required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--elf", type=Path, default=ROOT / "build/bw2-validation/validation.elf")
    p.add_argument("--binary", type=Path, default=ROOT / "build/bw2-validation/validation.3dsx")
    p.add_argument("--build-id", type=Path, default=ROOT / "build/bw2-validation/build_id.bin")
    p.add_argument("--client", type=Path, default=Path("D:/Emulators/Azahar/scripting/AzaharRPC.py"))
    p.add_argument("--nm", type=Path, default=Path("D:/Emulators/DevelopmentFiles/devkitPro/devkitARM/bin/arm-none-eabi-nm.exe"))
    p.add_argument("--overwrite", action="store_true")
    capture(p.parse_args())
