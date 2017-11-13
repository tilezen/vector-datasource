from . import FixtureTest


class AirportIataCodes(FixtureTest):
    def test_sfo(self):
        # San Francisco International
        self.load_fixtures(['https://www.openstreetmap.org/way/23718192'])

        self.assert_has_feature(
            13, 1311, 3170, 'pois',
            {'kind': 'aerodrome', 'iata': 'SFO'})

    def test_oak(self):
        # Oakland airport
        self.load_fixtures(['https://www.openstreetmap.org/way/54363486'])

        self.assert_has_feature(
            13, 1314, 3167, 'pois',
            {'kind': 'aerodrome', 'iata': 'OAK'})
