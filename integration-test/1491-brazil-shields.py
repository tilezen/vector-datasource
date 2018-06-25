from . import FixtureTest


class BrazilShieldTest(FixtureTest):
    def test_trans_amazonian(self):
        import dsl

        z, x, y = (16, 26409, 34070)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/258644490
            dsl.way(258644490, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '110', 'lanes': '2', 'surface': 'asphalt',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'BR-101;BR-230', 'highway': 'motorway',
            }),
            dsl.relation(1, {
                'source:name': 'Lei 10.292/01',
                'name': u'Rodovia Governador M\xe1rio Covas',
                'type': 'route', 'route': 'road', 'wikipedia': 'pt:BR-101',
                'note': u'BR-101 Regi\xe3o Nordeste',
                'source': 'openstreetmap.org', 'wikidata': 'Q2877408',
                'ref': 'BR-101', 'network': 'BR',
            }, ways=[258644490]),
            dsl.relation(2, {
                'name:en': 'Trans-Amazonian highway',
                'name': u'Rodovia Transamaz\xf4nica', 'type': 'route',
                'route': 'road', 'wikipedia': 'pt:BR-230',
                'source': 'openstreetmap.org', 'name:fr': 'Transamazonienne',
                'wikidata': 'Q1569903', 'ref': 'BR-230', 'network': 'BR',
            }, ways=[258644490]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 258644490,
                'shield_text': '230', 'network': 'BR:Trans-Amazonian',
                'all_networks': ['BR:Trans-Amazonian', 'BR'],
                'all_shield_texts': ['230', '101'],
            })

    def test_df(self):
        import dsl

        z, x, y = (16, 24049, 35668)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/12524589
            dsl.way(12524589, dsl.tile_diagonal(z, x, y), {
                'bridge': 'yes', 'layer': '1', 'maxspeed': '60', 'lanes': '4',
                'name': 'Ponte do Bragueto', 'surface': 'paved',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'sidewalk': 'right', 'ref': 'DF-002', 'highway': 'motorway',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 12524589, 'shield_text': '002', 'network': 'BR:DF'})

    def test_ac(self):
        import dsl

        z, x, y = (16, 20489, 34659)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31524493
            dsl.way(31524493, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'AC-040',
                'highway': 'primary', 'IBGE:CD_ADMINIS': 'estadual',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 31524493, 'shield_text': '040', 'network': 'BR:AC'})

    def test_al(self):
        import dsl

        z, x, y = (16, 26147, 34626)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31532787
            dsl.way(31532787, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'AL-105',
                'highway': 'primary', 'oneway': 'no',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 31532787,
                'shield_text': '105',
                'network': 'BR:AL',
            })

    def test_ap(self):
        import dsl

        z, x, y = (16, 23450, 32768)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/29111026
            dsl.way(29111026, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'AP-010',
                'name': 'Rodovia Juscelino Kubitschek', 'highway': 'primary',
                'surface': 'paved',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 29111026,
                'shield_text': '010',
                'network': 'BR:AP',
            })

    def test_am(self):
        import dsl

        z, x, y = (16, 21854, 33286)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/28958366
            dsl.way(28958366, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'AM-010',
                'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
             z, x, y, 'roads', {
                 'id': 28958366,
                 'shield_text': '010',
                 'network': 'BR:AM',
             })

    def test_ba(self):
        import dsl

        z, x, y = (16, 25332, 35512)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/8099519
            dsl.way(8099519, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': u'Rodovia Serra do Mar\xe7al',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'ref': 'BA-263', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 8099519, 'shield_text': '263', 'network': 'BR:BA'})

    def test_ce(self):
        import dsl

        z, x, y = (16, 25662, 33678)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/23328809
            dsl.way(23328809, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'CE-060',
                'highway': 'secondary', 'oneway': 'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 23328809, 'shield_text': '060', 'network': 'BR:CE'})

    def test_es(self):
        import dsl

        z, x, y = (16, 25390, 36607)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/24602299
            dsl.way(24602299, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '60', 'name': 'Rodovia Jones dos Santos Neves',
                'destination': 'Guarapari', 'surface': 'paved',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'ES-480', 'highway': 'primary',
            }),
            dsl.relation(1, {
                'name': 'Rodovia Jones dos Santos Neves', 'type': 'route',
                'route': 'road', 'source': 'openstreetmap.org',
                'ref': 'ES-480', 'network': 'BR:ES',
            }, ways=[24602299]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 24602299, 'shield_text': '480', 'network': 'BR:ES'})

    def test_go(self):
        import dsl

        z, x, y = (16, 23822, 35860)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/24012217
            dsl.way(24012217, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'GO-536',
                'highway': 'secondary', 'oneway': 'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 24012217, 'shield_text': '536', 'network': 'BR:GO'})

    def test_ma(self):
        import dsl

        z, x, y = (16, 24520, 33173)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/29137050
            dsl.way(29137050, dsl.tile_diagonal(z, x, y), {
                'bridge': 'yes', 'layer': '1', 'ref': 'MA-106',
                'highway': 'primary', 'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 29137050, 'shield_text': '106', 'network': 'BR:MA'})

    def test_mt(self):
        import dsl

        z, x, y = (16, 22466, 35738)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/28996480
            dsl.way(28996480, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'MT-451',
                'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 28996480, 'shield_text': '451', 'network': 'BR:MT'})

    def test_ms(self):
        import dsl

        z, x, y = (16, 22323, 36340)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/29012329
            dsl.way(29012329, dsl.tile_diagonal(z, x, y), {
                'bridge': 'yes', 'layer': '1', 'ref': 'MS-228',
                'highway': 'secondary', 'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 29012329, 'shield_text': '228', 'network': 'BR:MS'})

    def test_mg(self):
        import dsl

        z, x, y = (16, 24770, 36461)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/4543343
            dsl.way(4543343, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': u'Rua Jacu\xed',
                'source': 'openstreetmap.org', 'oneway': 'no',
                'ref': 'MG-020', 'highway': 'secondary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'MG-020',
                'network': 'BR:MG', 'source': 'openstreetmap.org',
            }, ways=[4543343]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 4543343, 'shield_text': '020', 'network': 'BR:MG'})

    def test_pa(self):
        import dsl

        z, x, y = (16, 24274, 32930)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/23983406
            dsl.way(23983406, dsl.tile_diagonal(z, x, y), {
                'source:highway': 'schema_br2013', 'maxspeed': '80',
                'lanes': '1', 'surface': 'paved',
                'source': 'openstreetmap.org', 'embankment': 'false',
                'ref': 'PA-458', 'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 23983406, 'shield_text': '458', 'network': 'BR:PA'})

    def test_pb(self):
        import dsl

        z, x, y = (16, 25886, 34039)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31514019
            dsl.way(31514019, dsl.tile_diagonal(z, x, y), {
                'horse': 'yes', 'maxspeed': '80', 'bicycle': 'yes',
                'oneway': 'no', 'surface': 'asphalt', 'cycleway': 'no',
                'access': 'yes', 'source': 'openstreetmap.org',
                'IBGE:CD_ADMINIS': 'estadual', 'foot': 'yes', 'lanes': '2',
                'sidewalk': 'none', 'ref': 'PB-366', 'highway': 'secondary',
            }),
            dsl.relation(1, {
                'source': 'openstreetmap.org', 'route': 'road',
                'ref': 'PB-366', 'network': 'BR:PB', 'type': 'route',
            }, ways=[31514019]),
            dsl.relation(2, {
                'type': 'route', 'route': 'road', 'ref': 'BR-426',
                'network': 'BR', 'source': 'openstreetmap.org',
            }, ways=[31514019]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 31514019,
                'shield_text': '426', 'network': 'BR',
                'all_networks': ['BR', 'BR:PB'],
                'all_shield_texts': ['426', '366'],
            })

    def test_pr(self):
        import dsl

        z, x, y = (16, 23900, 37556)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/25460043
            dsl.way(25460043, dsl.tile_diagonal(z, x, y), {
                'name': 'Rodovia Deputado Miguel Bufara', 'surface': 'asphalt',
                'source': 'openstreetmap.org', 'oneway': 'no', 'ref': 'PR-408',
                'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 25460043, 'shield_text': '408', 'network': 'BR:PR'})

    def test_pe(self):
        import dsl

        z, x, y = (16, 26383, 34306)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/23392694
            dsl.way(23392694, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '30', 'surface': 'paved',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'PE-038', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 23392694, 'shield_text': '038', 'network': 'BR:PE'})

    def test_pi(self):
        import dsl

        z, x, y = (16, 24979, 33664)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/30844349
            dsl.way(30844349, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': 'Rodovia Antonio Medeiros Filho',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'oneway': 'no', 'ref': 'PI-112', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 30844349, 'shield_text': '112', 'network': 'BR:PI'})

    def test_rj(self):
        import dsl

        z, x, y = (16, 24908, 36979)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/13076835
            dsl.way(13076835, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'RJ-107',
                'name': u'Rua Lopes Trov\xe3o', 'highway': 'secondary',
            }),
            dsl.relation(1, {
                'name': 'Caminho Novo', 'tourism': 'yes', 'route': 'road',
                'source': 'openstreetmap.org', 'historic': 'yes',
                'type': 'route',
            }, ways=[13076835]),
        )

        # note: we don't pick up the tourist route
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 13076835, 'shield_text': '107', 'network': 'BR:RJ'})

    def test_rn(self):
        import dsl

        z, x, y = (16, 26371, 33904)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/28659532
            dsl.way(28659532, dsl.tile_diagonal(z, x, y), {
                'shoulder': 'no', 'source:highway': 'schema_br2013',
                'lanes': '2', 'name': 'RN-003',
                'source:highway_classification': 'survey', 'surface': 'paved',
                'source': 'openstreetmap.org', 'oneway': 'no', 'ref': 'RN-003',
                'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 28659532, 'shield_text': '003', 'network': 'BR:RN'})

    def test_rs(self):
        import dsl

        z, x, y = (16, 23457, 38464)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/584381094
            dsl.way(584381094, dsl.tile_diagonal(z, x, y), {
                'name': u'Rodovia M\xe1rio Quintana', 'surface': 'paved',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'RS-118', 'highway': 'primary_link',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 584381094, 'shield_text': '118', 'network': 'BR:RS'})

    def test_ro(self):
        import dsl

        z, x, y = (16, 21488, 34875)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31525107
            dsl.way(31525107, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'RO-267',
                'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 31525107, 'shield_text': '267', 'network': 'BR:RO'})

    def test_rr(self):
        import dsl

        z, x, y = (16, 21616, 32213)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31481157
            dsl.way(31481157, dsl.tile_diagonal(z, x, y), {
                'name': 'RR-205', 'IBGE:CD_ADMINIS': 'estadual',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'oneway': 'no', 'ref': 'RR-205', 'highway': 'primary'}),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 31481157, 'shield_text': '205', 'network': 'BR:RR'})

    def test_sc(self):
        import dsl

        z, x, y = (16, 23936, 37994)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/10492763
            dsl.way(10492763, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '50', 'name': 'Rodovia Admar Gonzaga',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'postal_code': '88034-100', 'oneway': 'yes', 'ref': 'SC-404',
                'highway': 'primary',
            }),
            dsl.relation(1, {
                'name': 'SC-404', 'ref': 'SC-404', 'route': 'road',
                'source': 'openstreetmap.org', 'type': 'route',
                'network': 'BR:SC',
            }, ways=[10492763]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 10492763, 'shield_text': '404', 'network': 'BR:SC'})

    def test_sp(self):
        import dsl

        z, x, y = (16, 24262, 37201)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/4273875
            dsl.way(4273875, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '90', 'lanes': '2',
                'name': 'Marginal Pinheiros - Expressa', 'surface': 'asphalt',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'SP-015', 'highway': 'motorway',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 4273875, 'shield_text': '015', 'network': 'BR:SP'})

    def test_se(self):
        import dsl

        z, x, y = (16, 26010, 34601)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31529719
            dsl.way(31529719, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'SE-200',
                'surface': 'asphalt', 'highway': 'primary',
                'IBGE:CD_ADMINIS': 'estadual',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'SE-200',
                'network': 'SE', 'source': 'openstreetmap.org',
            }, ways=[31529719]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 31529719,
                'shield_text': '200', 'network': 'BR:SE',
                'all_shield_texts': ['200'],
                'all_networks': ['BR:SE'],
            })

    def test_to(self):
        import dsl

        z, x, y = (16, 23986, 34080)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/28782365
            dsl.way(28782365, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'TO-222',
                'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 28782365, 'shield_text': '222', 'network': 'BR:TO'})

    def test_br_AMG(self):
        import dsl

        z, x, y = (16, 24778, 36439)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/11507107
            dsl.way(11507107, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'AMG-0130',
                'highway': 'secondary_link', 'oneway': 'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 11507107, 'shield_text': '0130', 'network': 'BR:MG'})

    def test_br_LMG(self):
        import dsl

        z, x, y = (16, 24759, 36447)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/4946285
            dsl.way(4946285, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '60', 'name': 'Rua Padre Pedro Pinto',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'ref': 'LMG-806', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 4946285, 'shield_text': '806', 'network': 'BR:MG:local'})

    def test_br_MGC(self):
        import dsl

        z, x, y = (16, 24603, 36244)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31574746
            dsl.way(31574746, dsl.tile_diagonal(z, x, y), {
                'network': 'BR', 'IBGE:CD_ADMINIS': 'estadual',
                'surface': 'paved', 'source': 'openstreetmap.org',
                'incorrect:name': 'MGC-259', 'oneway': 'no',
                'ref': 'MGC-259;BR-259', 'highway': 'primary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'BR-259',
                'network': 'BR', 'source': 'openstreetmap.org',
            }, ways=[31574746]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 31574746,
                'all_shield_texts': ['259', '259'],
                'all_networks': ['BR', 'BR:MG'],
            })

    def test_br_CMG(self):
        import dsl

        z, x, y = (16, 24787, 35853)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31574975
            dsl.way(31574975, dsl.tile_diagonal(z, x, y), {
                'name': u'Avenida Governador Magalh\xe3es Pinto',
                'IBGE:CD_ADMINIS': 'federal', 'surface': 'paved',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'CMG-251;BR-251', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 31574975,
                'all_shield_texts': ['251', '251'],
                'all_networks': ['BR', 'BR:MG'],
            })

    def test_br_ERS(self):
        import dsl

        z, x, y = (16, 23101, 38967)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/20906150
            dsl.way(20906150, dsl.tile_diagonal(z, x, y), {
                'old_ref': 'RS-602', 'maxspeed': '80', 'surface': 'asphalt',
                'source': 'openstreetmap.org', 'ref': 'ERS-602',
                'highway': 'secondary',
            }),
            dsl.relation(1, {
                'network': 'BR:RS', 'ref': 'ERS-602', 'route': 'road',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'type': 'route',
            }, ways=[20906150]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 20906150,
                'shield_text': '602', 'network': 'BR:RS',
                'all_networks': ['BR:RS'],
                'all_shield_texts': ['602'],
            })

    def test_br_VRS(self):
        import dsl

        z, x, y = (16, 23312, 38227)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/26757190
            dsl.way(26757190, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'VRS-851',
                'highway': 'secondary', 'oneway': 'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26757190, 'shield_text': '851',
                'network': 'BR:RS',
            })

    def test_br_RSC(self):
        import dsl

        z, x, y = (16, 23450, 38314)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/25979338
            dsl.way(25979338, dsl.tile_diagonal(z, x, y), {
                'name': 'Rota do Sol', 'surface': 'paved',
                'source': 'openstreetmap.org', 'oneway': 'no',
                'ref': 'RSC-453', 'highway': 'primary',
            }),
            dsl.relation(1, {
                'network': 'BR', 'ref': 'BR-453', 'route': 'road',
                'wikipedia': 'pt:BR-453', 'source': 'openstreetmap.org',
                'wikidata': 'Q2877442', 'type': 'route',
            }, ways=[25979338]),
            dsl.relation(2, {
                'old_ref': 'RST-453', 'name': 'Rota do Sol', 'route': 'road',
                'source:official_name': 'LO 11432/2000', 'type': 'route',
                'official_name': 'Rota do Sol Euclides Triches',
                'source': 'openstreetmap.org', 'ref': 'RSC-453',
                'network': 'BR:RS',
            }, ways=[25979338]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25979338,
                'shield_text': '453', 'network': 'BR',
                'all_shield_texts': ['453', '453'],
                'all_networks': ['BR', 'BR:RS']
            })

    def test_br_SPA(self):
        import dsl

        z, x, y = (16, 24194, 37330)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/4964220
            dsl.way(4964220, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'SPA-344/055',
                'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4964220,
                'shield_text': '055', 'network': 'BR:SP',
                'all_shield_texts': ['055', '344'],
                'all_networks': ['BR:SP', 'BR:SP'],
            })

    def test_br_PRC(self):
        import dsl

        z, x, y = (16, 23383, 37517)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/31611447
            dsl.way(31611447, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '110', 'surface': 'paved',
                'source': 'openstreetmap.org', 'IBGE:CD_ADMINIS': 'federal',
                'nat_ref': 'BR-466', 'ref': 'PRC-466', 'highway': 'primary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'BR-466',
                'network': 'BR', 'source': 'openstreetmap.org',
            }, ways=[31611447]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 31611447,
                'shield_text': '466', 'network': 'BR',
                'all_shield_texts': ['466', '466'],
                'all_networks': ['BR', 'BR:PR']
            })

    def test_br_PLN(self):
        import dsl

        z, x, y = (16, 24178, 37017)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/116514858
            dsl.way(116514858, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '40', 'name': u'Avenida Jo\xe3o Vieira',
                'source': 'openstreetmap.org', 'postal_code': '13145-754',
                'oneway': 'yes', 'ref': 'PLN-346', 'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 116514858,
                'shield_text': '346', 'network': 'BR:SP:PLN',
            })

    def test_br_SP_many(self):
        import dsl

        z, x, y = (16, 24051, 36887)

        self.generate_fixtures(
            dsl.is_in('BR', z, x, y),
            # https://www.openstreetmap.org/way/258575188
            dsl.way(258575188, dsl.tile_diagonal(z, x, y), {
                'lanes': '1', 'name': 'Rodovia Municipal Domingos Innocentini',
                'wikipedia': 'pt:Rodovia Municipal Domingos Innocentini',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'ref': 'SPA-149/215;SCA-040',
                'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 258575188,
                'shield_text': '149',
                'network': 'BR:SP',
                'all_networks': ['BR:SP', 'BR:SP', 'BR:SP:SCA'],
                'all_shield_texts': ['149', '215', '040'],
            })
