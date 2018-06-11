# -*- encoding: utf-8 -*-
from . import FixtureTest


class TurkishShieldTest(FixtureTest):
    def test_d550_tr(self):
        import dsl

        z, x, y = (16, 37647, 24651)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/4354149
            dsl.way(4354149, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 87;E 90',
                'name': u'E-87',
                'oneway': u'yes',
                'ref': u'D550',
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
            }, ways=[4354149]),
            dsl.relation(2, {
                'network': u'TR-roads',
                'ref': u'D 550',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4354149]),
            dsl.relation(3, {
                'name': u'European Road 90',
                'name:de': u'Europastraße 90',
                'name:en': u'European Road 90',
                'network': u'e-road',
                'note': u'Turkey',
                'ref': u'E 90',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4354149]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4354149,
                'network': 'TR:highway',
                'shield_text': 'D550',
                'all_networks': ['TR:highway', 'e-road', 'e-road'],
                'all_shield_texts': ['D550', 'E87', 'E90'],
            })

    def test_3276_tr(self):
        import dsl

        z, x, y = (16, 38284, 25292)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/4370152
            dsl.way(4370152, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'32-76',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4370152,
                'network': u'TR:provincial',
                'shield_text': u'32-76',
            })

    def test_o31_tr(self):
        import dsl

        z, x, y = (16, 37725, 25197)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/4392510
            dsl.way(4392510, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 87',
                'lanes': u'3',
                'maxspeed': u'120',
                'oneway': u'yes',
                'ref': u'O-31',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'toll': u'yes',
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
            }, ways=[4392510]),
            dsl.relation(2, {
                'e-road': u'A_link',
                'from': u'E 87',
                'network': u'e-road',
                'route': u'road',
                'source': u'openstreetmap.org',
                'to': u'E 96',
                'type': u'route',
            }, ways=[4392510]),
            dsl.relation(3, {
                'description': u'İzmir - Aydın otoyolu',
                'network': u'TR-roads',
                'ref': u'O-31',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4392510]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4392510,
                'network': u'TR:motorway',
                'shield_text': u'O31',
                'all_networks': ['TR:motorway', 'e-road'],
                'all_shield_texts': ['O31', 'E87'],
            })

    def test_o4_tr(self):
        import dsl

        z, x, y = (16, 38700, 24768)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/4316183
            dsl.way(4316183, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 89',
                'lanes': u'3',
                'name': u'Anadolu Otoyolu',
                'oneway': u'yes',
                'ref': u'O-4',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'description:fr': u'E 89 Gerede - Ankara',
                'e-road:class': u'A-intermediate',
                'name:fr': u'Route européenne E 89',
                'network': u'e-road',
                'ref': u'E 89',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q2419632',
            }, ways=[4316183]),
            dsl.relation(2, {
                'description': u'İstanbul - Ankara Otoyolu',
                'network': u'TR-road',
                'ref': u'O-4',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4316183]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4316183,
                'network': u'TR:motorway',
                'shield_text': u'O4',
                'all_networks': ['TR:motorway', 'e-road'],
                'all_shield_texts': ['O4', 'E89'],
            })

    def test_d230_d650_tr(self):
        import dsl

        z, x, y = (16, 38239, 24918)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/4378290
            dsl.way(4378290, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'oneway': u'yes',
                'ref': u'D230;D650',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'TR-roads',
                'ref': u'D 230',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4378290]),
        )

        # note that D650, despite being numerically greater than D230, comes
        # first. this is because some highways are apparently "major" highways
        # although this doesn't make a difference to their shield.
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4378290,
                'network': 'TR:highway',
                'shield_text': 'D650',
                'all_networks': ['TR:highway', 'TR:highway'],
                'all_shield_texts': ['D650', 'D230'],
            })

    def test_d975_tr(self):
        import dsl

        z, x, y = (16, 40716, 25058)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/13753458
            dsl.way(13753458, dsl.tile_diagonal(z, x, y), {
                'access': u'yes',
                'bicycle': u'yes',
                'cycleway': u'no',
                'foot': u'yes',
                'highway': u'primary',
                'lanes': u'2',
                'maxspeed': u'90',
                'name': u'Van-Iğdır yolu',
                'oneway': u'no',
                'ref': u'D 975',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'D 975',
                'network': u'TR-roads',
                'ref': u'D 975',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[13753458]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 13753458,
                'network': u'TR:highway',
                'shield_text': u'D975',
            })

    def test_d550_07_tr(self):
        import dsl

        z, x, y = (16, 37691, 24911)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/4391958
            dsl.way(4391958, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 87',
                'lanes': u'2',
                'name': u'İzmir Çanakkale Yolu',
                'oneway': u'yes',
                'ref': u'D550-07',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
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
            }, ways=[4391958]),
            dsl.relation(2, {
                'network': u'TR-roads',
                'ref': u'D 550',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4391958]),
        )

        # we drop the "-07" suffix. it seems to be some kind of section number.
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4391958,
                'network': u'TR:highway',
                'shield_text': u'D550',
                'all_networks': ['TR:highway', 'e-road'],
                'all_shield_texts': ['D550', 'E87'],
            })

    def test_d260_tr(self):
        import dsl

        z, x, y = (16, 38509, 24944)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/4636868
            dsl.way(4636868, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'level': u'-1',
                'oneway': u'yes',
                'ref': u'D-260',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'TR-roads',
                'ref': u'D 260',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4636868]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4636868,
                'network': u'TR:highway',
                'shield_text': u'D260',
            })

    def test_d965_d060_tr(self):
        import dsl

        z, x, y = (16, 40623, 24630)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/47053015
            dsl.way(47053015, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'int_ref': u'E 691',
                'name': u'Kars-Ardahan yolu',
                'ref': u'D 965 / D 060',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            # this is in some relations, but this test is about parsing the ref
            # that has all those spaces and slashes in it.
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 47053015,
                'network': u'TR:highway',
                'shield_text': u'D060',
                'all_networks': ['TR:highway', 'TR:highway'],
                'all_shield_texts': ['D060', 'D965'],
            })

    def test_1102_trprovincial(self):
        import dsl

        z, x, y = (16, 38240, 24734)

        self.generate_fixtures(
            dsl.is_in('TR', z, x, y),
            # https://www.openstreetmap.org/way/4385439
            dsl.way(4385439, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'11-02',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4385439,
                'network': u'TR:provincial',
                'shield_text': u'11-02',
            })
