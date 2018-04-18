from . import FixtureTest


class TestCranes(FixtureTest):

    def test_crane_landuse_line(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/173458931'])

        self.assert_has_feature(
            16, 32891, 21813, 'landuse',
            {'id': 173458931, 'kind': 'crane', 'min_zoom': 16,
             'sort_rank': 271})

    def test_crane_pois(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/1842715058'])

        self.assert_has_feature(
            16, 32891, 21813, 'pois',
            {'id': 1842715058, 'kind': 'crane', 'min_zoom': 16})
