from . import OsmFixtureTest


class CyclewayEqualsNo(OsmFixtureTest):
    def test_centre(self):
        # Way: Grant Avenue (184956229)
        self.load_fixtures(['http://www.openstreetmap.org/way/184956229'])

        self.assert_no_matching_feature(
            16, 10484, 25327, 'roads',
            {'cycleway': 'no'})

    def test_left(self):
        # Way: Wedge Parkway (263563960)
        self.load_fixtures(['http://www.openstreetmap.org/way/263563960'])

        self.assert_no_matching_feature(
            16, 10966, 24952, 'roads',
            {'cycleway_left': 'no'})

        self.assert_has_feature(
            16, 10966, 24952, 'roads',
            {'cycleway_right': 'lane'})

    def test_right(self):
        # Way: Wedge Parkway (263563950)
        self.load_fixtures(['http://www.openstreetmap.org/way/263563950'])

        self.assert_no_matching_feature(
            16, 10965, 24952, 'roads',
            {'cycleway_right': 'no'})

        self.assert_has_feature(
            16, 10965, 24952, 'roads',
            {'cycleway_left': 'lane'})
