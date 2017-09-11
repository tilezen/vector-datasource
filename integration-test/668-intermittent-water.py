from . import OsmFixtureTest


class IntermittentWater(OsmFixtureTest):
    def test_river(self):
        # Arizona Canal Diversion Channel (ACDC)
        self.load_fixtures(['http://www.openstreetmap.org/way/107817218'])

        self.assert_has_feature(
            16, 12353, 26272, 'water',
            {'kind': 'river', 'intermittent': True})

    def test_drain(self):
        # 10th Street Wash
        self.load_fixtures(['http://www.openstreetmap.org/way/96528126'])

        self.assert_has_feature(
            16, 12368, 26272, 'water',
            {'kind': 'drain', 'intermittent': True})

    def test_unnamed_drain(self):
        # Unnamed drain
        self.load_fixtures(['http://www.openstreetmap.org/way/61954975'])

        self.assert_has_feature(
            16, 12372, 26272, 'water',
            {'kind': 'drain', 'intermittent': True})

    def test_unnamed_stream(self):
        # Unnamed stream
        self.load_fixtures(['http://www.openstreetmap.org/way/321690441'])

        self.assert_has_feature(
            16, 12492, 26279, 'water',
            {'kind': 'stream', 'intermittent': True})

    def test_unnamed_water(self):
        # Unnamed water (lake)
        self.load_fixtures(['http://www.openstreetmap.org/way/68709904'])

        self.assert_has_feature(
            16, 12349, 26257, 'water',
            {'kind': 'water', 'intermittent': True})
