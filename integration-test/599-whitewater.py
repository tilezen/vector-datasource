from . import OsmFixtureTest


class Whitewater(OsmFixtureTest):
    def test_put_in_egress(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3134398100'])

        self.assert_has_feature(
            16, 19591, 23939, 'pois',
            {'kind': 'put_in_egress'})

    def test_portage_way(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/308154534'])

        self.assert_has_feature(
            13, 2448, 2992, 'roads',
            {'kind': 'portage_way'})
