# -*- encoding: utf-8 -*-
from . import FixtureTest


class StripRoadCountryCodeTest(FixtureTest):

    def test_strip_country_code(self):
        import dsl

        z, x, y = (16, 32211, 20777)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/way/31862058
            dsl.way(31862058, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'lit': u'no',
                'maxspeed': u'60 mph',
                'maxspeed:type': u'GB:nsl_single',
                'ref': u'A595',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 31862058,
                'shield_text': 'A595',
                'network': 'GB:A-road-green',
                'country_code': type(None),
            })
