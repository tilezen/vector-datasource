# -*- encoding: utf-8 -*-
from . import FixtureTest


class SouthKoreanShields(FixtureTest):
    def test_asianhighway(self):
        import dsl

        z, x, y = (16, 55875, 25370)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/547188348
            dsl.way(547188348, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Tongil-ro', 'name': u'통일로', 'review': 'no',
                'source': 'openstreetmap.org', 'highway': 'primary',
            }),
            dsl.relation(1, {
                'alt_name': u'아주공로 1호선', 'int_ref': 'AH1', 'layer': '1',
                'section': 'Korea', 'int_name': 'Asian Highway AH1',
                'network': 'AH', 'name': u'아시안 하이웨이 1호선',
                'name:en': 'Asian Highway AH1', 'ref': 'AH1', 'route': 'road',
                'source': 'openstreetmap.org', 'state': 'connection',
                'type': 'route', 'wikidata': 'Q494205', 'wikipedia': 'en:AH1',
            }, ways=[547188348]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 547188348,
                'shield_text': '1',
                'network': 'AsianHighway',
            })

    def test_asianhighway_no_relation(self):
        import dsl

        z, x, y = (16, 55886, 25381)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/37399710
            dsl.way(37399710, dsl.tile_diagonal(z, x, y), {
                'tunnel:name:ko_rm': 'Namsan il ho teoneol', 'tunnel': 'yes',
                'layer': '-2', 'name:en': 'Samil-daero', 'name': u'삼일대로',
                'tunnel:name:ko': u'남산1호터널', 'name:ko': u'삼일대로',
                'review': 'no', 'name:ko_rm': 'Samil-daero',
                'tunnel:name:en': 'Namsan 1 Ho Tunnel',
                'source': 'openstreetmap.org', 'ncat': u'광역시도로',
                'oneway': 'yes', 'tunnel:name': u'남산1호터널', 'ref': 'AH1',
                'toll': 'yes', 'highway': 'primary', 'name:ja': u'三一大路',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 37399710,
                'shield_text': '1',
                'network': 'AsianHighway',
            })

    def test_kr_expressway_rel_no_net(self):
        import dsl

        z, x, y = (16, 55975, 25658)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/90611594
            dsl.way(90611594, dsl.tile_diagonal(z, x, y), {
                'name:en': u'Tongyeong–Daejeon Expressway', 'lanes': '2',
                'name': u'통영대전고속도로', 'name:ko': u'통영대전고속도로',
                'name:ko_rm': 'Tongyeong-daejeon-gosokdoro',
                'source': 'openstreetmap.org', 'maxspeed': '100',
                'oneway': 'yes', 'ref': '35', 'highway': 'motorway',
            }),
            dsl.relation(1, {
                'layer': '1', 'name:en': u'Tongyeong–Daejeon Expressway',
                'name': u'통영대전고속도로', 'name:ko': u'통영대전고속도로',
                'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org', 'ref': '35',
            }, ways=[90611594]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 90611594,
                'shield_text': '35',
                'network': 'KR:expressway',
            })

    def test_kr_expressway(self):
        import dsl

        z, x, y = (16, 55904, 25415)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/59242897
            dsl.way(59242897, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Seoul Ring Expressway', 'lanes': '4',
                'name': u'서울외곽순환고속도로',
                'name:ko': u'서울외곽순환고속도로',
                'name:ko_rm': 'Seouloegwaksunhwangosokdoro',
                'source': 'openstreetmap.org', 'oneway': 'yes', 'ref': '100',
                'highway': 'motorway',
            }),
            dsl.relation(1, {
                'name:en': 'Seoul Ring Expressway(KEC), bound for '
                'Pangyo(Ilsan)',
                'name': u'서울외곽순환고속도로(도로공사) 판교(일산)방향',
                'name:ko': u'서울외곽순환고속도로(도로공사) 판교(일산)방향',
                'route': 'road', 'source': 'openstreetmap.org',
                'operator': 'Korea Expressway Corporation', 'type': 'route',
                'road': 'kr:expressway', 'network': 'KR:expressway',
            }, ways=[59242897]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 59242897,
                'shield_text': '100',
                'network': 'KR:expressway',
            })

    def test_kr_national(self):
        import dsl

        z, x, y = (16, 55864, 25396)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/71503022
            dsl.way(71503022, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Nambusunhwan-ro', 'name': u'남부순환로',
                'name:ko': u'남부순환로', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'ref': '92', 'highway': 'primary',
                'name:ja': u'南部循環路',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '92',
                'network': 'KR:national', 'source': 'openstreetmap.org',
            }, ways=[71503022]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 71503022,
                'shield_text': '92',
                'network': 'KR:national',
            })

    def test_kr_national_no_rel(self):
        import dsl

        z, x, y = (16, 56158, 25837)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/542451694
            dsl.way(542451694, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Upo 1-daero', 'name': u'우포1대로',
                'name:ko': u'우포1대로', 'review': 'no',
                'source': 'openstreetmap.org', 'highway': 'primary',
                'ref': '20;24', 'ncat': u'국도',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 542451694,
                'shield_text': '20', 'network': 'KR:national',
                'all_shield_texts': ['20', '24'],
                'all_networks': ['KR:national', 'KR:national'],
            })

    def test_kr_expressway_no_rel(self):
        import dsl

        z, x, y = (16, 55923, 25876)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/574671133
            dsl.way(574671133, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Gwangjudaegu Expressway',
                'name': u'광주대구고속도로', 'name:ko': u'광주대구고속도로',
                'review': 'no', 'name:ko_rm': 'Gwangjudaegugosokdoro',
                'source': 'openstreetmap.org', 'maxspeed': '80',
                'ncat': u'고속도로', 'oneway': 'yes', 'ref': '12',
                'highway': 'motorway',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 574671133,
                'shield_text': '12',
                'network': 'KR:expressway',
            })

    def test_kr_expressway_no_name_en(self):
        import dsl

        z, x, y = (16, 56165, 25760)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/43543281
            dsl.way(43543281, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': u'중부내륙고속도로지선', 'review': 'no',
                'source': 'openstreetmap.org', 'highway': 'motorway',
                'oneway': 'yes', 'ref': '451', 'ncat': u'고속도로',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '451',
                'source': 'openstreetmap.org',
            }, ways=[43543281]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 43543281,
                'shield_text': '451',
                'network': 'KR:expressway',
            })

    def test_kr_expressway_no_name_en_no_ncat(self):
        # same as the test above, but without the "ncat" to test that it
        # backfills from the name.
        import dsl

        z, x, y = (16, 56165, 25760)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/43543281
            dsl.way(43543281, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': u'중부내륙고속도로지선', 'review': 'no',
                'source': 'openstreetmap.org', 'highway': 'motorway',
                'oneway': 'yes', 'ref': '451',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '451',
                'source': 'openstreetmap.org',
            }, ways=[43543281]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 43543281,
                'shield_text': '451',
                'network': 'KR:expressway',
            })

    def test_kr_jungbunaeryukgosokdoro(self):
        import dsl

        z, x, y = (16, 56156, 25839)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/562319872
            dsl.way(562319872, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Jungbunaeryuk Expressway', 'lanes': '2',
                'name': u'중부내륙고속도로', 'name:ko': u'중부내륙고속도로',
                'review': 'no', 'name:ko_rm': 'Jungbunaeryukgosokdoro',
                'source': 'openstreetmap.org', 'ncat': u'고속도로',
                'oneway': 'yes', 'ref': '45', 'toll': 'yes',
                'highway': 'motorway',
            }),
            dsl.relation(1, {
                'name:en': 'Jungbunaeryuk Expressway',
                'name': u'중부내륙고속도로', 'name:ko': u'중부내륙고속도로',
                'ref': '45', 'route': 'road', 'source': 'openstreetmap.org',
                'type': 'route',
            }, ways=[562319872]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 562319872,
                'shield_text': '45',
                'network': 'KR:expressway',
            })

    def test_kr_upo_2_ro(self):
        import dsl

        z, x, y = (16, 56158, 25837)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/179815107
            dsl.way(179815107, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Upo 2-ro', 'name': u'우포2로', 'name:ko': u'우포2로',
                'review': 'no', 'source': 'openstreetmap.org',
                'highway': 'secondary', 'ref': '1080', 'ncat': u'지방도',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 179815107,
                'shield_text': '1080',
                'network': 'KR:local',
            })

    def test_kr_special_city(self):
        import dsl

        z, x, y = (16, 55879, 25372)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/37395768
            dsl.way(37395768, dsl.tile_diagonal(z, x, y), {
                'bridge': 'viaduct', 'layer': '2',
                'name:en': 'Naebusunhwan-ro', 'bicycle': 'no',
                'name': u'내부순환로', 'name:ko': u'내부순환로', 'review': 'no',
                'source': 'openstreetmap.org', 'ncat': u'특별시도',
                'oneway': 'yes', 'ref': '30', 'highway': 'trunk',
                'name:ja': u'内部循環路',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 37395768,
                'shield_text': '30',
                'network': 'KR:metropolitan',
            })

    def test_kr_metropolitan(self):
        import dsl

        z, x, y = (16, 56178, 25761)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/577716125
            dsl.way(577716125, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Jungang-daero',
                'name': u'중앙대로', 'name:ko': u'중앙대로', 'review': 'no',
                'name:ko_rm': 'Jungangdaero', 'source': 'openstreetmap.org',
                'highway': 'primary', 'ref': '61', 'ncat': u'광역시도로',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 577716125,
                'shield_text': '61',
                'network': 'KR:metropolitan',
            })
