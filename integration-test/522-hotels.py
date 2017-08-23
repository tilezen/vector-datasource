from . import OsmFixtureTest


class Hotels(OsmFixtureTest):
    def test_ritz_carlton(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/32947245'])

        self.assert_has_feature(
            15, 5242, 12663, 'pois',
            {'kind': 'hotel', 'name': 'Ritz-Carlton'})

    def test_zephyr(self):
        self.load_fixtures(['http://www.openstreetmap.org/relation/1358120'])

        self.assert_has_feature(
            16, 10483, 25323, 'pois',
            {'kind': 'hotel', 'name': 'Hotel Zephyr'})
