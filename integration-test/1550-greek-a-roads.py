# -*- encoding: utf-8 -*-
from . import FixtureTest


class GreekARoadTest(FixtureTest):

    def test_a103_grprovincial(self):
        import dsl

        z, x, y = (16, 37061, 25262)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/544338748
            dsl.way(544338748, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'int_name': u'NATO',
                'lit': u'yes',
                'name': u'ΝΑΤΟ',
                'name:fr': u'Avenue NATO',
                'oneway': u'yes',
                'reg_ref': u'ΕΠ3',
                'source': u'openstreetmap.org',
                'source:reg_ref': u'ΦΕΚ 47 Α/8.2.1956',
            }),
            dsl.relation(1, {
                'description': u'Κηφισιά - Αχαρνές - Ασπρόπυργος',
                'name': u'Αττική Επαρχιακή Οδός 3 (Κηφισιά - Ασπρόπυργος)',
                'name:en': u'Attica Provincial Road 3 (Kifisia - Aspropyrgos)',
                'name:fr': u'Route Provinciale 3 (Kifisiá - Asprópyrgos)',
                'network': u'GR:provincial:A1',
                'ref': u'A103',
                'reg_ref': u'ΕΠ3',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[544338748]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 544338748,
                'network': u'GR:provincial',
                'shield_text': u'103',
            })
