from . import FixtureTest


class ToysNotFound(FixtureTest):

    def test_01(self):
        self._run_test(16, 10473, 25339,
                       'https://www.openstreetmap.org/way/215472849')

    def test_02(self):
        self._run_test(16, 10479, 25336,
                       'https://www.openstreetmap.org/node/1713279804')

    def test_03(self):
        self._run_test(16, 10480, 25337,
                       'https://www.openstreetmap.org/node/3188857553')

    def test_04(self):
        self._run_test(16, 10484, 25328,
                       'https://www.openstreetmap.org/node/3396659022')

    def test_05(self):
        self._run_test(16, 10506, 25318,
                       'https://www.openstreetmap.org/node/1467717312')

    def test_06(self):
        self._run_test(16, 10509, 25308,
                       'https://www.openstreetmap.org/node/2286100659')

    def test_07(self):
        self._run_test(16, 10514, 25322,
                       'https://www.openstreetmap.org/node/3711137981')

    def test_08(self):
        self._run_test(16, 19298, 24633,
                       'https://www.openstreetmap.org/node/3810578539')

    def test_09(self):
        self._run_test(16, 19300, 24630,
                       'https://www.openstreetmap.org/node/1429062988')

    def test_10(self):
        self._run_test(16, 19300, 24629,
                       'https://www.openstreetmap.org/node/1058296287')

    def _run_test(self, z, x, y, url):
        self.load_fixtures([url])

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'toys'})
