from . import FixtureTest


class FeatureTests(FixtureTest):

    def test_shops(self):
        self._run_test(
            'http://www.openstreetmap.org/node/2178336349',
            '16/19299/24638', {'kind': 'art'})
        self._run_test(
            'http://www.openstreetmap.org/node/2821335218',
            '16/19295/24639', {'kind': 'beauty'})
        self._run_test(
            'http://www.openstreetmap.org/node/4995839495',
            '16/19307/24631', {'kind': 'coffee'})
        self._run_test(
            'http://www.openstreetmap.org/node/3842837139',
            '16/19301/24630', {'kind': 'deli'})
        self._run_test(
            'http://www.openstreetmap.org/node/2328279410',
            '16/19296/24633', {'kind': 'furniture'})
        self._run_test(
            'http://www.openstreetmap.org/node/2898340720',
            '16/19313/24633', {'kind': 'hifi'})
        self._run_test(
            'http://www.openstreetmap.org/node/1581176007',
            '16/19301/24632', {'kind': 'newsagent'})
        self._run_test(
            'http://www.openstreetmap.org/node/4913377716',
            '16/19298/24629', {'kind': 'perfumery'})
        self._run_test(
            'http://www.openstreetmap.org/node/1853451180',
            '16/19296/24633', {'kind': 'shoes'})
        self._run_test(
            'http://www.openstreetmap.org/node/3676902925',
            '16/19299/24635', {'kind': 'stationery'})
        self._run_test(
            'http://www.openstreetmap.org/node/3116856932',
            '16/19304/24626', {'kind': 'tobacco'})
        self._run_test(
            'http://www.openstreetmap.org/node/4553346149',
            '16/19298/24632', {'kind': 'travel_agency'})
        self._run_test(
            'http://www.openstreetmap.org/node/2299770718',
            '16/19297/24633', {'kind': 'variety_store'})

    def _run_test(self, url, zxy, props):
        z, x, y = map(int, zxy.split('/'))
        self.load_fixtures([url])
        self.assert_has_feature(z, x, y, 'pois', props)
