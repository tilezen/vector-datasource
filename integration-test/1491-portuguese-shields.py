# -*- encoding: utf-8 -*-
from . import FixtureTest


class PortugueseShieldTest(FixtureTest):

    def test_a1_ptmotorway(self):
        import dsl

        z, x, y = (16, 31167, 24998)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/4246625
            dsl.way(4246625, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 01;E 80',
                'lanes': u'3',
                'maxspeed': u'120',
                'minspeed': u'50',
                'name': u'Autoestrada do Norte',
                'oneway': u'yes',
                'ref': u'A 1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'toll': u'yes',
            }),
            dsl.relation(1, {
                'from': u'Valença',
                'name': u'Itinerário Principal do Litoral',
                'network': u'PT:national',
                'ref': u'IP 1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'Castro Marim',
                'type': u'route',
                'wikidata': u'Q10299438',
                'wikipedia': u'pt:IP1',
            }, ways=[4246625]),
            dsl.relation(2, {
                'distance': u'303',
                'name': u'Autoestrada do Norte',
                'network': u'PT:national',
                'operator': u'Brisa',
                'ref': u'A 1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q786462',
                'wikipedia': u'pt:A1 (autoestrada)',
            }, ways=[4246625]),
            dsl.relation(3, {
                'description': u'European Route E80, Spain, west-west',
                'name': u'European Route 80',
                'name:bg': u'Европейски път E 80, Испания, 1',
                'name:de': u'Europastraße 80',
                'name:en': u'European Route 80',
                'name:es': u'Ruta Europea 80',
                'name:fr': u'route européenne 80',
                'network': u'e-road',
                'note': u'European Route E80, Spain',
                'ref': u'E 80',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4246625]),
            dsl.relation(4, {
                'name': u'E 01 Portugal (north)',
                'network': u'e-road',
                'ref': u'E 01',
                'route': u'road',
                'section': u'Portugal (north)',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'en:European route E01',
            }, ways=[4246625]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4246625,
                'network': 'PT:motorway',
                'shield_text': 'A1',
                'all_networks': ['PT:motorway', 'PT:primary', 'e-road',
                                 'e-road'],
                'all_shield_texts': ['A1', 'IP1', 'E1', 'E80'],
            })

    def test_ip4_ptmotorway(self):
        import dsl

        z, x, y = (16, 31531, 24384)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/10500592
            dsl.way(10500592, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'oneway': u'yes',
                'ref': u'IP 4',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Itinerário Principal Porto-Quintanilha',
                'ref': u'IP 4',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[10500592]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 10500592,
                'network': 'PT:primary',
                'shield_text': 'IP4',
            })

    def test_ic23_ptmotorway(self):
        import dsl

        z, x, y = (16, 31200, 24529)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/4257028
            dsl.way(4257028, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'4',
                'oneway': u'yes',
                'placement': u'middle_of:2',
                'ref': u'IC 23',
                'source': u'openstreetmap.org',
                'turn:lanes': u'through|through|through|right',
            }),
            dsl.relation(1, {
                'highway': u'motorway',
                'name': u'Circular Regional Interior do Porto',
                'ref': u'A 20',
                'route': u'road',
                'short_name': u'CRIP',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4257028]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4257028,
                'network': 'PT:motorway',
                'shield_text': 'A20',
                'all_networks': ['PT:motorway', 'PT:secondary'],
                'all_shield_texts': ['A20', 'IC23'],
            })

    def test_n247_ptnational(self):
        import dsl

        z, x, y = (16, 31054, 25056)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/3979163
            dsl.way(3979163, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'cycleway:right': u'yes',
                'highway': u'primary',
                'lanes': u'2',
                'oneway': u'no',
                'ref': u'EN 247',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3979163,
                'network': u'PT:national',
                'shield_text': u'N247',
            })

    def test_r228_ptregional(self):
        import dsl

        z, x, y = (16, 29669, 26451)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/5054578
            dsl.way(5054578, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'ER 228',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'description': u'Rosário – Serra de Água',
                'ref': u'ER 228',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[5054578]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 5054578,
                'network': u'PT:regional',
                'shield_text': u'R228',
            })

    def test_m550_ptmunicipal(self):
        import dsl

        z, x, y = (16, 31054, 25059)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/10579957
            dsl.way(10579957, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'1',
                'oneway': u'no',
                'ref': u'EM 550',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 10579957,
                'network': u'PT:municipal',
                'shield_text': u'M550',
            })

    def test_ve5_ptexpress(self):
        import dsl

        z, x, y = (16, 29700, 26472)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/24992736
            dsl.way(24992736, dsl.tile_diagonal(z, x, y), {
                'alt_name': u'ER 102',
                'highway': u'primary',
                'lanes': u'3',
                'lanes:backward': u'1',
                'lanes:forward': u'2',
                'layer': u'-1',
                'name': u'Túnel das Eiras',
                'ref': u'VE 5',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'tunnel': u'yes',
                'turn:lanes:backward': u'through',
                'turn:lanes:forward': u'through|through',
            }),
            dsl.relation(1, {
                'description': u'Caniço – Camacha',
                'name': u'Estrada Regional 102',
                'ref': u'ER 102',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[24992736]),
            dsl.relation(2, {
                'alt_name': u'ER 102',
                'name': u'Via Expresso 5',
                'ref': u'VE 5',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[24992736]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 24992736,
                'network': u'PT:express',
                'shield_text': u'VE5',
                'all_networks': ['PT:express', 'PT:regional'],
                'all_shield_texts': ['VE5', 'R102'],
            })

    def test_vr1_ptrapid(self):
        import dsl

        z, x, y = (16, 29710, 26466)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/19854039
            dsl.way(19854039, dsl.tile_diagonal(z, x, y), {
                'alt_name': u'Via Rápida 1',
                'bicycle': u'no',
                'foot': u'no',
                'highway': u'trunk',
                'maxspeed': u'80',
                'motor_vehicle': u'designated',
                'oneway': u'yes',
                'ref': u'VR 1',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
            dsl.relation(1, {
                'description': u'Litoral da ilha da Madeira',
                'name': u'Estrada Regional 101',
                'ref': u'ER 101',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[19854039]),
            dsl.relation(2, {
                'alt_name': u'Via Rápida',
                'name': u'Via Rápida 1',
                'operator': u'Via Litoral',
                'ref': u'VR 1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[19854039]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 19854039,
                'network': u'PT:rapid',
                'shield_text': u'VR1',
                'all_networks': ['PT:rapid', 'PT:regional'],
                'all_shield_texts': ['VR1', 'R101'],
            })

    def test_a40_ptmotorway(self):
        import dsl

        z, x, y = (16, 31097, 25092)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/8140216
            dsl.way(8140216, dsl.tile_diagonal(z, x, y), {
                'destination': u'Lisboa',
                'highway': u'trunk',
                'lanes': u'2',
                'oneway': u'yes',
                'ref': u'IC 22',
                'source': u'openstreetmap.org',
                'toll': u'no',
            }),
            dsl.relation(1, {
                'distance': u'4',
                'name': u'Radial de Odivelas',
                'nat_ref': u'IC 22',
                'ref': u'IC 22;A 40',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[8140216]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 8140216,
                'network': u'PT:motorway',
                'shield_text': u'A40',
                'all_networks': ['PT:motorway', 'PT:secondary'],
                'all_shield_texts': ['A40', 'IC22'],
            })

    def test_ic6_ptsecondary(self):
        import dsl

        z, x, y = (16, 31297, 24737)

        self.generate_fixtures(
            dsl.is_in('PT', z, x, y),
            # https://www.openstreetmap.org/way/569472716
            dsl.way(569472716, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'oneway': u'yes',
                'ref': u'IC 6',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 569472716,
                'network': u'PT:secondary',
                'shield_text': u'IC6',
            })
