from . import FixtureTest


class BuildingKindDetail(FixtureTest):

    def _assert_kind_detail(self, way_id, tile, kind_detail):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/%d' % (way_id,),
        ])

        z, x, y = map(int, tile.split('/'))
        self.assert_has_feature(
            z, x, y, 'buildings',
            {'id': way_id, 'kind': 'building', 'kind_detail': kind_detail})

    def test_whole_foods(self):
        self._assert_kind_detail(194906343, '16/10480/25336', 'supermarket')

    def test_foods_co(self):
        self._assert_kind_detail(25821952, '16/10482/25332', 'supermarket')

    def test_costco(self):
        self._assert_kind_detail(43100828, '16/10483/25332', 'supermarket')
