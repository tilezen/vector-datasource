from . import OsmFixtureTest


class NormalizeOperatorValues(OsmFixtureTest):
    def test_us_national_park_service(self):
        # Standardize operator values
        # US National Park Service in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/4285104560'])

        self.assert_has_feature(
            16, 15808, 25720, 'pois',
            {'id': 4285104560,
             'operator': 'United States National Park Service'})

        self.assert_no_matching_feature(
            16, 15808, 25720, 'pois',
            {'id': 4285104560, 'operator': 'US National Park Service'})

    def test_national_park_service(self):
        # National Park Service in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/368766687'])

        self.assert_has_feature(
            16, 13163, 25153, 'landuse',
            {'id': 368766687,
             'operator': 'United States National Park Service'})

        self.assert_no_matching_feature(
            16, 13163, 25153, 'landuse',
            {'id': 368766687, 'operator': 'National Park Service'})

    def test_us_national_forest_service(self):
        # US National Forest Service in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/796692690'])

        self.assert_has_feature(
            16, 10542, 23271, 'pois',
            {'id': 796692690, 'operator': 'United States Forest Service'})

        self.assert_no_matching_feature(
            16, 10542, 23271, 'pois',
            {'id': 796692690, 'operator': 'US National Forest Service'})

    def test_us_forest_service(self):
        # US Forest Service in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/432302983'])

        self.assert_has_feature(
            16, 11252, 25432, 'landuse',
            {'id': 432302983, 'operator': 'United States Forest Service'})

        self.assert_no_matching_feature(
            16, 11252, 25432, 'landuse',
            {'id': 432302983, 'operator': 'US Forest Service'})

    def test_nsw_parks_and_wildlife_service(self):
        # NSW Parks and Wildlife Service in POIs
        self.load_fixtures(['http://www.openstreetmap.org/node/2514034066'])

        self.assert_has_feature(
            16, 59800, 39773, 'pois',
            {'id': 2514034066,
             'operator': 'National Parks & Wildife Service NSW'})

        self.assert_no_matching_feature(
            16, 59800, 39773, 'pois',
            {'id': 2514034066, 'operator': 'NSW Parks and Wildlife Service'})

    def test_department_of_national_parks_nsw(self):
        # Department of National Parks NSW in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/429280600'])

        self.assert_has_feature(
            16, 60128, 39504, 'landuse',
            {'id': 429280600,
             'operator': 'National Parks & Wildife Service NSW'})

        self.assert_no_matching_feature(
            16, 60128, 39504, 'landuse',
            {'id': 429280600, 'operator': 'Department of National Parks NSW'})
