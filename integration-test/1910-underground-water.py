# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class UndergroundWaterTest(FixtureTest):
    def test_water_level_1(self):
        z, x, y = (16, 33199, 22547)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/236735251
            dsl.way(236735251, dsl.tile_diagonal(z, x, y), {
                'layer': '-1',
                'name': u'Vo\xfbte Richard Lenoir',
                'source': 'openstreetmap.org',
                'tunnel': 'yes',
                'waterway': 'riverbank',
            }),
        )

        # tunnels at level = 0
        self.assert_has_feature(
            16, 33199, 22547, "water",
            {"kind": "riverbank", "id": 236735251,
             "name": "Voûte Richard Lenoir", "is_tunnel": True, "sort_rank": 9})

    def test_water_level_2(self):
        z, x, y = (16, 33504, 22442)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/94321616
            dsl.way(94321616, dsl.tile_diagonal(z, x, y), {
                'layer': '-2',
                'source': 'openstreetmap.org',
                'tunnel': 'yes',
                'waterway': 'riverbank',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 94321616,
                "kind": "riverbank", "is_tunnel": True, "sort_rank": 8})

    def test_pedestrian(self):
        z, x, y = (16, 33199, 22546)

        # self.generate_fixtures(
        #     # https://www.openstreetmap.org/way/4040012
        #     dsl.way(4040012, dsl.tile_diagonal(z, x, y), {
        #         'highway': 'residential',
        #         'lit': 'yes',
        #         'name': 'Esplanade Roger Joseph Boscovich',
        #         'oneway': 'yes',
        #         'sidewalk': 'both',
        #         'source': 'openstreetmap.org',
        #         'surface': 'asphalt',
        #     }),
        # )

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/115027193
            dsl.way(115027193, dsl.tile_diagonal(z, x, y), {
                'area': 'yes',
                'bicycle': 'no',
                'highway': 'pedestrian',
                'lit': 'yes',
                'noname': 'yes',
                'source': 'openstreetmap.org',
                'surface': 'asphalt',
            }),
        )

        self.assert_has_feature(
                    z, x, y, "roads",
                    {"kind": "path", "id": 115027193,
                     "sort_rank": 354})

    def test_garden(self):
        z, x, y = (16, 33199, 22546)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/115027177
            dsl.way(115027177, dsl.tile_diagonal(z, x, y), {
                'leisure': 'garden',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
                z, x, y, "landuse",
                {"kind": "garden", "id": 115027177,
                 "sort_rank": 112})