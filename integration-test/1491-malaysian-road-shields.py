# -*- encoding: utf-8 -*-
from . import FixtureTest


class MalaysianShieldTest(FixtureTest):
    def test_54_myfederal(self):
        import dsl

        z, x, y = (16, 51239, 32174)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/258246542
            dsl.way(258246542, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'foot': u'yes',
                'highway': u'trunk',
                'lanes': u'2',
                'maxspeed': u'90',
                'motor_vehicle': u'yes',
                'name': u'Jalan Kepong - Kuala Selangor',
                'oneway': u'yes',
                'ref': u'FT54',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 258246542,
                'network': u'MY:federal',
                'shield_text': u'54',
            })

    def test_3214_myfederal(self):
        import dsl

        z, x, y = (16, 51255, 32205)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/4937362
            dsl.way(4937362, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'is_in': u'Shah Alam, Selangor, Malaysia',
                'name': u'Jalan Subang',
                'oneway': u'yes',
                'ref': u'3214',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4937362,
                'network': u'MY:federal',
                'shield_text': u'3214',
            })

    def test_111b1_myfederal(self):
        import dsl

        z, x, y = (16, 52853, 32493)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/68058997
            dsl.way(68058997, dsl.tile_diagonal(z, x, y), {
                'access': u'yes',
                'cycleway': u'no',
                'highway': u'trunk',
                'horse': u'no',
                'int_ref': u'AH150',
                'lanes': u'2',
                'lit': u'yes',
                'name': u'Jalan Datuk Amar Kalong Ningkan',
                'oneway': u'yes',
                'ref': u'1-11B1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'alt_name': u'Pan-Borneo Highway',
                'int_ref': u'AH150',
                'name': u'Asian Highway AH150',
                'name:de': u'Asien Fernstraße AH150',
                'name:en': u'Asian Highway AH150',
                'name:fr': u'Route asiatique AH150',
                'name:id': u'Jalan Asia AH150',
                'name:ja': u'アジアハイウェイ150号線',
                'name:ko': u'아시안 하이웨이 150호선',
                'name:ms': u'Lebuhraya Asia AH150',
                'name:ru': u'Азиатский маршрут AH150',
                'name:vi': u'Đường Xuyên Á AH150',
                'name:zh': u'亚洲公路150号线',
                'network': u'AsianHighway',
                'ref': u'AH150',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikipedia': u'en:Pan-Borneo Highway',
            }, ways=[68058997]),
            dsl.relation(2, {
                'name': u'Laluan Persekutuan 1 (Sabah & Sarawak) (arah timur)',
                'name:en': u'Federal Route 1 (Sabah & Sarawak) (eastbound)',
                'name:zh': u'联邦路线1（沙巴和沙捞越）（东向）',
                'network': u'my:federal',
                'ref': u'1',
                'role': u'east',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[68058997]),
        )

        # TODO! should the shield text be '1' or '1-11B1'? not sure from
        # available sources whether the '-11B1' part is important and/or
        # usually on signs.
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 68058997,
                'network': 'MY:federal',
                'shield_text': '1',
                'all_networks': ['MY:federal', 'AsianHighway'],
                'all_shield_texts': ['1', 'AH150'],
            })

    def test_e35_myexpressway(self):
        import dsl

        z, x, y = (16, 51253, 32202)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/5012022
            dsl.way(5012022, dsl.tile_diagonal(z, x, y), {
                'alt_name': u'GCE',
                'highway': u'motorway',
                'is_in': u'Shah Alam, Selangor, Malaysia',
                'lanes': u'3',
                'maxspeed': u'90',
                'name': u'Lebuhraya Koridor Guthrie',
                'name:en': u'Guthrie Corridor Expressway',
                'oneway': u'yes',
                'ref': u'E35',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Lebuhraya Koridor Guthrie',
                'name:en': u'Guthrie Corridor Expressway',
                'name:zh': u'牙直利大道',
                'operator': u'Projek Lintasan Kota Holdings Sdn Bhd',
                'ref': u'E35',
                'route': u'road',
                'short_name': u'GCE',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[5012022]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 5012022,
                'network': u'MY:expressway',
                'shield_text': u'E35',
            })

    def test_a1_my_prk(self):
        import dsl

        z, x, y = (16, 51168, 31915)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/27488344
            dsl.way(27488344, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'name': u'Jalan Jelapang',
                'ref': u'A1',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 27488344,
                'network': u'MY:PRK',
                'shield_text': u'A1',
            })

    def test_b9_my_sgr(self):
        import dsl

        z, x, y = (16, 51254, 32205)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/4931877
            dsl.way(4931877, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'is_in': u'Shah Alam, Selangor, Malaysia',
                'name': u'Jalan Montford',
                'oneway': u'-1',
                'ref': u'B9',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4931877,
                'network': u'MY:SGR',
                'shield_text': u'B9',
            })

    def test_c5_my_phg(self):
        import dsl

        z, x, y = (16, 51298, 32014)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/144865951
            dsl.way(144865951, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'C5',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 144865951,
                'network': u'MY:PHG',
                'shield_text': u'C5',
            })

    def test_d11_my_ktn(self):
        import dsl

        z, x, y = (16, 51437, 31705)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/27210505
            dsl.way(27210505, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'D11',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 27210505,
                'network': u'MY:KTN',
                'shield_text': u'D11',
            })

    def test_j137_my_jhr(self):
        import dsl

        z, x, y = (16, 51464, 32364)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/5037585
            dsl.way(5037585, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'is_in': u'Panchor, Muar, Johor, Malaysia',
                'is_in:country': u'Malaysia',
                'is_in:state': u'Johor',
                'name': u'Jalan Panchor',
                'ref': u'J137',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 5037585,
                'network': u'MY:JHR',
                'shield_text': u'J137',
            })

    def test_k1_my_kdh(self):
        import dsl

        z, x, y = (16, 51028, 31656)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/45896203
            dsl.way(45896203, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'oneway': u'yes',
                'ref': u'K1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 45896203,
                'network': u'MY:KDH',
                'shield_text': u'K1',
            })

    def test_m109_my_mlk(self):
        import dsl

        z, x, y = (16, 51408, 32370)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/25205742
            dsl.way(25205742, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'is_in': u'Melaka, Melaka, Malaysia',
                'is_in:state': u'Melaka',
                'ref': u'M109',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25205742,
                'network': u'MY:MLK',
                'shield_text': u'M109',
            })

    def test_n17_my_nsn(self):
        import dsl

        z, x, y = (16, 51389, 32287)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/26638985
            dsl.way(26638985, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'history': u'Retrieved from v3',
                'ref': u'N17',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26638985,
                'network': u'MY:NSN',
                'shield_text': u'N17',
            })

    def test_p210_my_png(self):
        import dsl

        z, x, y = (16, 51024, 31782)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/23118777
            dsl.way(23118777, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'name': u'Jalan Air Itam',
                'name:en': u'Ayer Itam Road',
                'oneway': u'yes',
                'ref': u'P210',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23118777,
                'network': u'MY:PNG',
                'shield_text': u'P210',
            })

    def test_r15_my_pls(self):
        import dsl

        z, x, y = (16, 51004, 31546)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/102244618
            dsl.way(102244618, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'ref': u'R15',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 102244618,
                'network': u'MY:PLS',
                'shield_text': u'R15',
            })

    def test_sa33_my_(self):
        import dsl

        z, x, y = (16, 53870, 31872)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/32770972
            dsl.way(32770972, dsl.tile_diagonal(z, x, y), {
                'access': u'yes',
                'bicycle': u'yes',
                'cycleway': u'no',
                'fixme': u'yes',
                'foot': u'yes',
                'highway': u'secondary',
                'horse': u'no',
                'lanes': u'2',
                'lit': u'no',
                'motor_vehicle': u'yes',
                'name': u'Jalan Paal-Kuala Tomani',
                'oneway': u'no',
                'ref': u'SA33',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 32770972,
                'network': u'MY:SBH',
                'shield_text': u'SA33',
            })

    def test_t11_my_trg(self):
        import dsl

        z, x, y = (16, 51497, 31821)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/32767537
            dsl.way(32767537, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'oneway': u'no',
                'ref': u'T11',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 32767537,
                'network': u'MY:TRG',
                'shield_text': u'T11',
            })

    def test_q115_my_swk(self):
        import dsl

        z, x, y = (16, 52818, 32507)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/53546059
            dsl.way(53546059, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Jalan Akses Bau',
                'oneway': u'no',
                'ref': u'Q115',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 53546059,
                'network': u'MY:SWK',
                'shield_text': u'Q115',
            })

    def test_mbsa15_mysgrmunicipal(self):
        import dsl

        z, x, y = (16, 51252, 32209)

        self.generate_fixtures(
            dsl.is_in('MY', z, x, y),
            # https://www.openstreetmap.org/way/24701880
            dsl.way(24701880, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'is_in': u'Shah Alam, Selangor, Malaysia',
                'lanes': u'2',
                'oneway': u'yes',
                'ref': u'MBSA 15',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 24701880,
                'network': u'MY:SGR:municipal',
                'shield_text': u'BSA15',
            })
