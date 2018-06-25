# -*- encoding: utf-8 -*-
from . import FixtureTest


class GenericNetworkTest(FixtureTest):
    def test_3_myfederal(self):
        import dsl

        z, x, y = (16, 51656, 32491)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/201941041
            dsl.way(201941041, dsl.tile_diagonal(z, x, y), {
                'alt_name': u'Johor Bahru-Kota Tinggi Highway',
                'alt_name:ms': u'Lebuhraya Johor Bahru-Kota Tinggi',
                'highway': u'trunk',
                'name': u'Tebrau Highway',
                'name:ms': u'Jalan Tebrau',
                'oneway': u'yes',
                'ref': u'3',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'739.06',
                'network': u'my:federal',
                'ref': u'3',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'en:Malaysia Federal Route 3',
            }, ways=[201941041]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 201941041,
                'network': u'MY:federal',
                'shield_text': u'3',
            })

    def test_baautoceste(self):
        import dsl

        z, x, y = (16, 35912, 23608)

        self.generate_fixtures(
            dsl.is_in('BA', z, x, y),
            # https://www.openstreetmap.org/way/88590170
            dsl.way(88590170, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 661',
                'lanes': u'2',
                'maxspeed': u'100',
                'oneway': u'yes',
                'ref': u'E-661',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description:fr': u'E 661 Balatonkeresztúr - Zenica',
                'name': u'European route E 661',
                'name:fr': u'Route européenne E 661',
                'name:ru': u'Европейский маршрут E 661',
                'network': u'e-road',
                'ref': u'E 661',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q676174',
                'wikipedia': u'en:European route E661',
            }, ways=[88590170]),
            dsl.relation(2, {
                'name': u'Autoput E-661',
                'network': u'ba:Autoceste',
                'ref': u'E-661',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[88590170]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 88590170,
                'network': u'BA:Autoceste',
            })

    def test_banational(self):
        import dsl

        z, x, y = (16, 35920, 23988)

        self.generate_fixtures(
            dsl.is_in('BA', z, x, y),
            # https://www.openstreetmap.org/way/114668830
            dsl.way(114668830, dsl.tile_diagonal(z, x, y), {
                'description': u'Gorica - Drinovci - Klobuk',
                'highway': u'tertiary',
                'ref': u'R 854;R-421',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'network': u'ba:national',
                'ref': u'R-421',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[114668830]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 114668830,
                'network': u'BA:national',
            })

    def test_bgmunicipal(self):
        import dsl

        z, x, y = (16, 37348, 24090)

        self.generate_fixtures(
            dsl.is_in('BG', z, x, y),
            # https://www.openstreetmap.org/way/291607259
            dsl.way(291607259, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'ref': u'GAB1005',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'bg:municipal',
                'ref': u'GAB1005',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[291607259]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 291607259,
                'network': u'BG:municipal',
            })

    def test_bgnational(self):
        import dsl

        z, x, y = (16, 36930, 23831)

        self.generate_fixtures(
            dsl.is_in('BG', z, x, y),
            # https://www.openstreetmap.org/way/236539372
            dsl.way(236539372, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'int_name': u'Shiroka',
                'name': u'Широка',
                'name:en': u'Shiroka',
                'oneway': u'yes',
                'ref': u'12',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Второкласен път 12',
                'network': u'bg:national',
                'ref': u'12',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[236539372]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 236539372,
                'network': u'BG:national',
            })

    def test_bgregional(self):
        import dsl

        z, x, y = (16, 37868, 23962)

        self.generate_fixtures(
            dsl.is_in('BG', z, x, y),
            # https://www.openstreetmap.org/way/141204241
            dsl.way(141204241, dsl.tile_diagonal(z, x, y), {
                'highway': u'residential',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'29608',
                'network': u'bg:regional',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[141204241]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 141204241,
                'network': u'BG:regional',
            })

    def test_bonational(self):
        import dsl

        z, x, y = (16, 20374, 35802)

        self.generate_fixtures(
            dsl.is_in('BO', z, x, y),
            # https://www.openstreetmap.org/way/333920841
            dsl.way(333920841, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'maxspeed': u'80',
                'name': u'RN3: La Paz-Cotapata-Caranavi',
                'oneway': u'no',
                'ref': u'F3',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'from': u'Calajahuira',
                'name': u'Ruta Nacional 3',
                'network': u'bo:national',
                'operator': u'ABC',
                'ref': u'F3',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'Trinidad',
                'type': u'route',
                'wikipedia': u'es:Ruta 3 (Bolivia)',
            }, ways=[333920841]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 333920841,
                'network': u'BO:national',
            })

    def test_bsnational(self):
        import dsl

        z, x, y = (16, 35968, 24047)

        self.generate_fixtures(
            dsl.is_in('BS', z, x, y),
            # https://www.openstreetmap.org/way/279974519
            dsl.way(279974519, dsl.tile_diagonal(z, x, y), {
                'description': u'Mostar - Čitluk - Ljubuški - Bijača',
                'highway': u'primary',
                'ref': u'M 120;R-423',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'network': u'bs:national',
                'ref': u'R-423',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[279974519]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 279974519,
                'network': u'BS:national',
            })

    def test_bynational(self):
        import dsl

        z, x, y = (16, 37059, 21611)

        self.generate_fixtures(
            dsl.is_in('BY', z, x, y),
            # https://www.openstreetmap.org/way/282927316
            dsl.way(282927316, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'no',
                'bus': u'no',
                'foot': u'no',
                'hgv': u'designated',
                'highway': u'trunk',
                'horse': u'no',
                'maxaxleload': u'11.5',
                'oneway': u'yes',
                'ref': u'М1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'611 km',
                'loc_name': u'Олимпийка',
                'network': u'by:national',
                'ref': u'М1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q267850',
                'wikipedia': u'ru:Магистраль М1 (Белоруссия)',
            }, ways=[282927316]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 282927316,
                'network': u'BY:national',
            })

    def test_byregional(self):
        import dsl

        z, x, y = (16, 37586, 20847)

        self.generate_fixtures(
            dsl.is_in('BY', z, x, y),
            # https://www.openstreetmap.org/way/198119075
            dsl.way(198119075, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'maxaxleload': u'10',
                'official_name': u'Ворняны — Гервяты — Жодишки — Р95',
                'ref': u'Н6009',
                'source': u'openstreetmap.org',
                'surface': u'unpaved',
            }),
            dsl.relation(1, {
                'name': u'Ворняны — Гервяты — Жодишки — Р95',
                'network': u'by:regional',
                'ref': u'Н6009',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[198119075]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 198119075,
                'network': u'BY:regional',
            })

    def test_cdrrig(self):
        # CD:RRIG appears to be the regional route network, with the national
        # network as CD:RN (route nationale).
        import dsl

        z, x, y = (16, 38053, 32520)

        self.generate_fixtures(
            dsl.is_in('CD', z, x, y),
            # https://www.openstreetmap.org/way/423970668
            dsl.way(423970668, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'oneway': u'yes',
                'ref': u'RP430',
                'source': u'openstreetmap.org',
                'surface': u'compacted',
            }),
            dsl.relation(1, {
                'name': u'Régionale prioritaire 430',
                'network': u'cd:rrig',
                'ref': u'RP430',
                'route': u'road',
                'rrig:id': u'243; 195',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[423970668]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 423970668,
                'network': u'CD:RRIG',
            })

    def test_chnational(self):
        import dsl

        z, x, y = (16, 34111, 23064)

        self.generate_fixtures(
            dsl.is_in('CH', z, x, y),
            # https://www.openstreetmap.org/way/435454755
            dsl.way(435454755, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'junction': u'roundabout',
                'lanes': u'1',
                'lit': u'yes',
                'maxspeed': u'50',
                'sidewalk': u'separate',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'is_in': u'CH',
                'name': u'Hauptstrasse 1',
                'name:de': u'Hauptstrasse 1',
                'name:fr': u'Route principale 1',
                'ref': u'1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[435454755]),
            dsl.relation(2, {
                'name': u'Hauptstrasse 10',
                'network': u'ch:national',
                'ref': u'10',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[435454755]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 435454755,
                'network': u'CH:national',
            })

    def test_chnationalstrasse(self):
        import dsl

        z, x, y = (16, 34566, 23088)

        self.generate_fixtures(
            dsl.is_in('CH', z, x, y),
            # https://www.openstreetmap.org/way/26686903
            dsl.way(26686903, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'cycleway': u'no',
                'destination:backward': u'Davos',
                'highway': u'primary',
                'lanes': u'2',
                'lanes:backward': u'1',
                'maxspeed': u'80',
                'oneway': u'no',
                'ref': u'28',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Hauptstrasse 28',
                'ref': u'28',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[26686903]),
            dsl.relation(2, {
                'name': u'Ausbau N28 Prättigauerstrasse',
                'network': u'ch:Nationalstrasse',
                'operator': u'Schweizerische Eidgenossenschaft',
                'ref': u'N28 (Projekt)',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[26686903]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26686903,
                'shield_text': '28',
                'network': u'CH:national',
                'all_shield_texts': ['28'],
                'all_networks': ['CH:national'],
            })

    def test_chregional(self):
        import dsl

        z, x, y = (16, 33887, 23260)

        self.generate_fixtures(
            dsl.is_in('CH', z, x, y),
            # https://www.openstreetmap.org/way/224035836
            dsl.way(224035836, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'horse': u'no',
                'lanes': u'5',
                'lanes:psv:forward': u'1',
                'lit': u'yes',
                'maxspeed': u'50',
                'name': u'Rue du Mont-Blanc',
                'oneway': u'no',
                'ref': u'101',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'trolley_wire': u'yes',
            }),
            dsl.relation(1, {
                'name': u'Genève — Meyrin — (F)',
                'network': u'ch:regional',
                'ref': u'101',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[224035836]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 224035836,
                'network': u'CH:regional',
            })

    def test_conational(self):
        import dsl

        z, x, y = (16, 19685, 31498)

        self.generate_fixtures(
            dsl.is_in('CO', z, x, y),
            # https://www.openstreetmap.org/way/346899351
            dsl.way(346899351, dsl.tile_diagonal(z, x, y), {
                'alt_name': u'Saravena - Arauquita',
                'highway': u'secondary',
                'lanes': u'2',
                'name': u'Diagonal 30',
                'oneway': u'no',
                'ref': u'66',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'description': u'Tramo La Lejía-Saravena',
                'name': u'66-04',
                'network': u'co:national',
                'operator': u'Invias',
                'ref': u'66',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[346899351]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 346899351,
                'network': u'CO:national',
            })

    def test_conationalold(self):
        import dsl

        z, x, y = (16, 19495, 30705)

        self.generate_fixtures(
            dsl.is_in('CO', z, x, y),
            # https://www.openstreetmap.org/way/388323188
            dsl.way(388323188, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'49-03',
                'network': u'co:national:old',
                'operator': u'Concesión departamental',
                'ref': u'49',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[388323188]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 388323188,
                'network': u'CO:national:old',
            })

    def test_cunational(self):
        import dsl

        z, x, y = (16, 18968, 29041)

        self.generate_fixtures(
            dsl.is_in('CU', z, x, y),
            # https://www.openstreetmap.org/way/38906926
            dsl.way(38906926, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway_link',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Autopista Nacional',
                'network': u'cu:national',
                'ref': u'A1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[38906926]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 38906926,
                'network': u'CU:national',
            })

    def test_cynational(self):
        import dsl

        z, x, y = (16, 38805, 25922)

        self.generate_fixtures(
            dsl.is_in('CY', z, x, y),
            # https://www.openstreetmap.org/way/189931877
            dsl.way(189931877, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'maxspeed': u'80',
                'oneway': u'yes',
                'ref': u'A9',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'cy:national',
                'operator': u'Public Works Department',
                'ref': u'A9',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[189931877]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 189931877,
                'network': u'CY:national',
            })

    def test_cznational(self):
        import dsl

        z, x, y = (16, 35556, 22008)

        self.generate_fixtures(
            dsl.is_in('CZ', z, x, y),
            # https://www.openstreetmap.org/way/31364470
            dsl.way(31364470, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'int_ref': u'E 65',
                'maxspeed': u'50',
                'name': u'Krkonošská',
                'ref': u'10',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'European route E 65 (Czechia)',
                'name:cs': u'Evropská silnice E65 (Česko)',
                'network': u'e-road',
                'ref': u'E 65',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q911135',
                'wikipedia': u'en:European route E65',
            }, ways=[31364470]),
            dsl.relation(2, {
                'name': u'Silnice I/10',
                'network': u'cz:national',
                'ref': u'10',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q9210921',
                'wikipedia': u'cs:Silnice I/10',
            }, ways=[31364470]),
            dsl.relation(3, {
                'complete': u'no',
                'name': u'Silnice I/10',
                'name:en': u'Expressway I/10',
                'network': u'cz:national',
                'ref': u'10',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q9210921',
                'wikipedia': u'cs:Silnice I/10',
            }, ways=[31364470]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 31364470,
                'network': u'CZ:national',
            })

    def test_czregional(self):
        import dsl

        z, x, y = (16, 35317, 22040)

        self.generate_fixtures(
            dsl.is_in('CZ', z, x, y),
            # https://www.openstreetmap.org/way/317120896
            dsl.way(317120896, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'maxspeed': u'50',
                'name': u'Tyršova',
                'ref': u'253',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'CZ:urban',
                'source:name': u'ruian',
            }),
            dsl.relation(1, {
                'description': u'Dubí — Krupka — Chabařovice — Ústí nad Labem',
                'name': u'Silnice II/253',
                'network': u'cz:regional',
                'ref': u'253',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q34663960',
                'wikipedia': u'cs:Silnice II/253',
            }, ways=[317120896]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 317120896,
                'network': u'CZ:regional',
            })

    def test_dknational(self):
        import dsl

        z, x, y = (16, 34933, 20723)

        self.generate_fixtures(
            dsl.is_in('DK', z, x, y),
            # https://www.openstreetmap.org/way/46836833
            dsl.way(46836833, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'1',
                'name': u'Brovejen',
                'oneway': u'yes',
                'ref': u'153',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Sekundærrute 153',
                'network': u'dk:national',
                'operator': u'The Danish Road Directorate',
                'ref': u'153',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[46836833]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 46836833,
                'network': u'DK:national',
            })

    def test_eenational(self):
        import dsl

        z, x, y = (16, 37276, 19234)

        self.generate_fixtures(
            dsl.is_in('EE', z, x, y),
            # https://www.openstreetmap.org/way/525145037
            dsl.way(525145037, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'maxspeed': u'50',
                'name': u'Pronksi',
                'oneway': u'yes',
                'ref': u'2',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'287.893 km',
                'name': u'Tallinn — Tartu — Võru — Luhamaa',
                'name:et': u'Tallinn — Tartu — Võru — Luhamaa',
                'name:ru': u'Таллинн — Тарту — Выру — Лухамаа',
                'network': u'ee:national',
                'ref': u'2',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q17638500',
                'wikipedia': u'et:Tallinna–Tartu–Võru–Luhamaa maantee',
            }, ways=[525145037]),
            dsl.relation(2, {
                'distance': u'212.604 km',
                'name': u'Tallinn — Narva',
                'name:de': u'Reval — Narwa',
                'name:et': u'Tallinn — Narva',
                'name:ru': u'Таллин — Нарва',
                'network': u'ee:national',
                'ref': u'1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1949796',
                'wikipedia': u'et:Tallinna–Narva maantee',
            }, ways=[525145037]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 525145037,
                'network': u'EE:national',
            })

    def test_eeregional(self):
        import dsl

        z, x, y = (16, 37248, 19265)

        self.generate_fixtures(
            dsl.is_in('EE', z, x, y),
            # https://www.openstreetmap.org/way/225479309
            dsl.way(225479309, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'name': u'Veskitammi',
                'oneway': u'yes',
                'ref': u'11401',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'6.279 km',
                'name': u'Laagri — Harku',
                'network': u'ee:regional',
                'ref': u'11401',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q16409176',
                'wikipedia': u'et:Laagri–Harku tee',
            }, ways=[225479309]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 225479309,
                'network': u'EE:regional',
            })

    def test_genational(self):
        import dsl

        z, x, y = (16, 40542, 24407)

        self.generate_fixtures(
            dsl.is_in('GE', z, x, y),
            # https://www.openstreetmap.org/way/250762262
            dsl.way(250762262, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'არტემ ბალახაშვილის ქუჩა (Artem Balakhashvili St)',
                'name:en': u'Artem Balakhashvili St',
                'name:ka': u'არტემ ბალახაშვილის ქუჩა',
                'oneway': u'yes',
                'ref': u'შ 1',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
            dsl.relation(1, {
                'is_in:country': u'Georgia',
                'name': u'Batumi–Akhaltsikhe Highway',
                'nat_ref': u'შ 1',
                'network': u'ge:national',
                'ref': u'შ 1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[250762262]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 250762262,
                'network': u'GE:national',
            })

    def test_grprovincial22(self):
        import dsl

        z, x, y = (16, 36383, 24903)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/503900908
            dsl.way(503900908, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'oneway': u'yes',
                'reg_ref': u'ΕΠ2;ΕΠ16',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'gr:provincial:22',
                'ref': u'2202',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[503900908]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 503900908,
                'network': u'GR:provincial',
            })

    def test_grprovincial52(self):
        import dsl

        z, x, y = (16, 37161, 24536)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/25144610
            dsl.way(25144610, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'int_name': u'Drama - Mavrolefki',
                'lanes': u'2',
                'name': u'Αμφίπολη - Δράμα',
                'oneway': u'yes',
                'reg_ref': u'ΕΠ1',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Δράμα - Μαυρολεύκη - Νέα Μπάφρα',
                'network': u'gr:provincial:52',
                'ref': u'5201',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[25144610]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25144610,
                'network': u'GR:provincial',
            })

    def test_grprovincial54(self):
        import dsl

        z, x, y = (16, 36967, 24661)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/14429261
            dsl.way(14429261, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Άγιος Βασίλειος - Χορτιάτης',
                'reg_ref': u'ΕΠ20',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Άγιος Βασίλειος - Χορτιάτης',
                'network': u'gr:provincial:54',
                'ref': u'5420',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[14429261]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 14429261,
                'network': u'GR:provincial',
            })

    def test_grprovincial55(self):
        import dsl

        z, x, y = (16, 37163, 24582)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/332922898
            dsl.way(332922898, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Καλαμπάκι - Νικήσιανη',
                'reg_ref': u'ΕΠ16',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Καλαμπάκι - Νικήσιανη',
                'network': u'gr:provincial:55',
                'ref': u'5516',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[332922898]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 332922898,
                'network': u'GR:provincial',
            })

    def test_grprovincial72(self):
        import dsl

        z, x, y = (16, 37265, 24523)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/223510857
            dsl.way(223510857, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Κεχρόκαμπος - Σταυρούπολη',
                'reg_ref': u'ΕΠ6',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'network': u'gr:provincial:72',
                'ref': u'7206',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[223510857]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 223510857,
                'network': u'GR:provincial',
            })

    def test_grprovincial73(self):
        import dsl

        z, x, y = (16, 37421, 24523)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/425300873
            dsl.way(425300873, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'1',
                'reg_ref': u'ΕΠ12',
                'smoothness': u'intermediate',
                'source': u'openstreetmap.org',
                'surface': u'gravel',
            }),
            dsl.relation(1, {
                'network': u'gr:provincial:73',
                'ref': u'7312',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[425300873]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 425300873,
                'network': u'GR:provincial',
            })

    def test_irfreeways(self):
        # it looks like roads in Iran are signed in both Arabic and Latin
        # scripts for the numbers, and that the Asian Highway is signed
        # something like "A1Tr", although the "Tr" is in a little box.
        #
        # https://en.wikipedia.org/wiki/Freeway_2_(Iran)

        import dsl

        z, x, y = (16, 41219, 25277)

        self.generate_fixtures(
            dsl.is_in('IR', z, x, y),
            # https://www.openstreetmap.org/way/549630346
            dsl.way(549630346, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'AH1',
                'name': u'آزادراه زنجان - تبریز',
                'oneway': u'yes',
                'ref': u'2',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'int_name': u'Asian Highway AH1',
                'int_ref': u'AH1',
                'name': u'بزرگراه آسیایی شماره ۱',
                'name:bn': u'এশিয়ান হাইওয়ে ১',
                'name:de': u'Asien Fernstraße AH1',
                'name:en': u'Asian Highway AH1',
                'name:fa': u'بزرگراه آسیایی شماره ۱',
                'name:fr': u'Route asiatique AH1',
                'name:hi': u'एशियाई राजमार्ग १',
                'name:id': u'Jalan Asia AH1',
                'name:ja': u'アジアハイウェイ1号線',
                'name:km': u'ផ្លូវហាយវេអាស៊ី១',
                'name:ko': u'아시안 하이웨이 1호선',
                'name:ms': u'Lebuh Raya Asia AH1',
                'name:my': u'အာရှအဝေးပြေး ၁',
                'name:ru': u'Азиатский маршрут AH1',
                'name:th': u'ทางหลวงสายเอเชียAH1',
                'name:tr': u'Asya Yolu AH1',
                'name:vi': u'Đường Xuyên Á AH1',
                'name:zh': u'亚洲公路1号线',
                'network': u'AH',
                'ref': u'AH1',
                'route': u'road',
                'section': u'Iran',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q494205',
                'wikipedia': u'en:AH1',
            }, ways=[549630346]),
            dsl.relation(2, {
                'name': u'آزادراه ۲',
                'name:en': u'Freeway 2',
                'network': u'ir:freeways',
                'ref': u'2',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q4812011',
                'wikipedia': u'en:Freeway 2 (Iran)',
            }, ways=[549630346]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 549630346,
                'network': u'IR:freeway',
                'shield_text': '2',
                'all_networks': ['IR:freeway', 'AsianHighway'],
                'all_shield_texts': ['2', 'A1'],
            })

    def test_irnational(self):
        import dsl

        z, x, y = (16, 43473, 25685)

        self.generate_fixtures(
            dsl.is_in('IR', z, x, y),
            # https://www.openstreetmap.org/way/35693445
            dsl.way(35693445, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'AH1',
                'maxspeed': u'90',
                'name': u'نیشابور - مشهد',
                'name:en': u'Neyshabur-Mashhad',
                'oneway': u'yes',
                'ref': u'44',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'int_name': u'Asian Highway AH1',
                'int_ref': u'AH1',
                'name': u'بزرگراه آسیایی شماره ۱',
                'name:bn': u'এশিয়ান হাইওয়ে ১',
                'name:de': u'Asien Fernstraße AH1',
                'name:en': u'Asian Highway AH1',
                'name:fa': u'بزرگراه آسیایی شماره ۱',
                'name:fr': u'Route asiatique AH1',
                'name:hi': u'एशियाई राजमार्ग १',
                'name:id': u'Jalan Asia AH1',
                'name:ja': u'アジアハイウェイ1号線',
                'name:km': u'ផ្លូវហាយវេអាស៊ី១',
                'name:ko': u'아시안 하이웨이 1호선',
                'name:ms': u'Lebuh Raya Asia AH1',
                'name:my': u'အာရှအဝေးပြေး ၁',
                'name:ru': u'Азиатский маршрут AH1',
                'name:th': u'ทางหลวงสายเอเชียAH1',
                'name:tr': u'Asya Yolu AH1',
                'name:vi': u'Đường Xuyên Á AH1',
                'name:zh': u'亚洲公路1号线',
                'network': u'AH',
                'ref': u'AH1',
                'route': u'road',
                'section': u'Iran',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q494205',
                'wikipedia': u'en:AH1',
            }, ways=[35693445]),
            dsl.relation(2, {
                'network': u'ir:national',
                'ref': u'44',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q4811748',
                'wikipedia': u'en:Road 44 (Iran)',
            }, ways=[35693445]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 35693445,
                'network': 'IR:national',
                'shield_text': '44',
                'all_networks': ['IR:national', 'AsianHighway'],
                'all_shield_texts': ['44', 'A1'],
            })

    def test_japrefectural(self):
        import dsl

        z, x, y = (16, 58348, 24085)

        self.generate_fixtures(
            dsl.is_in('JA', z, x, y),
            # https://www.openstreetmap.org/way/57706486
            dsl.way(57706486, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'北海道道270号岩内港線',
                'name:ja': u'北海道道270号岩内港線',
                'name:ja_rm': u'Hokkaidō dō nihyakunanajūgō Iwanai kō sen',
                'ref': u'270',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'北海道道270号岩内港線',
                'name:en': u'Hokkaido Prefectural Road Route 270',
                'name:ja': u'北海道道270号岩内港線',
                'network': u'ja:prefectural',
                'operator': u'北海道',
                'ref': u'270',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q11403263',
                'wikipedia': u'ja:北海道道270号岩内港線',
            }, ways=[57706486]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 57706486,
                'network': u'JA:prefectural',
            })

    def test_jpprefectural(self):
        import dsl

        z, x, y = (16, 57266, 26163)

        self.generate_fixtures(
            dsl.is_in('JP', z, x, y),
            # https://www.openstreetmap.org/way/23962887
            dsl.way(23962887, dsl.tile_diagonal(z, x, y), {
                'access': u'no',
                'highway': u'primary',
                'lanes': u'1',
                'name': u'徳島環状線',
                'oneway': u'yes',
                'ref': u'29',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'highway': u'primary',
                'name': u'徳島環状線',
                'network': u'jp:prefectural',
                'ref': u'29',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[23962887]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23962887,
                'network': u'JP:prefectural',
            })

    def test_jpprefecturalkanagawa(self):
        import dsl

        z, x, y = (16, 58185, 25885)

        self.generate_fixtures(
            dsl.is_in('JP', z, x, y),
            # https://www.openstreetmap.org/way/386400216
            dsl.way(386400216, dsl.tile_diagonal(z, x, y), {
                'bus': u'yes',
                'crossing': u'no',
                'hgv': u'yes',
                'highway': u'primary',
                'lanes': u'2',
                'maxspeed': u'40',
                'name': u'環状4号',
                'name:en': u'Circular Route 4',
                'name:ja': u'環状4号',
                'name:ja_rm': u'Kanjou 4 go',
                'ref': u'23',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'tourist_bus': u'yes',
            }),
            dsl.relation(1, {
                'name': u'神奈川県道23号 原宿六ツ浦線',
                'name:en': u'Kanagawa prefectural road No. 23',
                'name:ja': u'神奈川県道23号 原宿六ツ浦線',
                'name:ja_rm': u'Kendou 23 Gou Harajuku Mutsuura Sen',
                'network': u'jp:prefectural:kanagawa',
                'ref': u'23',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q11589265',
                'wikipedia': u'ja:神奈川県道23号原宿六ツ浦線',
            }, ways=[386400216]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 386400216,
                'network': u'JP:prefectural',
            })

    def test_kznational(self):
        import dsl

        z, x, y = (16, 45425, 24241)

        self.generate_fixtures(
            dsl.is_in('KZ', z, x, y),
            # https://www.openstreetmap.org/way/261067663
            dsl.way(261067663, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'AH61;AH62;E 38;E 123',
                'lanes': u'2',
                'nat_ref': u'M-32',
                'old_name': u'Ташкенская железная дорога',
                'oneway': u'yes',
                'ref': u'M-32',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description:fr': u'E 123 Tcheliabinsk - Nizhny Panj',
                'name': u'E 123 Chelyabinsk - Panji Poyon',
                'name:de': u'Europastraße 123',
                'name:en': u'European route E 123',
                'name:fr': u'Route européenne E 123',
                'name:pl': u'Trasa europejska E 123',
                'name:ru': u'Европейский маршрут E 123',
                'network': u'e-road',
                'ref': u'E 123',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1821054',
                'wikipedia': u'en:European route E123',
            }, ways=[261067663]),
            dsl.relation(2, {
                'int_ref': u'AH62',
                'name': u'Asian Highway AH62',
                'network': u'AsianHighway',
                'ref': u'AH62',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[261067663]),
            dsl.relation(3, {
                'int_ref': u'AH61',
                'name': u'Asian Highway AH61',
                'name:en': u'Asian Highway AH61',
                'name:ru': u'Азиатский маршрут AH61',
                'network': u'AsianHighway',
                'ref': u'AH61',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[261067663]),
            dsl.relation(4, {
                'distance': u'2083.1 km',
                'nat_ref': u'M-32',
                'network': u'kz:national',
                'ref': u'M-32',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[261067663]),
            dsl.relation(5, {
                'addr:country': u'KZ',
                'description:fr': u'E 38 Glukhov - Chimkent',
                'name': u'Европейский маршрут E 38',
                'name:de': u'Europastraße 38',
                'name:en': u'European Road E 38',
                'name:fr': u'Route européenne E 38',
                'name:pl': u'Trasa europejska E 38',
                'name:ru': u'Европейский маршрут E 38',
                'network': u'e-road',
                'ref': u'E 38',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q289474',
                'wikipedia': u'en:European route E38',
            }, ways=[261067663]),
        )

        # TODO: sort e-road or AH first/last?
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 261067663,
                'shield_text': 'M-32',
                'network': 'KZ:national',
                'all_shield_texts': ['M-32', 'E38', 'AH61', 'AH62', 'E123'],
                'all_networks': ['KZ:national', 'e-road', 'AsianHighway',
                                 'AsianHighway', 'e-road'],
            })

    def test_ltnational(self):
        import dsl

        z, x, y = (16, 37388, 20837)

        self.generate_fixtures(
            dsl.is_in('LT', z, x, y),
            # https://www.openstreetmap.org/way/202685182
            dsl.way(202685182, dsl.tile_diagonal(z, x, y), {
                'alt_name': u'Juodasis kelias',
                'highway': u'primary',
                'name': u'Šumsko pl.',
                'ref': u'101',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'alt_name': u'Juodasis kelias',
                'distance': u'35.99 km',
                'name': u'Vilnius — Šumskas',
                'name:pl': u'Wilno — Szumsk',
                'network': u'lt:national',
                'ref': u'101',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q14918956',
                'wikipedia': u'lt:KK101',
            }, ways=[202685182]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 202685182,
                'network': u'LT:national',
            })

    def test_ltregional(self):
        import dsl

        z, x, y = (16, 37070, 20720)

        self.generate_fixtures(
            dsl.is_in('LT', z, x, y),
            # https://www.openstreetmap.org/way/100482052
            dsl.way(100482052, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'name': u'Ąžuolų g.',
                'ref': u'1954',
                'source': u'openstreetmap.org',
                'surface': u'unpaved',
            }),
            dsl.relation(1, {
                'distance': u'1.2 km',
                'name': u'Jaučakiai — Antalkiai',
                'network': u'lt:regional',
                'ref': u'1954',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[100482052]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 100482052,
                'network': u'LT:regional',
            })

    def test_lvlocal(self):
        import dsl

        z, x, y = (16, 37428, 19964)

        self.generate_fixtures(
            dsl.is_in('LV', z, x, y),
            # https://www.openstreetmap.org/way/85698916
            dsl.way(85698916, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Valmiera — Rauna',
                'ref': u'V187',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'28.9 km',
                'name': u'Valmiera — Rauna',
                'network': u'lv:local',
                'ref': u'V187',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[85698916]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 85698916,
                'network': u'LV:local',
            })

    def test_lvnational(self):
        import dsl

        z, x, y = (16, 37796, 20465)

        self.generate_fixtures(
            dsl.is_in('LV', z, x, y),
            # https://www.openstreetmap.org/way/494863068
            dsl.way(494863068, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'maxspeed': u'90',
                'ref': u'А6',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'307.0 km',
                'name:lt': u'Ryga — Daugpilis — Kraslava — Baltarusijos siena',
                'network': u'lv:national',
                'ref': u'A6',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q786297',
                'wikipedia': u'lv:Autoceļš A6 (Latvija)',
            }, ways=[494863068]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 494863068,
                'network': u'LV:national',
            })

    def test_lvregional(self):
        import dsl

        z, x, y = (16, 37781, 20376)

        self.generate_fixtures(
            dsl.is_in('LV', z, x, y),
            # https://www.openstreetmap.org/way/15717770
            dsl.way(15717770, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'highway': u'primary',
                'name': u'Daugavpils iela',
                'ref': u'P55',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'58.0 km',
                'name': u'Rēzekne — Dagda',
                'network': u'lv:regional',
                'ref': u'P55',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q13979190',
                'wikipedia': u'lv:Autoceļš P55',
            }, ways=[15717770]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 15717770,
                'network': u'LV:regional',
            })

    def test_r29278_mknational(self):
        import dsl

        z, x, y = (16, 36578, 24359)

        self.generate_fixtures(
            dsl.is_in('MK', z, x, y),
            # https://www.openstreetmap.org/way/193364172
            dsl.way(193364172, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'R29278',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'from': u'Negotino',
                'name': u'R29278',
                'network': u'mk:national',
                'ref': u'R29278',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'A2',
                'type': u'route',
            }, ways=[193364172]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 193364172,
                'network': u'MK:national',
                'shield_text': u'R29278',
            })

    def test_mknational(self):
        import dsl

        z, x, y = (16, 36730, 24382)

        self.generate_fixtures(
            dsl.is_in('MK', z, x, y),
            # https://www.openstreetmap.org/way/461227650
            dsl.way(461227650, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_name': u'Prijatelstvo',
                'int_ref': u'E 75',
                'lanes': u'2',
                'name': u'Пријателство',
                'name:en': u'Friendship',
                'oneway': u'yes',
                'ref': u'A1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'from': u'Kumanovo',
                'name': u'A1',
                'network': u'mk:national',
                'old_ref': u'M1',
                'ref': u'А1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'Gevgelija',
                'type': u'route',
            }, ways=[461227650]),
            dsl.relation(2, {
                'name': u'European Route 75',
                'network': u'e-road',
                'ref': u'E 75',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'en:European route E75',
            }, ways=[461227650]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 461227650,
                'network': u'MK:national',
            })

    def test_myfederal(self):
        import dsl

        z, x, y = (16, 51652, 32357)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/553323706
            dsl.way(553323706, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'name': u'Jalan Kluang-Jemaluang',
                'oneway': u'no',
                'ref': u'50',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
            dsl.relation(1, {
                'distance': u'135.38',
                'name': u'Jalan Batu Pahat - Ayer Hitam - Jemaluang',
                'network': u'my:federal',
                'ref': u'50',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'en:Malaysia Federal Route 50',
            }, ways=[553323706]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 553323706,
                'network': u'MY:federal',
            })

    def test_nofylkesvei(self):
        import dsl

        z, x, y = (16, 33706, 18951)

        self.generate_fixtures(
            dsl.is_in('NO', z, x, y),
            # https://www.openstreetmap.org/way/106337203
            dsl.way(106337203, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'maxspeed': u'50',
                'ref': u'555',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Fylkesvei 555 (Hordaland)',
                'network': u'no:Fylkesvei',
                'operator': u'Hordaland Fylkeskommune',
                'ref': u'555',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q6367615',
                'wikipedia': u'no:Fylkesvei 555',
            }, ways=[106337203]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 106337203,
                'shield_text': '555',
                'network': u'NO:fylkesvei',
            })

    def test_noriksvei(self):
        import dsl

        z, x, y = (16, 34099, 18283)

        self.generate_fixtures(
            dsl.is_in('NO', z, x, y),
            # https://www.openstreetmap.org/way/521803129
            dsl.way(521803129, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'trunk',
                'layer': u'1',
                'maxspeed': u'70',
                'ref': u'15',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Riksvei 15',
                'network': u'no:riksvei',
                'operator': u'Statens vegvesen',
                'ref': u'Rv15',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q6396950',
                'wikipedia': u'no:Riksvei 15',
            }, ways=[521803129]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 521803129,
                'shield_text': '15',
                'network': u'NO:riksvei',
            })

    def test_noriksvei_capital(self):
        import dsl

        z, x, y = (16, 34089, 18878)

        self.generate_fixtures(
            dsl.is_in('NO', z, x, y),
            # https://www.openstreetmap.org/way/298679001
            dsl.way(298679001, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'maxspeed': u'80',
                'maxspeed:practical': u'70',
                'ref': u'7',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Riksvei 7',
                'network': u'no:Riksvei',
                'ref': u'7',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q6396499',
                'wikipedia': u'no:Riksvei 7',
            }, ways=[298679001]),
            dsl.relation(2, {
                'name': u'Hardangervidda',
                'route': u'road',
                'source': u'openstreetmap.org',
                'tourism': u'yes',
                'type': u'route',
            }, ways=[298679001]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 298679001,
                'shield_text': '7',
                'network': u'NO:riksvei',
            })

    def test_npnational(self):
        import dsl

        z, x, y = (16, 47354, 27249)

        self.generate_fixtures(
            dsl.is_in('NP', z, x, y),
            # https://www.openstreetmap.org/way/27030698
            dsl.way(27030698, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'AH2',
                'name': u'महेन्द्र राज्मार्ग्',
                'name:en': u'Mahendra Highway',
                'name:ne': u'महेन्द्र राज्मार्ग्',
                'ref': u'H01',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'int_ref': u'AH2',
                'name': u'Asian Highway AH2',
                'name:de': u'Asiatische Fernstraße 2',
                'name:en': u'Asian Highway AH2',
                'name:ms': u'Lebuhraya Asia AH2',
                'name:ru': u'Азиатский маршрут AH2',
                'name:zh': u'亚洲高速公路 AH2',
                'network': u'AsianHighway',
                'ref': u'AH2',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q727638',
                'wikipedia': u'en:AH2',
            }, ways=[27030698]),
            dsl.relation(2, {
                'distance': u'1027.67',
                'name': u'Mahendra Rajmarg',
                'name:en': u'Mahendra Highway',
                'name:ne': u'महेन्द्र राज्मार्ग्',
                'name:pl': u'Mahendra',
                'network': u'np:national',
                'ref': u'H01',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q3595565',
                'wikipedia': u'en:Mahendra Highway',
            }, ways=[27030698]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 27030698,
                'network': u'NP:national',
            })

    def test_npregional(self):
        import dsl

        z, x, y = (16, 48796, 27744)

        self.generate_fixtures(
            dsl.is_in('NP', z, x, y),
            # https://www.openstreetmap.org/way/352615958
            dsl.way(352615958, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'name': u'Birtamod — Chandragadhi',
                'ref': u'F1',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
            dsl.relation(1, {
                'distance': u'12.53 km',
                'name': u'Birtamod — Chandragadhi',
                'network': u'np:regional',
                'ref': u'F1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[352615958]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 352615958,
                'network': u'NP:regional',
            })

    def test_phnational(self):
        import dsl

        z, x, y = (16, 55524, 30719)

        self.generate_fixtures(
            dsl.is_in('PH', z, x, y),
            # https://www.openstreetmap.org/way/460910438
            dsl.way(460910438, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'AH26',
                'lanes': u'2',
                'name': u'Maharlika Highway',
                'nat_name': u'Daang Maharlika (LT)',
                'official_name': u'Daang Maharlika Highway',
                'ref': u'1;AH26',
                'source': u'openstreetmap.org',
                'surface': u'concrete',
            }),
            dsl.relation(1, {
                'name': u'N1',
                'network': u'ph:nhn',
                'nhn:class': u'primary',
                'ref': u'1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[460910438]),
            dsl.relation(2, {
                'int_ref': u'AH26',
                'int_ref:colour': u'blue',
                'name': u'National Highway',
                'name:en': u'National Highway',
                'name:tl': u'Manila South Road',
                'network': u'ph:national',
                'ref': u'1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1520784',
                'wikipedia': u'en:AH26',
            }, ways=[460910438]),
            dsl.relation(3, {
                'int_ref': u'AH26',
                'name': u'AH26: Leyte',
                'network': u'ph:nhn',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[460910438]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 460910438,
                'network': u'PH:national',
            })

    def test_phnhn(self):
        import dsl

        z, x, y = (16, 55451, 30748)

        self.generate_fixtures(
            dsl.is_in('PH', z, x, y),
            # https://www.openstreetmap.org/way/28315545
            dsl.way(28315545, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'name': u'Merida-Ormoc Road',
                'nat_name': u'Palompon-Isabel-Merida-Ormoc Road',
                'ref': u'684',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'N684: Palompon-Isabel-Merida-Ormoc Road',
                'network': u'ph:nhn',
                'nhn:class': u'secondary',
                'nhn:district': u'Leyte 4th District Engineering Office',
                'nhn:id': u'S00152LT',
                'nhn:length': u'64,754',
                'nhn:name': u'Palompon-Isabel-Merida-Ormoc Road',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[28315545]),
            dsl.relation(2, {
                'name': u'N684',
                'network': u'ph:nhn',
                'ph:class': u'secondary',
                'ref': u'684',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[28315545]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 28315545,
                'network': u'PH:NHN',
            })

    def test_plexpressways(self):
        import dsl

        z, x, y = (16, 36432, 21168)

        self.generate_fixtures(
            dsl.is_in('PL', z, x, y),
            # https://www.openstreetmap.org/way/540661648
            dsl.way(540661648, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 77',
                'lanes': u'2',
                'maxaxleload': u'11.5',
                'maxspeed': u'120',
                'maxspeed:bus': u'80',
                'maxspeed:trailer': u'80',
                'oneway': u'yes',
                'ref': u'S7',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'PL:trunk',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'E 77',
                'name:de': u'Europastraße 77',
                'name:en': u'European route E77',
                'name:lt': u'E 77 Pskovas - Budapeštas',
                'name:pl': u'Trasa europejska E 77',
                'name:ru': u'Европейский маршрут E 77',
                'network': u'e-road',
                'ref': u'E 77',
                'route': u'road',
                'section': u'Poland',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q918092',
                'wikipedia': u'pl:E77 (trasa europejska)',
            }, ways=[540661648]),
            dsl.relation(2, {
                'distance': u'780',
                'name': u'Droga krajowa nr 7',
                'name:de': u'Landesstraße 7',
                'name:pl': u'Droga krajowa nr 7',
                'network': u'pl:national',
                'ref': u'7',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1090066',
                'wikipedia': u'pl:Droga krajowa nr 7 (Polska)',
            }, ways=[540661648]),
            dsl.relation(3, {
                'name': u'Droga ekspresowa S7',
                'name:de': u'Schnellstraße S7',
                'name:pl': u'Droga ekspresowa S7',
                'network': u'pl:expressways',
                'osmonitor:road_components': u'3',
                'ref': u'S7',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1259569',
                'wikipedia': u'pl:Droga ekspresowa S7 (Polska)',
            }, ways=[540661648]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 540661648,
                'network': u'PL:expressway',
            })

    def test_pllocal(self):
        import dsl

        z, x, y = (16, 36866, 21585)

        self.generate_fixtures(
            dsl.is_in('PL', z, x, y),
            # https://www.openstreetmap.org/way/202273292
            dsl.way(202273292, dsl.tile_diagonal(z, x, y), {
                'highway': u'residential',
                'name': u'Olchowa',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'pl:local',
                'ref': u'3683W',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[202273292]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 202273292,
                'network': u'PL:local',
            })

    def test_plmotorway(self):
        import dsl

        z, x, y = (16, 35612, 21841)

        self.generate_fixtures(
            dsl.is_in('PL', z, x, y),
            # https://www.openstreetmap.org/way/390491502
            dsl.way(390491502, dsl.tile_diagonal(z, x, y), {
                'agricultural': u'no',
                'bicycle': u'no',
                'foot': u'no',
                'highway': u'motorway',
                'horse': u'no',
                'int_ref': u'E 36',
                'lanes': u'3',
                'lit': u'no',
                'maxaxleload': u'11.5',
                'maxspeed': u'110',
                'oneway': u'yes',
                'ref': u'A18',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'sign',
                'surface': u'concrete',
                'turn:lanes': u'none|none|right',
            }),
            dsl.relation(1, {
                'distance': u'78',
                'name': u'Droga krajowa nr 18',
                'network': u'pl:national',
                'ref': u'18',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1090666',
                'wikipedia': u'pl:Droga krajowa nr 18 (Polska)',
            }, ways=[390491502]),
            dsl.relation(2, {
                'description:fr': u'E 36 Berlin - Legnica',
                'e-road:class': u'A-intermediate',
                'name': u'E 36',
                'name:en': u'European route E 36',
                'name:fr': u'Route européenne E 36',
                'name:pl': u'Trasa europejska E 36',
                'name:ru': u'Европейский маршрут E 36',
                'network': u'e-road',
                'ref': u'E 36',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q240696',
                'wikipedia': u'de:Europastraße 36',
            }, ways=[390491502]),
            dsl.relation(3, {
                'distance': u'7',
                'name': u'Autostrada A18',
                'network': u'pl:motorways',
                'ref': u'A18',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q429300',
                'wikipedia': u'pl:Autostrada A18 (Polska)',
            }, ways=[390491502]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 390491502,
                'network': u'PL:motorway',
            })

    def test_plnational(self):
        import dsl

        z, x, y = (16, 35685, 21869)

        self.generate_fixtures(
            dsl.is_in('PL', z, x, y),
            # https://www.openstreetmap.org/way/488175622
            dsl.way(488175622, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'primary',
                'maxspeed': u'90',
                'ref': u'94',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'521',
                'name': u'Droga krajowa nr 94',
                'network': u'pl:national',
                'note': u'kolejność odcinków do sprawdzenia',
                'ref': u'94',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1123685',
                'wikipedia': u'pl:Droga krajowa nr 94 (Polska)',
            }, ways=[488175622]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 488175622,
                'network': u'PL:national',
            })

    def test_plregional(self):
        import dsl

        z, x, y = (16, 36128, 22049)

        self.generate_fixtures(
            dsl.is_in('PL', z, x, y),
            # https://www.openstreetmap.org/way/325897610
            dsl.way(325897610, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'lanes': u'1',
                'maxspeed': u'90',
                'maxspeed:bus': u'70',
                'maxspeed:trailer': u'70',
                'ref': u'901',
                'source': u'openstreetmap.org',
                'source:geometry': u'Bing',
                'source:maxspeed': u'PL:rural',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'75',
                'name': u'Droga wojewódzka nr 901',
                'network': u'pl:regional',
                'ref': u'901',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q9211920',
                'wikipedia': u'pl:Droga wojewódzka nr 901',
            }, ways=[325897610]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 325897610,
                'network': u'PL:regional',
            })

    def test_ptnational(self):
        import dsl

        z, x, y = (16, 31397, 24754)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/422696695
            dsl.way(422696695, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'ref': u'EN 230',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Estrada Nacional 230',
                'network': u'pt:national',
                'ref': u'EN 230',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[422696695]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 422696695,
                'shield_text': 'N230',
                'network': 'PT:national',
            })

    def test_ptregionalcentre(self):
        import dsl

        z, x, y = (16, 31339, 24728)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/182513565
            dsl.way(182513565, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary_link',
                'oneway': u'-1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Estrada Regional 230',
                'network': u'pt:regional:centre',
                'ref': u'ER 230',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[182513565]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 182513565,
                'shield_text': 'R230',
                'network': u'PT:regional',
            })

    def test_rodc(self):
        import dsl

        z, x, y = (16, 37338, 23227)

        self.generate_fixtures(
            dsl.is_in('RO', z, x, y),
            # https://www.openstreetmap.org/way/432600432
            dsl.way(432600432, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'lanes': u'2',
                'maxspeed': u'50',
                'ref': u'DC39',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'DC39',
                'network': u'ro:DC',
                'operator': u'Comuna Șimonești',
                'ref': u'DC39',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[432600432]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 432600432,
                'network': 'RO:local',
                'shield_text': '39',
            })

    def test_rodj(self):
        import dsl

        z, x, y = (16, 37077, 23814)

        self.generate_fixtures(
            dsl.is_in('RO', z, x, y),
            # https://www.openstreetmap.org/way/27861514
            dsl.way(27861514, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'maxspeed': u'50',
                'oneway': u'no',
                'ref': u'DJ561F',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'16.120',
                'name': u'DJ621F',
                'network': u'ro:DJ',
                'ref': u'DJ561F',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[27861514]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 27861514,
                'network': 'RO:county',
                'shield_text': '561F',
            })

    def test_rufederal(self):
        import dsl

        z, x, y = (16, 39807, 21164)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/40357283
            dsl.way(40357283, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Кимовск - Епифань - Куликово Поле - Кресты',
                'oneway': u'yes',
                'ref': u'Р145',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'116 km',
                'name': u'Кимовск - Епифань - Куликово Поле - Кресты',
                'network': u'ru:federal',
                'ref': u'Р145',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[40357283]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 40357283,
                'shield_text': u'Р145',
                'network': u'RU:federal',
            })

    def test_ruintermunicipal(self):
        # don't shield these H-type / intermunicipal roads
        import dsl

        z, x, y = (16, 39641, 19019)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/165806759
            dsl.way(165806759, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'maxspeed': u'60',
                'name': u'улица Свободы',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Белозерск — Карпово — Конец Мондра',
                'network': u'ru:intermunicipal',
                'ref': u'19Н-003',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[165806759]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 165806759,
                'shield_text': type(None),
                'network': u'RU:intermunicipal',
            })

    def test_rulocal(self):
        import dsl

        z, x, y = (16, 36650, 20911)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/272251749
            dsl.way(272251749, dsl.tile_diagonal(z, x, y), {
                'highway': u'unclassified',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'5.4 km',
                'name': u'«Липняки — Перевалово» — Косарево',
                'network': u'ru:local',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[272251749]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 272251749,
                'shield_text': type(None),
                'network': u'RU:local',
            })

    def test_rumunicipal(self):
        import dsl

        z, x, y = (16, 39549, 20515)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/156094979
            dsl.way(156094979, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'name': u'улица Яскино',
                'name:en': u'Yaskino Street',
                'name:ru': u'улица Яскино',
                'oneway': u'yes',
                'postal_code': u'143005',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Можайское шоссе (город Одинцово)',
                'network': u'ru:municipal',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[156094979]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 156094979,
                'shield_text': type(None),
                'network': u'RU:municipal',
            })

    def test_runational(self):
        import dsl

        z, x, y = (16, 39374, 22129)

        self.generate_fixtures(
            dsl.is_in('RU', z, x, y),
            # https://www.openstreetmap.org/way/24682239
            dsl.way(24682239, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 105',
                'lanes': u'4',
                'ref': u'М-2',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'720',
                'name': u'«Крым»',
                'network': u'ru:national',
                'ref': u'М-2',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q980249',
                'wikipedia': u'ru:Крым (автодорога)',
            }, ways=[24682239]),
            dsl.relation(2, {
                'e-road:class': u'A-intermediate',
                'name': u'E 105 South',
                'network': u'e-road',
                'ref': u'E 105',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[24682239]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 24682239,
                'shield_text': u'М2',
                'network': u'RU:national',
                'all_shield_texts': [u'М2', 'E105'],
                'all_networks': ['RU:national', 'e-road'],
            })

    def test_ruregional(self):
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
            dsl.relation(2, {
                'highway': u'primary',
                'network': u'ru:regional',
                'ref': u'Р382',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[342367532]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 342367532,
                'shield_text': u'Р382',
                'network': u'RU:regional',
            })

    def test_sknational(self):
        import dsl

        z, x, y = (16, 36647, 22565)

        self.generate_fixtures(
            dsl.is_in('SK', z, x, y),
            # https://www.openstreetmap.org/way/170954509
            dsl.way(170954509, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'motorway_link',
                'int_ref': u'E 50',
                'lanes': u'2',
                'layer': u'1',
                'maxspeed': u'60',
                'oneway': u'yes',
                'ref': u'D1',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'sign',
                'toll': u'yes',
                'toll:hgv': u'yes',
            }),
            dsl.relation(1, {
                'name': u'European Road E 50 (Slovakia)',
                'name:cs': u'Evropská silnice E50 (Slovensko)',
                'name:pl': u'Trasa europejska E 50',
                'name:ru': u'Европейский маршрут E 50',
                'name:sk': u'Európska cesta E 50',
                'network': u'e-road',
                'ref': u'E 50',
                'route': u'road',
                'section': u'Slovensko',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q687438',
                'wikipedia': u'en:European route E50',
            }, ways=[170954509]),
            dsl.relation(2, {
                'name': u'D1',
                'name:cs': u'Dálnice D1 (Slovensko)',
                'name:en': u'D1 motorway (Slovakia)',
                'name:hu': u'D1-es autópálya (Szlovákia)',
                'name:sk': u'Diaľnica D1',
                'network': u'sk:national',
                'ref': u'D1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q763202',
                'wikipedia': u'sk:Diaľnica D1 (Slovensko)',
            }, ways=[170954509]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 170954509,
                'network': u'SK:national',
            })

    def test_skregional(self):
        import dsl

        z, x, y = (16, 36083, 22805)

        self.generate_fixtures(
            dsl.is_in('SK', z, x, y),
            # https://www.openstreetmap.org/way/4694958
            dsl.way(4694958, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'90',
                'ref': u'511',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'SK:rural',
            }),
            dsl.relation(1, {
                'distance': u'88.837 km',
                'network': u'sk:regional',
                'ref': u'511',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q13402720',
                'wikipedia': u'sk:Cesta II. triedy 511 (Slovensko)',
            }, ways=[4694958]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4694958,
                'network': u'SK:regional',
            })

    def test_uainternational(self):
        import dsl

        z, x, y = (16, 38287, 23043)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/235109184
            dsl.way(235109184, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk_link',
                'loc_ref': u'Т-16-16',
                'oneway': u'yes',
                'ref': u'М-05',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Київ - Одеса + Обхід м. Одеса',
                'distance': u'537.2',
                'name': u'Автошлях М-05',
                'network': u'ua:international',
                'ref': u'М-05',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1051588',
                'wikipedia': u'uk:Автошлях М 05',
            }, ways=[235109184]),
            dsl.relation(2, {
                'distance': u'106.7',
                'loc_ref': u'Т-16-16',
                'name': u'Автошлях Т-16-16',
                'network': u'ua:territorial:ods',
                'ref': u'Т-16-16',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q12076394',
                'wikipedia': u'uk:Автошлях Т 1616',
            }, ways=[235109184]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 235109184,
                'shield_text': u'М05',
                'network': u'UA:international',
            })

    def test_ualocal(self):
        import dsl

        z, x, y = (16, 37525, 22222)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/386932416
            dsl.way(386932416, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'ref': u'О201722',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Великі Дедеркали-Ямпіль',
                'distance': u'3.7',
                'name': u'Автошлях О201722',
                'network': u'ua:local',
                'ref': u'О201722',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[386932416]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 386932416,
                'shield_text': type(None),
                'network': u'UA:local',
            })

    def test_ualocalzht(self):
        # we don't output shield text for the UA:local network, as they are
        # minor roads which don't appear to get shields.
        import dsl

        z, x, y = (16, 38025, 22012)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/368445267
            dsl.way(368445267, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'unclassified',
                'layer': u'1',
                'maxspeed': u'50',
                'ref': u'С061209',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'/ Забране - Візня / - Сичівка через Луки',
                'distance': u'5.6',
                'loc_ref': u'С061209',
                'name': u'Автошлях С061209',
                'network': u'ua:local:zht',
                'ref': u'С061209',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[368445267]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 368445267,
                'shield_text': type(None),
                'network': type(None),
            })

    def test_uanational(self):
        import dsl

        z, x, y = (16, 37677, 22392)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/131492257
            dsl.way(131492257, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'maxspeed': u'50',
                'name': u'Сковороди вулиця',
                'name:en': u'Skovorody Street',
                'name:ru': u'Сковороды улица',
                'name:uk': u'Сковороди вулиця',
                'nat_ref': u'Н-03',
                'oneway': u'yes',
                'ref': u'Н-03',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'337.7',
                'name': u'Автошлях Н-03',
                'nat_ref': u'Н-03',
                'network': u'ua:national',
                'ref': u'Н-03',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1126976',
                'wikipedia': u'uk:Автошлях Н 03',
            }, ways=[131492257]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 131492257,
                'shield_text': u'Н03',
                'network': u'UA:national',
            })

    def test_uaregional(self):
        import dsl

        z, x, y = (16, 38056, 22443)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/162675995
            dsl.way(162675995, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'oneway': u'yes',
                'ref': u'Р-17;Р-33',
                'reg_ref': u'Р-17;Р-33',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'366.3',
                'name': u'Автошлях Р-33',
                'network': u'ua:regional',
                'old_ref': u'Т-02-01',
                'ref': u'Р-33',
                'reg_ref': u'Р-33',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q12076174',
                'wikipedia': u'uk:Автошлях Р 33',
            }, ways=[162675995]),
            dsl.relation(2, {
                'distance': u'157.2',
                'name': u'Автошлях Р-17',
                'network': u'ua:regional',
                'ref': u'Р-17',
                'reg_ref': u'Р-17',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q12076160',
                'wikipedia': u'uk:Автошлях Р 17',
            }, ways=[162675995]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 162675995,
                'shield_text': u'Р17',
                'network': u'UA:regional',
                'all_shield_texts': [u'Р17', u'Р33'],
                'all_networks': ['UA:regional', 'UA:regional'],
            })

    def test_uaterrirorialluhansk(self):
        # note the spelling mistake: "ua:terrirorial" vs "ua:territorial".
        # we can't normalise this (it's a data error), and the ref is a
        # C-class, which is very minor and doesn't appear to get a shield.
        import dsl

        z, x, y = (16, 40024, 22539)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/234326072
            dsl.way(234326072, dsl.tile_diagonal(z, x, y), {
                'highway': u'unclassified',
                'ref': u'C131613',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Красна Талівка - Благовіщенка',
                'distance': u'19.2',
                'name': u'Автошлях С131613',
                'name:uk': u'Автошлях С131613',
                'network': u'ua:terrirorial:luhansk',
                'ref': u'С131613',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[234326072]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 234326072,
                'shield_text': type(None),
                'network': type(None),
            })

    def test_uaterritorial(self):
        import dsl

        z, x, y = (16, 38295, 22265)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/390887321
            dsl.way(390887321, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'Т-10-09',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'description': u'Устимівка — Гребінки — Узин',
                'distance': u'37.3',
                'loc_ref': u'Т-10-09',
                'name': u'Автошлях Т-10-09',
                'network': u'ua:territorial',
                'ref': u'Т-10-09',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q12076344',
                'wikipedia': u'uk:Автошлях Т 1009',
            }, ways=[390887321]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 390887321,
                'shield_text': u'Т1009',
                'network': u'UA:territorial',
            })

    def test_uaterritorialhrk(self):
        import dsl

        z, x, y = (16, 39529, 22169)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/458709032
            dsl.way(458709032, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'loc_ref': u'Т-21-04',
                'ref': u'Т-21-04',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'description': u'Харкiв-Вовчанськ-КПП "Чугунiвка"',
                'distance': u'116.6',
                'loc_ref': u'Т-21-04',
                'name': u'Автошлях Т-21-04',
                'network': u'ua:territorial:hrk',
                'ref': u'Т-21-04',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q4056227',
                'wikipedia': u'uk:Автошлях Т 2104',
            }, ways=[458709032]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 458709032,
                'shield_text': u'Т2104',
                'network': u'UA:territorial',
            })

    def test_uaterritorialhrs(self):
        import dsl

        z, x, y = (16, 38685, 23182)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/131709575
            dsl.way(131709575, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'1',
                'loc_ref': u'Т-22-16',
                'oneway': u'yes',
                'ref': u'Т-22-16',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Гола Пристань — Залізний Порт',
                'distance': u'50.8 km',
                'loc_ref': u'Т-22-16',
                'name': u'Автошлях Т-22-16',
                'name:ru': u'Автодорога Т-22-16',
                'network': u'ua:territorial:hrs',
                'ref': u'Т-22-16',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q12076471',
                'wikipedia': u'uk:Автошлях_Т_2216',
            }, ways=[131709575]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 131709575,
                'shield_text': u'Т2216',
                'network': u'UA:territorial',
            })

    def test_uaterritoriallug(self):
        import dsl

        z, x, y = (16, 39986, 22756)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/34911803
            dsl.way(34911803, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'loc_ref': u'Т-13-22',
                'ref': u'Т-13-22',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Краснодон - Антрацит',
                'distance': u'81.7',
                'loc_ref': u'Т-13-22',
                'name': u'Автошлях Т-13-22',
                'network': u'ua:territorial:lug',
                'ref': u'Т-13-22',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[34911803]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 34911803,
                'shield_text': u'Т1322',
                'network': u'UA:territorial',
            })

    def test_uaterritorialods(self):
        import dsl

        z, x, y = (16, 38023, 23487)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/60205997
            dsl.way(60205997, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'loc_ref': u'Т-16-07',
                'ref': u'Т-16-07',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Ізмаїл - Кілія - Вилкове',
                'distance': u'68.3',
                'loc_ref': u'Т-16-07',
                'name': u'Автошлях Т-16-07',
                'network': u'ua:territorial:ods',
                'ref': u'Т-16-07',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q12076386',
                'wikipedia': u'uk:Автошлях Т 1607',
            }, ways=[60205997]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 60205997,
                'shield_text': u'Т1607',
                'network': u'UA:territorial',
            })

    def test_uaterritorialpol(self):
        import dsl

        z, x, y = (16, 38828, 22287)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/345592644
            dsl.way(345592644, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'loc_ref': u'Т-17-09',
                'name': u'Фрунзе вулиця',
                'name:en': u'Frunze Street',
                'ref': u'Т-17-09',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'51.5',
                'loc_ref': u'Т-17-09',
                'name': u'Автошлях Т-17-09',
                'network': u'ua:territorial:pol',
                'ref': u'Т-17-09',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q12076418',
                'wikipedia': u'uk:Автошлях Т 1709',
            }, ways=[345592644]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 345592644,
                'shield_text': u'Т1709',
                'network': u'UA:territorial',
            })

    def test_uaterritorialzap(self):
        import dsl

        z, x, y = (16, 39359, 22998)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/189288216
            dsl.way(189288216, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'loc_ref': u'Т-08-13',
                'name': u'Соборна вулиця',
                'name:ru': u'Соборная улица',
                'name:uk': u'Соборна вулиця',
                'old_name': u'Леніна вулиця',
                'old_name:ru': u'Ленина улица',
                'old_name:uk': u'Леніна вулиця',
                'ref': u'Т-08-13',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Токмак - Чернігівка',
                'distance': u'31.1',
                'loc_ref': u'Т-08-13',
                'name': u'Автошлях Т-08-13',
                'network': u'ua:territorial:zap',
                'ref': u'Т-08-13',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q12076329',
                'wikipedia': u'uk:Автошлях Т 0813',
            }, ways=[189288216]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 189288216,
                'shield_text': u'Т0813',
                'network': u'UA:territorial',
            })

    def test_uatertiary(self):
        import dsl

        z, x, y = (16, 39722, 22495)

        self.generate_fixtures(
            dsl.is_in('UA', z, x, y),
            # https://www.openstreetmap.org/way/298743622
            dsl.way(298743622, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'name': u'Куйбишева вулиця',
                'name:en': u'Kuybyshev Street',
                'name:ru': u'Куйбышева улица',
                'name:uk': u'Куйбишева вулиця',
                'ref': u'О-130501',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Кремінна — Торське',
                'distance': u'10.2',
                'loc_ref': u'О-130501',
                'network': u'ua:tertiary',
                'ref': u'О-130501',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[298743622]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 298743622,
                'shield_text': type(None),
                'network': u'UA:tertiary',
            })

    def test_uznational(self):
        import dsl

        z, x, y = (16, 44858, 24915)

        self.generate_fixtures(
            dsl.is_in('UZ', z, x, y),
            # https://www.openstreetmap.org/way/213676743
            dsl.way(213676743, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'uz:national',
                'ref': u'4P52',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[213676743]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 213676743,
                'network': u'UZ:national',
            })

    def test_zacapetown(self):
        import dsl

        z, x, y = (16, 36119, 39340)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/4290234
            dsl.way(4290234, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'maxspeed': u'60',
                'name': u'Buitensingel Street',
                'ref': u'M3',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'ZA:urban',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'direction': u'north',
                'name': u'M3 (northbound)',
                'network': u'za:capetown',
                'ref': u'M3',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4290234]),
            dsl.relation(2, {
                'direction': u'south',
                'name': u'M3 (southbound)',
                'network': u'za:capetown',
                'ref': u'M3',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4290234]),
        )

        # note: ZA M-number shields have the M as part of the shield artwork
        # above the number, so removed it from the shield text.
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4290234,
                'shield_text': '3',
                'network': u'ZA:metropolitan',
            })

    def test_zanational(self):
        import dsl

        z, x, y = (16, 38071, 38140)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/257873380
            dsl.way(257873380, dsl.tile_diagonal(z, x, y), {
                'destination:backward': u'Durban',
                'destination:forward': u'Harrismith;Bethlehem',
                'destination:ref:backward': u'N3',
                'destination:ref:forward': u'N5',
                'destination:ref:to:forward': u'R74',
                'destination:to:forward': u'Phuthaditjaba',
                'highway': u'trunk',
                'lanes': u'2',
                'maxspeed': u'60',
                'oneway': u'no',
                'ref': u'N5',
                'smoothness': u'excellent',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'ZA:urban',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'direction': u'west',
                'name': u'SADC 231 (westbound)',
                'network': u'sadc',
                'ref': u'SADC 231',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[257873380]),
            dsl.relation(2, {
                'direction': u'east',
                'name': u'SADC 231 (eastbound)',
                'network': u'sadc',
                'ref': u'SADC 231',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[257873380]),
            dsl.relation(3, {
                'direction': u'west',
                'name': u'N5 (westbound)',
                'network': u'za:national',
                'ref': u'N5',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[257873380]),
            dsl.relation(4, {
                'direction': u'east',
                'name': u'N5 (eastbound)',
                'network': u'za:national',
                'ref': u'N5',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[257873380]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 257873380,
                'network': u'ZA:national',
            })

    def test_zaregional(self):
        import dsl

        z, x, y = (16, 37952, 37936)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/481135283
            dsl.way(481135283, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary_link',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'direction': u'south',
                'name': u'R26 (southbound)',
                'network': u'za:regional',
                'ref': u'R26',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[481135283]),
        )

        # note: the ZA shields have the R above the number (in a diamond for
        # provincial rather than regional shields), so removed that from the
        # shield text, as it's part of the artwork.
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 481135283,
                'shield_text': '26',
                'network': u'ZA:provincial',
            })

    def test_grnational(self):
        import dsl

        z, x, y = (16, 37113, 24489)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/561077644
            dsl.way(561077644, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'int_name': u'Drama - Kato Nevrokopi',
                'lanes': u'2',
                'name': u'Δράμα - Κάτω Νευροκόπι',
                'oneway': u'yes',
                'ref': u'ΕΟ57',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Εθνική Οδός 57 (Δράμα - Εξοχή)',
                'network': u'gr:national',
                'ref': u'ΕΟ57',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q5601824',
            }, ways=[561077644]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 561077644,
                'shield_text': '57',
                'network': u'GR:national',
            })

    def test_kzregional(self):
        import dsl

        z, x, y = (16, 42178, 24035)

        self.generate_fixtures(
            dsl.is_in('KZ', z, x, y),
            # https://www.openstreetmap.org/way/26395642
            dsl.way(26395642, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'name': u'Подъезд к станции Ералиево',
                'ref': u'KR-KG-4',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'distance': u'12. km',
                'name': u'Подъезд к станции Ералиево',
                'network': u'kz:regional',
                'ref': u'KR-KG-4',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[26395642]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26395642,
                'network': u'KZ:regional',
            })

    def test_biroads(self):
        import dsl

        z, x, y = (16, 38215, 33392)

        self.generate_fixtures(
            dsl.is_in('BI', z, x, y),
            # https://www.openstreetmap.org/way/208822117
            dsl.way(208822117, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'2',
                'name': u'RN2',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'survey': u'GPS',
            }),
            dsl.relation(1, {
                'name': u'RN2',
                'network': u'BI-roads',
                'ref': u'RN2',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[208822117]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 208822117,
                'network': u'BI:road',
            })

    def test_boroads(self):
        import dsl

        z, x, y = (16, 20552, 36089)

        self.generate_fixtures(
            dsl.is_in('BO', z, x, y),
            # https://www.openstreetmap.org/way/96056846
            dsl.way(96056846, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'name': u'Avenida Circunvalación',
                'oneway': u'yes',
                'ref': u'F1',
                'ref_1': u'F12',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'from': u'Desaguadero',
                'name': u'Ruta Nacional 1',
                'network': u'BO-roads',
                'operator': u'ABC',
                'ref': u'F1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'Bermejo',
                'type': u'route',
                'wikidata': u'Q1133917',
                'wikipedia': u'es:Ruta 1 (Bolivia)',
            }, ways=[96056846]),
            dsl.relation(2, {
                'from': u'Caihuasi (Cruce RN4)',
                'name': u'Ruta Nacional 12',
                'network': u'bo-roads',
                'operator': u'ABC',
                'ref': u'F12',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'Pisiga (Front Chile)',
                'type': u'route',
            }, ways=[96056846]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 96056846,
                'network': u'BO:road',
            })

    def test_boroads2(self):
        import dsl

        z, x, y = (16, 20742, 34783)

        self.generate_fixtures(
            dsl.is_in('BO', z, x, y),
            # https://www.openstreetmap.org/way/187629235
            dsl.way(187629235, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'junction': u'roundabout',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'from': u'Cruce F3 (Yucumo)',
                'name': u'Ruta Nacional 8',
                'network': u'BO-roads',
                'ref': u'F8',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'Guayanamerín',
                'type': u'route',
                'wikipedia': u'es:Ruta 8 (Bolivia)',
            }, ways=[187629235]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 187629235,
                'network': u'BO:road',
            })

    def test_boroads3(self):
        import dsl

        z, x, y = (16, 20418, 36170)

        self.generate_fixtures(
            dsl.is_in('BO', z, x, y),
            # https://www.openstreetmap.org/way/142334277
            dsl.way(142334277, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'maxspeed': u'80',
                'name': u'RN27: Ancaravi-Turco',
                'oneway': u'no',
                'ref': u'F27',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
            dsl.relation(1, {
                'from': u'Ancaravi',
                'is_in': u'Bolivia',
                'name': u'Ruta Nacional 27',
                'network': u'BO-Roads',
                'operator': u'ABC',
                'ref': u'F27',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'Juchus Huaylla (Cruce RN4)',
                'type': u'route',
            }, ways=[142334277]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 142334277,
                'network': u'BO:road',
            })

    def test_brbaroads(self):
        import dsl

        z, x, y = (16, 25787, 35137)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/552869142
            dsl.way(552869142, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'maxspeed': u'60',
                'name': u'Avenida Santos Dumont',
                'old_name': u'Estrada do Coco',
                'oneway': u'yes',
                'operator': u'CLN',
                'ref': u'BA-099',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'network': u'BR-BA-roads',
                'ref': u'BA-099',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[552869142]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 552869142,
                'shield_text': '099',
                'network': u'BR:BA',
            })

    def test_brmgroads(self):
        import dsl

        z, x, y = (16, 24235, 35954)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/355329134
            dsl.way(355329134, dsl.tile_diagonal(z, x, y), {
                'highway': u'residential',
                'name': u'Travessa VIII',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'BR-MG-roads',
                'ref': u'MG-188',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[355329134]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 355329134,
                'shield_text': '188',
                'network': u'BR:MG',
            })

    def test_brsp(self):
        import dsl

        z, x, y = (16, 24010, 37375)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/275485009
            dsl.way(275485009, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'name': u'Rodovia José Edgard Carneiro dos Santos',
                'oneway': u'no',
                'operator': u'DER',
                'ref': u'SP-193',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'BR-SP',
                'operator': u'DER',
                'ref': u'SP-193',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[275485009]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 275485009,
                'shield_text': '193',
                'network': u'BR:SP',
            })

    def test_brtoroads(self):
        import dsl

        z, x, y = (16, 24157, 35010)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/249260364
            dsl.way(249260364, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary_link',
                'lanes': u'1',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'network': u'BR-TO-roads',
                'ref': u'TO-050',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[249260364]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 249260364,
                'shield_text': '050',
                'network': u'BR:TO',
            })

    def test_cgroads(self):
        import dsl

        z, x, y = (16, 35672, 32984)

        self.generate_fixtures(
            dsl.is_in('CG', z, x, y),
            # https://www.openstreetmap.org/way/79513695
            dsl.way(79513695, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'ref': u'RN 2',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'network': u'CG-roads',
                'ref': u'RN 2',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[79513695]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 79513695,
                'network': u'CG:road',
            })

    def test_cmroads(self):
        import dsl

        z, x, y = (16, 34866, 32072)

        self.generate_fixtures(
            dsl.is_in('CM', z, x, y),
            # https://www.openstreetmap.org/way/203757381
            dsl.way(203757381, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'N2',
                'network': u'CM-roads',
                'ref': u'N2 (Cameroon)',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[203757381]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 203757381,
                'shield_text': 'N2',
                'network': u'CM:road',
            })

    def test_garoads(self):
        import dsl

        z, x, y = (16, 34888, 32456)

        self.generate_fixtures(
            dsl.is_in('GA', z, x, y),
            # https://www.openstreetmap.org/way/79297648
            dsl.way(79297648, dsl.tile_diagonal(z, x, y), {
                'access': u'yes',
                'highway': u'trunk',
                'ref': u'RN2',
                'source': u'openstreetmap.org',
                'start_date': u'befor 1970',
                'surface': u'unpaved',
            }),
            dsl.relation(1, {
                'network': u'GA-roads',
                'ref': u'RN2',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[79297648]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 79297648,
                'shield_text': 'N2',
                'network': u'GA:national',
            })

    def test_iqroads(self):
        import dsl

        z, x, y = (16, 40984, 26142)

        self.generate_fixtures(
            dsl.is_in('IQ', z, x, y),
            # https://www.openstreetmap.org/way/386326359
            dsl.way(386326359, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name:en': u'Highway 5',
                'network': u'IQ-roads',
                'ref': u'5',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[386326359]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 386326359,
                'network': u'IQ:road',
            })

    def test_lonetwork(self):
        import dsl

        z, x, y = (16, 51383, 28940)

        self.generate_fixtures(
            dsl.is_in('LA', z, x, y),
            # https://www.openstreetmap.org/way/477601864
            dsl.way(477601864, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'int_ref': u'AH12',
                'ref': u'13',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'int_ref': u'AH12',
                'name': u'Asian Highway AH12',
                'name:de': u'Asien Fernstraße AH12',
                'name:en': u'Asian Highway AH12',
                'name:ru': u'Азиатский маршрут AH12',
                'network': u'AsianHighway',
                'ref': u'AH12',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q727626',
                'wikipedia': u'en:AH12',
            }, ways=[477601864]),
            dsl.relation(2, {
                'network': u'LO-network',
                'ref': u'13',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[477601864]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 477601864,
                'network': u'LA:national',
            })

    def test_mzroads(self):
        import dsl

        z, x, y = (16, 38471, 36963)

        self.generate_fixtures(
            dsl.is_in('MZ', z, x, y),
            # https://www.openstreetmap.org/way/130302571
            dsl.way(130302571, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'old_ref': u'423',
                'ref': u'N222',
                'source': u'openstreetmap.org',
                'surface': u'unpaved',
            }),
            dsl.relation(1, {
                'network': u'MZ-roads',
                'old_ref': u'423',
                'ref': u'N222',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[130302571]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 130302571,
                'network': u'MZ:road',
            })

    def test_thnetwork(self):
        import dsl

        z, x, y = (16, 51091, 30043)

        self.generate_fixtures(
            dsl.is_in('TH', z, x, y),
            # https://www.openstreetmap.org/way/449165197
            dsl.way(449165197, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'junction': u'roundabout',
                'name': u'ถนนพหลโยธิน',
                'name:en': u'Phahon Yothin Road',
                'name:th': u'ถนนพหลโยธิน',
                'oneway': u'yes',
                'ref': u'1',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'ถนนพหลโยธิน',
                'name:de': u'Phahon Yothin Straße',
                'name:en': u'Phahon Yothin Road',
                'name:ja': u'パホンヨーティン通り',
                'name:nl': u'Phahonyothin',
                'name:th': u'ถนนพหลโยธิน',
                'name:zh': u'拍鳳裕庭路',
                'network': u'TH-network',
                'ref': u'1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q2063769',
                'wikipedia': u'th:ถนนพหลโยธิน',
            }, ways=[449165197]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 449165197,
                'network': u'TH:network',
            })

    def test_throads(self):
        import dsl

        z, x, y = (16, 51840, 29552)

        self.generate_fixtures(
            dsl.is_in('TH', z, x, y),
            # https://www.openstreetmap.org/way/544361823
            dsl.way(544361823, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'TH-roads',
                'ref': u'212',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[544361823]),
            dsl.relation(2, {
                'network': u'TH-roads',
                'ref': u'240',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[544361823]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 544361823,
                'network': u'TH:road',
            })

    def test_trmotorway(self):
        import dsl

        z, x, y = (16, 37688, 25164)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/184329678
            dsl.way(184329678, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 87',
                'lanes': u'3',
                'maxspeed': u'90',
                'minspeed': u'40',
                'name': u'İzmir Çevre Yolu',
                'oneway': u'yes',
                'ref': u'O-30',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name:bg': u'Европейски път Е 87, Турция',
                'name:de': u'Europastraße 87, Türkei',
                'name:en': u'European Route 87, Turkey',
                'network': u'e-road',
                'ref': u'E 87',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[184329678]),
            dsl.relation(2, {
                'network': u'TR-motorway',
                'ref': u'O-30',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[184329678]),
            dsl.relation(3, {
                'highway': u'motorway',
                'name': u'İzmir Çevre Yolu',
                'network': u'TR-motorway',
                'ref': u'O-30',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[184329678]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 184329678,
                'network': u'TR:motorway',
            })

    def test_trroad(self):
        import dsl

        z, x, y = (16, 38708, 24805)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/226373024
            dsl.way(226373024, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway_link',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description': u'Ankara Çevre Otoyolu',
                'network': u'TR-road',
                'ref': u'O-20',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[226373024]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 226373024,
                'shield_text': 'O20',
                'network': u'TR:motorway',
            })

    def test_trroads(self):
        import dsl

        z, x, y = (16, 37787, 24573)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/171673241
            dsl.way(171673241, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'maxspeed': u'50',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'TR-roads',
                'ref': u'D 555',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[171673241]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 171673241,
                'shield_text': 'D555',
                'network': 'TR:highway',
            })

    def test_zmroads(self):
        import dsl

        z, x, y = (16, 37204, 35232)

        self.generate_fixtures(
            dsl.is_in('ZM', z, x, y),
            # https://www.openstreetmap.org/way/44146353
            dsl.way(44146353, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'primary',
                'layer': u'1',
                'ref': u'M8',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'eef': u'M8',
                'name': u'M8',
                'network': u'ZM-roads',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[44146353]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 44146353,
                'network': u'ZM:road',
            })
