from . import FixtureTest


class AddKindDetailForPois(FixtureTest):
    def test_seafood_restaurant(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1426311638'])

        self.assert_has_feature(
            16, 19298, 24629, 'pois',
            {'id': 1426311638, 'kind': 'restaurant',
             'kind_detail': 'seafood'})

    def test_japanese_restaurant(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/280288213'])

        self.assert_has_feature(
            16, 19319, 24634, 'pois',
            {'id': 280288213, 'kind': 'restaurant',
             'kind_detail': 'japanese'})

    def test_baseball_pitch(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4305351592'])

        self.assert_has_feature(
            16, 19336, 24608, 'pois',
            {'id': 4305351592, 'kind': 'pitch', 'kind_detail': 'baseball'})

    def test_basketball_pitch(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/326894220'])

        self.assert_has_feature(
            16, 19321, 24634, 'pois',
            {'id': 326894220, 'kind': 'pitch', 'kind_detail': 'basketball'})
