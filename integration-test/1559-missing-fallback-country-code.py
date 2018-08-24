# -*- encoding: utf-8 -*-
from . import FixtureTest


class MissingFallbackCountryCodeTest(FixtureTest):

    def test_no(self):
        import dsl

        z, x, y = (16, 34749, 19016)

        self.generate_fixtures(
            dsl.is_in('NO', z, x, y),
            # https://www.openstreetmap.org/way/116419571
            dsl.way(116419571, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'lit': u'yes',
                'maxspeed': u'60',
                'name': u'Hadelandsveien',
                'ref': u'4',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 116419571,
                'shield_text': '4',
                'network': 'NO',
            })

    def test_ca(self):
        import dsl

        z, x, y = (16, 13515, 21656)

        self.generate_fixtures(
            dsl.is_in('CA', z, x, y),
            # https://www.openstreetmap.org/way/284925161
            dsl.way(284925161, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'2',
                'maxspeed': u'100',
                'name': u'Veterans Memorial Highway',
                'ref': u'2',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 284925161,
                'shield_text': '2',
                'network': 'CA',
            })
