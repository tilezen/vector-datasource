from . import FixtureTest


class GermanShieldTest(FixtureTest):
    def test_de_bab(self):
        import dsl

        z, x, y = (16, 34029, 22225)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/52480330
            dsl.way(52480330, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '130', 'lanes': '2', 'incline': '6%',
                'source:maxspeed': 'DE:motorway', 'lit': 'no',
                'source': 'openstreetmap.org', 'zone:traffic': 'DE:rural',
                'int_ref': 'E 44', 'oneway': 'yes', 'ref': 'A 1',
                'highway': 'motorway',
            }),
            dsl.relation(1, {
                'network': 'e-road', 'type': 'route', 'route': 'road',
                'name:fr': u'Route europ\xe9enne E 44',
                'source': 'openstreetmap.org',
                'e-road:class': 'A-intermediate', 'wikidata': 'Q705125',
                'ref': 'E 44', 'description:fr': 'E 44 Le Havre - Giessen',
                'name': 'E 44 Le Havre - Giessen',
            }, ways=[52480330]),
            dsl.relation(2, {
                'name': 'Bundesautobahn 1', 'type': 'route', 'route': 'road',
                'wikipedia': 'de:Bundesautobahn 1',
                'source': 'openstreetmap.org', 'short_name:de': 'BAB 1',
                'wikidata': 'Q9006', 'operator': 'Bundesrepublik Deutschland',
                'ref': 'A 1', 'TMC:cid_58:tabcd_1:Class': 'Road',
                'network': 'BAB',
            }, ways=[52480330]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 52480330,
                'shield_text': 'A1', 'network': 'DE:BAB',
                'all_shield_texts': ['A1', 'E44'],
                'all_networks': ['DE:BAB', 'e-road'],
            })

    def test_de_bab_operator_via(self):
        import dsl

        z, x, y = (16, 34234, 22595)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/207881430
            dsl.way(207881430, dsl.tile_diagonal(z, x, y), {
                'source:lit': 'http://www.autobahn-bilder.de',
                'maxspeed': 'none', 'lanes': '3', 'operator:type': 'private',
                'source:maxspeed': 'DE:motorway', 'surface': 'asphalt',
                'lit': 'no', 'source': 'openstreetmap.org',
                'zone:traffic': 'DE:motorway', 'int_ref': 'E 35;E 52',
                'oneway': 'yes', 'operator': u'Via Solutions S\xfcdwest',
                'shoulder:right': 'yes', 'ref': 'A 5', 'highway': 'motorway',
            }),
            dsl.relation(1, {
                'network': 'e-road', 'ref': 'E 52', 'route': 'road',
                'source': 'openstreetmap.org', 'type': 'route',
                'section': 'west-west',
            }, ways=[207881430]),
            dsl.relation(2, {
                'from': 'Amsterdam', 'network': 'e-road',
                'source': 'openstreetmap.org', 'type': 'route',
                'route': 'road', 'wikipedia': 'en:European route E35',
                'to': 'Roma', 'wikidata': 'Q313416', 'ref': 'E 35',
                'section': 'Germany (south-north)',
            }, ways=[207881430]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 207881430,
                'shield_text': 'A5', 'network': 'DE:BAB',
                'all_shield_texts': ['A5', 'E35', 'E52'],
                'all_networks': ['DE:BAB', 'e-road', 'e-road'],
            })

    def test_de_bab_operator_a8(self):
        import dsl

        z, x, y = (16, 34798, 22688)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/280688897
            dsl.way(280688897, dsl.tile_diagonal(z, x, y), {
                'source:lit': 'http://www.autobahn-bilder.de',
                'maxspeed': 'none', 'lanes': '3', 'operator:type': 'private',
                'source:maxspeed': 'DE:motorway', 'lit': 'no',
                'source': 'openstreetmap.org', 'tmc': 'DE:60763/12559',
                'bdouble': 'yes', 'int_ref': 'E 52', 'oneway': 'yes',
                'operator': 'autobahnplus A8 GmbH', 'ref': 'A 8',
                'highway': 'motorway',
            }),
            # note: was a relation in here, but i removed it because i want to
            # test the operator overload, not the relation handling.
            dsl.relation(2, {
                'name:en': 'European Road E 52', 'name': 'European Road E 52',
                'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org', 'ref': 'E 52',
                'section': 'east-west', 'network': 'e-road',
            }, ways=[280688897]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 280688897,
                'shield_text': 'A8', 'network': 'DE:BAB',
                'all_shield_texts': ['A8', 'E52'],
                'all_networks': ['DE:BAB', 'e-road'],
            })

    def test_de_bs(self):
        import dsl

        z, x, y = (16, 34605, 21611)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/5136775
            dsl.way(5136775, dsl.tile_diagonal(z, x, y), {
                'source:maxspeed': 'DE:rural', 'source': 'openstreetmap.org',
                'maxspeed': '100', 'ref': 'B 6', 'highway': 'secondary',
            }),
            dsl.relation(1, {
                'name': 'B 6 Salzgitter - Hildesheim', 'ref': 'B 6',
                'route': 'road', 'source': 'openstreetmap.org',
                'operator': 'Bundesrepublik Deutschland', 'type': 'route',
            }, ways=[5136775]),
            dsl.relation(2, {
                'name': 'B 6 Hildesheim - Salzgitter', 'ref': 'B 6',
                'route': 'road', 'source': 'openstreetmap.org',
                'operator': 'Bundesrepublik Deutschland', 'type': 'route',
            }, ways=[5136775]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 5136775,
                'shield_text': 'B6', 'network': 'DE:BS',
                'all_shield_texts': ['B6'],
                'all_networks': ['DE:BS'],
            })

    def test_de_bs_no_relation(self):
        import dsl

        z, x, y = (16, 33862, 21706)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/246556060
            dsl.way(246556060, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '100', 'lanes:backward': '1',
                'source:maxspeed': 'DE:rural', 'source': 'openstreetmap.org',
                'lanes': '2', 'ref': 'B 9', 'lanes:forward': '1',
                'highway': 'primary',
            }),
            # there _is_ a relation here, but it's useless because it has
            # neither ref nor network tags.
            dsl.relation(1, {
                'name': u'Bundesstra\xdfe 9', 'route': 'road',
                'source': 'openstreetmap.org', 'wikidata': 'Q34462',
                'type': 'route',
            }, ways=[246556060]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 246556060,
                'shield_text': 'B9', 'network': 'DE:BS',
                'all_shield_texts': ['B9'],
                'all_networks': ['DE:BS'],
            })

    def test_de_ls(self):
        import dsl

        z, x, y = (16, 34070, 21976)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/28859327
            dsl.way(28859327, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '80', 'name': u'Alte K\xf6lner Stra\xdfe',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'cycleway:both': 'no', 'loc_name': u'Panzerstra\xdfe',
                'ref': 'L 84', 'highway': 'secondary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'L 84',
                'network': u'Landesstra\xdfen NRW',
                'source': 'openstreetmap.org',
            }, ways=[28859327]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 28859327,
                'shield_text': 'L84', 'network': 'DE:LS',
                'all_shield_texts': ['L84'],
                'all_networks': ['DE:LS'],
            })

    def test_de_ls_pattern(self):
        import dsl

        z, x, y = (16, 33977, 22243)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/114110755
            dsl.way(114110755, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'maxspeed': '100',
                'ref': 'L 39', 'highway': 'secondary',
            }),
            dsl.relation(1, {
                'name': u'Landstra\xdfe 39', 'ref': 'L 39', 'route': 'road',
                'source': 'openstreetmap.org', 'operator': 'Rheinland-Pfalz',
                'type': 'route',
            }, ways=[114110755]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 114110755,
                'shield_text': 'L39', 'network': 'DE:LS',
                'all_shield_texts': ['L39'],
                'all_networks': ['DE:LS'],
            })

    def test_de_ks(self):
        import dsl

        z, x, y = (16, 34590, 21600)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/24319153
            dsl.way(24319153, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'K 203',
                'highway': 'tertiary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'K 203',
                'network': u'Kreisstra\xdfen Hildesheim',
                'source': 'openstreetmap.org',
            }, ways=[24319153]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 24319153,
                'shield_text': 'K203', 'network': 'DE:KS',
                'all_shield_texts': ['K203'],
                'all_networks': ['DE:KS'],
            })

    def test_de_ks_no_relation(self):
        import dsl

        z, x, y = (16, 33978, 22242)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/25839765
            dsl.way(25839765, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'K 40',
                'highway': 'tertiary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25839765,
                'shield_text': 'K40', 'network': 'DE:KS',
                'all_shield_texts': ['K40'],
                'all_networks': ['DE:KS'],
            })

    # https://de.wikipedia.org/wiki/Liste_der_Staatsstra%C3%9Fen_in_Bayern
    def test_de_staatstrasse_bayern(self):
        import dsl

        z, x, y = (16, 34765, 22335)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/3925136
            dsl.way(3925136, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '70', 'lanes': '4', 'source:maxspeed': 'sign',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'embankment': 'yes', 'sidewalk': 'separate', 'ref': 'St 2240',
                'highway': 'secondary',
            }),
            dsl.relation(1, {
                'description': u'Staatsstra\xdfe St 2240: ...',
                'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org', 'operator': 'Freistaat Bayern',
                'ref': 'St 2240',
            }, ways=[3925136]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3925136,
                'shield_text': 'St2240', 'network': 'DE:STS',
            })

    # https://de.wikipedia.org/wiki/Liste_der_Staatsstra%C3%9Fen_in_Sachsen_bis_zur_S_199
    def test_de_staatstrasse_sachsen(self):
        import dsl

        z, x, y = (16, 35269, 21920)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/3358875
            dsl.way(3358875, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '50', 'lanes': '2', 'surface': 'asphalt',
                'name': u'Gro\xdfenhainer Stra\xdfe', 'lit': 'yes',
                'source': 'openstreetmap.org', 'oneway': 'yes', 'foot': 'no',
                'bicycle': 'use_sidepath', 'sidewalk': 'separate',
                'ref': 'S 179', 'highway': 'secondary',
                'turn:lanes': 'through|through',
            }),
            dsl.relation(1, {
                'ref': 'S 179', 'route': 'road',
                'source': 'openstreetmap.org', 'type': 'route',
            }, ways=[3358875]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3358875,
                'shield_text': 'S179', 'network': 'DE:STS',
            })

    def test_de_bs_double(self):
        import dsl

        z, x, y = (16, 35115, 21991)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/3237220
            dsl.way(3237220, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '50', 'lanes': '2', 'name': u'Neefestra\xdfe',
                'turn:lanes': 'through|through;right', 'surface': 'asphalt',
                'source': 'openstreetmap.org', 'hazmat': 'designated',
                'oneway': 'yes', 'bicycle': 'no', 'ref': 'B 173;B 169',
                'highway': 'primary',
            }),
            dsl.relation(1, {
                'checked': '2014/01/06 Streckenkundler', 'name':
                'B 169 (Sachsen)', 'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org',
                'operator': 'Bundesrepublik Deutschland', 'ref': 'B 169',
            }, ways=[3237220]),
            dsl.relation(2, {
                'name': 'B 173', 'ref': 'B 173', 'route': 'road',
                'wikipedia': u'de:Bundesstra\xdfe 173',
                'source': 'openstreetmap.org', 'wikidata': 'Q52784',
                'operator': 'Bundesrepublik Deutschland', 'type': 'route',
            }, ways=[3237220]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3237220,
                'shield_text': 'B169', 'network': 'DE:BS',
                'all_networks': ['DE:BS', 'DE:BS'],
                'all_shield_texts': ['B169', 'B173'],
            })

    def test_de_bs_a(self):
        import dsl

        z, x, y = (16, 34437, 22569)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/13235013
            dsl.way(13235013, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '50', 'placement': 'right_of:2',
                'name': u'Roteb\xfchlstra\xdfe', 'surface': 'asphalt',
                'source': 'openstreetmap.org', 'oneway': 'yes', 'lanes': '4',
                'sidewalk': 'none', 'ref': 'B 27a', 'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 13235013,
                'shield_text': 'B27a', 'network': 'DE:BS',
            })

    def test_de_ring(self):
        import dsl

        z, x, y = (16, 34578, 21177)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/4644427
            dsl.way(4644427, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '50', 'lanes': '2', 'name': 'Holstenplatz',
                'source': 'openstreetmap.org', 'maxheight': 'none',
                'cycleway:right': 'track', 'surface': 'asphalt',
                'oneway': 'yes', 'sidewalk': 'right', 'ref': 'Ring 2',
                'highway': 'secondary',
            }),
            dsl.relation(1, {
                'name': 'Ring 2', 'ref': 'Ring 2', 'route': 'road',
                'wikipedia': 'de:Ring 2 (Hamburg)',
                'source': 'openstreetmap.org', 'wikidata': 'Q20731702',
                'type': 'route',
            }, ways=[4644427]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4644427,
                'shield_text': 'Ring 2', 'network': 'DE:Hamburg:Ring'})

    def test_de_bs_ring_order(self):
        import dsl

        z, x, y = (16, 34583, 21151)

        self.generate_fixtures(
            dsl.is_in('DE', z, x, y),
            # https://www.openstreetmap.org/way/4329503
            dsl.way(4329503, dsl.tile_diagonal(z, x, y), {
                'toll:N3': 'yes', 'maxspeed': '60', 'lanes': '2',
                'name': 'Krohnstieg', 'surface': 'asphalt', 'lit': 'yes',
                'source': 'openstreetmap.org', 'oneway': 'yes', 'foot': 'no',
                'bicycle': 'no', 'ref': 'Ring 3;B 433', 'highway': 'trunk',
            }),
            dsl.relation(1, {
                'source': 'openstreetmap.org', 'route': 'road',
                'type': 'route', 'name': 'Ring 3',
            }, ways=[4329503]),
            dsl.relation(3, {
                'name': 'B433', 'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org', 'ref': 'B 433',
            }, ways=[4329503]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4329503,
                'shield_text': 'B433', 'network': 'DE:BS',
                'all_shield_texts': ['B433', 'Ring 3'],
                'all_networks': ['DE:BS', 'DE:Hamburg:Ring'],
            })
