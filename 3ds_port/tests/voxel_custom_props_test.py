"""Authored furniture: VOX palette, complete exposed surface, legs and bounds."""
import collections
import pathlib
import sys
import unittest

from PIL import Image

PORT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PORT / "scripts"))
import voxel_building as vb
import voxel_custom_props as props


class AuthoredTableTest(unittest.TestCase):
    def setUp(self):
        self.path = str(PORT / "assets/voxel/props/yellow_table.vox")
        self.dims, self.voxels, self.palette = props.read_vox(self.path)

    def test_source_palette_and_open_legs(self):
        self.assertEqual(self.dims, (40, 28, 32))
        self.assertEqual(len(self.voxels), 8384)
        self.assertEqual(self.palette[4], (255, 248, 138, 255))
        self.assertEqual(self.palette[1], (140, 105, 52, 255))
        self.assertNotIn((20, 0, 16), self.voxels)
        self.assertNotIn((20, 17, 16), self.voxels)
        self.assertIn((20, 27, 16), self.voxels)
        for x in (3, 35):
            for z in (3, 27):
                self.assertIn((x, 0, z), self.voxels)

    def test_merged_faces_cover_exactly_the_exposed_surface(self):
        expected = collections.Counter()
        for p, colour in self.voxels.items():
            for axis in range(3):
                for sign in (-1, 1):
                    q = list(p)
                    q[axis] += sign
                    if tuple(q) not in self.voxels:
                        expected[axis, sign, colour] += 1
        actual = collections.Counter()
        rectangles = list(props.face_rectangles(self.voxels))
        for axis, sign, plane, colour, u0, v0, u1, v1 in rectangles:
            actual[axis, sign, colour] += (u1 - u0) * (v1 - v0)
        self.assertEqual(actual, expected)
        self.assertLess(len(rectangles) * 2, 2048)

    def test_import_is_local_and_preserves_the_original_model(self):
        model = vb.Model("rustboro_city_house_table", Image.new("RGBA", (32, 100)), [], (2, 2), 0x32c)
        result = props.replace_table(model, self.path)
        points = [v for tri, shade, tag in result.mesh.tris for v in tri]
        self.assertEqual([min(v[k] for v in points) for k in range(3)], [2, 0, 9])
        self.assertEqual([max(v[k] for v in points) for k in range(3)], [30, 9, 31])
        self.assertEqual(model.mesh.tris, [])
        self.assertEqual(model.art.size, (32, 100))
        for v in points:
            self.assertGreaterEqual(result.art.getpixel((int(v[3]), int(v[4])))[3], 128)


class AuthoredBookshelfTest(unittest.TestCase):
    def setUp(self):
        self.path = str(PORT / "assets/voxel/props/green_bookshelf.vox")
        self.dims, self.voxels, self.palette = props.read_vox(self.path)

    test_merged_faces_cover_exactly_the_exposed_surface = (
        AuthoredTableTest.test_merged_faces_cover_exactly_the_exposed_surface)

    def test_books_are_separate_in_a_recessed_shelf(self):
        self.assertEqual(self.dims, (24, 28, 12))
        self.assertEqual(self.palette[3], (164, 205, 106, 255))
        self.assertEqual(self.palette[6], (213, 197, 74, 255))
        self.assertNotIn((8, 18, 8), self.voxels)
        self.assertNotIn((5, 18, 11), self.voxels)
        self.assertIn((5, 18, 8), self.voxels)
        self.assertIn((8, 18, 0), self.voxels)
        self.assertIn((8, 12, 5), self.voxels)

    def test_fit_stands_against_the_wall(self):
        model = vb.Model("rustboro_city_house_green_bookshelf",
                         Image.new("RGBA", (16, 100)), [], (1, 2), 0x32c)
        model.spec = {"rect": (2, 1, 1, 2)}
        result = props.replace_bookshelf(model, self.path)
        points = [v for tri, shade, tag in result.mesh.tris for v in tri]
        self.assertEqual([min(v[k] for v in points) for k in range(3)], [0, 0, 16])
        self.assertEqual([max(v[k] for v in points) for k in range(3)], [16, 16, 24])
        self.assertEqual(model.mesh.tris, [])


class AuthoredDisplayCabinetTest(unittest.TestCase):
    def setUp(self):
        self.path = str(PORT / "assets/voxel/props/purple_display_cabinet.vox")
        self.dims, self.voxels, self.palette = props.read_vox(self.path)

    test_merged_faces_cover_exactly_the_exposed_surface = (
        AuthoredTableTest.test_merged_faces_cover_exactly_the_exposed_surface)

    def test_glazing_is_recessed_behind_the_frame(self):
        self.assertEqual(self.dims, (40, 36, 14))
        self.assertEqual(self.palette[7], (189, 189, 246, 255))
        self.assertNotIn((10, 20, 12), self.voxels)
        self.assertIn((10, 20, 11), self.voxels)
        self.assertIn((19, 20, 13), self.voxels)
        self.assertIn((10, 6, 13), self.voxels)

    def test_fit_in_the_east_corner(self):
        model = vb.Model("rustboro_city_house_display_cabinet",
                         Image.new("RGBA", (32, 120)), [], (2, 3), 0x32c)
        model.spec = {"rect": (10, 0, 2, 3)}
        result = props.replace_display_cabinet(model, self.path)
        points = [v for tri, shade, tag in result.mesh.tris for v in tri]
        self.assertEqual([min(v[k] for v in points) for k in range(3)], [0, 0, 32])
        self.assertEqual([max(v[k] for v in points) for k in range(3)], [32, 20, 40])


class AuthoredWhiteConsoleTest(unittest.TestCase):
    def setUp(self):
        self.path = str(PORT / "assets/voxel/props/white_console.vox")
        self.dims, self.voxels, self.palette = props.read_vox(self.path)

    test_merged_faces_cover_exactly_the_exposed_surface = (
        AuthoredTableTest.test_merged_faces_cover_exactly_the_exposed_surface)

    def test_upright_white_panel_controls_and_feet(self):
        self.assertEqual(self.dims, (40, 24, 12))
        self.assertEqual(self.palette[4], (255, 255, 255, 255))
        self.assertEqual(self.voxels[20, 17, 10], 4)
        self.assertEqual(self.voxels[27, 5, 11], 7)
        self.assertIn((3, 0, 2), self.voxels)
        self.assertNotIn((20, 0, 6), self.voxels)

    def test_fit_beside_the_television(self):
        model = vb.Model("rustboro_city_house_white_console",
                         Image.new("RGBA", (32, 100)), [], (2, 2), 0x32c)
        model.spec = {"rect": (6, 1, 2, 2)}
        result = props.replace_white_console(model, self.path)
        points = [v for tri, shade, tag in result.mesh.tris for v in tri]
        self.assertEqual([min(v[k] for v in points) for k in range(3)], [0, 0, 16])
        self.assertEqual([max(v[k] for v in points) for k in range(3)], [31, 21, 24])


class AuthoredPlantTest(unittest.TestCase):
    def setUp(self):
        self.path = str(PORT / "assets/voxel/props/potted_plant.vox")
        self.dims, self.voxels, self.palette = props.read_vox(self.path)

    test_merged_faces_cover_exactly_the_exposed_surface = (
        AuthoredTableTest.test_merged_faces_cover_exactly_the_exposed_surface)

    def test_solid_crown_open_pot_and_soil(self):
        self.assertEqual(self.dims, (24, 48, 24))
        self.assertIn(self.voxels[12, 47, 12], (4, 5))
        self.assertEqual(self.voxels[8, 8, 8], 13)
        self.assertEqual(self.voxels[4, 11, 8], 9)
        self.assertNotIn((8, 11, 8), self.voxels)
        self.assertIn((12, 20, 8), self.voxels)
        self.assertLessEqual(len(list(props.face_rectangles(self.voxels))) * 2, 512)

    def test_reuse_is_split_without_changing_other_rooms(self):
        model = vb.Model("house1_plant_se_bare", Image.new("RGBA", (16, 100)), [], (1, 2), 0x223)
        selected = [("LAYOUT_RUSTBORO_CITY_HOUSE", 0, 7, None),
                    ("LAYOUT_RUSTBORO_CITY_HOUSE", 11, 7, None)]
        other = [("LAYOUT_HOUSE2", 10, 6, None)]
        model.spec = {"bare": True, "reused_at": selected + other}
        original, local = props.room_plants(model, self.path)
        self.assertEqual(original.spec["reused_at"], other)
        self.assertEqual(local.spec["reused_at"], selected)
        self.assertEqual(model.spec["reused_at"], selected + other)
        self.assertEqual(model.mesh.tris, [])
        points = [v for tri, shade, tag in local.mesh.tris for v in tri]
        self.assertEqual(max(v[1] for v in points), 23.25)
        self.assertEqual(min(v[1] for v in points), 0)
        self.assertTrue(all(2 <= v[0] <= 14 and 76 / 3 <= v[2] <= 112 / 3 for v in points))


class KitchenFridgeTest(unittest.TestCase):
    def setUp(self):
        self.path = str(PORT / "assets/voxel/props/kitchen_fridge.vox")
        self.dims, self.voxels, self.palette = props.read_vox(self.path)

    test_merged_faces_cover_exactly_the_exposed_surface = (
        AuthoredTableTest.test_merged_faces_cover_exactly_the_exposed_surface)

    def test_doors_handles_and_feet(self):
        self.assertEqual(self.dims, (24, 40, 16))
        self.assertEqual(self.voxels[10, 31, 14], 4)
        self.assertEqual(self.voxels[10, 20, 14], 3)
        self.assertEqual(self.voxels[4, 20, 15], 1)
        self.assertIn((3, 0, 2), self.voxels)
        self.assertNotIn((12, 0, 6), self.voxels)


class KitchenSinkTest(unittest.TestCase):
    def setUp(self):
        self.path = str(PORT / "assets/voxel/props/kitchen_sink.vox")
        self.dims, self.voxels, self.palette = props.read_vox(self.path)

    test_merged_faces_cover_exactly_the_exposed_surface = (
        AuthoredTableTest.test_merged_faces_cover_exactly_the_exposed_surface)

    def test_open_basin_raised_faucet_and_hob(self):
        self.assertEqual(self.dims, (48, 32, 20))
        self.assertNotIn((12, 15, 10), self.voxels)
        self.assertNotIn((12, 13, 10), self.voxels)
        self.assertEqual(self.voxels[12, 11, 10], 9)
        self.assertEqual(self.voxels[12, 29, 8], 2)
        self.assertEqual(self.voxels[37, 16, 11], 2)
        self.assertEqual(self.voxels[22, 8, 19], 1)


class StripedKitchenTableTest(unittest.TestCase):
    def setUp(self):
        self.path = str(PORT / "assets/voxel/props/striped_kitchen_table.vox")
        self.dims, self.voxels, self.palette = props.read_vox(self.path)

    test_merged_faces_cover_exactly_the_exposed_surface = (
        AuthoredTableTest.test_merged_faces_cover_exactly_the_exposed_surface)

    def test_stripes_run_front_to_back_over_four_open_legs(self):
        self.assertNotEqual(self.voxels[4, 27, 10], self.voxels[8, 27, 10])
        self.assertEqual(self.voxels[8, 27, 10], self.voxels[8, 27, 20])
        self.assertNotIn((20, 0, 16), self.voxels)
        for x in (3, 35):
            for z in (3, 27):
                self.assertIn((x, 0, z), self.voxels)


class ActualFlat2PlacementTest(unittest.TestCase):
    def test_third_floor_green_bookshelf_uses_volume_at_its_own_coordinates(self):
        model = vb.Model("rustboro_city_flat2_3f_green_bookshelf",
                         Image.new("RGBA", (16, 140)), [], (1, 2), 0x32c)
        model.spec = {"rect": (7, 1, 1, 2)}
        result, = props.for_render([model], str(PORT))
        points = [v for tri, shade, tag in result.mesh.tris for v in tri]
        self.assertTrue(points)
        self.assertEqual((min(v[0] for v in points) + 112, max(v[0] for v in points) + 112), (112, 128))
        self.assertEqual((min(v[2] for v in points) + 16, max(v[2] for v in points) + 16), (32, 40))
        self.assertEqual(max(v[1] for v in points), 16)
        self.assertEqual(model.mesh.tris, [])

    def test_second_floor_yellow_table_keeps_its_actual_room_coordinates(self):
        model = vb.Model("rustboro_city_flat2_2f_table", Image.new("RGBA", (32, 140)), [], (2, 2), 0x32c)
        model.spec = {"rect": (12, 3, 2, 2)}
        result, = props.for_render([model], str(PORT))
        points = [v for tri, shade, tag in result.mesh.tris for v in tri]
        self.assertEqual((min(v[0] for v in points) + 192, max(v[0] for v in points) + 192), (194, 222))
        self.assertEqual((min(v[2] for v in points) + 48, max(v[2] for v in points) + 48), (57, 79))
        self.assertEqual(max(v[1] for v in points), 9)
        self.assertEqual(model.mesh.tris, [])

    def test_running_rooms_names_select_the_three_authored_assets(self):
        cases = [("fridge", (11, 0, 1, 3), 24, 16),
                 ("sink", (12, 1, 2, 2), 16, 32),
                 ("table", (9, 3, 2, 2), 9, 30)]
        for name, rect, height, width in cases:
            with self.subTest(name=name):
                model = vb.Model("rustboro_city_flat2_1f_" + name,
                                 Image.new("RGBA", (32, 140)), [], rect[2:], 0x32c)
                model.spec = {"rect": rect}
                result, = props.for_render([model], str(PORT))
                points = [v for tri, shade, tag in result.mesh.tris for v in tri]
                self.assertTrue(points, "actual Flat2 placement must receive authored geometry")
                self.assertEqual(max(v[1] for v in points), height)
                self.assertEqual(max(v[0] for v in points), width)
                self.assertEqual(min(v[0] for v in points), 0)
                self.assertEqual(model.mesh.tris, [])


if __name__ == "__main__":
    unittest.main()
