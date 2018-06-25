# -*- encoding: utf-8 -*-
from . import FixtureTest


class FrenchShieldTest(FixtureTest):
    def test_e_road(self):
        import dsl

        z, x, y = (16, 33186, 22554)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/16108247
            dsl.way(16108247, dsl.tile_diagonal(z, x, y), {
                'horse': 'no', 'hazmat': 'no', 'bicycle': 'no',
                'name': u'Boulevard Périphérique Intérieur',
                'toll': 'no', 'surface': 'asphalt', 'lit': 'yes',
                'source': 'openstreetmap.org', 'maxspeed': '70',
                'int_ref': 'E 05', 'oneway': 'yes', 'foot': 'no', 'lanes': '3',
                'sidewalk': 'no', 'smoothness': 'excellent',
                'highway': 'trunk',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'bicycle': 'no',
                'name': u'Boulevard Périphérique de Paris',
                'source': 'openstreetmap.org',
            }, ways=[16108247]),
            dsl.relation(2, {
                'network': 'e-road', 'ref': 'E 05', 'route': 'road',
                'wikipedia': u'fr:Route européenne 5',
                'source': 'openstreetmap.org', 'wikidata': 'Q693493',
                'type': 'route', 'section': 'France (north-south)',
            }, ways=[16108247]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 16108247,
                'shield_text': 'E5', 'network': 'e-road',
            })

    def test_fr_d_road_no_relation(self):
        import dsl

        z, x, y = (16, 33094, 22481)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/35593697
            dsl.way(35593697, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'old_ref': 'N 183',
                'maxspeed': '90', 'ref': 'D 983', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 35593697,
                'shield_text': 'D983', 'network': 'FR:D-road',
            })

    def test_fr_d_road_relation(self):
        import dsl

        z, x, y = (16, 33716, 23296)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/137943124
            dsl.way(137943124, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'D 17',
                'highway': 'secondary',
            }),
            dsl.relation(1, {
                'name': 'D17(FR:01)', 'ref': 'D 17', 'route': 'road',
                'source': 'openstreetmap.org', 'type': 'route',
                'network': 'FR:01:D-road',
            }, ways=[137943124]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 137943124,
                'shield_text': 'D17', 'network': 'FR:D-road',
            })

    def test_fr_a_road_multiple_shields(self):
        import dsl

        z, x, y = (16, 32525, 22586)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/147156883
            dsl.way(147156883, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '130', 'lanes': '2',
                'name': 'Autoroute des Estuaires', 'toll': 'no',
                'source': 'openstreetmap.org', 'int_ref': 'E 03;E 401',
                'oneway': 'yes', 'operator': 'DIRNO', 'ref': 'A 84',
                'highway': 'motorway',
            }),
            dsl.relation(1, {
                'name': 'E 401 Saint-Brieuc - Caen', 'type': 'route',
                'route': 'road', 'source': 'openstreetmap.org',
                'name:fr': u'Route européenne E 401',
                'wikidata': 'Q1922885', 'ref': 'E 401',
                'description:fr': 'E 401 Saint-Brieuc - Caen',
                'network': 'e-road',
            }, ways=[147156883]),
            dsl.relation(2, {
                'name:en': 'E 03 Cherbourg - La Rochelle',
                'name': u'Route européenne E 03', 'type': 'route',
                'route': 'road', 'name:cs': u'Evropská silnice E03',
                'name:fr': u'Route européenne E 03',
                'source': 'openstreetmap.org',
                'e-road:class': 'A-intermediate',
                'wikipedia': 'en:European route E03',
                'wikidata': 'Q585439', 'ref': 'E 03',
                'description:fr': 'E 03 Cherbourg - La Rochelle',
                'network': 'e-road',
            }, ways=[147156883]),
            dsl.relation(3, {
                'name': 'Autoroute des Estuaires', 'ref': 'A 84',
                'route': 'road', 'source': 'openstreetmap.org',
                'type': 'route', 'network': 'FR:A-road',
            }, ways=[147156883]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 147156883,
                'shield_text': 'A84', 'network': 'FR:A-road',
                'all_networks': ['FR:A-road', 'e-road', 'e-road'],
                'all_shield_texts': ['A84', 'E3', 'E401'],
            })

    def test_fr_m_road(self):
        import dsl

        z, x, y = (16, 34078, 23914)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/4117272
            dsl.way(4117272, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '70', 'bicycle': 'no',
                'name': 'Promenade Edouard Corniglion-Molinier',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'ref': 'M 6098', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4117272,
                'shield_text': 'M6098', 'network': 'FR:M-road',
            })

    def test_fr_d_bis_road(self):
        import dsl

        z, x, y = (16, 33472, 22990)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/20225575
            dsl.way(20225575, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'D 977bis',
                'highway': 'secondary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 20225575,
                'shield_text': 'D977bis', 'network': 'FR:D-road',
            })

    # apparently RNIL roads used to be RN (national routes) but were delegated
    # to the local (department) government to look after. most were
    # re-designated as D-roads, but some are still RNIL and signed as if RN,
    # so we might as well treat them as RN?
    def test_fr_rnil_road(self):
        import dsl

        z, x, y = (16, 33218, 22520)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/10292212
            dsl.way(10292212, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'old_ref': 'N 2bis;N 2',
                'ref': 'RNIL 2', 'highway': 'primary', 'oneway': 'yes',
            }),
            dsl.relation(1, {
                'name': 'RNIL2(FR:93)', 'ref': 'RNIL 2', 'route': 'road',
                'source': 'openstreetmap.org', 'type': 'route',
                'network': 'FR:93:RNIL-road',
            }, ways=[10292212]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 10292212,
                'shield_text': 'N2', 'network': 'FR:N-road',
            })

    def test_fr_route_nationale(self):
        import dsl

        z, x, y = (16, 33512, 22698)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/28470567
            dsl.way(28470567, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '50', 'lanes': '2', 'name': 'Avenue du 1er Mai',
                'lit': 'yes', 'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'RN 19', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 28470567,
                'shield_text': 'N19', 'network': 'FR:N-road',
            })

    def test_fr_rnil_n_road(self):
        import dsl

        z, x, y = (16, 33208, 22525)

        self.generate_fixtures(
            dsl.is_in('FR', z, x, y),
            # https://www.openstreetmap.org/way/23306869
            dsl.way(23306869, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': 'Avenue de la Division Leclerc',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'operator': 'CG93', 'ref': 'N 2',
                'highway': 'primary',
            }),
            dsl.relation(1, {
                'name': 'RNIL2(FR:93)', 'ref': 'RNIL 2', 'route': 'road',
                'source': 'openstreetmap.org', 'type': 'route',
                'network': 'FR:93:RNIL-road',
            }, ways=[23306869]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 23306869,
                'shield_text': 'N2', 'network': 'FR:N-road',
                'all_networks': ['FR:N-road'],
                'all_shield_texts': ['N2'],
            })
