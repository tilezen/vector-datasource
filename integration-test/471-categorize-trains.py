from . import OsmFixtureTest


class CategorizeTrains(OsmFixtureTest):
    def test_long_distance(self):
        self.load_fixtures(
            ['https://www.openstreetmap.org/relation/2812900'],
            clip=self.tile_bbox(14, 2624, 5722))

        self.assert_has_feature(
            5, 5, 11, 'transit',
            {'kind': 'train', 'service': 'long_distance'})

    def test_high_speed(self):
        self.load_fixtures(
            ['https://www.openstreetmap.org/relation/4460896'],
            clip=self.tile_bbox(13, 2412, 3078))

        self.assert_has_feature(
            5, 9, 12, 'transit',
            {'kind': 'train', 'service': 'high_speed'})

    def test_international(self):
        self.load_fixtures(
            ['https://www.openstreetmap.org/relation/4467189'],
            clip=self.tile_bbox(13, 2412, 3078))

        self.assert_has_feature(
            5, 9, 12, 'transit',
            {'kind': 'train', 'service': 'international'})
