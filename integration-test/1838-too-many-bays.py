# -*- encoding: utf-8 -*-
from . import FixtureTest


class BayTest(FixtureTest):

    def test_bays(self):
        import dsl

        z, x, y = 8, 0, 0

        def _bay(osm_id, area, name):
            return dsl.way(osm_id, dsl.box_area(z, x, y, area), {
                'source': 'openstreetmap.org',
                'natural': 'bay',
                'name': name,
            })

        # generate some bays - the IDs are out of order, but should get
        # reordered before the rank is assigned.
        self.generate_fixtures(
            _bay(3, 200000000, "Bay 5"),
            _bay(9, 70000000, "Bay 9"),
            _bay(5, 400000000, "Bay 3"),
            _bay(4, 300000000, "Bay 4"),
            _bay(1, 90000000, "Bay 7"),
            _bay(2, 100000000, "Bay 6"),
            _bay(8, 80000000, "Bay 8"),
            _bay(10, 600000000, "Bay 1"),
            _bay(11, 500000000, "Bay 2"),
            _bay(6, 60000000, "Bay 10"),
            _bay(7, 50000000, "Bay 11"),
        )

        with self.features_in_tile_layer(z, x, y, 'water') as features:
            # should only have top 10 features
            self.assertEqual(10, len(features))

            # check that they're in order
            ranks = [f['properties']['kind_tile_rank'] for f in features]
            self.assertEqual(range(1, 11), ranks)
