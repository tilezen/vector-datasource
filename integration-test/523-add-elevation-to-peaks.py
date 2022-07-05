from . import FixtureTest


class AddElevationToPeaks(FixtureTest):
    def test_mt_elbert(self):
        ##
        # A selection of very tall peaks which should be visible at zoom 9.
        ##
        # Mount Elbert, CO
        self.load_fixtures(['http://www.openstreetmap.org/node/358915477'])

        self.assert_has_feature(
            9, 104, 195, 'pois',
            {'kind': 'peak', 'id': 358915477, 'elevation': 4401.2})

    def test_mt_rainier(self):
        # Mount Rainier, WA (volcano)
        self.load_fixtures(['http://www.openstreetmap.org/node/1744903493'])

        self.assert_has_feature(
            9, 82, 180, 'pois',
            {'kind': 'volcano', 'id': 1744903493, 'elevation': 4392})

    def _assert_min_zoom(self, z, x, y, node_id, elevation):
        self.load_fixtures(
            ['https://www.openstreetmap.org/node/%d' % node_id])
        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'peak', 'id': node_id, 'elevation': elevation})
        self.assert_no_matching_feature(
            z-1, x//2, y//2, 'pois',
            {'kind': 'peak', 'id': node_id})

    def test_san_gorgonio(self):
        self._assert_min_zoom(10, 179, 408, 358792071, 3502)

    def test_toro_peak(self):
        self._assert_min_zoom(11, 361, 821, 358793535, 2650)

    def test_ventana_double_cone(self):
        self._assert_min_zoom(12, 663, 1604, 549642731, 1477)

    def test_chamisal_mountain(self):
        self._assert_min_zoom(13, 1274, 3100, 358796064, 785)
