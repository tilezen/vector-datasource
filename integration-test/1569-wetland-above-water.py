# -*- encoding: utf-8 -*-
from . import FixtureTest


class WetlandAboveWaterTest(FixtureTest):

    def test_wetland_above_water(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'natural': 'wetland',
                'wetland': 'bog',
                'source': 'openstreetmap.org',
            }),
            dsl.way(2, dsl.tile_box(z, x, y), {
                'natural': 'water',
                'source': 'openstreetmap.org',
            }),
        )

        # set here for convenience, in case we change them later. the exact
        # values aren't as important as the wetland one being more than the
        # water one.
        wetland_rank = 220
        water_rank = 204

        self.assertTrue(wetland_rank > water_rank)
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 1,
                'kind': 'wetland',
                'sort_rank': wetland_rank,
            })
        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 2,
                'kind': 'water',
                'sort_rank': water_rank,
            })
