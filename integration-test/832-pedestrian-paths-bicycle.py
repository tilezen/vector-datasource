from . import OsmFixtureTest


class PedestrianPathsBicycle(OsmFixtureTest):
    def test_path(self):
        # Add footway properties to pedestrian paths and piers
        # Pedestrian path
        self.load_fixtures(['http://www.openstreetmap.org/way/8919991'])

        self.assert_has_feature(
            13, 1309, 3165, 'roads',
            {'id': 8919991, 'kind': 'path', 'is_bicycle_related': True,
             'bicycle': 'designated'})

    def test_pier(self):
        # Pier
        self.load_fixtures(['http://www.openstreetmap.org/way/133920164'])

        self.assert_has_feature(
            13, 1304, 2933, 'roads',
            {'id': 133920164, 'kind': 'path', 'is_bicycle_related': True,
             'bicycle': 'yes'})
