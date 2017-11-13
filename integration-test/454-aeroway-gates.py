from . import FixtureTest


class AerowayGates(FixtureTest):
    def test_aeroway_gate(self):
        # Gate A5, SFO
        self.load_fixtures(['https://www.openstreetmap.org/node/656398641'])

        self.assert_has_feature(
            16, 10487, 25368, 'pois',
            {'kind': 'aeroway_gate'})
