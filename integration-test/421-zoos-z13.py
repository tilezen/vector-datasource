from . import FixtureTest


class ZoosZ13(FixtureTest):
    def test_zoo_appears_at_z13(self):
        # Zoo Montana, Billings, MT
        self.load_fixtures(['https://www.openstreetmap.org/node/2274329294'])

        self.assert_has_feature(
            13, 1624, 2923, 'pois',
            {'kind': 'zoo'})
