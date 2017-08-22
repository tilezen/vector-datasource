from . import OsmFixtureTest


class CategorizeTrains(OsmFixtureTest):
    def test_long_distance(self):
        self.load_fixtures(['https://www.openstreetmap.org/relation/2812900'])

        self.assert_has_feature(
            5, 5, 12, 'transit',
            {'kind': 'train', 'service': 'long_distance'})

    def test_high_speed(self):
        self.load_fixtures(['https://www.openstreetmap.org/relation/4460896'])

        self.assert_has_feature(
            5, 9, 12, 'transit',
            {'kind': 'train', 'service': 'high_speed'})

    def test_international(self):
        self.load_fixtures(['https://www.openstreetmap.org/relation/4467189'])

        self.assert_has_feature(
            5, 9, 12, 'transit',
            {'kind': 'train', 'service': 'international'})
