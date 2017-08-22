from . import OsmFixtureTest


class SwimmingPools(OsmFixtureTest):

    def test_amenity_swimming_pool(self):
        # Bayonne Municipal Pool, amenity=swimming_pool
        self.load_fixtures(['https://www.openstreetmap.org/way/361100118'])

        self.assert_has_feature(
            16, 19273, 24652, 'water',
            {'kind': 'swimming_pool'})

    def test_leisure_swimming_pool(self):
        # McCarren Park Swimming Pool, leisure=swimming_pool
        self.load_fixtures(['https://www.openstreetmap.org/way/118987681'])

        self.assert_has_feature(
            16, 19305, 24638, 'water',
            {'kind': 'swimming_pool'})
