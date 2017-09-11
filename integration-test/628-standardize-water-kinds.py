from . import FixtureTest


class StandardizeWaterKinds(FixtureTest):
    def test_great_salt_lake_ne(self):
        # ne_10m_lakes gid 1298: Great Salt Lake, UT
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_lakes/628-standardize-water-kinds.shp',
        ])

        self.assert_has_feature(
            7, 23, 47, 'water',
            {'kind': 'lake', 'alkaline': True})

    def test_reservoir(self):
        # Francisco Reservoir, SF
        self.load_fixtures(['https://www.openstreetmap.org/way/386662458'])

        self.assert_has_feature(
            16, 10481, 25324, 'water',
            {'kind': 'lake', 'reservoir': True})
