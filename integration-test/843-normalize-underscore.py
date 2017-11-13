from . import FixtureTest


class NormalizeUnderscore(FixtureTest):
    def test_drive_through(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/219071307'])

        self.assert_has_feature(
            16, 10478, 25338, 'roads',
            {'id': 219071307, 'kind': 'minor_road',
             'service': 'drive_through'})

    def test_ski_lift_t_bar(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/258020271'])

        self.assert_has_feature(
            16, 11077, 25458, 'roads',
            {'id': 258020271, 'kind': 'aerialway', 'kind_detail': 't_bar'})

    def test_ski_lift_j_bar(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/256717307'])

        self.assert_has_feature(
            16, 18763, 24784, 'roads',
            {'id': 256717307, 'kind': 'aerialway', 'kind_detail': 'j_bar'})

    def test_aerialway_no_detail(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/232074914'])

        self.assert_has_feature(
            16, 13304, 24998, 'roads',
            {'id': 232074914, 'kind': 'aerialway', 'kind_detail': type(None)})
