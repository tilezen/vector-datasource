from . import OsmFixtureTest


class StandardizeWaterKinds(OsmFixtureTest):
    # TODO: reinstate this test when NE fixture loading is implemented
    #def test_great_salt_lake_ne(self):
    #    # ne_10m_lakes gid 1298: Great Salt Lake, UT
    #    self.load_fixtures([])
    #
    #    self.assert_has_feature(
    #        7, 23, 47, 'water',
    #        {'kind': 'lake', 'alkaline': True})

    def test_reservoir(self):
        # Francisco Reservoir, SF
        self.load_fixtures(['https://www.openstreetmap.org/way/386662458'])

        self.assert_has_feature(
            16, 10481, 25324, 'water',
            {'kind': 'lake', 'reservoir': True})
