"""Ensure the plan cannot close units with missing, stale or swapped evidence."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/bw2_progress.py'
spec = importlib.util.spec_from_file_location('bw2_progress', SCRIPT)
progress = importlib.util.module_from_spec(spec)
spec.loader.exec_module(progress)


class EvidenceTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        old_root = progress.ROOT
        self.addCleanup(setattr, progress, 'ROOT', old_root)
        progress.ROOT = Path(self.temp.name)
        self.folder = progress.ROOT / 'unit'
        self.item = dict(cartella='unit', id_emerald=277, forme_da_verificare=False,
                         prove={'front': {}, 'back': {}})
        png, video = b'screenshot fixture', b'video fixture'
        ph, vh = hashlib.sha256(png).hexdigest(), hashlib.sha256(video).hexdigest()
        meta = dict(visual_reviewed=True, test_build={'build_id': 'same-build', 'sha256': 'same-binary'}, directions={})
        for name, side in (('front', 1), ('back', 0)):
            folder = self.folder / name
            folder.mkdir(parents=True)
            (folder / 'screenshot.png').write_bytes(png)
            (folder / 'demo.mp4').write_bytes(video)
            (folder / 'shiny.png').write_bytes(png)
            report = dict(passed=True, kind='idle', build_id='same-build', binary_sha256='same-binary',
                          scenario={'player': 277, 'enemy': 277}, screenshot_sha256=ph,
                          video={'sha256': vh})
            (folder / 'capture.json').write_text(json.dumps(report))
            palette = dict(passed=True, build_id='same-build', screenshot_sha256=ph,
                           actors=[{'species': 277, 'battler': side, 'shiny': True}])
            (folder / 'shiny-capture.json').write_text(json.dumps(palette))
            meta['directions'][name] = dict(screenshot_sha256=ph, video_sha256=vh)
        (self.folder / 'metadata.json').write_text(json.dumps(meta))
        (self.folder / 'verifica.md').write_text('Fixture verification')

    def modify_json(self, path, change):
        p = self.folder / path
        data = json.loads(p.read_text())
        change(data)
        p.write_text(json.dumps(data))

    def test_matching_reports_mark_both_views_verified(self):
        progress.check_dossier(self.item, 'pokemon')
        self.assertEqual(self.item['prove']['front']['stato'], 'verificato')
        self.assertEqual(self.item['prove']['back']['build_verificata'], 'same-build')

    def test_changed_video_is_rejected(self):
        (self.folder / 'front/demo.mp4').write_bytes(b'changed bytes')
        with self.assertRaisesRegex(ValueError, 'Video changed'):
            progress.check_dossier(self.item, 'pokemon')

    def test_swapped_species_is_rejected(self):
        self.modify_json('front/capture.json', lambda d: d['scenario'].update(enemy=286))
        with self.assertRaisesRegex(ValueError, 'Wrong Pokemon'):
            progress.check_dossier(self.item, 'pokemon')

    def test_stale_shiny_build_is_rejected(self):
        self.modify_json('back/shiny-capture.json', lambda d: d.update(build_id='old-build'))
        with self.assertRaisesRegex(ValueError, 'Shiny verification'):
            progress.check_dossier(self.item, 'pokemon')

    def test_same_engine_id_with_changed_optional_data_is_rejected(self):
        self.modify_json('front/capture.json', lambda d: d.update(binary_sha256='different-binary'))
        with self.assertRaisesRegex(ValueError, 'Mismatched capture binary'):
            progress.check_dossier(self.item, 'pokemon')

    def test_unreviewed_capture_cannot_be_completed(self):
        self.modify_json('metadata.json', lambda d: d.update(visual_reviewed=False))
        with self.assertRaisesRegex(ValueError, 'Review the actual'):
            progress.check_dossier(self.item, 'pokemon')

    def test_unfinished_forms_block_completion(self):
        item = copy.deepcopy(self.item)
        item['forme_da_verificare'] = True
        with self.assertRaisesRegex(ValueError, 'Forms/personality'):
            progress.check_dossier(item, 'pokemon')


if __name__ == '__main__':
    unittest.main()
