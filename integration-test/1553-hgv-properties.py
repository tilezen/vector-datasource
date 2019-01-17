# -*- encoding: utf-8 -*-
from . import FixtureTest


class LowEmissionZoneTest(FixtureTest):

    def test_low_emission_zone_way(self):
        import dsl

        z, x, y = (13, 4212, 2702)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/373249337
            dsl.way(373249337, dsl.box_area(z, x, y, 8608219), {
                'boundary': 'low_emission_zone',
                'name': 'Milieuzone Utrecht',
                'source': 'openstreetmap.org',
                'website': 'http://www.utrecht.nl/verkeersbeleid/milieuzone/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 373249337,
                'min_zoom': lambda z: 12 <= z < 13,
                'kind': 'low_emission_zone',
            })


class HgvRoadPropertiesTest(FixtureTest):

    def test_hgv_access(self):
        import dsl

        z, x, y = (16, 0, 0)

        for value in ('no', 'designated', 'destination', 'delivery', 'local',
                      'agricultural'):
            self.generate_fixtures(
                dsl.way(1, dsl.tile_diagonal(z, x, y), {
                    'highway': 'unclassified',
                    'hgv': value,
                    'source': 'openstreetmap.org',
                }),
            )

            self.assert_has_feature(
                z, x, y, 'roads', {
                    'kind': 'minor_road',
                    'kind_detail': 'unclassified',
                    'hgv': value,
                })

    def test_hgv_whitelist(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'unclassified',
                'hgv': 'not_a_whitelisted_value',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'kind': 'minor_road',
                'kind_detail': 'unclassified',
                'hgv': type(None),
            })
