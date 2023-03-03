from . import FixtureTest


class ElectronicsShops(FixtureTest):

    def test_best_buy(self):
        self._run_test(
            'https://www.openstreetmap.org/way/25821942',
            16, 10483, 25332, 'Best Buy')

    def test_another_best_buy(self):
        self._run_test(
            'https://www.openstreetmap.org/way/143811375',
            15, 5236, 12676, 'Best Buy')

    def test_yet_another_best_buy(self):
        self._run_test(
            'https://www.openstreetmap.org/way/25821942',
            15, 5241, 12666, 'Best Buy')

    def test_apple_store(self):
        self._run_test(
            'https://www.openstreetmap.org/way/332223480',
            16, 10484, 25327, 'Apple Union Square')

    def _run_test(self, url, z, x, y, name):
        self.load_fixtures([url])

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'electronics',
             'name': name})
