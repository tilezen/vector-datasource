from . import FixtureTest


class BasicOutdoorPois(FixtureTest):
    def test_bbq(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/1387024181'])

        self.assert_has_feature(
            16, 10550, 25297, 'pois',
            {'kind': 'bbq', 'min_zoom': 18})

    def test_bicycle_repair_station(self):
        # Node: Valencia Cyclery (3443701422)
        self.load_fixtures(['http://www.openstreetmap.org/node/3443701422'])

        self.assert_has_feature(
            16, 10481, 25335, 'pois',
            {'id': 3443701422, 'kind': 'bicycle_repair_station',
             'min_zoom': 18})

    def test_dive_centre(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2910259124'])

        self.assert_has_feature(
            16, 10798, 25903, 'pois',
            {'kind': 'dive_centre', 'min_zoom': 16})

    def test_life_ring(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2844159164'])

        self.assert_has_feature(
            16, 18308, 23892, 'pois',
            {'kind': 'life_ring', 'min_zoom': 18})

    def test_lifeguard_tower(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/4083762008'])

        self.assert_has_feature(
            16, 10805, 25927, 'pois',
            {'kind': 'lifeguard_tower', 'min_zoom': 17})

    def test_picnic_table(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/696801847'])

        self.assert_has_feature(
            16, 10597, 25151, 'pois',
            {'kind': 'picnic_table', 'min_zoom': 18})

    def test_shower(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/1128776802'])

        self.assert_has_feature(
            16, 10466, 25372, 'pois',
            {'kind': 'shower', 'min_zoom': 18})

    def test_waste_disposal(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2287784170'])

        self.assert_has_feature(
            16, 10514, 25255, 'pois',
            {'kind': 'waste_disposal', 'min_zoom': 18})

    def test_watering_place(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2640323071'])

        self.assert_has_feature(
            16, 10502, 25290, 'pois',
            {'kind': 'watering_place', 'min_zoom': 18})

    def test_water_point(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3954505509'])

        self.assert_has_feature(
            16, 10174, 23848, 'pois',
            {'kind': 'water_point', 'min_zoom': 18})

        self.load_fixtures(['https://www.openstreetmap.org/node/3984333433'])

        self.assert_has_feature(
            16, 12348, 25363, 'pois',
            {'kind': 'water_point', 'min_zoom': 18})

    def test_pylon(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/1978323412'])

        self.assert_has_feature(
            16, 10878, 25000, 'pois',
            {'kind': 'pylon', 'min_zoom': 17})

    def test_power_pole(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2398019418'])

        self.assert_has_feature(
            16, 10566, 25333, 'pois',
            {'kind': 'power_pole', 'min_zoom': 18})

    def test_power_tower(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/1378418272'])

        self.assert_has_feature(
            16, 10480, 25352, 'pois',
            {'kind': 'power_tower', 'min_zoom': 16})

    def test_petroleum_well(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2890101480'])

        self.assert_has_feature(
            16, 11080, 26141, 'pois',
            {'kind': 'petroleum_well', 'min_zoom': 17})
