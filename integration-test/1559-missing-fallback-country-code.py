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
