from . import OsmFixtureTest


class TransitFeatures(OsmFixtureTest):
    def test_bus_stop_way(self):
        # way 91806504
        self.load_fixtures(['https://www.openstreetmap.org/way/91806504'])

        self.assert_has_feature(
            16, 10470, 25316, 'transit',
            {'kind': 'bus_stop'})

    def test_bus_stop_node(self):
        # node 1241518350
        self.load_fixtures(['https://www.openstreetmap.org/node/1241518350'])

        self.assert_has_feature(
            16, 10480, 25332, 'pois',
            {'kind': 'bus_stop'})

    def test_platform(self):
        # way 196670577
        self.load_fixtures(['https://www.openstreetmap.org/way/196670577'])

        self.assert_has_feature(
            16, 10486, 25326, 'transit',
            {'kind': 'platform'})
