# -*- encoding: utf-8 -*-
from . import FixtureTest


class SpanishShieldTest(FixtureTest):

    def test_a1_esa(self):
        import dsl

        z, x, y = (16, 32092, 24415)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/570170886
            dsl.way(570170886, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 05',
                'lanes': u'2',
                'name': u'Autovía del Norte',
                'oneway': u'yes',
                'ref': u'A-1',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Autovía del Norte',
                'network': u'ES:A-road',
                'ref': u'A-1',
                'ref:colour': u'#19408B',
                'ref:colour_bg': u'#19408B',
                'ref:colour_tx': u'white',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'es:Autovía del Norte',
            }, ways=[570170886]),
            dsl.relation(2, {
                'name': u'E 05',
                'network': u'e-road',
                'ref': u'E 05',
                'route': u'road',
                'section': u'Spain (north-south)',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q693493',
                'wikipedia': u'en:European route E5',
            }, ways=[570170886]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 570170886,
                'network': u'ES:A-road',
                'shield_text': u'A-1',
                'all_networks': ['ES:A-road', 'e-road'],
                'all_shield_texts': ['A-1', 'E-5'],
            })

    def test_ap1_esa(self):
        import dsl

        z, x, y = (16, 32116, 24233)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/34078314
            dsl.way(34078314, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 05;E 80',
                'lanes': u'2',
                'name': u'Autopista del Norte',
                'oneway': u'yes',
                'ref': u'AP-1',
                'source': u'openstreetmap.org',
                'toll': u'yes',
            }),
            dsl.relation(1, {
                'name': u'Autopista del Norte',
                'name:es': u'Autopista Vitoria/Gasteiz-Irun por Eibar',
                'name:eu': u'Gasteiz-Irun, Eibartik autobidea',
                'network': u'ES:A-road',
                'ref': u'AP-1',
                'ref:colour': u'#19408B',
                'ref:colour_bg': u'#19408B',
                'ref:colour_tx': u'white',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q788262',
                'wikipedia': u'es:Autopista del Norte',
            }, ways=[34078314]),
            dsl.relation(2, {
                'name': u'E 05',
                'network': u'e-road',
                'ref': u'E 05',
                'route': u'road',
                'section': u'Spain (north-south)',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q693493',
                'wikipedia': u'en:European route E5',
            }, ways=[34078314]),
            dsl.relation(3, {
                'description': u'European Route E80, Spain, middle',
                'name': u'European Route 80',
                'name:bg': u'Европейски път E 80, Испания, 3',
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
            }, ways=[34078314]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 34078314,
                'network': 'ES:A-road',
                'shield_text': 'AP-1',
                'all_networks': ['ES:A-road', 'e-road', 'e-road'],
                'all_shield_texts': ['AP-1', 'E-5', 'E-80'],
            })

    def test_n232_esnroad(self):
        import dsl

        z, x, y = (16, 32166, 24163)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/294840103
            dsl.way(294840103, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'name': u'Carretera Santander - Vinaroz',
                'ref': u'N-232',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Carretera Santander - Vinaroz',
                'ref': u'N-232',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[294840103]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 294840103,
                'network': u'ES:N-road',
                'shield_text': u'N-232',
            })

    def test_niii_esnroad(self):
        import dsl

        z, x, y = (16, 32390, 24913)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/395960441
            dsl.way(395960441, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'maxspeed': u'100',
                'ref': u'N-III',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 395960441,
                'network': u'ES:N-road',
                'shield_text': u'N-III',
            })

    def test_ab301_es(self):
        import dsl

        z, x, y = (16, 32501, 25085)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/155558564
            dsl.way(155558564, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'AB-301',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 155558564,
                'network': u'ES:province',
                'shield_text': u'AB-301',
            })

    def test_ac305_es(self):
        import dsl

        z, x, y = (16, 31161, 24161)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/7753386
            dsl.way(7753386, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes:backward': u'1',
                'lanes:forward': u'1',
                'oneway': u'no',
                'ref': u'AC-305',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 7753386,
                'network': u'ES:province',
                'shield_text': u'AC-305',
            })

    def test_ae3_es(self):
        import dsl

        z, x, y = (16, 31724, 24039)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/194846533
            dsl.way(194846533, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Moreda-Santibáñez',
                'oneway': u'yes',
                'ref': u'AE-3',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 194846533,
                'network': u'ES:province',
                'shield_text': u'AE-3',
            })

    def test_ag57n_es(self):
        import dsl

        z, x, y = (16, 31164, 24295)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/9218818
            dsl.way(9218818, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'2',
                'motorroad': u'yes',
                'oneway': u'yes',
                'ref': u'AG-57N',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 9218818,
                'network': u'ES:autonoma',
                'shield_text': u'AG-57N',
            })

    def test_ai81_es(self):
        import dsl

        z, x, y = (16, 31695, 23942)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4600940
            dsl.way(4600940, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'2',
                'maxspeed': u'120',
                'name:es': u'Acceso al centro de Avilés',
                'nat_ref': u'AI-81',
                'oneway': u'yes',
                'ref': u'AI-81',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4600940,
                'network': u'ES:city',
                'shield_text': u'AI-81',
            })

    def test_al14_es(self):
        import dsl

        z, x, y = (16, 32315, 25546)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23290717
            dsl.way(23290717, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'layer': u'1',
                'maxspeed': u'50',
                'name': u'Acceso oeste a Almería',
                'oneway': u'yes',
                'ref': u'AL-14',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23290717,
                'network': u'ES:province',
                'shield_text': u'AL-14',
            })

    def test_araa1_es(self):
        import dsl

        z, x, y = (16, 32644, 24435)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/53213667
            dsl.way(53213667, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'motorway',
                'layer': u'1',
                'name': u'ARA-A1',
                'oneway': u'yes',
                'ref': u'ARA-A1',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 53213667,
                'network': u'ES:autonoma',
                'shield_text': u'ARA-A1',
            })

    def test_as266_es(self):
        import dsl

        z, x, y = (16, 31715, 23970)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/407780
            dsl.way(407780, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'1',
                'name': u'Oviedo-Porceyo',
                'old_ref': u'AS-18;N-630',
                'oneway': u'yes',
                'ref': u'AS-266',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 407780,
                'network': u'ES:province',
                'shield_text': u'AS-266',
            })

    def test_av20_es(self):
        import dsl

        z, x, y = (16, 31915, 24648)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4300495
            dsl.way(4300495, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'2',
                'maxspeed': u'120',
                'name': u'Circunvalación de Ávila',
                'nat_ref': u'AV-20',
                'old_ref': u'A-51',
                'oneway': u'yes',
                'ref': u'AV-20',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Circunvalación de Ávila',
                'nat_ref': u'AV-20',
                'network': u'ES:A-road',
                'old_ref': u'A-51',
                'operator': u'Junta de Castilla y León',
                'ref': u'AV-20',
                'ref:colour': u'#19408B',
                'ref:colour_bg': u'#19408B',
                'ref:colour_tx': u'white',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'es:A-51',
            }, ways=[4300495]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4300495,
                'network': u'ES:province',
                'shield_text': u'AV-20',
            })

    def test_b250a_es(self):
        import dsl

        z, x, y = (16, 33151, 24492)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/8376343
            dsl.way(8376343, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'oneway': u'yes',
                'ref': u'B-250a',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 8376343,
                'network': u'ES:province',
                'shield_text': u'B-250a',
            })

    def test_ba20_es(self):
        import dsl

        z, x, y = (16, 31508, 25072)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23268459
            dsl.way(23268459, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'oneway': u'yes',
                'ref': u'BA-20',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23268459,
                'network': u'ES:province',
                'shield_text': u'BA-20',
            })

    def test_bi633_es(self):
        import dsl

        z, x, y = (16, 32313, 24010)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4324114
            dsl.way(4324114, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'highway': u'primary',
                'lanes': u'2',
                'oneway': u'no',
                'ref': u'BI-633',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4324114,
                'network': u'ES:province',
                'shield_text': u'BI-633',
            })

    def test_bp5002_es(self):
        import dsl

        z, x, y = (16, 33185, 24451)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/21292155
            dsl.way(21292155, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'name': u'Carretera de Granollers al Masnou',
                'ref': u'BP-5002',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 21292155,
                'network': u'ES:province',
                'shield_text': u'BP-5002',
            })

    def test_bu571_es(self):
        import dsl

        z, x, y = (16, 32117, 24043)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/6279079
            dsl.way(6279079, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Carretera al Portillo de la Sía',
                'ref': u'BU-571',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 6279079,
                'network': u'ES:province',
                'shield_text': u'BU-571',
            })

    def test_bv4132z_es(self):
        import dsl

        z, x, y = (16, 33109, 24320)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/14488252
            dsl.way(14488252, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'ref': u'BV-4132z',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 14488252,
                'network': u'ES:province',
                'shield_text': u'BV-4132z',
            })

    def test_c250_es(self):
        import dsl

        z, x, y = (16, 33285, 24342)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4784144
            dsl.way(4784144, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'C-250',
                'ref': u'C-250',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4784144,
                'network': u'ES:autonoma',
                'shield_text': u'C-250',
            })

    def test_ca901_es(self):
        import dsl

        z, x, y = (16, 32072, 23966)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4336684
            dsl.way(4336684, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'1',
                'name': u'Calle de San Fernando',
                'oneway': u'yes',
                'postal_code': u'39010',
                'ref': u'CA-901',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4336684,
                'network': u'ES:autonoma',
                'shield_text': u'CA-901',
            })

    def test_cc21_es(self):
        import dsl

        z, x, y = (16, 31598, 24937)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/22966379
            dsl.way(22966379, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'highway': u'trunk',
                'junction': u'roundabout',
                'lanes': u'2',
                'layer': u'0',
                'ref': u'CC-21',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'operator': u'Ministerio de Fomento',
                'ref': u'N-521',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[22966379]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22966379,
                'network': u'ES:N-road',
                'shield_text': u'N-521',
                'all_networks': ['ES:N-road', 'ES:province'],
                'all_shield_texts': ['N-521', 'CC-21'],
            })

    def test_che1504_es(self):
        import dsl

        z, x, y = (16, 32543, 24286)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/32367394
            dsl.way(32367394, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'CHE-1504',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 32367394,
                'network': u'ES:city',
                'shield_text': u'CHE-1504',
            })

    def test_chms1_es(self):
        import dsl

        z, x, y = (16, 31565, 24189)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/37524381
            dsl.way(37524381, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'lanes': u'2',
                'maxspeed': u'50',
                'ref': u'CHMS-1',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 37524381,
                'network': u'ES:city',
                'shield_text': u'CHMS-1',
            })

    def test_cl621_es(self):
        import dsl

        z, x, y = (16, 31752, 24249)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4860096
            dsl.way(4860096, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'2',
                'name': u'Carretera de Mayorga de Campos a Hospital de Órbigo',
                'oneway': u'no',
                'ref': u'CL-621',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4860096,
                'network': u'ES:autonoma',
                'shield_text': u'CL-621',
            })

    def test_cm3127_es(self):
        import dsl

        z, x, y = (16, 32247, 25117)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4816816
            dsl.way(4816816, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'CM-3127',
                'source': u'openstreetmap.org',
                'source:name': u'local knowledge',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4816816,
                'network': u'ES:autonoma',
                'shield_text': u'CM-3127',
            })

    def test_co31_es(self):
        import dsl

        z, x, y = (16, 31904, 25304)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/8392206
            dsl.way(8392206, dsl.tile_diagonal(z, x, y), {
                'converted_by': u'Track2osm',
                'highway': u'motorway',
                'oneway': u'yes',
                'ref': u'CO-31',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 8392206,
                'network': u'ES:province',
                'shield_text': u'CO-31',
            })

    def test_cp002_es(self):
        import dsl

        z, x, y = (16, 32519, 24341)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23342761
            dsl.way(23342761, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'CP-002',
                'source': u'openstreetmap.org',
            }),
        )

        # TODO: leading zeros?
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23342761,
                'network': u'ES:province',
                'shield_text': u'CP-002',
            })

    def test_cr4194_es(self):
        import dsl

        z, x, y = (16, 31882, 25051)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/42251605
            dsl.way(42251605, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Calle Carretas',
                'ref': u'CR-4194',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 42251605,
                'network': u'ES:province',
                'shield_text': u'CR-4194',
            })

    def test_cs22_es(self):
        import dsl

        z, x, y = (16, 32765, 24816)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23985225
            dsl.way(23985225, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'2',
                'maxspeed': u'80',
                'name': u'Acceso al Puerto de Castellón',
                'oneway': u'yes',
                'ref': u'CS-22',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23985225,
                'network': u'ES:city',
                'shield_text': u'CS-22',
            })

    def test_ct33_es(self):
        import dsl

        z, x, y = (16, 32593, 25368)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/33779155
            dsl.way(33779155, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'maxspeed': u'60',
                'name': u'Acceso Dársena de Cartagena',
                'oneway': u'yes',
                'ref': u'CT-33',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 33779155,
                'network': u'ES:city',
                'shield_text': u'CT-33',
            })

    def test_cu3_es(self):
        import dsl

        z, x, y = (16, 31644, 23941)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/9250047
            dsl.way(9250047, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Carretera Las Dueñas - Puerto de Cudillero',
                'ref': u'CU-3',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 9250047,
                'network': u'ES:city',
                'shield_text': u'CU-3',
            })

    def test_cv905_es(self):
        import dsl

        z, x, y = (16, 32639, 25274)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4857393
            dsl.way(4857393, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'lanes': u'2',
                'name': u'Carretera Benijófar - Torrevieja',
                'ref': u'CV-905',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4857393,
                'network': u'ES:autonoma',
                'shield_text': u'CV-905',
            })

    def test_cv799_es(self):
        import dsl

        z, x, y = (16, 32668, 25133)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/43962964
            dsl.way(43962964, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'oneway': u'yes',
                'ref': u'Cv-799',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 43962964,
                'network': u'ES:autonoma',
                'shield_text': u'Cv-799',
            })

    def test_dp7206_es(self):
        import dsl

        z, x, y = (16, 31179, 24161)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/7656083
            dsl.way(7656083, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'DP-7206',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 7656083,
                'network': u'ES:province',
                'shield_text': u'DP-7206',
            })

    def test_dsa600_es(self):
        import dsl

        z, x, y = (16, 31741, 24582)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/22810174
            dsl.way(22810174, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'3',
                'lit': u'yes',
                'maxspeed': u'50',
                'name': u'Avenida de la Serna',
                'oneway': u'yes',
                'parking:lane:both': u'no_parking',
                'ref': u'DSA-600',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22810174,
                'network': u'ES:province',
                'shield_text': u'DSA-600',
            })

    def test_ei700_es(self):
        import dsl

        z, x, y = (16, 33006, 25054)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/15239069
            dsl.way(15239069, dsl.tile_diagonal(z, x, y), {
                'FIXME': u'need review',
                'highway': u'primary',
                'ref': u'EI-700',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 15239069,
                'network': u'ES:city',
                'shield_text': u'EI-700',
            })

    def test_el20_es(self):
        import dsl

        z, x, y = (16, 32640, 25221)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/69146172
            dsl.way(69146172, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'trunk',
                'maxspeed': u'60',
                'name': u'Circunvalación Sur de Elche',
                'oneway': u'yes',
                'ref': u'EL-20',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 69146172,
                'network': u'ES:city',
                'shield_text': u'EL-20',
            })

    def test_ep8001_es(self):
        import dsl

        z, x, y = (16, 31193, 24169)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/7656097
            dsl.way(7656097, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'EP-8001',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 7656097,
                'network': u'ES:province',
                'shield_text': u'EP-8001',
            })

    def test_ex207_es(self):
        import dsl

        z, x, y = (16, 31580, 24939)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/22926785
            dsl.way(22926785, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk_link',
                'lanes': u'1',
                'maxspeed': u'60',
                'oneway': u'yes',
                'ref': u'EX-207',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Carretera de Cáceres a Portugal por Alcántara',
                'network': u'Red de carreteras de Extremadura',
                'operator': u'Junta de Extremadura',
                'ref': u'EX-207',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[22926785]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22926785,
                'network': u'ES:autonoma',
                'shield_text': u'EX-207',
            })

    def test_f24_es(self):
        import dsl

        z, x, y = (16, 32614, 25302)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/107700090
            dsl.way(107700090, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'F-24',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 107700090,
                'network': u'ES:province',
                'shield_text': u'F-24',
            })

    def test_fe15_es(self):
        import dsl

        z, x, y = (16, 31266, 23959)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/10262756
            dsl.way(10262756, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 01',
                'maxspeed': u'80',
                'nat_ref': u'FE-15',
                'oneway': u'yes',
                'ref': u'FE-15',
                'source': u'openstreetmap.org',
                'toll': u'no',
            }),
            dsl.relation(1, {
                'name': u'E 01 Spain (north)',
                'network': u'e-road',
                'ref': u'E 01',
                'route': u'road',
                'section': u'Spain (north)',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'de:Europastraße 1',
            }, ways=[10262756]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 10262756,
                'network': u'ES:city',
                'shield_text': u'FE-15',
                'all_networks': ['ES:city', 'e-road'],
                'all_shield_texts': ['FE-15', 'E-1'],
            })

    def test_gi2137_es(self):
        import dsl

        z, x, y = (16, 32412, 24007)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4256875
            dsl.way(4256875, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Martutene Pasealekua',
                'ref': u'GI-2137',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4256875,
                'network': u'ES:province',
                'shield_text': u'GI-2137',
            })

    def test_gip4033_es(self):
        import dsl

        z, x, y = (16, 33110, 24236)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/19850716
            dsl.way(19850716, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'90',
                'name': u'Carretera Alp-Bellver de Cerdanya',
                'oneway': u'yes',
                'ref': u'GIP-4033',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 19850716,
                'network': u'ES:province',
                'shield_text': u'GIP-4033',
            })

    def test_giv5264_es(self):
        import dsl

        z, x, y = (16, 33198, 24251)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/28242808
            dsl.way(28242808, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'layer': u'-1',
                'ref': u'GIV-5264',
                'source': u'openstreetmap.org',
                'tunnel': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 28242808,
                'network': u'ES:province',
                'shield_text': u'GIV-5264',
            })

    def test_gj10_es(self):
        import dsl

        z, x, y = (16, 31728, 23948)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4267997
            dsl.way(4267997, dsl.tile_diagonal(z, x, y), {
                'foot': u'no',
                'highway': u'trunk',
                'junction': u'roundabout',
                'lanes': u'2',
                'maxspeed': u'40',
                'name': u'Carretera Xixón-Avilés',
                'name:es': u'Carretera Gijón-Avilés',
                'ref': u'GJ-10',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4267997,
                'network': u'ES:city',
                'shield_text': u'GJ-10',
            })

    def test_gr14_es(self):
        import dsl

        z, x, y = (16, 32119, 25566)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/25694915
            dsl.way(25694915, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 902',
                'lanes': u'2',
                'oneway': u'yes',
                'ref': u'GR-14',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description:fr': u'E 902 Jaén - Malaga',
                'name:fr': u'Route européenne E 902',
                'network': u'e-road',
                'ref': u'E 902',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q8353069',
                'wikipedia': u'en:European route E902',
            }, ways=[25694915]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25694915,
                'network': u'ES:province',
                'shield_text': u'GR-14',
            })

    def test_gu102_es(self):
        import dsl

        z, x, y = (16, 32177, 24674)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/32918480
            dsl.way(32918480, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'ref': u'GU-102',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 32918480,
                'network': u'ES:province',
                'shield_text': u'GU-102',
            })

    def test_h31_es(self):
        import dsl

        z, x, y = (16, 31518, 25436)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/24849341
            dsl.way(24849341, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'2',
                'maxspeed': u'120',
                'oneway': u'yes',
                'ref': u'H-31',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 24849341,
                'network': u'ES:city',
                'shield_text': u'H-31',
            })

    def test_huv2301_es(self):
        import dsl

        z, x, y = (16, 32645, 24196)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/18945398
            dsl.way(18945398, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'HU-V-2301',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 18945398,
                'network': u'ES:province',
                'shield_text': u'HU-V-2301',
            })

    def test_ia1_es(self):
        import dsl

        z, x, y = (16, 31681, 23957)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/259323740
            dsl.way(259323740, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Carretera La Caizuela - La Llaguna',
                'ref': u'IA-1',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 259323740,
                'network': u'ES:city',
                'shield_text': u'IA-1',
            })

    def test_j14_es(self):
        import dsl

        z, x, y = (16, 32083, 25330)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/28959936
            dsl.way(28959936, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'junction': u'roundabout',
                'lanes': u'2',
                'name': u'Prolongación Avenida de Granada',
                'ref': u'J-14',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 28959936,
                'network': u'ES:city',
                'shield_text': u'J-14',
            })

    def test_ja6104_es(self):
        import dsl

        z, x, y = (16, 32123, 25245)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/61899450
            dsl.way(61899450, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'foot': u'yes',
                'highway': u'secondary',
                'lanes': u'1',
                'oneway': u'no',
                'ref': u'JA-6104',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 61899450,
                'network': u'ES:province',
                'shield_text': u'JA-6104',
            })

    def test_jv2031_es(self):
        import dsl

        z, x, y = (16, 32001, 25291)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/243869870
            dsl.way(243869870, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Carretera de Andújar',
                'ref': u'JV-2031',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 243869870,
                'network': u'ES:province',
                'shield_text': u'JV-2031',
            })

    def test_lp4033b_es(self):
        import dsl

        z, x, y = (16, 33099, 24238)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/14604117
            dsl.way(14604117, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'L-P-4033b',
                'ref': u'L-P-4033B',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 14604117,
                'network': u'ES:province',
                'shield_text': u'L-P-4033B',
            })

    def test_le493_es(self):
        import dsl

        z, x, y = (16, 31711, 24134)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4869407
            dsl.way(4869407, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'50',
                'ref': u'LE-493',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4869407,
                'network': u'ES:province',
                'shield_text': u'LE-493',
            })

    def test_ll12_es(self):
        import dsl

        z, x, y = (16, 32880, 24436)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/30136519
            dsl.way(30136519, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'maxspeed': u'60',
                'oneway': u'yes',
                'ref': u'LL-12',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 30136519,
                'network': u'ES:city',
                'shield_text': u'LL-12',
            })

    def test_ln6_es(self):
        import dsl

        z, x, y = (16, 31708, 24054)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/94658802
            dsl.way(94658802, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'LN-6',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 94658802,
                'network': u'ES:city',
                'shield_text': u'LN-6',
            })

    def test_lo20_es(self):
        import dsl

        z, x, y = (16, 32320, 24216)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/8085360
            dsl.way(8085360, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'is_in': u'Logroño, La Rioja, Spain',
                'lanes': u'2',
                'layer': u'-1',
                'maxspeed': u'80',
                'name': u'Circunvalación de Logroño',
                'oneway': u'yes',
                'ref': u'LO-20',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Circunvalación sur de Logroño',
                'ref': u'LO-20',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q2099134',
                'wikipedia': u'es:LO-20',
            }, ways=[8085360]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 8085360,
                'network': u'ES:city',
                'shield_text': u'LO-20',
            })

    def test_lp7032_es(self):
        import dsl

        z, x, y = (16, 32939, 24468)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/11985562
            dsl.way(11985562, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'ref': u'LP-7032',
                'source': u'openstreetmap.org',
                'source:name': u'local knowledge',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 11985562,
                'network': u'ES:province',
                'shield_text': u'LP-7032',
            })

    def test_lr134_es(self):
        import dsl

        z, x, y = (16, 32411, 24250)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4305846
            dsl.way(4305846, dsl.tile_diagonal(z, x, y), {
                'abutters': u'industrial',
                'highway': u'primary',
                'junction': u'roundabout',
                'ref': u'LR-134',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4305846,
                'network': u'ES:province',
                'shield_text': u'LR-134',
            })

    def test_lu617_es(self):
        import dsl

        z, x, y = (16, 31365, 24174)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23458502
            dsl.way(23458502, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'LU-617 Estrada de Monforte - Belesar',
                'oneway': u'no',
                'ref': u'LU-617',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23458502,
                'network': u'ES:province',
                'shield_text': u'LU-617',
            })

    def test_lv3344_es(self):
        import dsl

        z, x, y = (16, 32950, 24417)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/24209301
            dsl.way(24209301, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'oneway': u'no',
                'ref': u'LV-3344',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 24209301,
                'network': u'ES:province',
                'shield_text': u'LV-3344',
            })

    def test_m40_es(self):
        import dsl

        z, x, y = (16, 32086, 24724)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/3996189
            dsl.way(3996189, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 90',
                'lanes': u'3',
                'maxspeed': u'100',
                'name': u'M-40',
                'oneway': u'yes',
                'ref': u'M-40',
                'source': u'openstreetmap.org',
                'source:name': u'local knowledge',
            }),
            dsl.relation(1, {
                'name': u'Carretera Europea 90',
                'name:de': u'Europastraße 90',
                'name:en': u'European Road 90',
                'name:es': u'Carretera Europea 90',
                'network': u'e-road',
                'note': u'Spain',
                'ref': u'E 90',
                'ref:colour': u'#00cc00',
                'ref:colour_bg': u'#19408B',
                'ref:colour_tx': u'#ffffff',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[3996189]),
            dsl.relation(2, {
                'name': u'Autopista de Circunvalación M-40',
                'ref': u'M-40',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q2872994',
                'wikipedia': u'es:Autopista M-40',
            }, ways=[3996189]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3996189,
                'network': u'ES:autonoma',
                'shield_text': u'M-40',
            })

    def test_ma5103_es(self):
        import dsl

        z, x, y = (16, 32041, 25545)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4676310
            dsl.way(4676310, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'ref': u'MA-5103',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'comment': u'Árchez - Corumbela',
                'ref': u'MA-5103',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4676310]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4676310,
                'network': u'ES:province',
                'shield_text': u'MA-5103',
            })

    def test_me11_es(self):
        import dsl

        z, x, y = (16, 31613, 25060)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/74489915
            dsl.way(74489915, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'name': u'Acceso Norte a Mérida',
                'oneway': u'yes',
                'ref': u'ME-11',
                'ref_old': u'ME-11',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 74489915,
                'network': u'ES:city',
                'shield_text': u'ME-11',
            })

    def test_ml204_es(self):
        import dsl

        z, x, y = (16, 32230, 25897)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/38489610
            dsl.way(38489610, dsl.tile_diagonal(z, x, y), {
                'highway': u'tertiary',
                'lanes': u'2',
                'layer': u'-5',
                'lit': u'yes',
                'name': u'Carretera del Aeropuerto',
                'oneway': u'no',
                'ref': u'ML-204',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'tunnel': u'yes',
            }),
            dsl.relation(1, {
                'ref': u'ML-204',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[38489610]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 38489610,
                'network': u'ES:autonoma',
                'shield_text': u'ML-204',
            })

    def test_mp203_es(self):
        import dsl

        z, x, y = (16, 32144, 24712)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/30545206
            dsl.way(30545206, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'motorway',
                'layer': u'1',
                'oneway': u'yes',
                'ref': u'MP-203',
                'source': u'openstreetmap.org',
                'toll': u'no',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 30545206,
                'network': u'ES:province',
                'shield_text': u'MP-203',
            })

    def test_mu30_es(self):
        import dsl

        z, x, y = (16, 32559, 25291)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/17716810
            dsl.way(17716810, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway_link',
                'name': u'Circunvalación de Murcia',
                'oneway': u'no',
                'ref': u'MU-30',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Circunvalación de Murcia',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[17716810]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 17716810,
                'network': u'ES:city',
                'shield_text': u'MU-30',
            })

    def test_ma2220a_es(self):
        import dsl

        z, x, y = (16, 33328, 24836)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4225841
            dsl.way(4225841, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name:es': u'Paseo de Alemania',
                'oneway': u'yes',
                'ref': u'Ma-2220a',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4225841,
                'network': u'ES:autonoma',
                'shield_text': u'Ma-2220a',
            })

    def test_me1_es(self):
        import dsl

        z, x, y = (16, 33471, 24808)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/6620546
            dsl.way(6620546, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'Me-1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 6620546,
                'network': u'ES:autonoma',
                'shield_text': u'Me-1',
            })

    def test_na6630_es(self):
        import dsl

        z, x, y = (16, 32438, 24246)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4300207
            dsl.way(4300207, dsl.tile_diagonal(z, x, y), {
                'abutters': u'industrial',
                'highway': u'tertiary',
                'junction': u'roundabout',
                'name': u'Carretera Peralta - Funes - Marcilla',
                'ref': u'NA-6630',
                'source': u'openstreetmap.org',
                'source:name': u'BON nº182 - 14 de septiembre de 2012',
            }),
            dsl.relation(1, {
                'name': u'Carretera Peralta - Funes - Marcilla',
                'ref': u'NA-6630',
                'route': u'road',
                'source': u'openstreetmap.org',
                'source:name': u'BON nº182 - 14 de septiembre de 2012',
                'type': u'route',
            }, ways=[4300207]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4300207,
                'network': u'ES:province',
                'shield_text': u'NA-6630',
            })

    def test_nia_es(self):
        import dsl

        z, x, y = (16, 32115, 24525)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/45858922
            dsl.way(45858922, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'ref': u'NI-a',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 45858922,
                'network': u'ES:province',
                'shield_text': u'NI-a',
            })

    def test_o14_es(self):
        import dsl

        z, x, y = (16, 31704, 23989)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4853102
            dsl.way(4853102, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'is_in:city': u'Oviedo',
                'is_in:continent': u'Europe',
                'is_in:country': u'España',
                'is_in:province': u'Asturias',
                'is_in:region': u'Principado de Asturias',
                'lanes': u'1',
                'name': u'Enlace a Bulevar de San Julián de los Prados',
                'ref': u'O-14',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4853102,
                'network': u'ES:city',
                'shield_text': u'O-14',
            })

    def test_ou103_es(self):
        import dsl

        z, x, y = (16, 31378, 24271)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/25863479
            dsl.way(25863479, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'lanes': u'2',
                'ref': u'OU-103',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25863479,
                'network': u'ES:province',
                'shield_text': u'OU-103',
            })

    def test_p431_es(self):
        import dsl

        z, x, y = (16, 31967, 24263)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/22970377
            dsl.way(22970377, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'50',
                'name': u'Carretera de Astudillo',
                'ref': u'P-431',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22970377,
                'network': u'ES:province',
                'shield_text': u'P-431',
            })

    def test_pa32_es(self):
        import dsl

        z, x, y = (16, 32470, 24134)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4348471
            dsl.way(4348471, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'maxspeed': u'70',
                'name': u'Acceso Pamplona Sureste',
                'name:es': u'Acceso Pamplona Sureste',
                'oneway': u'yes',
                'ref': u'PA-32',
                'source': u'openstreetmap.org',
                'source:name': u'BON nº55 2 de mayo 2008',
            }),
            dsl.relation(1, {
                'name': u'Acceso Pamplona Sureste',
                'ref': u'PA-32',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4348471]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4348471,
                'network': u'ES:city',
                'shield_text': u'PA-32',
            })

    def test_pi13_es(self):
        import dsl

        z, x, y = (16, 31813, 24000)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/66336790
            dsl.way(66336790, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'PI-13',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 66336790,
                'network': u'ES:city',
                'shield_text': u'PI-13',
            })

    def test_pm801_es(self):
        import dsl

        z, x, y = (16, 33017, 25074)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/3318645
            dsl.way(3318645, dsl.tile_diagonal(z, x, y), {
                'FIXME': u'need review',
                'highway': u'secondary',
                'lanes': u'2',
                'oneway': u'yes',
                'ref': u'PM-801',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3318645,
                'network': u'ES:province',
                'shield_text': u'PM-801',
            })

    def test_pmv8031_es(self):
        import dsl

        z, x, y = (16, 33000, 25072)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/15239278
            dsl.way(15239278, dsl.tile_diagonal(z, x, y), {
                'FIXME': u'need review',
                'highway': u'secondary',
                'name': u'Ctra. Des Cubells',
                'ref': u'PMV-803.1',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 15239278,
                'network': u'ES:province',
                'shield_text': u'PMV-803.1',
            })

    def test_po11_es(self):
        import dsl

        z, x, y = (16, 31189, 24225)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/7654141
            dsl.way(7654141, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'oneway': u'yes',
                'ref': u'PO-11',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 7654141,
                'network': u'ES:province',
                'shield_text': u'PO-11',
            })

    def test_pp6303_es(self):
        import dsl

        z, x, y = (16, 32011, 24114)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/25197510
            dsl.way(25197510, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'junction': u'roundabout',
                'lanes': u'2',
                'ref': u'PP-6303',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25197510,
                'network': u'ES:province',
                'shield_text': u'PP-6303',
            })

    def test_pr3_es(self):
        import dsl

        z, x, y = (16, 31816, 23992)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/237395519
            dsl.way(237395519, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'PR-3',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 237395519,
                'network': u'ES:city',
                'shield_text': u'PR-3',
            })

    def test_pt10_es(self):
        import dsl

        z, x, y = (16, 32020, 25115)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23440177
            dsl.way(23440177, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'junction': u'roundabout',
                'ref': u'PT-10',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23440177,
                'network': u'ES:city',
                'shield_text': u'PT-10',
            })

    def test_r4_es(self):
        import dsl

        z, x, y = (16, 32134, 24830)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/6276316
            dsl.way(6276316, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'name': u'Radial 4',
                'oneway': u'yes',
                'ref': u'R-4',
                'source': u'openstreetmap.org',
                'toll': u'yes',
            }),
            dsl.relation(1, {
                'name': u'Radial R-4',
                'ref': u'R-4',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[6276316]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 6276316,
                'network': u'ES:autonoma',
                'shield_text': u'R-4',
            })

    def test_rc2_es(self):
        import dsl

        z, x, y = (16, 33471, 24808)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/25557690
            dsl.way(25557690, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'2',
                'name': u'Ronda sud Ciutadella',
                'name:es': u'Ronda sur Ciudadela',
                'oneway': u'yes',
                'ref': u'RC-2',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25557690,
                'network': u'ES:autonoma',
                'shield_text': u'RC-2',
            })

    def test_rm19_es(self):
        import dsl

        z, x, y = (16, 32612, 25323)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/17709127
            dsl.way(17709127, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'1',
                'oneway': u'yes',
                'ref': u'RM-19',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 17709127,
                'network': u'ES:autonoma',
                'shield_text': u'RM-19',
            })

    def test_s10_es(self):
        import dsl

        z, x, y = (16, 32071, 23968)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4332313
            dsl.way(4332313, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'2',
                'maxspeed': u'80',
                'name': u'Avenida de Parayas',
                'oneway': u'yes',
                'postal_code': u'39011',
                'ref': u'S-10',
                'source': u'openstreetmap.org',
                'wikipedia': u'es:S-10',
            }),
            dsl.relation(1, {
                'name': u'S-10',
                'nat_ref': u'S-10',
                'ref': u'S-10',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'es:S-10',
            }, ways=[4332313]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4332313,
                'network': u'ES:city',
                'shield_text': u'S-10',
            })

    def test_sa200_es(self):
        import dsl

        z, x, y = (16, 31572, 24672)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23211839
            dsl.way(23211839, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'lanes': u'2',
                'ref': u'SA-200',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23211839,
                'network': u'ES:province',
                'shield_text': u'SA-200',
            })

    def test_sc20_es(self):
        import dsl

        z, x, y = (16, 31211, 24113)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/9863691
            dsl.way(9863691, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'junction': u'roundabout',
                'lanes': u'2',
                'ref': u'SC-20',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 9863691,
                'network': u'ES:city',
                'shield_text': u'SC-20',
            })

    def test_se30(self):
        import dsl

        z, x, y = (16, 31685, 25415)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/19783204
            dsl.way(19783204, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 05',
                'lanes': u'4',
                'maxspeed': u'80',
                'oneway': u'yes',
                'ref': u'SE-30; A-4',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'sign',
                'turn:lanes': u'none|none|none|slight_right',
            }),
            dsl.relation(1, {
                'network': u'e-road',
                'ref': u'E 05',
                'route': u'road',
                'section': u'Spain (south-south)',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q693493',
                'wikipedia': u'en:European route E5',
            }, ways=[19783204]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 19783204,
                'network': u'ES:A-road',
                'shield_text': u'A-4',
                'all_networks': ['ES:A-road', 'ES:province', 'e-road'],
                'all_shield_texts': ['A-4', 'SE-30', 'E-5'],
            })

    def test_si8_es(self):
        import dsl

        z, x, y = (16, 31737, 23985)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/197726519
            dsl.way(197726519, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Carretera de La Pola a Bendición',
                'ref': u'SI-8',
                'source': u'openstreetmap.org',
                'source:date': u'2009',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 197726519,
                'network': u'ES:city',
                'shield_text': u'SI-8',
            })

    def test_sl9_es(self):
        import dsl

        z, x, y = (16, 31650, 23983)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/459026558
            dsl.way(459026558, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'junction': u'roundabout',
                'lanes': u'2',
                'ref': u'SL-9',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 459026558,
                'network': u'ES:city',
                'shield_text': u'SL-9',
            })

    def test_so132_es(self):
        import dsl

        z, x, y = (16, 32311, 24525)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/19909201
            dsl.way(19909201, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'de N-II a SO-160 por Barahona',
                'ref': u'SO-132',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 19909201,
                'network': u'ES:province',
                'shield_text': u'SO-132',
            })

    # TODO: need to tell if this is in Tarragona or Murcia province. will need
    # to look at the geometry!
    #
    # def test_t730_es(self):
    #     import dsl

    #     z, x, y = (16, 32427, 25258)

    #     self.generate_fixtures(
    #         dsl.is_in('ES', z, x, y),
    #         # https://www.openstreetmap.org/way/17945750
    #         dsl.way(17945750, dsl.tile_diagonal(z, x, y), {
    #             'highway': u'secondary',
    #             'name': u'Carretera de Granada',
    #             'oneway': u'yes',
    #             'ref': u'T-730',
    #             'source': u'openstreetmap.org',
    #         }),
    #     )

    #     self.assert_has_feature(
    #         z, x, y, 'roads', {
    #             'id': 17945750,
    #             'network': u'ES:province',
    #             'shield_text': u'T-730',
    #         })

    def test_tev8005_es(self):
        import dsl

        z, x, y = (16, 32569, 24719)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23069546
            dsl.way(23069546, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'layer': u'1',
                'oneway': u'no',
                'ref': u'TE-V-8005',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23069546,
                'network': u'ES:province',
                'shield_text': u'TE-V-8005',
            })

    def test_to20_es(self):
        import dsl

        z, x, y = (16, 32032, 24840)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23513439
            dsl.way(23513439, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'oneway': u'yes',
                'ref': u'TO-20',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23513439,
                'network': u'ES:province',
                'shield_text': u'TO-20',
            })

    def test_tp2402_es(self):
        import dsl

        z, x, y = (16, 33041, 24505)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/30043275
            dsl.way(30043275, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes:backward': u'1',
                'lanes:forward': u'1',
                'name': u'Avinguda de la Bisbal',
                'oneway': u'no',
                'ref': u'TP-2402',
                'source': u'openstreetmap.org',
                'width': u'8',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 30043275,
                'network': u'ES:province',
                'shield_text': u'TP-2402',
            })

    def test_tv3141_es(self):
        import dsl

        z, x, y = (16, 32967, 24537)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/23266743
            dsl.way(23266743, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'junction': u'roundabout',
                'name': u'TV-3141',
                'ref': u'TV-3141',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23266743,
                'network': u'ES:province',
                'shield_text': u'TV-3141',
            })

    def test_v31_es(self):
        import dsl

        z, x, y = (16, 32700, 24941)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/10689165
            dsl.way(10689165, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'3',
                'oneway': u'yes',
                'ref': u'V-31',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 10689165,
                'network': u'ES:autonoma',
                'shield_text': u'V-31',
            })

    def test_va20_es(self):
        import dsl

        z, x, y = (16, 31910, 24408)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4850505
            dsl.way(4850505, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'trunk',
                'lanes': u'2',
                'layer': u'1',
                'maxspeed': u'50',
                'name': u'Puentes del Cabildo',
                'oneway': u'yes',
                'ref': u'VA-20',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4850505,
                'network': u'ES:province',
                'shield_text': u'VA-20',
            })

    def test_vg20_es(self):
        import dsl

        z, x, y = (16, 31180, 24282)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/10145722
            dsl.way(10145722, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'layer': u'-1',
                'name': u'Tunel de Valladares',
                'oneway': u'yes',
                'ref': u'VG-20',
                'source': u'openstreetmap.org',
                'tunnel': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 10145722,
                'network': u'ES:city',
                'shield_text': u'VG-20',
            })

    def test_vm497_es(self):
        import dsl

        z, x, y = (16, 31496, 25446)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/26756572
            dsl.way(26756572, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'70',
                'name': u'Puente de Santa Eulalia',
                'ref': u'VM-497',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26756572,
                'network': u'ES:city',
                'shield_text': u'VM-497',
            })

    def test_z30_es(self):
        import dsl

        z, x, y = (16, 32602, 24417)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/4766157
            dsl.way(4766157, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'3',
                'name': u'Vía Hispanidad',
                'oneway': u'yes',
                'ref': u'Z-30',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4766157,
                'network': u'ES:province',
                'shield_text': u'Z-30',
            })

    def test_za20_es(self):
        import dsl

        z, x, y = (16, 31720, 24445)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/13894462
            dsl.way(13894462, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'maxspeed': u'50',
                'motorroad': u'no',
                'name': u'Avenida del Cardenal Cisneros',
                'oneway': u'yes',
                'ref': u'ZA-20',
                'source': u'openstreetmap.org',
                'source:date': u'2009',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 13894462,
                'network': u'ES:province',
                'shield_text': u'ZA-20',
            })

    def test_a132_alava(self):
        # NOTE: this A-132 is in Álava, Basque Country.
        # TODO: one rainy day, use the geometry to tell it's in Álava, rather
        # than one of the other autonoma which _also_ use the A- prefix for
        # roads which aren't ES:A-road.
        import dsl

        z, x, y = (16, 32302, 24125)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/503269748
            dsl.way(503269748, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'maxspeed': u'100',
                'name': u'Carretera Sangüesa-Vitoria',
                'name:es': u'Carretera Sangüesa-Vitoria',
                'name:eu': u'Zangotza-Gasteiz errepidea',
                'ref': u'A-132',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 503269748,
                'network': u'ES:autonoma',
                'shield_text': u'A-132',
            })

    def test_a132_aragon(self):
        # NOTE: this A-132 is near Huesca, Aragon
        # TODO: one rainy day, use the geometry to tell it's in Aragon, rather
        # than one of the other autonoma / provinces which _also_ use the A-
        # prefix for roads which aren't ES:A-road.
        import dsl

        z, x, y = (16, 32671, 24278)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/389741906
            dsl.way(389741906, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'name': u'Carretera de Huesca a Puente la Reina',
                'ref': u'A-132',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 389741906,
                'network': u'ES:autonoma',
                'shield_text': u'A-132',
            })

    def test_a308_andalusia(self):
        # NOTE: this A-132 is in Andalusia.
        # TODO: one rainy day, use the geometry to tell it's in Andalusia,
        # rather than one of the other autonoma / provinces which _also_ use
        # the A- prefix for roads which aren't ES:A-road.
        import dsl

        z, x, y = (16, 32169, 25430)

        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            # https://www.openstreetmap.org/way/328246083
            dsl.way(328246083, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'ref': u'A-308',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 328246083,
                'network': u'ES:autonoma',
                'shield_text': u'A-308',
            })
