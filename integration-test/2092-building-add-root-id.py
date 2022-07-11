import dsl

from . import FixtureTest


class TestBuildingsAddRootID(FixtureTest):
    def test_add_root_id(self):
        import dsl

        z, x, y = 16, 0, 0

        def test_costco(self):
            import dsl
        z, x, y = (16, 10483, 25332)
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
            {'id': 43100828, 'kind': 'building', 'kind_detail': 'supermarket', 'root_id': 43100828})
