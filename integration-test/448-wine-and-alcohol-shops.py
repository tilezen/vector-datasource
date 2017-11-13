from . import FixtureTest


class WineAndAlcoholShops(FixtureTest):

    def test_shop_wine(self):
        # Wine, New York, NY (shop=wine)
        self.load_fixtures(['https://www.openstreetmap.org/node/2549960970'])

        self.assert_has_feature(
            16, 19298, 24632, 'pois',
            {'kind': 'wine'})

    def test_shop_alcohol(self):
        # Noe Valley Wine Merchants, San Francisco, CA
        self.load_fixtures(['https://www.openstreetmap.org/node/1713269631'])

        self.assert_has_feature(
            16, 10480, 25336, 'pois',
            {'kind': 'alcohol'})
