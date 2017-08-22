from . import OsmFixtureTest


class IncludeStatePois(OsmFixtureTest):
    def test_proposed_stations(self):
        # Antioch Station
        self.load_fixtures(['https://www.openstreetmap.org/node/3353451464'])

        self.assert_has_feature(
            16, 10597, 25279, 'pois',
            {'id': 3353451464, 'state': 'proposed'})

        # Pittsburg Center
        self.load_fixtures(['https://www.openstreetmap.org/node/3354463416'])

        self.assert_has_feature(
            16, 10578, 25275, 'pois',
            {'id': 3354463416, 'state': 'proposed'})
