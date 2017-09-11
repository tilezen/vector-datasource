from . import OsmFixtureTest


class Waterfall(OsmFixtureTest):
    def test_more_than_300m(self):
        # Upper Yosemite Falls, because it's so tall at 550 meters, more than
        # 300 meters
        self.load_fixtures(['https://www.openstreetmap.org/node/2389658224'])

        self.assert_has_feature(
            12, 687, 1583, 'pois',
            {'kind': 'waterfall', 'min_zoom': 12, 'height': 550})

    def test_more_than_50m(self):
        # Middle Yosemite Falls, 206 meters, more than 50 meters
        self.load_fixtures(['https://www.openstreetmap.org/node/2384221575'])

        self.assert_has_feature(
            13, 1374, 3166, 'pois',
            {'kind': 'waterfall', 'min_zoom': 13})

    def test_98m_fall(self):
        # Lower Yosemite Falls, only 98 meters
        self.load_fixtures(['https://www.openstreetmap.org/node/2389657981'])

        self.assert_has_feature(
            13, 1374, 3167, 'pois',
            {'kind': 'waterfall', 'min_zoom': 13})

    def test_niagara_horseshoe_falls(self):
        # Niagara Falls (Horseshoe Falls)
        self.load_fixtures(['https://www.openstreetmap.org/way/56539663'])

        self.assert_has_feature(
            12, 1148, 1503, 'pois',
            {'kind': 'waterfall', 'min_zoom': 12})

        # We had considered this for label_placement:yes,
        # but there are only 19 in all of North America
        self.assert_no_matching_feature(
            12, 1148, 1503, 'water',
            {'kind': 'waterfall'})

    def test_height_missing(self):
        # Alamere Falls (no height)
        # Assume falls are important, show at zoom 14 default
        self.load_fixtures(['https://www.openstreetmap.org/node/2375445789'])

        self.assert_has_feature(
            14, 2604, 6322, 'pois',
            {'kind': 'waterfall', 'min_zoom': 14})

        # Lower Chilnualna Fall, no height
        self.load_fixtures(['http://www.openstreetmap.org/node/1247873121'])

        self.assert_has_feature(
            14, 2747, 6345, 'pois',
            {'kind': 'waterfall', 'min_zoom': 14})

        # https://www.openstreetmap.org/node/1247872815
        # Chilnualna Creek Cascades, no height
        self.load_fixtures(['https://www.openstreetmap.org/node/1247872815'])

        self.assert_has_feature(
            14, 2748, 6344, 'pois',
            {'kind': 'waterfall', 'min_zoom': 14})

    def test_less_than_8m(self):
        # Abrigo Falls, 4.5 meters (less than 8 meters)
        # Allow short waterfalls to be suppressed a zoom
        self.load_fixtures(['http://www.openstreetmap.org/node/3257658773'])

        self.assert_has_feature(
            15, 5265, 12645, 'pois',
            {'kind': 'waterfall', 'min_zoom': 15})

    def test_unit_conversion_height(self):
        # Rainbow Falls - height 150ft = 45m
        self.load_fixtures(['https://www.openstreetmap.org/node/877270365'])

        self.assert_has_feature(
            14, 4416, 6484, 'pois',
            {'kind': 'waterfall', 'min_zoom': 14, 'height': 45.72})

        # Toccoa Falls - height 186' = 56.6929m
        self.load_fixtures(['https://www.openstreetmap.org/node/404574988'])

        self.assert_has_feature(
            13, 2199, 3256, 'pois',
            {'kind': 'waterfall', 'min_zoom': 13, 'height': 56.6928})

        # Eternal Flame Falls - height 9m (with unit)
        self.load_fixtures(['https://www.openstreetmap.org/node/3647404249'])

        self.assert_has_feature(
            15, 9215, 12077, 'pois',
            {'kind': 'waterfall', 'min_zoom': 15, 'height': 9})
