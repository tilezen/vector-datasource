# -*- encoding: utf-8 -*-
from . import FixtureTest


class IndianShieldTest(FixtureTest):
    def test_547e_innh(self):
        import dsl

        z, x, y = (16, 47127, 28829)

        self.generate_fixtures(
            dsl.is_in('IN', z, x, y),
            # https://www.openstreetmap.org/way/28465477
            dsl.way(28465477, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'ref': u'NH547E',
                'ref:old': u'SH265',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'IN:NH:MH',
                'note': u'NH547E in MH',
                'ref': u'NH547E',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[28465477]),
            dsl.relation(2, {
                'network': u'IN:NH',
                'ref': u'NH547E',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[28465477]),
            dsl.relation(3, {
                'name': u'SH265',
                'ref': u'SH265',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[28465477]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 28465477,
                'network': 'IN:NH',
                'shield_text': '547E',
                'all_networks': ['IN:NH', 'IN:SH'],
                'all_shield_texts': ['547E', '265'],
            })

    def test_161_innh(self):
        import dsl

        z, x, y = (16, 46811, 29105)

        self.generate_fixtures(
            dsl.is_in('IN', z, x, y),
            # https://www.openstreetmap.org/way/22865906
            dsl.way(22865906, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'ref': u'NH161;SH204',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'IN:NH:MH',
                'note': u'NH161 in MH',
                'ref': u'NH161',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[22865906]),
            dsl.relation(2, {
                'name': u'National Highway 161',
                'network': u'IN:NH',
                'ref': u'NH161',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[22865906]),
            dsl.relation(3, {
                'name': u'SH204',
                'ref': u'SH204',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[22865906]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22865906,
                'network': 'IN:NH',
                'shield_text': '161',
                'all_networks': ['IN:NH', 'IN:SH'],
                'all_shield_texts': ['161', '204'],
            })

    def test_6a_insh(self):
        import dsl

        z, x, y = (16, 47119, 30547)

        self.generate_fixtures(
            dsl.is_in('IN', z, x, y),
            # https://www.openstreetmap.org/way/22832164
            dsl.way(22832164, dsl.tile_diagonal(z, x, y), {
                'AND:importance_level': u'5',
                'AND_a_nosr_r': u'15061209',
                'highway': u'primary',
                'name': u'Tiruvannamalai - Harur State Highway',
                'ref': u'SH6A',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22832164,
                'network': u'IN:SH',
                'shield_text': u'6A',
            })

    def test_54_inmdr(self):
        import dsl

        z, x, y = (16, 46579, 26841)

        self.generate_fixtures(
            dsl.is_in('IN', z, x, y),
            # https://www.openstreetmap.org/way/11760010
            dsl.way(11760010, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Rahon Road',
                'ref': u'MDR54',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'IN:SH:PB',
                'ref': u'MDR54',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[11760010]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 11760010,
                'network': u'IN:MDR',
                'shield_text': u'54',
            })

    def test_none_inmdr(self):
        import dsl

        z, x, y = (16, 48428, 27975)

        self.generate_fixtures(
            dsl.is_in('IN', z, x, y),
            # https://www.openstreetmap.org/way/22828011
            dsl.way(22828011, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'MDR',
                'source': u'openstreetmap.org',
                'surface': u'paved',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22828011,
                'network': u'IN:MDR',
                'shield_text': type(None),
            })

    def test_inroads(self):
        import dsl

        z, x, y = (16, 46765, 26893)

        self.generate_fixtures(
            dsl.is_in('IN', z, x, y),
            # https://www.openstreetmap.org/way/169248989
            dsl.way(169248989, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'maxspeed': u'50',
                'name': u'Panchkula - Nahan Road',
                'ref': u'MDR118',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Haryana Major District Road 118',
                'network': u'IN:SH:HR',
                'ref': u'MDR118',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[169248989]),
            dsl.relation(2, {
                'name': u'Panchkula - Nahan Road',
                'name:en': u'Panchkula - Nahan Road',
                'network': u'IN-roads',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[169248989]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 169248989,
                'network': 'IN:MDR',
                'shield_text': '118',
                'all_networks': ['IN:MDR'],
                'all_shield_texts': ['118'],
            })

    def test_orr_innh_chennai(self):
        import dsl

        z, x, y = (16, 47346, 30371)

        self.generate_fixtures(
            dsl.is_in('IN', z, x, y),
            # https://www.openstreetmap.org/way/26807719
            dsl.way(26807719, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'3',
                'layer': u'1',
                'maxspeed': u'100',
                'motorroad': u'yes',
                'name': u'Outer Ring Road',
                'oneway': u'yes',
                'ref': u'ORR',
                'source': u'openstreetmap.org',
                'source:lanes': u'DigitalGlobeStandard',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26807719,
                'network': u'IN:NH',
                'shield_text': u'ORR',
            })

    def test_orr_innh_hyderabad(self):
        import dsl

        z, x, y = (16, 47010, 29526)

        self.generate_fixtures(
            dsl.is_in('IN', z, x, y),
            # https://www.openstreetmap.org/way/520309418
            dsl.way(520309418, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'no',
                'foot': u'no',
                'highway': u'motorway',
                'horse': u'no',
                'lanes': u'4',
                'maxspeed': u'120',
                'motor_vehicle': u'designated',
                'motorcycle': u'no',
                'name': u'Outer Ring Road',
                'official_name': u'Nehru Outer Ring Road',
                'oneway': u'yes',
                'ref': u'ORR',
                'smoothness': u'excellent',
                'source': u'openstreetmap.org',
                'start_date': u'2011-08-14',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Nehru Outer Ring Road',
                'note': u'see other relation',
                'operator': u'HMDA',
                'ref': u'ORR',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q7112004',
            }, ways=[520309418]),
            dsl.relation(2, {
                'highway': u'motorway',
                'name': u'Outer Ring Road',
                'official_name': u'Nehru Outer Ring Road',
                'operator': u'HMDA',
                'ref': u'ORR',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q7112004',
                'wikipedia': u'en:Outer Ring Road, Hyderabad',
            }, ways=[520309418]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 520309418,
                'network': u'IN:NH',
                'shield_text': u'ORR',
            })
