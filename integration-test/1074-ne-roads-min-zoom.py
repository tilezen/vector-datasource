# -*- encoding: utf-8 -*-
from . import FixtureTest


class NEroadminzoom(FixtureTest):

    def test_ne_road_min_zoom(self):
        import dsl

        z, x, y = (5, 5, 12)

        self.generate_fixtures(
            # Natural Earth sample, 101 in California
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'scalerank': 4.0,
                'featurecla': 'Road',
                'type': 'Major Highway',
                'name': '101',
                'toll': 0,
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
                'min_zoom': 5.1,
            })
