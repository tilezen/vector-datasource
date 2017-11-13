from . import FixtureTest


class EarlierBikeProperties(FixtureTest):
    def test_bobcat_trail(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/12188550'])

        self.assert_has_feature(
            13, 1308, 3164, 'roads',
            {'motor_vehicle': 'no'})
