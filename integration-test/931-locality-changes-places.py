from . import OsmFixtureTest


class LocalityChangesPlacesNe(OsmFixtureTest):

    def setUp(self):
        super(LocalityChangesPlacesNe, self).setUp()
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_populated_places/931-normalize-place-kind.shp',
        ])

    def test_admin0_capital(self):
        # ne Admin-0 capital
        self.assert_has_feature(
            3, 6, 3, 'places',
            {'kind': 'locality', 'name': 'Seoul', 'country_capital': True})

        self.assert_no_matching_feature(
            3, 6, 3, 'places',
            {'kind': 'city', 'name': 'Seoul', 'country_capital': True})

    def test_admin1_capital(self):
        # ne Admin-1 capital
        self.assert_has_feature(
            3, 7, 4, 'places',
            {'kind': 'locality', 'name': 'Sydney', 'region_capital': True})

        self.assert_no_matching_feature(
            3, 7, 4, 'places',
            {'kind': 'city', 'name': 'Sydney', 'state_capital': True})

    def test_populated_place(self):
        # ne Populated place
        self.assert_has_feature(
            3, 1, 3, 'places',
            {'kind': 'locality', 'name': 'San Francisco'})

        self.assert_no_matching_feature(
            3, 1, 3, 'places',
            {'kind': 'city', 'name': 'San Francisco'})

    def test_scientific_station(self):
        # ne Scientific station
        self.assert_has_feature(
            9, 164, 377, 'places',
            {'kind': 'locality', 'name': 'Palmer Station',
             'kind_detail': 'scientific_station'})


class LocalityChangesPlacesOsm(OsmFixtureTest):
    def test_no_region_capital_false(self):
        # Washington (158368533)
        # no region_capital false
        self.load_fixtures(['http://www.openstreetmap.org/node/158368533'])

        self.assert_has_feature(
            8, 73, 97, 'places',
            {'id': 158368533, 'region_capital': type(None)})

    def test_no_country_capital_false(self):
        # Node: Deerfield, Nova Scotia (3441540432)
        # no country_capital when falsey
        self.load_fixtures(['http://www.openstreetmap.org/node/3441540432'])

        self.assert_has_feature(
            16, 20752, 23846, 'places',
            {'id': 3441540432, 'country_capital': type(None)})
