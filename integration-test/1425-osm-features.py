from . import FixtureTest


class FeatureTests(FixtureTest):

    def test_shops(self):
        self._run_poi_test(
            'http://www.openstreetmap.org/node/2178336349',
            '16/19299/24638', {'kind': 'art'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/2821335218',
            '16/19295/24639', {'kind': 'beauty'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/4995839495',
            '16/19307/24631', {'kind': 'coffee'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/3842837139',
            '16/19301/24630', {'kind': 'deli'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/2328279410',
            '16/19296/24633', {'kind': 'furniture'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/2898340720',
            '16/19313/24633', {'kind': 'hifi'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/1581176007',
            '16/19301/24632', {'kind': 'newsagent'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/4913377716',
            '16/19298/24629', {'kind': 'perfumery'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/1853451180',
            '16/19296/24633', {'kind': 'shoes'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/3676902925',
            '16/19299/24635', {'kind': 'stationery'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/3116856932',
            '16/19304/24626', {'kind': 'tobacco'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/4553346149',
            '16/19298/24632', {'kind': 'travel_agency'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/2299770718',
            '16/19297/24633', {'kind': 'variety_store'})

    def test_amenities(self):
        self._run_poi_test(
            'http://www.openstreetmap.org/node/3573482149',
            '16/19297/24627', {'kind': 'car_wash'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/5209295977',
            '16/19309/24654',
            {'kind': 'car_wash', 'name': 'Tropical Breeze Car Wash'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/5209295977',
            '16/19309/24654', {'kind': 'car_wash'})

        self._run_poi_test(
            'http://www.openstreetmap.org/node/3656027075',
            '16/19337/24632', {'kind': 'charging_station'})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/3220603991',
            '16/33575/21727',
            {'kind': 'charging_station', 'scooter': True, 'car': False})
        self._run_poi_test(
            'http://www.openstreetmap.org/node/4882913388',
            '16/33896/23686',
            {'kind': 'charging_station', 'truck': True})

        self._run_poi_test(
            'http://www.openstreetmap.org/node/2463484707',
            '16/19179/24481', {'kind': 'hunting_stand'})

        self._run_poi_test(
            'http://www.openstreetmap.org/node/4042835711',
            '16/19298/24638', {'kind': 'marketplace'})

        self._run_poi_test(
            'http://www.openstreetmap.org/node/841558023',
            '16/19295/24639', {'kind': 'motorcycle_parking'})
        # motorcycle_parking with capacity and access
        self._run_poi_test(
            'http://www.openstreetmap.org/node/3517269144',
            '16/33688/21642',
            {'kind': 'motorcycle_parking', 'capacity': 15, 'access': 'private',
             'fee': False})
        # motorcycle_parking with covered=no and access
        self._run_poi_test(
            'http://www.openstreetmap.org/node/5198844293',
            '16/33565/21643',
            {'kind': 'motorcycle_parking', 'covered': False, 'access':
             'customers', 'fee': False})

        self._run_poi_test(
            'http://www.openstreetmap.org/node/2716231111',
            '16/19298/24629', {'kind': 'nightclub'})

    def _run_test(self, url, zxy, layer, props):
        z, x, y = map(int, zxy.split('/'))
        self.load_fixtures([url])
        self.assert_has_feature(z, x, y, layer, props)

    def _run_poi_test(self, url, zxy, props):
        return self._run_test(url, zxy, 'pois', props)
