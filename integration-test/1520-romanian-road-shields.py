# -*- encoding: utf-8 -*-
from . import FixtureTest


class RomanianShieldTest(FixtureTest):
    def test_a2_ro(self):
        import dsl

        z, x, y = (16, 37541, 23726)

        self.generate_fixtures(
            dsl.is_in('RO', z, x, y),
            # https://www.openstreetmap.org/way/15241569
            dsl.way(15241569, dsl.tile_diagonal(z, x, y), {
                'access': u'yes',
                'highway': u'motorway',
                'int_ref': u'E 81',
                'lanes': u'2',
                'maxspeed': u'100',
                'name': u'Autostrada Soarelui',
                'oneway': u'yes',
                'ref': u'A2',
                'smoothness': u'good',
                'source': u'openstreetmap.org',
                'start_date': u'2004',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'description:fr': u'E 81 Moukatchevo - Constanţa',
                'e-road:class': u'A-intermediate',
                'name:fr': u'Route européenne E 81',
                'network': u'e-road',
                'ref': u'E 81',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q987350',
            }, ways=[15241569]),
            dsl.relation(2, {
                'name': u'Autostrada A2',
                'network': u'A',
                'ref': u'A2',
                'route': u'road',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'type': u'route',
                'wikidata': u'Q429447',
                'wikipedia': u'en:A2 motorway (Romania)',
            }, ways=[15241569]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 15241569,
                'network': u'RO:motorway',
                'shield_text': u'A2',
                'all_networks': ['RO:motorway', 'e-road'],
                'all_shield_texts': ['A2', 'E81'],
            })

    def test_dn21_ro(self):
        import dsl

        z, x, y = (16, 37764, 23639)

        self.generate_fixtures(
            dsl.is_in('RO', z, x, y),
            # https://www.openstreetmap.org/way/2160
            dsl.way(2160, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 584',
                'lanes': u'2',
                'maxspeed': u'100',
                'nat_ref': u'DN21',
                'oneway': u'no',
                'ref': u'DN21',
                'smoothness': u'good',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'surface_survey': u'2015',
            }),
            dsl.relation(1, {
                'description:fr': u'E 584 Poltava - Slobozia',
                'e-road:class': u'B',
                'name:fr': u'Route européenne E 584',
                'network': u'e-road',
                'ref': u'E 584',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q546742',
            }, ways=[2160]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 2160,
                'network': u'RO:national',
                'shield_text': u'21',
                'all_networks': ['RO:national', 'e-road'],
                'all_shield_texts': ['21', 'E584'],
            })

    def test_dj200b_ro(self):
        import dsl

        z, x, y = (16, 37519, 23715)

        self.generate_fixtures(
            dsl.is_in('RO', z, x, y),
            # https://www.openstreetmap.org/way/3118247
            dsl.way(3118247, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'is_in:city': u'București',
                'lanes': u'2',
                'maxspeed': u'50',
                'name': u'Bulevardul Iancu de Hunedoara',
                'oneway': u'yes',
                'ref': u'DJ200B',
                'smoothness': u'excellent',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3118247,
                'network': u'RO:county',
                'shield_text': u'200B',
            })

    def test_dc86_ro(self):
        import dsl

        z, x, y = (16, 37979, 23748)

        self.generate_fixtures(
            dsl.is_in('RO', z, x, y),
            # https://www.openstreetmap.org/way/12109479
            dsl.way(12109479, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'highway': u'primary',
                'is_in:city': u'Năvodari',
                'lanes': u'2',
                'maxspeed': u'70',
                'oneway': u'no',
                'ref': u'DC86',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 12109479,
                'network': u'RO:local',
                'shield_text': u'86',
            })
