# -*- encoding: utf-8 -*-
from . import FixtureTest


class PeruShieldTest(FixtureTest):
    def test_peayroads(self):
        import dsl

        z, x, y = (16, 19261, 35238)

        self.generate_fixtures(
            dsl.is_in('PE', z, x, y),
            # https://www.openstreetmap.org/way/414535595
            dsl.way(414535595, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'ref': u'AY-104',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'PE-AY-roads',
                'ref': u'AY-104',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[414535595]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 414535595,
                'shield_text': '104',
                'network': u'PE:AY',
            })

    def test_peroads(self):
        import dsl

        z, x, y = (16, 19145, 35496)

        self.generate_fixtures(
            dsl.is_in('PE', z, x, y),
            # https://www.openstreetmap.org/way/68875825
            dsl.way(68875825, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'ref': u'PE-30A',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'PE-roads',
                'ref': u'PE-30A',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[68875825]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 68875825,
                'shield_text': '30A',
                'network': u'PE:PE',
            })

    def test_pemunicipal(self):
        # despite "network=pe:municipal" in the relation, the ref should give
        # us a network of PE:AM
        import dsl

        z, x, y = (16, 18516, 33900)

        self.generate_fixtures(
            dsl.is_in('PE', z, x, y),
            # https://www.openstreetmap.org/way/262205335
            dsl.way(262205335, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'ref': u'AM-103',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Ruta nacional AM-103',
                'network': u'pe:municipal',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[262205335]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 262205335,
                'shield_text': '103',
                'network': 'PE:AM',
                'all_networks': ['PE:AM'],
                'all_shield_texts': ['103'],
            })

    def test_penational(self):
        # "pe:national" is spelled "PE:PE"
        import dsl

        z, x, y = (16, 18872, 34030)

        self.generate_fixtures(
            dsl.is_in('PE', z, x, y),
            # https://www.openstreetmap.org/way/372608804
            dsl.way(372608804, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'PE-5N',
                'name': u'Carretera Fernando Belaunde Terry',
                'oneway': u'yes',
                'ref': u'PE-5N',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
            dsl.relation(1, {
                'int_ref': u'PE-5',
                'name': u'Longitudinal de la Selva Norte',
                'network': u'pe:national',
                'ref': u'PE-5N',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q627318',
                'wikipedia': u'es:Ruta nacional PE-5N',
            }, ways=[372608804]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 372608804,
                'shield_text': '5N',
                'network': 'PE:PE',
                'all_shield_texts': ['5N'],
                'all_networks': ['PE:PE'],
            })
