# -*- encoding: utf-8 -*-
from . import FixtureTest


class RussianShieldTest(FixtureTest):
    def test_m5_rumroad(self):
        import dsl

        z, x, y = (16, 41943, 21204)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/14395684
            dsl.way(14395684, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 30;AH6',
                'lit': u'no',
                'oneway': u'yes',
                'ref': u'М-5',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'E 30 Russia middle (east)',
                'name:ru': u'Европейский маршрут E 30',
                'network': u'e-road',
                'ref': u'E 30',
                'route': u'road',
                'section': u'Russia middle (east)',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q160249',
                'wikipedia': u'en:European route E30',
            }, ways=[14395684]),
            dsl.relation(2, {
                'distance': u'1879 km',
                'name': u'«Урал»',
                'network': u'ru:national',
                'ref': u'М-5',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1848985',
                'wikipedia': u'ru:Урал (автодорога)',
            }, ways=[14395684]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 14395684,
                'network': u'RU:national',
                'shield_text': u'М5',
                'all_networks': ['RU:national', 'e-road'],
                'all_shield_texts': [u'М5', 'E30'],
            })

    def test_p226_ruregional(self):
        import dsl

        z, x, y = (16, 41506, 21675)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/26210615
            dsl.way(26210615, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'ref': u'Р226',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'96.75 km',
                'name': u'Самара — Пугачев — Энгельс — Волгоград',
                'network': u'ru:regional',
                'old_ref': u'Р226',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[26210615]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26210615,
                'network': u'RU:regional',
                'shield_text': u'Р226',
            })

    def test_p315_ruregional(self):
        import dsl

        z, x, y = (16, 42977, 20755)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/23128560
            dsl.way(23128560, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'2',
                'oneway': u'no',
                'ref': u'P315',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23128560,
                'network': u'RU:regional',
                'shield_text': u'Р315',
            })

    def test_a143_ruregional(self):
        import dsl

        z, x, y = (16, 40318, 21420)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/53270709
            dsl.way(53270709, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'4',
                'maxspeed': u'60',
                'name': u'Советская улица',
                'ref': u'А143',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 53270709,
                'network': u'RU:regional',
                'shield_text': u'А143',
            })

    def test_a119_ruregional(self):
        import dsl

        z, x, y = (16, 39090, 17942)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/4397183
            dsl.way(4397183, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'maxspeed': u'90',
                'name': u'Вологда — Медвежьегорск',
                'old_ref': u'Р5',
                'old_ref2': u'86К-2',
                'ref': u'А-119',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'606 km',
                'network': u'ru:regional',
                'ref': u'Р5',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4397183]),
            dsl.relation(2, {
                'distance': u'636',
                'network': u'ru:national',
                'ref': u'А-119',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q4386409',
                'wikipedia': u'ru:А119 (автодорога)',
            }, ways=[4397183]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4397183,
                'network': u'RU:national',
                'shield_text': u'А119',
            })

    def test_ru_k_road(self):
        # the K roads (actually cyrillic capital Ka) are regional roads with
        # some very long refs. it doesn't look like they ever get displayed
        # as a shield, so we drop the shield text.
        import dsl

        z, x, y = (16, 47192, 21042)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/342367532
            dsl.way(342367532, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary_link',
                'lanes': u'2',
                'old_ref': u'P382',
                'oneway': u'yes',
                'ref': u'50К-17р',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Новосибирск — Кочки — Павлодар (в пред. РФ)',
                'network': u'ru:regional',
                'ref': u'50К-17р',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[342367532]),
            # note: P382 relation should go here. this tests what happens if
            # there's no additional relation.
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 342367532,
                'shield_text': type(None),
                'network': u'RU:regional',
            })
