# -*- encoding: utf-8 -*-
from . import FixtureTest


class MudTest(FixtureTest):

    def test_mud_sort_rank(self):
        # Mud landuse should sort above water, below wetland
        import dsl

        z, x, y = (16, 0, 0)
        water_sort_rank = 204
        mud_sort_rank = 219
        wetland_sort_rank = 220

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'natural': 'mud',
                'source': 'openstreetmap.org',
            }),
            dsl.way(2, dsl.tile_box(z, x, y), {
                'natural': 'water',
                'source': 'openstreetmap.org',
            }),
            dsl.way(3, dsl.tile_box(z, x, y), {
                'natural': 'wetland',
                'source': 'openstreetmap.org',
            }),
        )

        # first, check the ordering
        self.assertTrue(water_sort_rank < mud_sort_rank)
        self.assertTrue(mud_sort_rank < wetland_sort_rank)

        # now check features match that
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 1,
                'kind': 'mud',
                'sort_rank': mud_sort_rank,
            })

        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 2,
                'kind': 'water',
                'sort_rank': water_sort_rank,
            })

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 3,
                'kind': 'wetland',
                'sort_rank': wetland_sort_rank,
            })
