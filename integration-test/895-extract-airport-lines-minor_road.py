from . import OsmFixtureTest


class ExtractAirportLinesMinorRoad(OsmFixtureTest):
    def test_runway(self):
        # Way: 10L/28R (22567191)
        self.load_fixtures(['http://www.openstreetmap.org/way/22567191'])

        self.assert_has_feature(
            16, 10490, 25366, 'roads',
            {'id': 22567191, 'kind': 'aeroway', 'kind_detail': 'runway'})

    def test_taxiway(self):
        # Way: Q (23718500)
        self.load_fixtures(['http://www.openstreetmap.org/way/23718500'])

        self.assert_has_feature(
            16, 10488, 25365, 'roads',
            {'id': 23718500, 'kind': 'aeroway', 'kind_detail': 'taxiway'})
