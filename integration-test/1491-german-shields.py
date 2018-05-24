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
