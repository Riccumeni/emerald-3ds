"""Authored VOX furniture, applied after the original-art ownership proof.

The room decomposition still proves which original pixels are replaced and
which floor marks are retained. Authored geometry intentionally changes that
view; it is checked by voxel_custom_props_test rather than the GBA pixel proof.
"""

import collections
import copy
import os
import struct

from PIL import Image
import voxel_building as vb


def read_vox(path):
    with open(path, "rb") as stream:
        raw = stream.read()
    if raw[:4] != b"VOX " or len(raw) < 20:
        raise ValueError("not a VOX model: " + path)
    size, voxels, palette = None, None, None
    offset = 8
    while offset + 12 <= len(raw):
        name, length, children = struct.unpack_from("<4sII", raw, offset)
        start = offset + 12
        if start + length + children > len(raw):
            raise ValueError("truncated VOX chunk")
        data = raw[start:start + length]
        if name == b"SIZE":
            size = struct.unpack("<III", data)
        elif name == b"XYZI":
            count, = struct.unpack_from("<I", data)
            if len(data) != 4 + count * 4:
                raise ValueError("invalid voxel count")
            # MagicaVoxel Z is up; this renderer uses Y up.
            voxels = {(x, z, y): i for x, y, z, i in struct.iter_unpack("BBBB", data[4:])}
        elif name == b"RGBA":
            palette = list(struct.iter_unpack("BBBB", data))
        offset = start + length
    if size is None or not voxels or palette is None or len(palette) != 256:
        raise ValueError("expected one nonempty model with an explicit palette")
    dims = (size[0], size[2], size[1])
    if any(i == 0 or any(p[a] >= dims[a] for a in range(3)) for p, i in voxels.items()):
        raise ValueError("voxel outside model or using transparent index")
    return dims, voxels, {i: palette[i - 1] for i in set(voxels.values())}


def face_rectangles(voxels):
    """Merge exposed coplanar faces of one colour, preserving all holes."""
    groups = collections.defaultdict(set)
    for p, colour in voxels.items():
        for axis in range(3):
            u, v = (axis + 1) % 3, (axis + 2) % 3
            for sign in (-1, 1):
                neighbour = list(p)
                neighbour[axis] += sign
                if tuple(neighbour) not in voxels:
                    groups[axis, sign, p[axis] + (sign > 0), colour].add((p[u], p[v]))
    for (axis, sign, plane, colour), cells in sorted(groups.items()):
        while cells:
            u0, v0 = min(cells)
            u1 = u0 + 1
            while (u1, v0) in cells:
                u1 += 1
            v1 = v0 + 1
            while all((u, v1) in cells for u in range(u0, u1)):
                v1 += 1
            cells.difference_update((u, v) for u in range(u0, u1) for v in range(v0, v1))
            yield axis, sign, plane, colour, u0, v0, u1, v1


def replace_vox(model, path, origin, extent):
    dims, voxels, palette = read_vox(path)
    result = copy.copy(model)
    scale = tuple(extent[a] / dims[a] for a in range(3))
    old_height = model.art.height
    result.art = Image.new("RGBA", (max(model.art.width, len(palette) * 4), old_height + 4))
    result.art.paste(model.art, (0, 0))
    uv = {}
    for n, (i, rgba) in enumerate(sorted(palette.items())):
        result.art.paste(rgba, (n * 4, old_height, n * 4 + 4, old_height + 4))
        uv[i] = (n * 4 + 2, old_height + 2)
    result.mesh = vb.Mesh()
    # Keep the room's rug and its reconstruction beneath the furniture.
    for part in model.prisms:
        if isinstance(part, vb.Decal):
            part.emit(result.mesh)
    for axis, sign, plane, colour, u0, v0, u1, v1 in face_rectangles(voxels):
        u, v = (axis + 1) % 3, (axis + 2) % 3
        points = []
        for a, b in ((u0, v0), (u1, v0), (u1, v1), (u0, v1)):
            p = [0, 0, 0]
            p[axis], p[u], p[v] = plane, a, b
            points.append(tuple(origin[k] + p[k] * scale[k] for k in range(3)) + uv[colour])
        if sign < 0:
            points.reverse()
        shade = 1.0 if axis == 1 and sign > 0 else 0.86 if axis == 2 else 0.72
        result.mesh.poly(points, shade, model.name + ".authored")
    if len(result.mesh.tris) > 2048:
        raise ValueError("authored furniture exceeds its triangle budget")
    result.glass = None
    print("  authored: %s uses %s (%d voxels, %d triangles)" %
          (model.name, os.path.basename(path), len(voxels), len(result.mesh.tris)))
    return result


def replace_table(model, path):
    # Table x82..110, back73, front95; its cell rectangle starts80,64.
    return replace_vox(model, path, (2, 0, 9), (28, 9, 22))


def replace_bookshelf(model, path):
    x, z, _, _ = model.spec["rect"]
    # Against the back wall: top projects onto rows16..24, front to40.
    gx = 112 if model.name == "rustboro_city_flat2_3f_green_bookshelf" else 32
    return replace_vox(model, path, (gx - x * 16, 0, 32 - z * 16), (16, 16, 8))


def replace_display_cabinet(model, path):
    x, z, _, _ = model.spec["rect"]
    return replace_vox(model, path, (160 - x * 16, 0, 32 - z * 16), (32, 20, 8))


def replace_white_console(model, path):
    x, z, _, _ = model.spec["rect"]
    return replace_vox(model, path, (96 - x * 16, 0, 32 - z * 16), (31, 21, 8))


def replace_plant(model, path):
    # Scale to 75% about the pot's floor anchor (x8, z29+1/3), retaining
    # its placement and ground contact in both corners of the room.
    return replace_vox(model, path, (2, 0, 76 / 3), (12, 23.25, 12))


def replace_kitchen_fridge(model, path):
    x, z, _, _ = model.spec["rect"]
    gx = 176 if model.name.startswith("rustboro_city_flat2_1f_") else 128
    return replace_vox(model, path, (gx - x * 16, 0, 32 - z * 16), (16, 24, 8))


def replace_kitchen_sink(model, path):
    x, z, _, _ = model.spec["rect"]
    gx = 192 if model.name.startswith("rustboro_city_flat2_1f_") else 144
    return replace_vox(model, path, (gx - x * 16, 0, 32 - z * 16), (32, 16, 8))


def replace_striped_table(model, path):
    x, z, _, _ = model.spec["rect"]
    gx, gz = (144, 57) if model.name.startswith("rustboro_city_flat2_1f_") else (128, 73)
    return replace_vox(model, path, (gx - x * 16, 0, gz - z * 16), (30, 9, 22))


def room_plants(model, path):
    """Split reused plant placements so only this room gets the new asset."""
    placements = model.spec.get("reused_at", ())
    selected = [p for p in placements if p[0] == "LAYOUT_RUSTBORO_CITY_HOUSE"]
    if not selected:
        return [model]
    remaining = [p for p in placements if p[0] != "LAYOUT_RUSTBORO_CITY_HOUSE"]
    original = copy.copy(model)
    original.spec = dict(model.spec, reused_at=remaining)
    local = copy.copy(model)
    local.name = "rustboro_city_house_potted_plant" + ("_bare" if model.spec.get("bare") else "")
    local.spec = dict(model.spec, name=local.name, reused_at=selected, bare=True)
    return [original, replace_plant(local, path)]


def for_render(models, port):
    replacements = {
        "rustboro_city_house_table": ("yellow_table.vox", replace_table),
        "rustboro_city_house_green_bookshelf": ("green_bookshelf.vox", replace_bookshelf),
        "rustboro_city_house_display_cabinet": ("purple_display_cabinet.vox", replace_display_cabinet),
        "rustboro_city_house_white_console": ("white_console.vox", replace_white_console),
        "rustboro_city_cutters_house_fridge": ("kitchen_fridge.vox", replace_kitchen_fridge),
        "rustboro_city_cutters_house_sink": ("kitchen_sink.vox", replace_kitchen_sink),
        "rustboro_city_cutters_house_table": ("striped_kitchen_table.vox", replace_striped_table),
        "rustboro_city_flat2_1f_fridge": ("kitchen_fridge.vox", replace_kitchen_fridge),
        "rustboro_city_flat2_1f_sink": ("kitchen_sink.vox", replace_kitchen_sink),
        "rustboro_city_flat2_1f_table": ("striped_kitchen_table.vox", replace_striped_table),
        "rustboro_city_flat2_2f_table": ("yellow_table.vox", replace_table),
        "rustboro_city_flat2_3f_green_bookshelf": ("green_bookshelf.vox", replace_bookshelf),
    }
    out = []
    for model in models:
        if model.name in ("rustboro_city_cutters_house_tap", "rustboro_city_flat2_1f_tap"):
            # The authored sink includes its faucet. Keep this source
            # piece's floor ownership/decals, without a second faucet.
            floor = copy.copy(model)
            floor.mesh = vb.Mesh()
            for part in model.prisms:
                if isinstance(part, vb.Decal):
                    part.emit(floor.mesh)
            out.append(floor)
            continue
        if model.name in ("house1_plant_se", "house1_plant_se_bare"):
            out.extend(room_plants(model, os.path.join(port, "assets", "voxel", "props", "potted_plant.vox")))
            continue
        replacement = replacements.get(model.name)
        if replacement:
            filename, replace = replacement
            model = replace(model, os.path.join(port, "assets", "voxel", "props", filename))
        out.append(model)
    return out
