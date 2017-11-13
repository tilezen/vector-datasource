from . import FixtureTest


class GardenPois(FixtureTest):
    def test_garden_with_area(self):
        # update gardens in pois
        # garden with area in pois
        self.load_fixtures(['https://www.openstreetmap.org/way/120480164'])

        self.assert_has_feature(
            13, 1309, 3166, 'pois',
            {'id': 120480164, 'kind': 'garden'})

        # garden with area in landuse
        self.assert_has_feature(
            13, 1309, 3166, 'landuse',
            {'id': 120480164, 'kind': 'garden'})

    def test_garden_point(self):
        # garden without area in pois
        self.load_fixtures(['https://www.openstreetmap.org/node/2969748431'])

        self.assert_has_feature(
            16, 10473, 25332, 'pois',
            {'id': 2969748431, 'kind': 'garden'})
