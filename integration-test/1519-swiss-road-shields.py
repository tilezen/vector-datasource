# -*- encoding: utf-8 -*-
from . import FixtureTest


class SwissShieldTest(FixtureTest):
    def test_1_chmotorway(self):
        import dsl

        z, x, y = (16, 34086, 23060)

        self.generate_fixtures(
            dsl.is_in('CH', z, x, y),
            # https://www.openstreetmap.org/way/40653024
            dsl.way(40653024, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 25',
                'lanes': u'2',
                'lit': u'no',
                'maxspeed': u'120',
                'oneway': u'yes',
                'ref': u'A1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'toll': u'yes',
            }),
            dsl.relation(1, {
                'name': u'A1',
                'network': u'motorway',
                'ref': u'A1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'toll': u'yes',
                'type': u'route',
                'wikidata': u'Q675903',
                'wikipedia': u'de:Autobahn 1 (Schweiz)',
            }, ways=[40653024]),
            dsl.relation(2, {
                'network': u'e-road',
                'ref': u'E 25',
                'route': u'road',
                'section': u'Switzerland middle',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'en:European route E25',
            }, ways=[40653024]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 40653024,
                'network': u'CH:motorway',
                'shield_text': u'1',
            })

    def test_28_chnational(self):
        import dsl

        z, x, y = (16, 34520, 23057)

        self.generate_fixtures(
            dsl.is_in('CH', z, x, y),
            # https://www.openstreetmap.org/way/366999324
            dsl.way(366999324, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'no',
                'destination:forward': u'Landquart',
                'highway': u'primary',
                'lanes': u'2',
                'lanes:backward': u'1',
                'maxheight': u'default',
                'maxspeed': u'80',
                'overtaking': u'no',
                'ref': u'28',
                'source': u'openstreetmap.org',
                'width': u'7',
            }),
            dsl.relation(1, {
                'name': u'Hauptstrasse 28',
                'ref': u'28',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[366999324]),
            dsl.relation(2, {
                'name': u'Ausbau N28 Prättigauerstrasse',
                'network': u'ch:Nationalstrasse',
                'operator': u'Schweizerische Eidgenossenschaft',
                'ref': u'N28 (Projekt)',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[366999324]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 366999324,
                'network': u'CH:national',
                'shield_text': u'28',
            })

    def test_20_chnational(self):
        import dsl

        z, x, y = (16, 34009, 23025)

        self.generate_fixtures(
            dsl.is_in('CH', z, x, y),
            # https://www.openstreetmap.org/way/24521024
            dsl.way(24521024, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lit': u'yes',
                'name': u'Boulevard de la Liberté',
                'ref': u'20',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Hauptstrasse 20',
                'name:fr': u'Route Principale 20',
                'network': u'ch:national',
                'note': u'(F)–Le Locle–La Chaux-de-Fonds–Neuchâtel',
                'ref': u'20',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[24521024]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 24521024,
                'network': u'CH:national',
                'shield_text': u'20',
            })

    def test_104_chregional(self):
        import dsl

        z, x, y = (16, 33880, 23262)

        self.generate_fixtures(
            dsl.is_in('CH', z, x, y),
            # https://www.openstreetmap.org/way/27912771
            dsl.way(27912771, dsl.tile_diagonal(z, x, y), {
                'avz': u'152',
                'bicycle': u'no',
                'bridge': u'yes',
                'cs_dir:forward': u'1',
                'foot': u'no',
                'highway': u'secondary',
                'layer': u'1',
                'maxspeed': u'60',
                'name': u'Pont Butin',
                'oneway': u'yes',
                'ref': u'104',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Plan-les-Ouates–Pont-Butin–Cointrin',
                'network': u'ch:regional',
                'ref': u'104',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[27912771]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 27912771,
                'network': u'CH:regional',
                'shield_text': u'104',
            })
