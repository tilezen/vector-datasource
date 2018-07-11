from . import FixtureTest


class CategorizeTrains(FixtureTest):
    def test_long_distance(self):
        import dsl

        z, x, y = 5, 5, 11
        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/2812900
            dsl.way(2812900, dsl.tile_diagonal(z, x, y), {
                "FIXME": "Underlying infrastructure \"Seattle Subdivision\"" \
                "needs some fixing",
                "colour": "#191970",
                "from": "Los Angeles",
                "name": "Coast Starlight",
                "network": "Amtrak",
                "operator": "Amtrak",
                "public_transport:version": "1",
                "ref": "11-14",
                "route": "train",
                "service": "long_distance",
                "to": "Seattle",
                "type": "route",
                "via": "Portland"
            }),
        )

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
