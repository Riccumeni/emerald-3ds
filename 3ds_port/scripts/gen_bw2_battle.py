#!/usr/bin/env python3
"""Export selected Emerald battle actors and the pilot moves from a Black 2 ROM.

No ROM data belongs in source control. Outputs go in romfs/bw2/ and previews
in the build directory. The game retains Emerald's 64-pixel actor canvas and
fixed camera. Nitro multi-cell animation is rasterized before the game runs;
SPL particles are projected into that same canvas, with quantized alpha.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import struct
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops

SPECIES = {252: (277, "treecko"), 261: (286, "poochyena")}
MOVES = {1: "pound", 33: "tackle", 43: "leer", 336: "howl"}
# Argument counts in this deliberately limited effect VM. Refuse other opcodes.
ARGS = {0: 5, 6: 1, 7: 11, 9: 11, 18: 7, 21: 7, 26: 2,
        42: 5, 52: 9, 56: 1, 58: 1, 59: 4, 67: 7, 77: 0}


def u16(data, off=0):
    return struct.unpack_from("<H", data, off)[0]


def u32(data, off=0):
    return struct.unpack_from("<I", data, off)[0]


class Nds:
    def __init__(self, path):
        self.data = Path(path).read_bytes()
        if len(self.data) < 0x200 or self.data[:10] != b"POKEMON B2":
            raise ValueError("Expected a Pokemon Black 2 NDS ROM")
        self.code = self.data[12:16].decode("ascii")
        self.files = {}
        fnt, fnt_size, fat, fat_size = struct.unpack_from("<4I", self.data, 0x40)
        if not (fnt_size >= 8 and fat_size % 8 == 0 and
                fnt + fnt_size <= len(self.data) and fat + fat_size <= len(self.data)):
            raise ValueError("Invalid ROM filesystem")
        table = self.data[fnt:fnt + fnt_size]

        def walk(directory, prefix, visited):
            if directory in visited or len(visited) > 32:
                raise ValueError("Invalid ROM directory tree")
            off, file_id, _ = struct.unpack_from("<IHH", table, (directory & 4095) * 8)
            while table[off]:
                length = table[off]
                off += 1
                name = table[off:off + (length & 127)].decode("ascii")
                off += length & 127
                if "/" in name or name in (".", ".."):
                    raise ValueError("Invalid ROM filename")
                if length & 128:
                    child = u16(table, off)
                    off += 2
                    walk(child, prefix + name + "/", visited | {directory})
                else:
                    if file_id * 8 + 8 > fat_size:
                        raise ValueError("ROM file ID outside FAT")
                    start, end = struct.unpack_from("<II", self.data, fat + file_id * 8)
                    if not 0 <= start <= end <= len(self.data):
                        raise ValueError("ROM file outside image")
                    self.files[prefix + name] = self.data[start:end]
                    file_id += 1
                if off >= len(table):
                    raise ValueError("Unterminated ROM directory")
        walk(0xF000, "", set())

    def archive(self, path):
        data = self.files[path]
        if data[:4] != b"NARC":
            raise ValueError(f"{path}: not a NARC archive")
        off = u16(data, 12)
        members = None
        image = None
        for _ in range(u16(data, 14)):
            kind, size = struct.unpack_from("<4sI", data, off)
            if size < 8 or off + size > len(data):
                raise ValueError("Invalid NARC section")
            if kind == b"BTAF":
                members = [struct.unpack_from("<II", data, off + 12 + i * 8)
                           for i in range(u16(data, off + 8))]
            if kind == b"GMIF":
                image = data[off + 8:off + size]
            off += size
        if members is None or image is None or any(not 0 <= a <= b <= len(image) for a, b in members):
            raise ValueError("Invalid NARC file table")
        return [image[a:b] for a, b in members]


def decompress(data):
    if not data or data[0] not in (0x10, 0x11):
        return data
    kind, size, pos = data[0], int.from_bytes(data[1:4], "little"), 4
    if size == 0:
        size, pos = u32(data, 4), 8
    if size > 8 * 1024 * 1024:
        raise ValueError("Oversized compressed resource")
    out = bytearray()
    while len(out) < size:
        flags = data[pos]
        pos += 1
        for bit in range(7, -1, -1):
            if len(out) == size:
                break
            if not flags & (1 << bit):
                out.append(data[pos]); pos += 1
                continue
            a, b = data[pos:pos + 2]; pos += 2
            if kind == 0x10:
                length, distance = (a >> 4) + 3, ((a & 15) << 8 | b) + 1
            elif a >> 4 == 0:
                c = data[pos]; pos += 1
                length, distance = ((a & 15) << 4 | b >> 4) + 17, ((b & 15) << 8 | c) + 1
            elif a >> 4 == 1:
                c, d = data[pos:pos + 2]; pos += 2
                length = ((a & 15) << 12 | b << 4 | c >> 4) + 273
                distance = ((c & 15) << 8 | d) + 1
            else:
                length, distance = (a >> 4) + 1, ((a & 15) << 8 | b) + 1
            if distance > len(out) or len(out) + length > size:
                raise ValueError("Invalid LZ back reference")
            for _ in range(length):
                out.append(out[-distance])
    return bytes(out)


def block(data, kind):
    data = decompress(data)
    off = u16(data, 12)
    for _ in range(u16(data, 14)):
        size = u32(data, off + 4)
        if size < 8 or off + size > len(data):
            raise ValueError("Invalid Nitro block")
        if data[off:off + 4] == kind:
            return data[off + 8:off + size]
        off += size
    raise ValueError(f"Missing Nitro block {kind!r}")


def rgb(value):
    return tuple(((value >> shift) & 31) * 255 // 31 for shift in (0, 5, 10))


def palette(data):
    b = block(data, b"TTLP")
    offset = u32(b, 12)
    raw = b[offset:offset + u32(b, 8)]
    if len(raw) != 32:
        raise ValueError("Expected a 16-color Pokemon palette")
    return raw


@dataclass
class Sequence:
    frames: list
    loop_start: int
    mode: int

    @property
    def duration(self):
        return sum(d for d, _ in self.frames)

    def sample(self, tick):
        total = self.duration
        loop = sum(d for d, _ in self.frames[:self.loop_start])
        if tick >= total:
            tick = loop + (tick - loop) % (total - loop) if self.mode == 2 else total - 1
        start = 0
        for duration, content in self.frames:
            if duration and tick < start + duration:
                return content, tick - start, start
            start += duration
        raise ValueError("Empty animation sequence")


def animations(data):
    b = block(data, b"KNBA")
    count, _, sequences, frames, contents = struct.unpack_from("<HHIII", b)
    result = []
    for i in range(count):
        n, loop, kind, mode, off = struct.unpack_from("<HHIII", b, sequences + 16 * i)
        if mode not in (1, 2):
            raise ValueError(f"Unsupported animation play mode {mode}")
        seq = []
        for j in range(n):
            co, duration, _ = struct.unpack_from("<IHH", b, frames + off + j * 8)
            p = contents + co
            index, rot, sx, sy, px, py = u16(b, p), 0, 1., 1., 0, 0
            if kind & 255 == 1:
                index, rot, sx, sy, px, py = struct.unpack_from("<HHii hh", b, p)
                sx, sy = sx / 4096, sy / 4096
            elif kind & 255 == 2:
                px, py = struct.unpack_from("<hh", b, p + 4)
            elif kind & 255 != 0:
                raise ValueError("Unsupported animation element")
            seq.append((duration, (index, rot, sx, sy, px, py)))
        result.append(Sequence(seq, loop, mode))
    return result


def matrix(srt, extra=(0, 0)):
    _, rot, sx, sy, x, y = srt
    angle = rot * math.tau / 65536
    return (math.cos(angle) * sx, -math.sin(angle) * sy, x + extra[0],
            math.sin(angle) * sx, math.cos(angle) * sy, y + extra[1])


def compose(m, n):
    a,b,c,d,e,f = m; g,h,i,j,k,l = n
    return a*g+b*j, a*h+b*k, a*i+b*l+c, d*g+e*j, d*h+e*k, d*i+e*l+f


def transform(image, m, size=(192, 192)):
    a,b,c,d,e,f = m
    det = a*e-b*d
    if abs(det) < 1e-9:
        return Image.new(image.mode, size)
    inv = e/det, -b/det, (b*f-e*c)/det, -d/det, a/det, (d*c-a*f)/det
    return image.transform(size, Image.Transform.AFFINE, inv, Image.Resampling.NEAREST)


def cell_poses(nodes, cells, tick, age):
    """MCSS nodes can share a controller; its first node initializes it."""
    shared = {}
    for seq, _, _, attr in nodes:
        instance = attr >> 8 & 255
        if instance not in shared:
            shared[instance] = cells[seq].sample(tick if attr & 15 == 1 else age)[0]
    return [shared[attr >> 8 & 255] for _, _, _, attr in nodes]


def composite_parts(parts, size=(192, 192)):
    """The first MCSS quad is nearest the camera, so paint it last.

    DS depth testing preserves the earlier quad over later opaque texels.
    A painter that simply traverses the nodes forward hides eyes and limbs.
    """
    canvas = Image.new(parts[0][0].mode if parts else "P", size)
    for piece, matrix_ in reversed(parts):
        placed = transform(piece, matrix_, size)
        canvas.paste(placed, (0, 0), (placed if placed.mode=="P" else placed.convert("L")).point(lambda p: 255 if p else 0, "L"))
    return canvas


# BW2 MCSS spot masks, expressed as rows relative to their texture origins.
# Nibbles of Emerald personality retain the same -8..+7 displacement semantics.
SPINDA_SPOTS = [(9, 7, [60, 126, 255, 255, 255, 255, 126, 60, 0, 0, 0, 0, 0, 0, 0, 0]), (33, 9, [60, 126, 255, 255, 255, 255, 126, 60, 0, 0, 0, 0, 0, 0, 0, 0]), (12, 25, [28, 62, 127, 127, 127, 127, 127, 62, 28, 0, 0, 0, 0, 0, 0, 0]), (24, 25, [56, 254, 511, 511, 511, 511, 511, 511, 254, 56, 0, 0, 0, 0, 0, 0])]


def spinda_texture(atlas, personality):
    result = atlas.copy()
    for x0,y0,rows in SPINDA_SPOTS:
        dx=(personality&15)-8;dy=((personality>>4)&15)-8
        for y,row in enumerate(rows):
            for x in range(16):
                if not row & (1<<x):continue
                px,py=x0+x+dx,y0+y+dy
                # Off-texture texels are invisible; never emulate the DS callback's out-of-range writes.
                if not (0<=px<256 and 0<=py<88):continue
                for shift in (0,40):
                    value=result.getpixel((px,py+shift))
                    if 1<=value<=3:result.putpixel((px,py+shift),value+5)
        personality >>= 8
    return result


def pokemon_frames(members, number, side, personality=None, labels=False, base_override=None):
    base = (number * 20 if base_override is None else base_override) + (0 if side == "front" else 9)
    chars = block(members[base + 2], b"RAHC")
    pixels = chars[u32(chars, 20):u32(chars, 20) + u32(chars, 16)]
    if len(pixels) != 16384:
        raise ValueError("Unexpected Pokemon texture size")
    atlas = Image.frombytes("P", (256,128), bytes(v for p in pixels for v in (p&15,p>>4)))
    if number==327 and side=='front' and personality is not None:
        atlas=spinda_texture(atlas,personality)
    label_atlas=None
    if labels:
        label_atlas=Image.new('I',atlas.size)
        label_atlas.putdata([i+1 if 1<=v<=3 else 65535 if v else 0 for i,v in enumerate(atlas.tobytes())])
    cells = animations(members[base + 5])
    multi = animations(members[base + 7])[0]
    b = block(members[base + 6], b"KBCM")
    count, _, arr, hierarchy = struct.unpack_from("<HHII", b)
    nodes = []
    for i in range(count):
        n, _, off = struct.unpack_from("<HHI", b, arr + i*8)
        nodes.append([struct.unpack_from("<HhhH", b, hierarchy + off + j*8) for j in range(n)])
    info = members[base + 8]
    quads = [struct.unpack_from("<12i", info, 12 + i*48) for i in range(u32(info))]
    raw_frames = []; raw_labels=[]
    for tick in range(multi.duration):
        msrt, age, start = multi.sample(tick)
        mc = compose((1,0,96,0,1,96), matrix(msrt))
        pose_nodes = nodes[msrt[0]]
        poses = cell_poses(pose_nodes, cells, tick, age)
        parts = []; label_parts=[]
        for (_, x, y, _), csrt in zip(pose_nodes, poses):
            cell = quads[csrt[0]]
            cm = compose(mc, matrix(csrt, (x,y)))
            # MCSS draws a second quad first when one is present.
            for q in (cell[6:], cell[:6]):
                qx,qy,w,h,s,t = q
                if not w or not h:
                    continue
                sx,sy,width,height = (round(v/4096) for v in (s,t,w,h))
                piece = atlas.crop((sx,sy,sx+width,sy+height))
                matrix_=compose(cm,(1,0,qx/256,0,1,-qy/256))
                parts.append((piece,matrix_))
                if labels:label_parts.append((label_atlas.crop((sx,sy,sx+width,sy+height)),matrix_))
        raw_frames.append(composite_parts(parts))
        if labels:raw_labels.append(composite_parts(label_parts))
    boxes = [im.getbbox() for im in raw_frames if im.getbbox()]
    if not boxes:
        raise ValueError("Pokemon rendered empty")
    box = (min(b[0] for b in boxes), min(b[1] for b in boxes),
           max(b[2] for b in boxes), max(b[3] for b in boxes))
    w,h = box[2]-box[0], box[3]-box[1]
    scale = min(60/w, 60/h, 1.)
    result=[]
    for im in raw_frames:
        im = im.crop(box).resize((max(1,round(w*scale)),max(1,round(h*scale))), Image.Resampling.NEAREST)
        out=Image.new("P",(64,64)); out.paste(im,((64-im.width)//2,62-im.height))
        result.append(out)
    loop=sum(d for d,_ in multi.frames[:multi.loop_start])
    if labels:
        mapped=[]
        for im in raw_labels:
            im=im.crop(box).resize((max(1,round(w*scale)),max(1,round(h*scale))),Image.Resampling.NEAREST)
            out=Image.new('I',(64,64));out.paste(im,((64-im.width)//2,62-im.height));mapped.append(out)
        return result,loop,box,mapped
    return result,loop,box


def tiles(image):
    p = image.tobytes()
    return bytes(p[(ty+y)*64+tx+x] | p[(ty+y)*64+tx+x+1]<<4
                 for ty in range(0,64,8) for tx in range(0,64,8)
                 for y in range(8) for x in range(0,8,2))


def write_layout(path, bounds, paired_bounds=None):
    w, h = bounds[2] - bounds[0], bounds[3] - bounds[1]
    other = paired_bounds if paired_bounds is not None else bounds
    ow, oh = other[2] - other[0], other[3] - other[1]
    if not all(0 < n <= 192 for n in (w,h,ow,oh)):
        raise ValueError("Invalid native Pokemon bounds")
    path.write_bytes(struct.pack('<4s4H', b'BWL2', w, h, ow, oh))


def write_clip(path, images, normal, shiny=None, loop=0, uv_frames=None):
    unique=[]; lookup={}; timeline=[]
    unique_uv=[]
    for index,im in enumerate(images):
        tile = tiles(im)
        key=(tile,uv_frames[index].tobytes()) if uv_frames is not None else tile
        if key not in lookup:
            lookup[key]=len(unique);unique.append(tile)
            if uv_frames is not None:unique_uv.append(uv_frames[index])
        timeline.append(lookup[key])
    if len(unique)>512 or not 0<=loop<len(timeline) or len(timeline)>1024:
        raise ValueError("Clip exceeds prototype limits")
    header = struct.pack("<4s6I",b"BWA1",len(unique),len(timeline),loop,64,64,60)
    raw_timeline=struct.pack("<"+"H"*len(timeline),*timeline)
    path.write_bytes(header + normal + (shiny or normal) + raw_timeline +
                     b"\0"*(-len(raw_timeline)%4) + b"".join(unique))
    if uv_frames is not None:
        shapes=b''.join(struct.pack('<BBH16H',x,y,0,*rows) for x,y,rows in SPINDA_SPOTS)
        payload=bytearray();offsets=[]
        start=152+4*(len(unique)+1)
        for uv in unique_uv:
            offsets.append(start+len(payload))
            for pos,value in enumerate(uv.get_flattened_data()):
                if not 0<value<65535:continue
                # Destination in tile order, one nibble per output pixel.
                x,y=pos%64,pos//64;destination=(y//8*8+x//8)*64+(y%8)*8+x%8
                payload+=struct.pack('<HH',destination,value-1)
        offsets.append(start+len(payload))
        path.with_suffix(path.suffix+'.spots').write_bytes(b'BWS1'+struct.pack('<I',len(unique))+shapes+struct.pack('<'+'I'*len(offsets),*offsets)+payload)
    return {"frames":len(images),"unique":len(unique),"bytes":path.stat().st_size,"loop":loop}


def preview(path, frames, pal):
    colors=[c for v in struct.unpack("<16H",pal) for c in rgb(v)] + [0]*720
    views=[]
    for im in frames:
        im=im.copy(); im.putpalette(colors)
        im.info['transparency']=0
        views.append(im.resize((256,256),Image.Resampling.NEAREST))
    views[0].save(path,save_all=True,append_images=views[1:],duration=17,loop=0,
                  transparency=0,disposal=2,optimize=False)


def decode_script(data):
    if len(data)<60 or u32(data)!=1:
        raise ValueError("Unsupported move script header")
    pos=u32(data,4); result=[]
    while pos+2<=len(data):
        op=u16(data,pos)
        if op not in ARGS:
            raise ValueError(f"Unsupported move opcode {op} at {pos}")
        args=struct.unpack_from('<'+'i'*ARGS[op],data,pos+2)
        result.append((pos,op,args)); pos+=2+4*ARGS[op]
        if op==77:
            starts={p for p,_,_ in result}
            for p,op,a in result:
                if op==59 and p+2+4*ARGS[op]+a[3] not in starts:
                    raise ValueError("Conditional jump does not land on a command")
            return result
    raise ValueError("Unterminated move script")


def particle_resource(data):
    if data[:4] != b" APS":
        raise ValueError("Not an SPL resource")
    count, texture_count = struct.unpack_from('<HH',data,8)
    pos=32; emitters=[]
    for _ in range(count):
        h=data[pos:pos+88]; pos+=88; extras={}
        flags=u32(h)
        for bit,size in ((8,12),(9,12),(10,8),(11,12),(16,20),(24,8),(25,8),(26,16),(27,4),(28,8),(29,16)):
            if flags & 1<<bit:
                extras[bit]=data[pos:pos+size];pos+=size
        emitters.append((h,extras))
    if pos != u32(data,24):
        raise ValueError("SPL emitter layout is unsupported")
    textures=[]
    for _ in range(texture_count):
        sig,param,size,po,ps,_,_,length=struct.unpack_from('<8I',data,pos)
        if sig!=0x53505420 or param&15!=6 or ps%2 or po+ps>length:
            raise ValueError("Only the selected A5I3 particle textures are supported")
        w,h=8<<((param>>4)&15),8<<((param>>8)&15)
        colors=[rgb(u16(data,pos+po+i)) for i in range(0,ps,2)]
        tex=data[pos+32:pos+32+size]
        if len(tex)!=w*h:
            raise ValueError("Invalid particle texture")
        image=Image.new('RGBA',(w,h)); image.putdata([(*colors[v&7],(v>>3)*255//31) for v in tex])
        textures.append(image);pos+=length
    return emitters,textures


def envelope(age, duration, start, mid, end, fade_in, fade_out):
    life=age*255/max(1,duration)
    if life<fade_in:
        return start+(mid-start)*life/max(1,fade_in)
    if life>fade_out:
        return mid+(end-mid)*(life-fade_out)/max(1,255-fade_out)
    return mid


def particle_frames(resource, index, seed):
    """Project SPL textures, lifetime curves and emission into a fixed 2D plane.

    This is a bounded presentation adaptation, not a Nintendo DS SPL emulator.
    Child sparks and depth/axis-dependent motion are flattened into this plane.
    """
    emitters,textures=resource; h,extra=emitters[index]; flags=u32(h)
    lifetime=u16(h,62); delay=u16(h,50); emitter_time=u16(h,60)
    if not lifetime or not emitter_time or emitter_time>180 or lifetime>180:
        raise ValueError("Unbounded particle lifetime")
    rng=random.Random(seed); particles=[]; carry=0.; frames=[]
    emission=struct.unpack_from('<i',h,16)[0]/4096
    radius=struct.unpack_from('<i',h,20)[0]/4096*9
    speed=struct.unpack_from('<i',h,36)[0]/4096*7
    base_scale=struct.unpack_from('<i',h,44)[0]/4096
    aspect=struct.unpack_from('<h',h,48)[0]/4096
    interval=max(1,h[68]); texture=h[71]
    color=rgb(u16(h,34)); gravity=(0.,0.)
    if 24 in extra:
        gx,gy,gz=struct.unpack_from('<hhh',extra[24]); gravity=(gx/4096*8,-gy/4096*8)
    for tick in range(delay+emitter_time+lifetime+1):
        if delay<=tick<delay+emitter_time and (tick-delay)%interval==0:
            carry+=emission
            for _ in range(min(24,int(carry))):
                theta=rng.random()*math.tau
                r=radius*(math.sqrt(rng.random()) if flags&15 in (4,5,7,9) else 1)
                if flags&15==0:r=0
                life=max(1,round(lifetime*(1-rng.random()*h[65]/255)))
                angle=u16(h,56)*math.tau/65536 if flags&4096 else 0
                if flags&8192:angle=rng.random()*math.tau
                particles.append([r*math.cos(theta),r*math.sin(theta),
                                  speed*math.cos(theta),speed*math.sin(theta),0,life,angle])
            carry-=int(carry)
        canvas=Image.new('RGBA',(128,128))
        alive=[]
        for p in particles:
            x,y,vx,vy,age,life,angle=p
            if age>=life:continue
            scale=1.;alpha=h[69]/31; tint=color
            if 8 in extra:
                a,b,c,fi,fo=struct.unpack_from('<hhhBB',extra[8])
                scale=envelope(age,life,a,b,c,fi,fo)/4096
            if 10 in extra:
                vals=u16(extra[10]); fi,fo=extra[10][4:6]
                alpha*=envelope(age,life,vals&31,(vals>>5)&31,(vals>>10)&31,fi,fo)/31
            if 9 in extra:
                ca,cb,fi,peak,fo=struct.unpack_from('<HHBBB',extra[9])
                tint=tuple(round(envelope(age,life,rgb(ca)[i],color[i],rgb(cb)[i],peak,fo)) for i in range(3))
            ti=texture
            if 11 in extra:
                ta=extra[11];count=ta[8]; step=max(1,ta[9]);ti=ta[min(count-1,int(age*255/life)//step)]
            tex=textures[ti].copy()
            mult=Image.new('RGBA',tex.size,(*tint,max(0,min(255,round(alpha*255)))))
            tex=ImageChops.multiply(tex,mult)
            sy=max(1,min(120,round(base_scale*scale*20)))
            sx=max(1,min(120,round(sy*aspect)))
            tex=tex.resize((sx,sy),Image.Resampling.BILINEAR)
            if flags&4096:
                tex=tex.rotate(math.degrees(angle),Image.Resampling.BILINEAR,expand=True)
            canvas.alpha_composite(tex,(round(64+x-tex.width/2),round(64+y-tex.height/2)))
            resistance=(384+h[70])/512
            alive.append([x+vx,y+vy,(vx+gravity[0])*resistance,(vy+gravity[1])*resistance,
                          age+1,life,angle+struct.unpack_from('<h',h,52)[0]*math.tau/65536])
        particles=alive
        frames.append(canvas.resize((64,64),Image.Resampling.LANCZOS))
    # Quantize all frames with one palette, retaining a stable transparent index.
    sheet=Image.new('RGB',(64,len(frames)*64))
    for i,im in enumerate(frames):sheet.paste(im.convert('RGB'),(0,i*64))
    pal=sheet.quantize(colors=15,method=Image.Quantize.MEDIANCUT).getpalette()[:45]
    pimage=Image.new('P',(1,1));pimage.putpalette(pal+[0]*(768-len(pal)))
    result=[]
    for im in frames:
        q=im.convert('RGB').quantize(palette=pimage,dither=Image.Dither.NONE)
        pixels=bytes(v+1 if a>=32 else 0 for v,a in zip(q.tobytes(),im.getchannel('A').tobytes()))
        result.append(Image.frombytes('P',(64,64),pixels))
    colors=[0]+[round(pal[i]*31/255)|round(pal[i+1]*31/255)<<5|round(pal[i+2]*31/255)<<10
                for i in range(0,len(pal),3)]
    return result,struct.pack('<16H',*(colors+[0]*(16-len(colors))))


def generate(rom_path, output, previews=None, species=None, moves=None):
    nds=Nds(rom_path); output.mkdir(parents=True,exist_ok=True)
    if previews:previews.mkdir(parents=True,exist_ok=True)
    report={"rom_code":nds.code,"rom_sha256":hashlib.sha256(nds.data).hexdigest(),
            "canvas":[64,64],"pokemon":{},"moves":{},
            "adaptations":["fixed Emerald camera", "SPL projected to 2D; child particles omitted",
                           "particle alpha quantized into a stable 15-color palette", "Emerald move sound effects"]}
    # Add one reviewed unit at a time without dropping the manifest entries of
    # previously imported Pokemon. Never mix data from two different ROMs.
    existing=output/'manifest.json'
    if existing.exists():
        previous=json.loads(existing.read_text(encoding='utf-8'))
        if previous.get('rom_sha256') != report['rom_sha256'] or previous.get('canvas') != report['canvas']:
            raise ValueError('Output contains assets from another ROM or canvas format')
        for section in ('pokemon','moves','effects','forms'):
            report[section]=previous.get(section,{}).copy()
    mons=nds.archive('a/0/0/4')
    for number,(emerald,name) in (SPECIES if species is None else species).items():
        normal,shiny=palette(mons[number*20+18]),palette(mons[number*20+19])
        for side in ('front','back'):
            uv=None
            if number==327 and side=='front':
                images,loop,bounds,uv=pokemon_frames(mons,number,side,labels=True)
            else:images,loop,bounds=pokemon_frames(mons,number,side)
            key=f'{emerald}_{side}'
            report['pokemon'][key]=write_clip(output/(key+'.bin'),images,normal,shiny,loop,uv)
            report['pokemon'][key]['source_bounds']=bounds
            if previews:preview(previews/(name+'_'+side+'.gif'),images,normal)
    if 351 in (SPECIES if species is None else species):
        personal=nds.archive('a/0/1/6')[351]
        sprite_offset,form_count,flags=struct.unpack_from('<HBB',personal,30)
        if form_count!=4 or flags&128:raise ValueError('Unexpected Castform resource mapping')
        report.setdefault('forms',{})['385']={}
        for form,name in [(1,'sunny'),(2,'rainy'),(3,'snowy')]:
            base=0x3584+(sprite_offset+form-1)*20
            normal,shiny=palette(mons[base+18]),palette(mons[base+19])
            report['forms']['385'][str(form)]=dict(name=name,resource_base=base)
            for side in ('front','back'):
                images,loop,bounds=pokemon_frames(mons,351,side,base_override=base)
                key=f'385_form{form}_{side}'
                report['pokemon'][key]=write_clip(output/(key+'.bin'),images,normal,shiny,loop)
                report['pokemon'][key]['source_bounds']=bounds
                if previews:preview(previews/(f'castform_{name}_{side}.gif'),images,normal)
    if 386 in (SPECIES if species is None else species):
        personal=nds.archive('a/0/1/6')[386]
        sprite_offset,form_count,flags=struct.unpack_from('<HBB',personal,30)
        if form_count!=4 or flags&128:raise ValueError('Unexpected Deoxys resource mapping')
        # Preserve Normal as the base clip; Emerald's own rear view uses Speed.
        base=0x3584+(sprite_offset+2)*20
        report.setdefault('forms',{})['410']={
            '0':dict(name='normal',resource_base=386*20),
            '3':dict(name='speed',resource_base=base),
            'excluded':dict(forms=['attack','defense'],reason='Not selected by Emerald battle loaders')}
        normal,shiny=palette(mons[base+18]),palette(mons[base+19])
        for side in ('front','back'):
            images,loop,bounds=pokemon_frames(mons,386,side,base_override=base)
            key=f'410_form3_{side}'
            report['pokemon'][key]=write_clip(output/(key+'.bin'),images,normal,shiny,loop)
            report['pokemon'][key]['source_bounds']=bounds
            if previews:preview(previews/(f'deoxys_speed_{side}.gif'),images,normal)
    scripts=nds.archive('a/0/6/5'); particles=nds.archive('a/0/0/6'); exported=set()
    selected_moves = MOVES if moves is None else moves
    for move,name in selected_moves.items():
        decoded=decode_script(scripts[move])
        report['moves'][str(move)]={'name':name,'commands':decoded}
        (output/f'move_{move}.bin').write_bytes(scripts[move])
        for _,op,args in decoded:
            if op not in (7,9):continue
            fid,index=args[:2]
            if (fid,index) in exported:continue
            exported.add((fid,index))
            images,pal=particle_frames(particle_resource(particles[fid]),index,fid*10+index)
            key=f'effect_{fid}_{index}'
            report.setdefault('effects',{})[key]=write_clip(output/(key+'.bin'),images,pal)
            if previews:preview(previews/(key+'.gif'),images,pal)
    # Also migrate prior incremental exports, retaining their BWA data bytes.
    for key, clip in report['pokemon'].items():
        if 'source_bounds' in clip:
            species_id, side = key.rsplit('_',1)
            paired = report['pokemon'].get(species_id+('_back' if side=='front' else '_front'),clip)
            write_layout(output/(key+'.bin.layout'), clip['source_bounds'], paired.get('source_bounds',clip['source_bounds']))
    (output/'manifest.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(f"BW2 import: {len(report['pokemon'])} Pokemon views, {len(report['moves'])} moves, {len(exported)} selected emitters ({nds.code})")
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--rom',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--previews',type=Path)
    selection=p.add_mutually_exclusive_group()
    selection.add_argument('--species',type=int,nargs='+',help='National dex numbers to add to the export')
    selection.add_argument('--all-species',action='store_true',help='Export all base species in the catalog')
    p.add_argument('--catalog',type=Path,default=Path(__file__).resolve().parents[1]/'data/bw2_species.json')
    p.add_argument('--moves',type=int,nargs='+',help='Move IDs to add; unsupported scripts are rejected')
    p.add_argument('--move-catalog',type=Path,default=Path(__file__).resolve().parents[1]/'data/bw2_moves.json')
    a=p.parse_args()
    selected=None
    if a.species or a.all_species:
        catalog=json.loads(a.catalog.read_text(encoding='utf-8'))
        selected={}
        for number in sorted(map(int,catalog)) if a.all_species else a.species:
            item=catalog[str(number)]
            emerald,name=int(item['emerald']),item['name']
            if not 1<=number<=386 or not (1<=emerald<=251 or 277<=emerald<=411) or not name.replace('_','').isalnum():
                raise ValueError('Invalid catalog species')
            selected[number]=(emerald,name)
    selected_moves=None
    if a.moves:
        catalog=json.loads(a.move_catalog.read_text(encoding='utf-8'))
        selected_moves={}
        for move in a.moves:
            if not 1<=move<=354:raise ValueError('Invalid Emerald move ID')
            selected_moves[move]=catalog[str(move)]['name']
    generate(a.rom,a.out,a.previews,selected,selected_moves)
