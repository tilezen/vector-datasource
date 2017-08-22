from . import OsmFixtureTest


class IceCreamShops(OsmFixtureTest):
    def test_amenity_ice_cream(self):
        # New York, NY (amenity=ice_cream)
        self.load_fixtures(['https://www.openstreetmap.org/node/2782000317'])

        self.assert_has_feature(
            16, 19299, 24629, 'pois',
            {'kind': 'ice_cream'})

    def test_shop_ice_cream(self):
        # Oakland, CA (shop=ice_cream)
        self.load_fixtures(['https://www.openstreetmap.org/node/661742947'])

        self.assert_has_feature(
            16, 10512, 25314, 'pois',
            {'kind': 'ice_cream'})
