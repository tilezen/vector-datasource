from . import FixtureTest


class RemoveUnstyledNePlaces(FixtureTest):

    def setUp(self):
        super(RemoveUnstyledNePlaces, self).setUp()
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_populated_places/981-remove-unstyled-ne-places.shp',
        ])

    def assert_add_place(self, z, x, y, name):
        self.assert_has_feature(
            z, x, y, 'places',
            {'kind': 'locality', 'name': name,
             'source': 'naturalearthdata.com',
             'min_zoom': z})
        self.assert_no_matching_feature(
            z-1, x/2, y/2, 'places',
            {'kind': 'locality', 'name': name,
             'source': 'naturalearthdata.com'})

    def assert_remove_place(self, z, x, y, name):
        self.assert_no_matching_feature(
            z, x, y, 'places',
            {'kind': 'locality', 'name': name,
             'source': 'naturalearthdata.com'})
        self.assert_has_feature(
            z-1, x/2, y/2, 'places',
            {'kind': 'locality', 'name': name,
             'source': 'naturalearthdata.com'})

    def test_z2_add_nyc(self):
        # z2: Add New York City
        self.assert_add_place(2, 1, 1, 'New York')

    def test_z3_add_sf(self):
        # z3: Add San Francisco
        self.assert_add_place(3, 1, 3, 'San Francisco')

    def test_z4_add_seattle(self):
        # z4: Add Seattle
        self.assert_add_place(4, 2, 5, 'Seattle')

    def test_z5_add_eureka(self):
        # z5: Add Eureka, California
        self.assert_add_place(5, 4, 12, 'Eureka')

    def test_z6_add_medford(self):
        # z6: Add Medford, Oregon
        self.assert_add_place(6, 10, 23, 'Medford')

    def test_z7_add_arcata(self):
        # z7: Add Arcata, California
        self.assert_add_place(7, 19, 48, 'Arcata')
        self.assert_add_place(7, 20, 48, 'Ukiah')

    def test_z8_remove_nyc(self):
        # z8: Remainder Ukiah, California
        self.assert_remove_place(8, 75, 96, 'New York')
        self.assert_remove_place(8, 40, 94, 'Medford')

    def test_z9_add_mendocino(self):
        # z9: Remainder Mendocino, California
        self.assert_add_place(9, 79, 195, 'Mendocino')

    def test_z10_add_harnosand(self):
        # z10: Remainder Harnosand, Sweden (62.6339970391, 17.9340036175)
        self.assert_add_place(10, 563, 281, 'Harnosand')
        self.assert_remove_place(10, 159, 384, 'Arcata')
        self.assert_remove_place(10, 161, 390, 'Ukiah')

    def test_z11_mendocino_exists(self):
        # z11 Mendocino should still be here
        self.assert_has_feature(
            9, 79, 195, 'places',
            {'kind': 'locality', 'name': 'Mendocino',
             'source': 'naturalearthdata.com'})
