# -*- encoding: utf-8 -*-
from . import FixtureTest


class CemeteryTest(FixtureTest):

    def test_holy_cross(self):
        import dsl

        z, x, y = (13, 1309, 3169)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/24513384
            dsl.way(24513384, dsl.box_area(z, x, y, 1312871), {
                'ALAND': '1323862',
                'AREAID': '110413857999',
                'AWATER': '0',
                'COUNTYFP': '081',
                'landuse': 'cemetery',
                'MTFCC': 'K2582',
                'name': 'Holy Cross Cemetery',
                'source': 'openstreetmap.org',
                'STATEFP': '06',
                'Tiger:MTFCC': 'K2582',
                'wikidata': 'Q8509540',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 24513384,
                'kind': 'cemetery',
                'min_zoom': 13,
            })
