# -*- encoding: utf-8 -*-
import dsl

from . import FixtureTest


class CoveredWaterOSMTest(FixtureTest):
    def test_water_level_1(self):
        z, x, y = (16, 33199, 22547)

        self.generate_fixtures(
            # to represent https://www.openstreetmap.org/way/28575415
            dsl.way(28575415, dsl.tile_box(z, x, y), {
                'covered': 'yes',
                'name': u'Sutro Reservoir',
                'source': 'openstreetmap.org',
                'man_made': 'reservoir_covered',
                'water': 'reservoir',
                'natural': 'water',
            }),
        )

        self.assert_no_matching_feature(
            16, 33199, 22547, 'water',
            {'id': 28575415})
