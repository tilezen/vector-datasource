from . import FixtureTest


class FeaturesTest(FixtureTest):
    def test_shops(self):
        self._run_test(
            'http://www.openstreetmap.org/node/2893904480',
            '16/19299/24631', {'kind': 'bakery'})
        self._run_test(
            'http://www.openstreetmap.org/node/886392347',
            '16/19297/24636', {'kind': 'books'})
        self._run_test(
            'http://www.openstreetmap.org/node/2709493928',
            '16/19297/24629', {'kind': 'butcher'})
        self._run_test(
            'http://www.openstreetmap.org/node/2565702300',
            '16/19295/24638', {'kind': 'car'})
        self._run_test(
            'http://www.openstreetmap.org/node/2065155887',
            '16/19310/24632', {'kind': 'car_repair'})

    def _run_test(self, url, zxy, props):
        z, x, y = map(int, zxy.split('/'))
        self.load_fixtures([url])
        self.assert_has_feature(
            z, x, y, 'pois', props)
