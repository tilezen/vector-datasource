from . import FixtureTest


class BicycleRouteRefs(FixtureTest):

    def test_lcn45(self):
        import dsl

        z, x, y = (16, 10481, 25336)

        self.generate_fixtures(
            dsl.way(417389551, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'highway': 'tertiary',
                'cycleway': 'lane',
                'lcn_ref': '45',
            }),
            dsl.relation(32310, {
                'type': 'route',
                'route': 'bicycle',
                'network': 'lcn',
                'ref': '45',
            }, ways=[417389551]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 417389551,
             'bicycle_network': None,
             'bicycle_shield_text': '45',
             'all_bicycle_networks': None,
             'all_bicycle_shield_texts': ['45']})

        # make sure the properties are gone by zoom 15
        self.assert_no_matching_feature(
            z-1, x//2, y//2, 'roads',
            {'all_bicycle_networks': None})

        self.assert_no_matching_feature(
            z-1, x//2, y//2, 'roads',
            {'all_bicycle_shield_texts': None})
