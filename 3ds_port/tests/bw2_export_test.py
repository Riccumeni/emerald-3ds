#!/usr/bin/env python3
"""Format and scope checks for the BW2 prototype exporter; no ROM required."""
import importlib.util
import hashlib
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from PIL import Image

SCRIPT=Path(__file__).resolve().parents[1]/'scripts/gen_bw2_battle.py'
spec=importlib.util.spec_from_file_location('bw2_export',SCRIPT)
bw=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=bw
spec.loader.exec_module(bw)


class ExportTest(unittest.TestCase):
    def test_nearest_parts_cover_body_but_keep_transparent_holes(self):
        eye = Image.new('P', (2, 2)); eye.putpixel((0, 0), 3)
        body = Image.new('P', (2, 2), 7)
        image = bw.composite_parts([(eye, (1, 0, 0, 0, 1, 0)),
                                    (body, (1, 0, 0, 0, 1, 0))], (2, 2))
        self.assertEqual(list(image.tobytes()), [3, 7, 7, 7])

    def test_shared_controller_uses_first_node_sequence(self):
        first = (2, 0, 1., 1., 0, 0)
        other = (9, 0, 1., 1., 0, 0)
        cells = [bw.Sequence([(4, first)], 0, 2), bw.Sequence([(4, other)], 0, 2)]
        self.assertEqual(bw.cell_poses([(0, 0, 0, 0), (1, 0, 0, 0)], cells, 0, 0),
                         [first, first])

    def test_scope(self):
        self.assertEqual(set(bw.SPECIES),{252,261})
        self.assertEqual(set(bw.MOVES),{1,33,43,336})

    def test_move_catalog_covers_emerald(self):
        catalog=json.loads((SCRIPT.parents[1]/'data/bw2_moves.json').read_text())
        self.assertEqual(set(map(int,catalog)),set(range(1,355)))
        self.assertEqual(catalog['10']['name'],'scratch')
        self.assertEqual(catalog['45']['name'],'growl')

    def test_selected_move_export_keeps_existing_entries(self):
        script=struct.pack('<15IH',1,*([60]*14),77)
        nds=SimpleNamespace(data=b'local-rom',code='TEST',archive=lambda path: {10:script} if path=='a/0/6/5' else [])
        with tempfile.TemporaryDirectory() as folder:
            output=Path(folder)
            (output/'manifest.json').write_text(json.dumps({'rom_sha256':hashlib.sha256(nds.data).hexdigest(),
                'canvas':[64,64],'pokemon':{},'moves':{'1':{'name':'pound'}},'effects':{}}))
            with patch.object(bw,'Nds',return_value=nds):
                report=bw.generate('unused.nds',output,species={},moves={10:'scratch'})
            self.assertEqual(set(report['moves']),{'1','10'})
            self.assertEqual((output/'move_10.bin').read_bytes(),script)
            self.assertFalse((output/'move_1.bin').exists())

    def test_national_catalog_preserves_emerald_ids_and_excludes_placeholders(self):
        catalog=json.loads((SCRIPT.parents[1]/'data/bw2_species.json').read_text())
        self.assertEqual(set(map(int,catalog)),set(range(1,387)))
        ids={v['emerald'] for v in catalog.values()}
        self.assertEqual(ids,set(range(1,252))|set(range(277,412)))
        self.assertEqual(catalog['252'],{'emerald':277,'name':'treecko'})
        self.assertEqual(catalog['253'],{'emerald':278,'name':'grovyle'})
        self.assertEqual(catalog['261'],{'emerald':286,'name':'poochyena'})

    def test_incremental_export_refuses_another_rom_before_writing_assets(self):
        with tempfile.TemporaryDirectory() as folder:
            output=Path(folder)
            manifest=output/'manifest.json'
            original=json.dumps({'rom_sha256':hashlib.sha256(b'other').hexdigest(),'canvas':[64,64]})
            manifest.write_text(original)
            with patch.object(bw,'Nds',return_value=SimpleNamespace(data=b'source',code='TEST')):
                with self.assertRaisesRegex(ValueError,'another ROM'):
                    bw.generate('unused.nds',output,species={})
            self.assertEqual(manifest.read_text(),original)
            self.assertEqual(list(output.glob('*.bin')),[])

    def test_lz10_back_reference(self):
        self.assertEqual(bw.decompress(bytes.fromhex('10 06 00 00 10 61 62 63 00 02')),b'abcabc')

    def test_lz11_back_reference(self):
        self.assertEqual(bw.decompress(bytes.fromhex('11 06 00 00 10 61 62 63 20 02')),b'abcabc')

    def test_bad_lz_back_reference(self):
        with self.assertRaises(ValueError):
            bw.decompress(bytes.fromhex('10 03 00 00 80 00 02'))

    def test_move_rejects_unknown_opcode(self):
        with self.assertRaises(ValueError):
            bw.decode_script(struct.pack('<15IH',1,*([60]*14),78))

    def test_move_rejects_jump_into_argument(self):
        body=struct.pack('<H4iH',59,19,0,1,1,77)
        with self.assertRaises(ValueError):
            bw.decode_script(struct.pack('<15I',1,*([60]*14))+body)

    def test_move_rejects_missing_end(self):
        with self.assertRaises(ValueError):
            bw.decode_script(struct.pack('<15IHi',1,*([60]*14),56,0))

    def test_tile_order_and_deduplication(self):
        a=Image.new('P',(64,64));a.putpixel((8,0),3);a.putpixel((9,0),4)
        b=a.copy();b.putpixel((0,8),5)
        self.assertEqual(bw.tiles(a)[32],0x43)
        self.assertEqual(bw.tiles(b)[256],5)
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'clip.bin'
            bw.write_clip(p,[a,b,a],bytes(32),loop=1)
            data=p.read_bytes()
            self.assertEqual(struct.unpack_from('<4s6I',data),(b'BWA1',2,3,1,64,64,60))
            self.assertEqual(struct.unpack_from('<3H',data,92),(0,1,0))
            self.assertEqual(len(data),100+4096)

    def test_procedural_uv_frames_are_not_deduplicated_by_base_pixels(self):
        a=Image.new('P',(64,64),1);uv=Image.new('I',(64,64));uv.putpixel((2,3),1)
        other=uv.copy();other.putpixel((2,3),2)
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'clip.bin'
            bw.write_clip(p,[a,a,a],bytes(32),uv_frames=[uv,other,uv])
            self.assertEqual(struct.unpack_from('<3H',p.read_bytes(),92),(0,1,0))
            sidecar=p.with_suffix('.bin.spots').read_bytes()
            self.assertEqual(struct.unpack_from('<4sI',sidecar),(b'BWS1',2))
            offsets=struct.unpack_from('<3I',sidecar,152)
            self.assertEqual(offsets[-1],len(sidecar))
            self.assertEqual(struct.unpack_from('<HH',sidecar,offsets[0]),(26,0))
            self.assertEqual(struct.unpack_from('<HH',sidecar,offsets[1]),(26,1))

    def test_spinda_overlap_is_a_union_and_extreme_y_is_clipped(self):
        atlas=Image.new('P',(256,128),1)
        marked=bw.spinda_texture(atlas,0x808f8888)
        self.assertEqual(set(marked.tobytes()),{1,6})
        extreme=bw.spinda_texture(atlas,0)
        self.assertEqual(list(extreme.crop((0,120,256,128)).tobytes()),[1]*(256*8))
        # An opaque foreground quad must cover the UV labels of parts behind it.
        body=Image.new('I',(2,2),13);cover=Image.new('I',(2,2));cover.putpixel((0,0),65535)
        out=bw.composite_parts([(cover,(1,0,0,0,1,0)),(body,(1,0,0,0,1,0))],(2,2))
        self.assertEqual(list(out.get_flattened_data()),[65535,13,13,13])

    def test_source_footprint_preserves_native_dimensions(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'clip.bin.layout'
            bw.write_layout(p,(46,25,146,97),(48,25,150,95))
            self.assertEqual(struct.unpack('<4s4H',p.read_bytes()),(b'BWL2',100,72,102,70))
            with self.assertRaises(ValueError):bw.write_layout(p,(0,0,193,10))
            with self.assertRaises(ValueError):bw.write_layout(p,(4,4,4,10))

    def test_incremental_migration_keeps_pixels_and_pairs_source_views(self):
        nds=SimpleNamespace(data=b'local-rom',code='TEST',archive=lambda path: [])
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)
            clips={'300_front':{'source_bounds':[46,25,146,97]},
                   '300_back':{'source_bounds':[48,25,150,95]}}
            (output/'manifest.json').write_text(json.dumps({'rom_sha256':hashlib.sha256(nds.data).hexdigest(),
                'canvas':[64,64],'pokemon':clips,'moves':{},'effects':{},'forms':{'385':{'1':{'name':'sunny','resource_base':14240}}}}))
            (output/'300_front.bin').write_bytes(b'original-pixels')
            with patch.object(bw,'Nds',return_value=nds):bw.generate('unused.nds',output,species={},moves={})
            self.assertEqual((output/'300_front.bin').read_bytes(),b'original-pixels')
            self.assertEqual(json.loads((output/'manifest.json').read_text())['forms']['385']['1']['name'],'sunny')
            self.assertEqual(struct.unpack('<4s4H',(output/'300_front.bin.layout').read_bytes()),(b'BWL2',100,72,102,70))
            self.assertEqual(struct.unpack('<4s4H',(output/'300_back.bin.layout').read_bytes()),(b'BWL2',102,70,100,72))


    def test_deoxys_exports_only_emerald_normal_and_speed_views(self):
        personal=bytearray(44);struct.pack_into('<HBB',personal,30,30,4,0)
        members=[None]*15065
        nds=SimpleNamespace(data=b'local-rom',code='TEST',archive=lambda path: members if path=='a/0/0/4' else [personal]*387 if path=='a/0/1/6' else [])
        image=Image.new('P',(64,64),1)
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)
            with patch.object(bw,'Nds',return_value=nds),patch.object(bw,'palette',return_value=bytes(32)),patch.object(bw,'pokemon_frames',return_value=([image],0,(32,32,96,96))) as frames:
                report=bw.generate('unused.nds',output,species={386:(410,'deoxys')},moves={})
            self.assertEqual(set(report['pokemon']),{'410_front','410_back','410_form3_front','410_form3_back'})
            self.assertEqual(report['forms']['410']['3']['resource_base'],0x3584+32*20)
            self.assertEqual(report['forms']['410']['excluded']['forms'],['attack','defense'])
            self.assertEqual([call.kwargs.get('base_override') for call in frames.call_args_list],[None,None,0x3584+32*20,0x3584+32*20])
            for side in ['front','back']:
                self.assertTrue((output/f'410_form3_{side}.bin.layout').exists())
            # Incremental exports keep the complete Deoxys form inventory.
            with patch.object(bw,'Nds',return_value=nds):
                again=bw.generate('unused.nds',output,species={},moves={})
            self.assertEqual(again['forms'],report['forms'])

    def test_deoxys_rejects_unknown_rom_form_mapping(self):
        personal=bytearray(44);struct.pack_into('<HBB',personal,30,30,3,0)
        nds=SimpleNamespace(data=b'local-rom',code='TEST',archive=lambda path: [None]*15065 if path=='a/0/0/4' else [personal]*387 if path=='a/0/1/6' else [])
        image=Image.new('P',(64,64),1)
        with tempfile.TemporaryDirectory() as directory,patch.object(bw,'Nds',return_value=nds),patch.object(bw,'palette',return_value=bytes(32)),patch.object(bw,'pokemon_frames',return_value=([image],0,(32,32,96,96))):
            with self.assertRaisesRegex(ValueError,'Unexpected Deoxys'):
                bw.generate('unused.nds',Path(directory),species={386:(410,'deoxys')},moves={})


if __name__=='__main__':unittest.main()
