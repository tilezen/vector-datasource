from . import FixtureTest


class SouthKoreanShields(FixtureTest):
    def test_asianhighway(self):
        import dsl

        z, x, y = (16, 55875, 25370)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/547188348
            dsl.way(547188348, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Tongil-ro', 'name': u'\ud1b5\uc77c\ub85c',
                'review': 'no', 'source': 'openstreetmap.org',
                'highway': 'primary',
            }),
            dsl.relation(1, {
                'alt_name': u'\uc544\uc8fc\uacf5\ub85c 1\ud638\uc120',
                'int_ref': 'AH1', 'layer': '1', 'section': 'Korea',
                'int_name': 'Asian Highway AH1', 'network': 'AH',
                'name': u'\uc544\uc2dc\uc548 \ud558\uc774\uc6e8\uc774 1'
                u'\ud638\uc120', 'name:en': 'Asian Highway AH1', 'ref': 'AH1',
                'route': 'road', 'source': 'openstreetmap.org',
                'state': 'connection', 'type': 'route',
                'wikidata': 'Q494205', 'wikipedia': 'en:AH1',
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
                'layer': '-2', 'name:en': 'Samil-daero',
                'name': u'\uc0bc\uc77c\ub300\ub85c',
                'tunnel:name:ko': u'\ub0a8\uc0b01\ud638\ud130\ub110',
                'name:ko': u'\uc0bc\uc77c\ub300\ub85c', 'review': 'no',
                'name:ko_rm': 'Samil-daero',
                'tunnel:name:en': 'Namsan 1 Ho Tunnel',
                'source': 'openstreetmap.org',
                'ncat': u'\uad11\uc5ed\uc2dc\ub3c4\ub85c', 'oneway': 'yes',
                'tunnel:name': u'\ub0a8\uc0b01\ud638\ud130\ub110',
                'ref': 'AH1', 'toll': 'yes', 'highway': 'primary',
                'name:ja': u'\u4e09\u4e00\u5927\u8def',
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
                'name:en': u'Tongyeong\u2013Daejeon Expressway', 'lanes': '2',
                'name': u'\ud1b5\uc601\ub300\uc804\uace0\uc18d\ub3c4\ub85c',
                'name:ko': u'\ud1b5\uc601\ub300\uc804\uace0\uc18d\ub3c4\ub85c',
                'name:ko_rm': 'Tongyeong-daejeon-gosokdoro',
                'source': 'openstreetmap.org', 'maxspeed': '100',
                'oneway': 'yes', 'ref': '35', 'highway': 'motorway',
            }),
            dsl.relation(1, {
                'layer': '1', 'name:en': u'Tongyeong\u2013Daejeon Expressway',
                'name': u'\ud1b5\uc601\ub300\uc804\uace0\uc18d\ub3c4\ub85c',
                'name:ko': u'\ud1b5\uc601\ub300\uc804\uace0\uc18d\ub3c4\ub85c',
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
                'name': u'\uc11c\uc6b8\uc678\uacfd\uc21c\ud658\uace0'
                u'\uc18d\ub3c4\ub85c', 'name:ko': u'\uc11c\uc6b8\uc678'
                u'\uacfd\uc21c\ud658\uace0\uc18d\ub3c4\ub85c',
                'name:ko_rm': 'Seouloegwaksunhwangosokdoro',
                'source': 'openstreetmap.org', 'oneway': 'yes', 'ref': '100',
                'highway': 'motorway',
            }),
            dsl.relation(1, {
                'name:en': 'Seoul Ring Expressway(KEC), bound for '
                'Pangyo(Ilsan)', 'name': u'\uc11c\uc6b8\uc678\uacfd\uc21c'
                u'\ud658\uace0\uc18d\ub3c4\ub85c(\ub3c4\ub85c\uacf5\uc0ac)'
                u' \ud310\uad50(\uc77c\uc0b0)\ubc29\ud5a5',
                'name:ko': u'\uc11c\uc6b8\uc678\uacfd\uc21c\ud658\uace0'
                u'\uc18d\ub3c4\ub85c(\ub3c4\ub85c\uacf5\uc0ac) \ud310'
                u'\uad50(\uc77c\uc0b0)\ubc29\ud5a5', 'route': 'road',
                'source': 'openstreetmap.org',
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
                'name:en': 'Nambusunhwan-ro', 'name': u'\ub0a8\ubd80'
                u'\uc21c\ud658\ub85c', 'name:ko': u'\ub0a8\ubd80\uc21c'
                u'\ud658\ub85c', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'ref': '92', 'highway': 'primary',
                'name:ja': u'\u5357\u90e8\u5faa\u74b0\u8def',
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
