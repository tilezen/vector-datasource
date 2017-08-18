from . import OsmFixtureTest


class BicycleYesDesignatedRoads(OsmFixtureTest):

    def test_bicycle_yes(self):
        # Add bicycle properties to roads
        # Road with bicycle=yes in Washington, DC
        self.load_fixtures(['http://www.openstreetmap.org/way/281677984'])

        self.assert_has_feature(
            16, 18758, 25078, 'roads',
            {'id': 281677984, 'kind': 'major_road',
             'is_bicycle_related': True, 'bicycle': 'yes'})

    def test_bicycle_designated(self):
        # Road with bicycle=designated in Eureka, California
        self.load_fixtures(['http://www.openstreetmap.org/way/10273013'])

        self.assert_has_feature(
            16, 10163, 24621, 'roads',
            {'id': 10273013, 'kind': 'major_road',
             'is_bicycle_related': True, 'bicycle': 'designated'})
