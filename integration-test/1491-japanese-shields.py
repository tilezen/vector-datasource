from . import FixtureTest


class JapaneseShieldTest(FixtureTest):
    def test_jp_national(self):
        import dsl

        z, x, y = (16, 57463, 26016)

        self.generate_fixtures(
            dsl.is_in('JP', z, x, y),
            # https://www.openstreetmap.org/way/242802845
            dsl.way(242802845, dsl.tile_diagonal(z, x, y), {
                'name:en': 'National Route 163',
                'name': u'\u56fd\u9053163\u53f7', 'oneway:bicycle': 'yes',
                'source': 'openstreetmap.org', 'maxspeed': '50',
                'oneway': 'yes', 'ref': '163', 'highway': 'trunk',
                'name:ja': u'\u56fd\u9053163\u53f7',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 242802845,
                'shield_text': '163', 'network': 'JP:national',
            })

    def test_jp_prefectural(self):
        import dsl

        z, x, y = (16, 58201, 25799)

        self.generate_fixtures(
            dsl.is_in('JP', z, x, y),
            # https://www.openstreetmap.org/way/415221603
            dsl.way(415221603, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '50', 'int_name': 'Meiji-dori',
                'name': u'\u660e\u6cbb\u901a\u308a',
                'name:ja_kana': u'\u3081\u3044\u3058\u3069\u304a\u308a',
                'surface': 'paved', 'source': 'openstreetmap.org',
                'name:en': 'Meiji-dori', 'oneway': 'yes', 'ref': '305',
                'route': 'road', 'highway': 'primary',
                'name:ja': u'\u660e\u6cbb\u901a\u308a',
            }),
            dsl.relation(1, {
                'name:en': 'Meiji Dori', 'name': u'\u660e\u6cbb\u901a\u308a',
                'route': 'road', 'source': 'openstreetmap.org',
                'wikidata': 'Q8011176', 'type': 'route',
                'network': 'jp:prefectural',
            }, ways=[415221603]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 415221603,
                'shield_text': '305', 'network': 'JP:prefectural',
            })

    def test_jp_e_expressway(self):
        import dsl

        z, x, y = (16, 57350, 26039)

        self.generate_fixtures(
            dsl.is_in('JP', z, x, y),
            # https://www.openstreetmap.org/way/18576866
            dsl.way(18576866, dsl.tile_diagonal(z, x, y), {
                'bridge': 'yes', 'layer': '3', 'maxspeed': '80',
                'bicycle': 'no',
                'name': u'\u795e\u6238\u6de1\u8def\u9cf4\u9580\u81ea'
                u'\u52d5\u8eca\u9053',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'surface': 'paved',
                'bridge:name': u'\u660e\u77f3\u6d77\u5ce1\u5927\u6a4b',
                'name:en': 'Kobe-Awaji-Naruto Expressway',
                'motorcycle': 'designated', 'motorcar': 'designated',
                'foot': 'no', 'lanes': '3', 'toll': 'yes', 'ref': 'E28',
                'smoothness': 'excellent', 'highway': 'motorway',
                'name:ja': u'\u795e\u6238\u6de1\u8def\u9cf4\u9580\u81ea'
                u'\u52d5\u8eca\u9053',
            }),
            dsl.relation(1, {
                'name:en': 'Kobe Awaji Naruto Expressway',
                'name': u'\u795e\u6238\u6de1\u8def\u9cf4\u9580\u81ea'
                u'\u52d5\u8eca\u9053', 'short_name': u'\u795e\u6238'
                u'\u6de1\u8def\u9cf4\u9580\u9053', 'type': 'route',
                'name:ja_kana': u'\u3053\u3046\u3079\u3042\u308f\u3058'
                u'\u306a\u308b\u3068\u3058\u3069\u3046\u3057\u3083'
                u'\u3069\u3046', 'name:ja_rm': u'Kobe-Awaji-Naruto Jid'
                u'\u014dshad\u014d', 'source': 'openstreetmap.org',
                'wikipedia': u'ja:\u795e\u6238\u6de1\u8def\u9cf4\u9580'
                u'\u81ea\u52d5\u8eca\u9053', 'ref': 'E28', 'route': 'road',
                'name:ja': u'\u795e\u6238\u6de1\u8def\u9cf4\u9580\u81ea'
                u'\u52d5\u8eca\u9053',
            }, ways=[18576866]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 18576866,
                'shield_text': 'E28', 'network': 'JP:expressway'})

    def test_jp_ea_expressway(self):
        import dsl

        z, x, y = (16, 58512, 24062)

        self.generate_fixtures(
            dsl.is_in('JP', z, x, y),
            # https://www.openstreetmap.org/way/24268939
            dsl.way(24268939, dsl.tile_diagonal(z, x, y), {
                'bridge': 'yes', 'layer': '2', 'maxspeed': '80',
                'bicycle': 'no', 'name': u'\u672d\u6a3d\u81ea\u52d5'
                u'\u8eca\u9053', 'oneway': 'yes',
                'name:ja_rm': u'Sasson jid\u014dshad\u014d',
                'surface': 'paved', 'source': 'openstreetmap.org',
                'name:en': 'Sasson Expressway', 'motorcycle': 'designated',
                'motorcar': 'designated', 'foot': 'no', 'lanes': '2',
                'toll': 'yes', 'ref': 'E5A', 'smoothness': 'excellent',
                'highway': 'motorway', 'name:ja': u'\u672d\u6a3d\u81ea'
                u'\u52d5\u8eca\u9053',
            }),
            dsl.relation(1, {
                'name:en': 'Sasson Expressway', 'name': u'\u672d\u6a3d'
                u'\u81ea\u52d5\u8eca\u9053', 'type': 'route',
                'name:ja_kana': u'\u3055\u3063\u305d\u3093\u3058\u3069'
                u'\u3046\u3057\u3083\u3069\u3046',
                'name:ja_rm': u'Sasson Jid\u014dshad\u014d',
                'source': 'openstreetmap.org',
                'wikipedia': u'ja:\u672d\u6a3d\u81ea\u52d5\u8eca\u9053',
                'wikidata': 'Q867986', 'ref': 'E5A', 'route': 'road',
                'name:ja': u'\u672d\u6a3d\u81ea\u52d5\u8eca\u9053',
            }, ways=[24268939]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 24268939,
                'shield_text': 'E5A', 'network': 'JP:expressway',
            })

    def test_jp_c_expressway(self):
        import dsl

        z, x, y = (16, 58181, 25788)

        self.generate_fixtures(
            dsl.is_in('JP', z, x, y),
            # https://www.openstreetmap.org/way/297142400
            dsl.way(297142400, dsl.tile_diagonal(z, x, y), {
                'layer': '-1', 'name:en': 'Tokyo Gaikan Expressway',
                'lanes': '3', 'name': u'\u6771\u4eac\u5916\u74b0\u81ea'
                u'\u52d5\u8eca\u9053', 'oneway': 'yes', 'surface': 'paved',
                'source': 'openstreetmap.org', 'motorcycle': 'designated',
                'motorcar': 'designated', 'foot': 'no', 'bicycle': 'no',
                'toll': 'yes', 'ref': 'C3', 'smoothness': 'excellent',
                'highway': 'motorway', 'name:ja': u'\u6771\u4eac\u5916'
                u'\u74b0\u81ea\u52d5\u8eca\u9053',
            }),
            dsl.relation(1, {
                'name:en': 'Tokyo Gaikan Expressway',
                'from': u'\u5927\u6cc9IC', 'name': u'\u6771\u4eac\u5916'
                u'\u74b0\u81ea\u52d5\u8eca\u9053',
                'source': 'openstreetmap.org', 'wikipedia': u'ja:\u6771'
                u'\u4eac\u5916\u74b0\u81ea\u52d5\u8eca\u9053',
                'name:ja_kana': u'\u3068\u3046\u304d\u3087\u3046\u304c'
                '\u3044\u304b\u3093\u3058\u3069\u3046\u3057\u3083\u3069'
                u'\u3046', 'name:ja_rm': u'T\u014dky\u014d Gaikan Jid'
                u'\u014dshad\u014d', 'to': u'\u4e09\u90f7\u5357IC',
                'type': 'route', 'route': 'road',
                'name:ja': u'\u6771\u4eac\u5916\u74b0\u81ea\u52d5\u8eca\u9053',
            }, ways=[297142400]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 297142400,
                'shield_text': 'C3', 'network': 'JP:expressway',
            })

    def test_not_national_route(self):
        # as far as i can tell, anyway!
        import dsl

        z, x, y = (16, 56506, 26765)

        self.generate_fixtures(
            dsl.is_in('JP', z, x, y),
            # https://www.openstreetmap.org/way/240337769
            dsl.way(240337769, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': '262;29',
                'name': u'\u77f3\u57a3\u52a0\u4e16\u7530\u7dda',
                'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 240337769,
                'shield_text': type(None),
                'network': type(None),
            })
