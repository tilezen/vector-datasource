from . import FixtureTest


class OutdoorShops(FixtureTest):
    def test_fishing(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/3056897308'])

        self.assert_has_feature(
            16, 11111, 25360, 'pois',
            {'kind': 'fishing', 'min_zoom': 16})

    def test_hunting(self):
        # http://www.openstreetmap.org/node/1467729495
        self.load_fixtures(['http://www.openstreetmap.org/node/1467729495'])

        self.assert_has_feature(
            16, 10165, 24618, 'pois',
            {'kind': 'hunting', 'min_zoom': 16})

    def test_outdoor(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/766201791'])

        self.assert_has_feature(
            16, 10179, 24602, 'pois',
            {'kind': 'outdoor', 'min_zoom': 16})

    def test_small_outdoor(self):
        # Smaller Sports Basement store in SF
        # This should really be in 16, 10483, 25332, but is in zoom 15 now
        self.load_fixtures(['http://www.openstreetmap.org/way/35343322'])

        self.assert_has_feature(
            15, 5241, 12666, 'pois',
            {'kind': 'outdoor', 'id': 35343322})

    def test_large_outdoor(self):
        # http://www.openstreetmap.org/way/377630800
        # Large Bass Pro building that should appear earlier
        self.load_fixtures(['http://www.openstreetmap.org/way/377630800'])

        self.assert_has_feature(
            15, 6842, 12520, 'pois',
            {'kind': 'outdoor', 'id': 377630800})

        # Large REI building that should appear earlier
        self.load_fixtures(['http://www.openstreetmap.org/way/290195878'])

        self.assert_has_feature(
            15, 6207, 12321, 'pois',
            {'kind': 'outdoor', 'id': 290195878})

    def test_scuba_diving(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/3931687122'])

        self.assert_has_feature(
            16, 10467, 25309, 'pois',
            {'kind': 'scuba_diving', 'min_zoom': 17})

    def test_gas_canister(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2135237099'])

        self.assert_has_feature(
            16, 10558, 25443, 'pois',
            {'kind': 'gas_canister', 'min_zoom': 18})

    def test_motorcycle(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3799971066'])

        self.assert_has_feature(
            16, 10483, 25331, 'pois',
            {'kind': 'motorcycle', 'min_zoom': 17})
