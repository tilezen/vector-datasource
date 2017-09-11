from . import OsmFixtureTest


class NaturalManMade(OsmFixtureTest):
    def test_mineshaft(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/4305375025'])

        self.assert_has_feature(
            15, 10394, 19077, 'pois',
            {'kind': 'mineshaft'})

    def test_adit(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/369156437'])

        self.assert_has_feature(
            16, 11932, 25298, 'pois',
            {'kind': 'adit'})

    def test_water_well(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/2794798164'])

        self.assert_has_feature(
            16, 10549, 25431, 'pois',
            {'kind': 'water_well', 'min_zoom': 17})

    def test_saddle(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/966585438'])

        self.assert_has_feature(
            14, 2764, 6333, 'pois',
            {'kind': 'saddle'})

    def test_geyser(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/358832354'])

        self.assert_has_feature(
            15, 5224, 12570, 'pois',
            {'kind': 'geyser'})

    def test_hot_spring(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4020311689'])

        self.assert_has_feature(
            16, 10805, 25827, 'pois',
            {'kind': 'hot_spring'})

    def test_rock(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/1804644217'])

        self.assert_has_feature(
            16, 27431, 36586, 'pois',
            {'kind': 'rock', 'min_zoom': 17})
