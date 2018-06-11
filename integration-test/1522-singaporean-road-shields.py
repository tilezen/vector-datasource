# -*- encoding: utf-8 -*-
from . import FixtureTest


class SingaporeanShieldTest(FixtureTest):

    def test_aye_sgexpressway(self):
        import dsl

        z, x, y = (16, 51670, 32536)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/15005218
            dsl.way(15005218, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'motorway',
                'lanes': u'2',
                'layer': u'1',
                'maxspeed': u'90',
                'name': u'Ayer Rajah Expressway',
                'oneway': u'yes',
                'ref': u'AYE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 15005218,
                'network': u'SG:expressway',
                'shield_text': u'AYE',
            })

    def test_bke_sgexpressway(self):
        import dsl

        z, x, y = (16, 51662, 32522)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/44839300
            dsl.way(44839300, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'3',
                'maxspeed': u'90',
                'name': u'Bukit Timah Expressway',
                'oneway': u'yes',
                'ref': u'BKE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 44839300,
                'network': u'SG:expressway',
                'shield_text': u'BKE',
            })

    def test_cte_sgexpressway(self):
        import dsl

        z, x, y = (16, 51674, 32514)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/14061945
            dsl.way(14061945, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'4',
                'maxspeed': u'80',
                'name': u'Central Expressway',
                'oneway': u'yes',
                'ref': u'CTE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 14061945,
                'network': u'SG:expressway',
                'shield_text': u'CTE',
            })

    def test_ecp_sgexpressway(self):
        import dsl

        z, x, y = (16, 51697, 32523)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/23149902
            dsl.way(23149902, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'4',
                'maxspeed': u'50',
                'name': u'East Coast Parkway',
                'oneway': u'yes',
                'ref': u'ECP',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23149902,
                'network': u'SG:expressway',
                'shield_text': u'ECP',
            })

    def test_kje_sgexpressway(self):
        import dsl

        z, x, y = (16, 51652, 32516)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/109401032
            dsl.way(109401032, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'motorway',
                'lanes': u'3',
                'layer': u'1',
                'maxspeed': u'90',
                'name': u'Lam Sam Flyover',
                'oneway': u'yes',
                'ref': u'KJE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 109401032,
                'network': u'SG:expressway',
                'shield_text': u'KJE',
            })

    def test_kpe_sgexpressway(self):
        import dsl

        z, x, y = (16, 51682, 32520)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/22791293
            dsl.way(22791293, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'3',
                'maxspeed': u'80',
                'name': u'Kallang-Paya Lebar Expressway',
                'oneway': u'yes',
                'ref': u'KPE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22791293,
                'network': u'SG:expressway',
                'shield_text': u'KPE',
            })

    def test_mce_sgexpressway(self):
        import dsl

        z, x, y = (16, 51678, 32532)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/116796554
            dsl.way(116796554, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'4',
                'layer': u'-2',
                'maxspeed': u'80',
                'name': u'Marina Coastal Expressway',
                'oneway': u'yes',
                'ref': u'MCE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'tunnel': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 116796554,
                'network': u'SG:expressway',
                'shield_text': u'MCE',
            })

    def test_pie_sgexpressway(self):
        import dsl

        z, x, y = (16, 51639, 32526)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/32877553
            dsl.way(32877553, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'4',
                'name': u'Pan-Island Expressway',
                'oneway': u'yes',
                'ref': u'PIE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 32877553,
                'network': u'SG:expressway',
                'shield_text': u'PIE',
            })

    def test_sle_sgexpressway(self):
        import dsl

        z, x, y = (16, 51674, 32513)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/15092487
            dsl.way(15092487, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'3',
                'maxspeed': u'80',
                'name': u'Seletar Expressway',
                'oneway': u'yes',
                'ref': u'SLE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 15092487,
                'network': u'SG:expressway',
                'shield_text': u'SLE',
            })

    def test_tpe_sgexpressway(self):
        import dsl

        z, x, y = (16, 51673, 32513)

        self.generate_fixtures(
            dsl.is_in('SG', z, x, y),
            # https://www.openstreetmap.org/way/14058412
            dsl.way(14058412, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'lanes': u'2',
                'maxspeed': u'90',
                'name': u'Tampines Expressway',
                'oneway': u'yes',
                'ref': u'TPE',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 14058412,
                'network': u'SG:expressway',
                'shield_text': u'TPE',
            })
