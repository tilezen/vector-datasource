from . import OsmFixtureTest


class HistoricTransitStops(OsmFixtureTest):
    def test_historic_railway_stop(self):
        # Check if historic stops are shown in pois and in transit layers.
        # Historic railway stop
        self.load_fixtures(['https://www.openstreetmap.org/node/3039734894'])

        self.assert_no_matching_feature(
            13, 2412, 3081, 'pois',
            {'id': 3039734894})

    def test_historic_tram_stop(self):
        # Historic tram stop
        self.load_fixtures(['http://www.openstreetmap.org/node/413573669'])

        self.assert_no_matching_feature(
            13, 1320, 3189, 'pois',
            {'id': 413573669})

    def test_historic_railway_halt(self):
        # Historic railway halt
        self.load_fixtures(['http://www.openstreetmap.org/node/708144563'])

        self.assert_no_matching_feature(
            13, 4433, 2416, 'pois',
            {'id': 708144563})

        self.load_fixtures(['http://www.openstreetmap.org/node/2468597590'])

        self.assert_no_matching_feature(
            13, 4304, 2906, 'pois',
            {'id': 2468597590})

    def test_historic_railway_station(self):
        # Historic railway station
        self.load_fixtures(['http://www.openstreetmap.org/node/985085275'])

        self.assert_no_matching_feature(
            13, 4275, 2756, 'pois',
            {'id': 985085275})

    def test_historic_tram_stop_2(self):
        # Historic tram stop
        self.load_fixtures(['http://www.openstreetmap.org/node/3367033945'])

        self.assert_no_matching_feature(
            13, 1312, 2854, 'pois',
            {'id': 3367033945})

    def test_current_railway_stop(self):
        # Current railway stop
        self.load_fixtures(['http://www.openstreetmap.org/node/2986320002'])

        self.assert_has_feature(
            16, 19306, 24648, 'pois',
            {'id': 2986320002, 'min_zoom': 13})

    def test_current_tram_stop(self):
        # Current tram stop
        self.load_fixtures(['http://www.openstreetmap.org/node/257074010'])

        self.assert_has_feature(
            13, 1310, 3166, 'pois',
            {'id': 257074010})

    def test_current_railway_halt(self):
        # Current railway halt
        # http://www.openstreetmap.org/node/302735255
        self.load_fixtures(['http://www.openstreetmap.org/node/302735255'])

        self.assert_has_feature(
            13, 4478, 2843, 'pois',
            {'id': 302735255})
