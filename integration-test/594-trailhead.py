from . import OsmFixtureTest


class Trailhead(OsmFixtureTest):
    def test_trailhead(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3447700493'])

        self.assert_has_feature(
            15, 5234, 12664, 'pois',
            {'kind': 'trailhead'})
