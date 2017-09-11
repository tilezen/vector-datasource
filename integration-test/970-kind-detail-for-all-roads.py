from . import FixtureTest


class KindDetailForAllRoads(FixtureTest):
    def test_ferry(self):
        # Alameda <-> SF Ferry bldg
        self.load_fixtures(['http://www.openstreetmap.org/way/98752535'])

        self.assert_has_feature(
            16, 10487, 25326, 'roads',
            {'kind': 'ferry', 'id': 98752535})

        # SF Pier 41 <-> SF Ferry bldg
        self.load_fixtures(['http://www.openstreetmap.org/way/98752545'])

        self.assert_has_feature(
            16, 10487, 25326, 'roads',
            {'kind': 'ferry', 'id': 98752545})

        # South SF <-> SF Ferry bldg
        self.load_fixtures(['http://www.openstreetmap.org/way/289694213'])

        self.assert_has_feature(
            16, 10487, 25326, 'roads',
            {'kind': 'ferry', 'id': 289694213})
