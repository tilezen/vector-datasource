from . import FixtureTest


class ChinaShieldTest(FixtureTest):
    def test_cn_expressway(self):
        import dsl

        z, x, y = (16, 54413, 26599)

        self.generate_fixtures(
            dsl.is_in('CN', z, x, y),
            # https://www.openstreetmap.org/way/127553001
            dsl.way(127553001, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Huning Expressway', 'lanes': '4',
                'name': u'\u6caa\u5b81\u9ad8\u901f', 'surface': 'asphalt',
                'source': 'openstreetmap.org', 'maxspeed': '120',
                'int_ref': 'AH5', 'oneway': 'yes', 'ref': 'G42',
                'highway': 'motorway',
            }),
            dsl.relation(1, {
                'name:en': 'G42 Hurong Expressway',
                'network': 'CN-expressways', 'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org', 'ref': 'G42',
                'name': u'\u6caa\u84c9\u9ad8\u901f',
            }, ways=[127553001]),
            dsl.relation(2, {
                'from': 'Shanghai', 'int_name': 'Asian Highway AH5',
                'name:id': 'AH5', 'int_ref': 'AH5',
                'name': 'Asian Highway AH5', 'network': 'AsianHighway',
                'ref': 'AH5', 'route': 'road', 'source': 'openstreetmap.org',
                'to': 'Istanbul', 'type': 'route', 'wikidata': 'Q4651742',
                'wikipedia': 'en:AH5',
            }, ways=[127553001]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 127553001,
                'shield_text': 'G42', 'network': 'CN:expressway',
                'all_shield_texts': ['G42', 'AH5'],
                'all_networks': ['CN:expressway', 'AsianHighway'],
            })

    def test_cn_expressway_regional(self):
        import dsl

        z, x, y = (16, 54858, 26781)

        self.generate_fixtures(
            dsl.is_in('CN', z, x, y),
            # https://www.openstreetmap.org/way/168706293
            dsl.way(168706293, dsl.tile_diagonal(z, x, y), {
                'old_ref': 'A20', 'name:en': 'Outer Ring Expressway',
                'lanes': '4', 'name': u'\u5916\u73af\u9ad8\u901f',
                'source': 'openstreetmap.org', 'oneway': 'yes', 'ref': 'S20',
                'highway': 'motorway',
            }),
            dsl.relation(1, {
                'old_ref': 'A20', 'name:en': 'Outer Ring Expressway',
                'name': u'\u5916\u73af\u9ad8\u901f', 'type': 'route',
                'route': 'road', 'source': 'openstreetmap.org', 'ref': 'S20',
                'network': 'CN-expressways',
            }, ways=[168706293]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 168706293,
                'shield_text': 'S20',
                'network': 'CN:expressway:regional',
            })

    # test for road with multiple CN-expressway shields on it
    def test_cn_multiple_expressway(self):
        import dsl

        z, x, y = (16, 54161, 26636)

        self.generate_fixtures(
            dsl.is_in('CN', z, x, y),
            # https://www.openstreetmap.org/way/65176048
            dsl.way(65176048, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Hefei Ring Expressway', 'lanes': '2',
                'name': u'\u5408\u80a5\u7ed5\u57ce\u9ad8\u901f',
                'source': 'openstreetmap.org', 'int_ref': 'AH5',
                'oneway': 'yes', 'ref': 'G3;G40;G42;G4001',
                'highway': 'motorway_link',
            }),
            dsl.relation(1, {
                'name:en': 'G40 Hushan Expressway',
                'network': 'CN-expressways', 'type': 'route', 'route': 'road',
                'wikipedia': u'zh:\u6caa\u9655\u9ad8\u901f\u516c\u8def',
                'source': 'openstreetmap.org',
                'alt_name:en': "G40 Shanghai-Xi'an Expressway",
                'wikidata': 'Q785438', 'ref': 'G40',
                'name': u'\u6caa\u9655\u9ad8\u901f',
            }, ways=[65176048]),
            dsl.relation(2, {
                'name:en': 'G42 Hurong Expressway',
                'network': 'CN-expressways', 'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org', 'ref': 'G42',
                'name': u'\u6caa\u84c9\u9ad8\u901f',
            }, ways=[65176048]),
            dsl.relation(3, {
                'alt_name:en': u'G3 Beijing\u2013Taipei Expressway',
                'name': u'\u4eac\u53f0\u9ad8\u901f',
                'source': 'openstreetmap.org', 'type': 'route',
                'route': 'road', 'network': 'CN-expressways', 'ref': 'G3',
            }, ways=[65176048]),
            dsl.relation(4, {
                'from': 'Shanghai', 'int_name': 'Asian Highway AH5',
                'int_ref': 'AH5', 'name': 'Asian Highway AH5',
                'network': 'AsianHighway', 'ref': 'AH5', 'route': 'road',
                'source': 'openstreetmap.org', 'to': 'Istanbul',
                'type': 'route', 'wikidata': 'Q4651742',
                'wikipedia': 'en:AH5',
            }, ways=[65176048]),
            dsl.relation(5, {
                'name': u'\u5408\u80a5\u7ed5\u57ce\u9ad8\u901f',
                'name:en': 'G4001 Hefei Ring Expressway',
                'network': 'CN-expressways', 'ref': 'G4001', 'route': 'road',
                'source': 'openstreetmap.org', 'type': 'route',
            }, ways=[65176048]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 65176048,
                'shield_text': 'G3', 'network': 'CN:expressway',
                'all_networks': [
                    'CN:expressway',
                    'CN:expressway',
                    'CN:expressway',
                    'CN:expressway',
                    'AsianHighway',
                ],
                'all_shield_texts': [
                    'G3', 'G40', 'G42', 'G4001', 'AH5',
                ],
            })

    # China appears to have a fairly common 3rd type of road, signified with an
    # X000 number. based on the positions of X & S in the ref, it seems like a
    # less important route type. the network is occasionally given as
    # "JX-roads", which appears to mean Jianxi province. therefore we designate
    # as "CN:JX"
    def test_cn_x102(self):
        import dsl

        z, x, y = (16, 51492, 28421)

        self.generate_fixtures(
            dsl.is_in('CN', z, x, y),
            # https://www.openstreetmap.org/way/50677938
            dsl.way(50677938, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'X102;S214',
                'highway': 'primary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'S214',
                'name': 'S214', 'source': 'openstreetmap.org',
            }, ways=[50677938]),
            dsl.relation(2, {
                'type': 'route', 'route': 'road', 'ref': 'X102',
                'name': 'X102', 'source': 'openstreetmap.org',
            }, ways=[50677938]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 50677938,
                'shield_text': 'S214', 'network': 'CN:expressway:regional',
                'all_shield_texts': ['S214', 'X102'],
                'all_networks': [
                    'CN:expressway:regional',
                    'CN:JX',
                ],
            })

    def test_cn_jx_roads_without_relation(self):
        import dsl

        z, x, y = (16, 51525, 27998)

        self.generate_fixtures(
            dsl.is_in('CN', z, x, y),
            # https://www.openstreetmap.org/way/137979647
            dsl.way(137979647, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'X032;X059',
                'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 137979647,
                'shield_text': 'X032',
                'network': 'CN:JX',
                'all_shield_texts': ['X032', 'X059'],
            })

    # test that the more elaborate ref G4W2 passes through the system OK, and
    # doesn't get mangled by any assumptions that refs fit into a
    # "^[GSX][0-9]+$" pattern.
    #
    # note that the G107 relation also has "network=CN-roads", which we should
    # correct to "CN:expressway".
    #
    def test_cn_g4w2(self):
        import dsl

        z, x, y = (16, 53263, 28168)

        self.generate_fixtures(
            dsl.is_in('CN', z, x, y),
            # https://www.openstreetmap.org/way/49242320
            dsl.way(49242320, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': 'Qinglian Expressway',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'G4W2;G107', 'highway': 'motorway',
            }),
            dsl.relation(1, {
                'name:en': 'China National Highway 107', 'network': 'CN-roads',
                'ref': 'G107', 'route': 'road', 'name': u'107\u56fd\u9053',
                'source': 'openstreetmap.org', 'type': 'route',
                'name:zh': u'107\u56fd\u9053', 'highway': 'trunk',
                'description': 'G107 runs from Beijing to Shenzhen via Wuhan',
            }, ways=[49242320]),
            dsl.relation(2, {
                'name:en': 'Xuchang-Guangzhou Expressway',
                'name': u'\u8bb8\u5e7f\u9ad8\u901f',
                'name:zh': u'\u8bb8\u5e7f\u9ad8\u901f', 'route': 'road',
                'wikipedia': u'zh:\u8bb8\u5e7f\u9ad8\u901f\u516c\u8def',
                'source': 'openstreetmap.org', 'type': 'route', 'ref': 'G4W2',
                'network': 'CN-expressways',
            }, ways=[49242320]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 49242320,
                'shield_text': 'G4W2', 'network': 'CN:expressway',
                'all_shield_texts': ['G4W2', 'G107'],
                'all_networks': ['CN:expressway', 'CN:expressway'],
            })
