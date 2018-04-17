from . import FixtureTest


class FencesWalls(FixtureTest):

    def test_long_wall(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/295483721'])

        self.assert_has_feature(
            16, 10465, 25331, 'landuse',
            {'id': 295483721, 'kind': 'wall', 'min_zoom': 16})

    def test_wall_kind_detail_from_wall_col(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/526327448'])

        self.assert_has_feature(
            16, 10576, 25471, 'landuse',
            {'id': 526327448, 'kind': 'wall', 'kind_detail': 'dry_stone',
             'min_zoom': 16})

    def test_fence_kind_detail_from_fence_type_col(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/231049157'])

        self.assert_has_feature(
            16, 10556, 25335, 'landuse',
            {'id': 231049157, 'kind': 'fence', 'kind_detail': 'barbed_wire',
             'min_zoom': 16})
