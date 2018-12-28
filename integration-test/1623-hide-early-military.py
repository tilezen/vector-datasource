# -*- encoding: utf-8 -*-
from . import FixtureTest


class MilitaryTest(FixtureTest):

    def test_military(self):
        import dsl

        z, x, y = (11, 325, 788)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/44018189
            dsl.way(44018189, dsl.box_area(z, x, y, 5508153), {
                'ALAND': '3346627',
                'AREAID': '110860158137',
                'AWATER': '44981',
                'landuse': 'military',
                'latitude': '+38.2498679',
                'longitude': '-122.7896975',
                'MTFCC': 'K2110',
                'name': 'Coast Guard Training Center Petaluma',
                'source': 'openstreetmap.org',
                'Tiger:MTFCC': 'K2110',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 44018189,
                'kind': 'military',
                'min_zoom': 11,
            })
