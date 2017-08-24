from . import OsmFixtureTest


class Corridor(OsmFixtureTest):
    def test_corridor(self):
        # Way: The Nave (205644309)
        self.load_fixtures(['http://www.openstreetmap.org/way/205644309'])

        self.assert_has_feature(
            16, 10485, 25332, 'roads',
            {'id': 205644309, 'kind': 'path', 'kind_detail': 'corridor'})
