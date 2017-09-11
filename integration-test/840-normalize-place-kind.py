from . import OsmFixtureTest


class NormalizePlaceKind(OsmFixtureTest):
    def test_state(self):
        # Node: California (671022)
        self.load_fixtures(['http://www.openstreetmap.org/node/671022'])

        self.assert_has_feature(
            16, 11149, 25576, 'places',
            {'id': 671022, 'kind': 'region', 'kind_detail': 'state'})

    def test_province(self):
        # Node: Saga Prefecture (1499608655)
        self.load_fixtures(['http://www.openstreetmap.org/node/1499608655'])

        self.assert_has_feature(
            16, 56457, 26350, 'places',
            {'id': 1499608655, 'kind': 'region', 'kind_detail': 'province'})

    def test_city(self):
        # Node: San Francisco (26819236)
        self.load_fixtures(['http://www.openstreetmap.org/node/26819236'])

        self.assert_has_feature(
            16, 10482, 25330, 'places',
            {'id': 26819236, 'kind': 'locality', 'kind_detail': 'city'})

    def test_town(self):
        # Node: Daly City (140983265)
        self.load_fixtures(['http://www.openstreetmap.org/node/140983265'])

        self.assert_has_feature(
            16, 10474, 25346, 'places',
            {'id': 140983265, 'kind': 'locality', 'kind_detail': 'town'})

    def test_village(self):
        # Node: Broadmoor (140983130)
        self.load_fixtures(['http://www.openstreetmap.org/node/140983130'])

        self.assert_has_feature(
            16, 10470, 25350, 'places',
            {'id': 140983130, 'kind': 'locality', 'kind_detail': 'village'})

    def test_hamlet(self):
        # Node: Baden (150937258)
        self.load_fixtures(['http://www.openstreetmap.org/node/150937258'])

        self.assert_has_feature(
            16, 10479, 25359, 'places',
            {'id': 150937258, 'kind': 'locality', 'kind_detail': 'hamlet'})

    def test_locality(self):
        # Node: McCovey Cove (317091394)
        self.load_fixtures(['http://www.openstreetmap.org/node/317091394'])

        self.assert_has_feature(
            16, 10487, 25330, 'places',
            {'id': 317091394, 'kind': 'locality', 'kind_detail': 'locality'})

    def test_isolated_dwelling(self):
        # Node: Gilman Ranch (2682626694)
        self.load_fixtures(['http://www.openstreetmap.org/node/2682626694'])

        self.assert_has_feature(
            16, 10592, 25477, 'places',
            {'id': 2682626694, 'kind': 'locality',
             'kind_detail': 'isolated_dwelling'})

    def test_farm(self):
        # Node: Stevens Canyon Ranch (3219761323)
        self.load_fixtures(['http://www.openstreetmap.org/node/3219761323'])

        self.assert_has_feature(
            16, 10539, 25446, 'places',
            {'id': 3219761323, 'kind': 'locality', 'kind_detail': 'farm'})


class NormalizePlaceKindNaturalEarth(OsmFixtureTest):

    def setUp(self):
        super(NormalizePlaceKindNaturalEarth, self).setUp()
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_populated_places/840-normalize-place-kind.shp',
        ])

    def test_historic_place(self):
        # ne historic place
        self.assert_has_feature(
            16, 38247, 21826, 'places',
            {'id': int, 'name': 'Chernobyl',
             'kind': 'locality', 'kind_detail': 'hamlet'})

    def test_scientific_station(self):
        # ne scientific station
        self.assert_has_feature(
            16, 22209, 47255, 'places',
            {'id': int, 'name': 'Elephant Island',
             'kind': 'locality', 'kind_detail': 'scientific_station'})

    def test_country_capital(self):
        # ne capitals
        self.assert_has_feature(
            7, 109, 49, 'places',
            {'id': int, 'name': 'Seoul',
             'kind': 'locality', 'country_capital': True})

        self.assert_has_feature(
            7, 112, 50, 'places',
            {'id': int, 'name': 'Kyoto',
             'kind': 'locality', 'country_capital': True})

        self.assert_has_feature(
            7, 104, 55, 'places',
            {'id': int, 'name': 'Hong Kong',
             'kind': 'locality', 'country_capital': True})

    def test_region_capital(self):
        # ne state_capitals
        self.assert_has_feature(
            7, 117, 76, 'places',
            {'id': int, 'name': 'Sydney',
             'kind': 'locality', 'region_capital': True})

        self.assert_has_feature(
            7, 112, 50, 'places',
            {'id': int, 'name': 'Osaka',
             'kind': 'locality', 'region_capital': True})

    def test_populated_place_not_capital(self):
        # ne populated place
        self.assert_has_feature(
            7, 20, 49, 'places',
            {'id': int, 'name': 'San Francisco',
             'kind': 'locality', 'region_capital': type(None),
             'country_capital': type(None)})
