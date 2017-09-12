from . import FixtureTest


class LanduseScree(FixtureTest):
    def test_scree(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/59621863'])

        self.assert_has_feature(
            16, 10481, 25319, 'landuse',
            {'kind': 'scree'})
