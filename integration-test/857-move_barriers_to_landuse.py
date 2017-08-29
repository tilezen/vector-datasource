from . import OsmFixtureTest


# update landuse to include barriers features and delete from boundaries
class MoveBarriersToLanduse(OsmFixtureTest):

    def test_city_wall(self):
        # city_wall in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/81522922'])

        self.assert_has_feature(
            12, 2030, 1300, 'landuse',
            {'kind': 'city_wall'})

        # city_wall not in boundaries
        self.assert_no_matching_feature(
            12, 2030, 1300, 'boundaries',
            {'kind': 'city_wall'})

    def test_citywalls(self):
        # citywalls in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/392978585'])

        self.assert_has_feature(
            12, 2326, 1617, 'landuse',
            {'kind': 'city_wall'})

        # citywalls not in boundaries
        self.assert_no_matching_feature(
            12, 2326, 1617, 'boundaries',
            {'kind': 'city_wall'})

    def test_dam(self):
        # dam in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/109629543'])

        self.assert_has_feature(
            12, 740, 1606, 'landuse',
            {'kind': 'dam'})

        # dam not in boundaries
        self.assert_no_matching_feature(
            12, 740, 1606, 'boundaries',
            {'kind': 'dam'})

    def test_fence(self):
        # fence in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/345599214'])

        self.assert_has_feature(
            16, 19296, 24635, 'landuse',
            {'kind': 'fence'})

        # fence not in boundaries
        self.assert_no_matching_feature(
            16, 19296, 24635, 'boundaries',
            {'kind': 'fence'})

    def test_retaining_wall(self):
        # retaining_wall in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/288896098'])

        self.assert_has_feature(
            15, 9648, 12315, 'landuse',
            {'kind': 'retaining_wall'})

        # retaining_wall not in boundaries
        self.assert_no_matching_feature(
            15, 9648, 12315, 'boundaries',
            {'kind': 'retaining_wall'})

    def test_snow_fence(self):
        # snow_fence in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/356771680'])

        self.assert_has_feature(
            15, 6788, 12264, 'landuse',
            {'kind': 'snow_fence'})

        # snow_fence not in boundaries
        self.assert_no_matching_feature(
            15, 6788, 12264, 'boundaries',
            {'kind': 'snow_fence'})
