from . import OsmFixtureTest


class RemoveOsmNeighbourhoods(OsmFixtureTest):
    def test_no_borough(self):
        # Node: Mount Pocono (158473043)
        self.load_fixtures(['http://www.openstreetmap.org/node/158473043'])

        self.assert_no_matching_feature(
            16, 19048, 24541, 'places',
            {'kind': 'borough', 'source': 'openstreetmap.org'})

    def test_no_suburb(self):
        # Node: Centerville District (150939391)
        self.load_fixtures(['http://www.openstreetmap.org/node/150939391'])

        self.assert_no_matching_feature(
            16, 10558, 25381, 'places',
            {'kind': 'suburb', 'source': 'openstreetmap.org'})

    def test_no_quarter(self):
        # Node: Northeast (2790349074)
        self.load_fixtures(['http://www.openstreetmap.org/node/2790349074'])

        self.assert_no_matching_feature(
            16, 18754, 25065, 'places',
            {'kind': 'quarter', 'source': 'openstreetmap.org'})
