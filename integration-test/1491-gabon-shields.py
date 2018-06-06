# -*- encoding: utf-8 -*-
from . import FixtureTest


class GabonShieldTest(FixtureTest):
    def test_l101_galroad(self):
        import dsl

        z, x, y = (16, 34482, 32687)

        self.generate_fixtures(
            dsl.is_in('GA', z, x, y),
            # https://www.openstreetmap.org/way/43157378
            dsl.way(43157378, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'history': u'Retrieved from v2',
                'oneway': u'yes',
                'ref': u'L101',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 43157378,
                'network': u'GA:L-road',
                'shield_text': u'L101',
            })

    def test_n1_ganroad(self):
        import dsl

        z, x, y = (16, 34501, 32694)

        self.generate_fixtures(
            dsl.is_in('GA', z, x, y),
            # https://www.openstreetmap.org/way/514565739
            dsl.way(514565739, dsl.tile_diagonal(z, x, y), {
                'access': u'yes',
                'highway': u'trunk',
                'ref': u'RN1',
                'source': u'openstreetmap.org',
                'start_date': u'before 1970',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'network': u'GA-roads',
                'ref': u'RN1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[514565739]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 514565739,
                'network': u'GA:national',
                'shield_text': u'N1',
            })
