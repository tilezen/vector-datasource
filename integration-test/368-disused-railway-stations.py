from . import OsmFixtureTest


class DisusedRailwayStations(OsmFixtureTest):

    def test_old_south_ferry(self):
        # Old South Ferry (1) (disused=yes)
        self.load_fixtures(
            ['https://www.openstreetmap.org/node/2086974744'])

        self.assert_no_matching_feature(
            16, 19294, 24643, 'pois',
            {'kind': 'station', 'id': 2086974744})

    def test_valle_az(self):
        # Valle, AZ (disused=station)
        self.load_fixtures(
            ['https://www.openstreetmap.org/node/366220389'])

        self.assert_no_matching_feature(
            16, 12342, 25813, 'pois',
            {'id': 366220389})
