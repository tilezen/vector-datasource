# -*- encoding: utf-8 -*-
import dsl

from . import FixtureTest


class UndergroundWaterTest(FixtureTest):
    def test_water_level_1(self):
        z, x, y = (16, 33199, 22547)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/236735251
            dsl.way(236735251, dsl.tile_box(z, x, y), {
                'layer': '-1',
                'name': u'Vo\xfbte Richard Lenoir',
                'source': 'openstreetmap.org',
                'tunnel': 'yes',
                'waterway': 'riverbank',
            }),
        )

        self.assert_has_feature(
            16, 33199, 22547, 'water',
            {'kind': 'riverbank', 'id': 236735251,
             'name': 'Voûte Richard Lenoir', 'is_tunnel': True,
             'sort_rank': 9})

    def test_water_level_2(self):
        z, x, y = (16, 33504, 22442)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/94321616
            dsl.way(94321616, dsl.tile_box(z, x, y), {
                'layer': '-2',
                'source': 'openstreetmap.org',
                'tunnel': 'yes',
                'waterway': 'riverbank',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 94321616,
                'kind': 'riverbank', 'is_tunnel': True, 'sort_rank': 8})

    def test_pedestrian(self):
        z, x, y = (16, 33199, 22546)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/115027186
            dsl.way(115027186, dsl.tile_box(z, x, y), {
                'highway': 'pedestrian',
                'source': 'openstreetmap.org',
                'area': 'yes',
                'type': 'polygon',
            }),
            dsl.relation(1602299, {
                'area': 'yes',
                'bicycle': 'no',
                'highway': 'pedestrian',
                'source': 'openstreetmap.org',
                'name': 'Esplanade Roger Joseph Boscovich',
                'type': 'polygon',
            }, ways=[115027186])
        )

        self.assert_has_feature(
            z, x, y, 'landuse',
            {'kind': 'pedestrian', 'id': 115027186,
                     'sort_rank': 110})

    def test_garden(self):
        z, x, y = (16, 33199, 22546)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/115027177
            dsl.way(115027177, dsl.tile_box(z, x, y), {
                'leisure': 'garden',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse',
            {'kind': 'garden', 'id': 115027177,
             'sort_rank': 112})
