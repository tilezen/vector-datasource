from . import OsmFixtureTest


class BarrierTollBooth(OsmFixtureTest):
    def test_01(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/52529616'])

        self.assert_has_feature(
            16, 10501, 25319, 'pois',
            {'id': 52529616, 'kind': 'toll_booth'})

    def test_02(self):
        # Node: Main Gate (392430963)
        self.load_fixtures(['http://www.openstreetmap.org/node/392430963'])

        self.assert_has_feature(
            16, 10473, 25332, 'pois',
            {'id': 392430963, 'kind': 'toll_booth'})
