# -*- encoding: utf-8 -*-
from . import FixtureTest


class NEroadtoll(FixtureTest):

    def test_ne_road_toll(self):
        import dsl

        z, x, y = (5, 5, 12)

        self.generate_fixtures(
            # Natural Earth sample, fake 101 toll road in California
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'scalerank': 4.0,
                'featurecla': 'Road',
                'type': 'Major Highway',
                'name': '101',
                'toll': 1,
                'continent': 'North America',
                'expressway': 0,
                'level': 'Federal',
                'min_zoom': 4.0,
                'min_label': 7.0,
                'source': u'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 1,
                'kind': u'major_road',
                'toll': True,
            })
