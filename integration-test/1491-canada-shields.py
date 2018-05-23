from . import FixtureTest


class CanadaShieldTest(FixtureTest):
    def test_tch(self):
        import dsl

        z, x, y = (16, 18027, 23200)

        self.generate_fixtures(
            dsl.is_in('CA', z, x, y),
            # https://www.openstreetmap.org/way/348819775
            dsl.way(348819775, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '90', 'lanes': '2', 'name': 'Highway 69',
                'nat_name': 'Trans-Canada Highway', 'surface': 'asphalt',
                'nat_name:en': 'Trans-Canada Highway',
                'source': 'openstreetmap.org',
                'nat_name:fr': 'Route Transcanadienne',
                'NHS': 'yes', 'oneway': 'yes', 'ref': '69',
                'highway': 'trunk',
            }),
            dsl.relation(1, {
                'network': 'CA:ON:primary', 'ref': '69', 'route': 'road',
                'source': 'openstreetmap.org', 'NHS': 'yes', 'type': 'route'
            }, ways=[348819775]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 348819775,
                'shield_text': '69', 'network': 'CA:transcanada',
                'all_shield_texts': ['69', '69'],
                'all_networks': ['CA:transcanada', 'CA:ON:primary'],
            })

    def test_yellowhead(self):
        import dsl

        z, x, y = (16, 11190, 21389)

        self.generate_fixtures(
            dsl.is_in('CA', z, x, y),
            # https://www.openstreetmap.org/way/51442002
            dsl.way(51442002, dsl.tile_diagonal(z, x, y), {
                'name': 'Yellowhead Highway',
                'nat_name': 'Trans-Canada Highway',
                'source': 'openstreetmap.org',
                'attribution': u'GeoBase\xae', 'ref': '16', 'highway': 'trunk',
            }),
            dsl.relation(1, {
                'name': 'Yellowhead Highway (BC)', 'type': 'route',
                'route': 'road', 'wikipedia': 'en:British Columbia Highway 16',
                'source': 'openstreetmap.org', 'wikidata': 'Q129818',
                'ref': '16', 'network': 'CA:yellowhead'
            }, ways=[51442002]),
            # NOTE: this relation doesn't really exist. i only added it to test
            # the sorting!
            dsl.relation(2, {
                'name': 'Fake highway', 'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org', 'ref': '0',
                'network': 'CA:BC:something',
            }, ways=[51442002]),
        )

        # transcanada should sort before yellowhead, and yellowhead before
        # state networks.
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 51442002,
                'shield_text': '16', 'network': 'CA:transcanada',
                'all_networks': ['CA:transcanada', 'CA:yellowhead',
                                 'CA:BC:something'],
                'all_shield_texts': ['16', '16', '0'],
            })

    def test_nb2(self):
        import dsl

        z, x, y = (16, 20618, 23240)

        self.generate_fixtures(
            dsl.is_in('CA', z, x, y),
            # https://www.openstreetmap.org/way/151157327
            dsl.way(151157327, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': 'Graveyard Hill Road',
                'surface': 'paved', 'source': 'openstreetmap.org',
                'ref': '107', 'highway': 'primary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '107',
                'network': 'CA:NB', 'source': 'openstreetmap.org'
            }, ways=[151157327]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 151157327, 'shield_text': '107', 'network': 'CA:NB2'})

    def test_nb3(self):
        import dsl

        z, x, y = (16, 20613, 23243)

        self.generate_fixtures(
            dsl.is_in('CA', z, x, y),
            # https://www.openstreetmap.org/way/151109081
            dsl.way(151109081, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': 'Limekiln Road', 'surface': 'paved',
                'source': 'openstreetmap.org', 'ref': '620',
                'highway': 'secondary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '620',
                'network': 'CA:NB', 'source': 'openstreetmap.org',
            }, ways=[151109081]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 151109081, 'shield_text': '620', 'network': 'CA:NB3'})
