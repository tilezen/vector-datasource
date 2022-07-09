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
        import dsl
        z, x, y = (16, 10482, 25332)
        # https://www.openstreetmap.org/way/25821952
        self.generate_fixtures(
            dsl.way(25821952, dsl.tile_box(z, x, y), {
                'name': 'Foods Co', 'building': 'yes',
                'opening_hours': '06:00-01:00', 'shop': 'supermarket',
                'source': 'openstreetmap.org'
            })
        )

        self.assert_has_feature(
            z, x, y, 'buildings',
            {'id': 25821952, 'kind': 'building', 'kind_detail': 'supermarket'})

    def test_costco(self):
        import dsl
        z, x, y = (16, 10483, 25332)
        # https://www.openstreetmap.org/way/43100828
        self.generate_fixtures(
            dsl.way(43100828, dsl.tile_box(z, x, y), {
                'name': 'Costco', 'addr:city': 'San Francisco',
                'addr:housenumber': '450', 'addr:postcode': '94103',
                'addr:state': 'CA', 'addr:street': '10th Street', 'building': 'yes',
                'shop': 'supermarket', 'wheelchair': 'yes', 'source': 'openstreetmap.org'
            })
        )

        self.assert_has_feature(
            z, x, y, 'buildings',
            {'id': 43100828, 'kind': 'building', 'kind_detail': 'supermarket'})
