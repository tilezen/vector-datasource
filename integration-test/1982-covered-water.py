# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads
from tilequeue.tile import deg2num
from . import FixtureTest

class CoveredWaterOSMTest(FixtureTest):
    def test_water_level_1(self):
        z, x, y = (16, 33199, 22547)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/236735251
            dsl.way(236735251, dsl.tile_box(z, x, y), {
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
            {"id": 236735251})
