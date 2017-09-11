from . import OsmFixtureTest


class AddBoatRental(OsmFixtureTest):
    def test_shop_boat_rental(self):
        # shop=boat_rental
        self.load_fixtures(['https://www.openstreetmap.org/node/1306277961'])

        self.assert_has_feature(
            16, 18316, 23921, 'pois',
            {'kind': 'boat_rental'})

    def test_amenity_boat_rental(self):
        # amenity=boat_rental
        self.load_fixtures(['https://www.openstreetmap.org/node/4362555638'])

        self.assert_has_feature(
            16, 10978, 26089, 'pois',
            {'kind': 'boat_rental'})

    def test_shop_boat_rental_yes(self):
        # shop=boat, rental=yes
        self.load_fixtures(['https://www.openstreetmap.org/node/3466463119'])

        self.assert_has_feature(
            16, 19458, 24522, 'pois',
            {'kind': 'boat_rental'})

    def test_rental_boat(self):
        # rental=boat
        self.load_fixtures(['https://www.openstreetmap.org/node/2425308146'])

        self.assert_has_feature(
            16, 33611, 23091, 'pois',
            {'kind': 'boat_rental'})
