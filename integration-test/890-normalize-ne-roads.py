from . import OsmFixtureTest


class NormalizeNeRoads(OsmFixtureTest):

    def setUp(self):
        super(NormalizeNeRoads, self).setUp()
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_roads/890-normalize-ne-roads.shp',
        ])

    def test_ferry(self):
        # ferry
        self.assert_has_feature(
            7, 37, 48, 'roads',
            {'id': int, 'kind': 'ferry', 'type': type(None)})

    def test_expressway(self):
        # expressway
        self.assert_has_feature(
            7, 37, 48, 'roads',
            {'id': int, 'kind': 'highway', 'kind_detail': 'motorway',
             'type': type(None)})

    def test_major_highway(self):
        # major highway
        self.assert_has_feature(
            7, 108, 61, 'roads',
            {'id': int, 'kind': 'highway', 'kind_detail': 'trunk'})

    def test_beltway(self):
        # beltway
        self.assert_has_feature(
            7, 30, 48, 'roads',
            {'id': int, 'kind': 'highway', 'kind_detail': 'trunk'})

    def test_bypass(self):
        # bypass
        self.assert_has_feature(
            7, 34, 50, 'roads',
            {'id': int, 'kind': 'highway', 'kind_detail': 'trunk'})

    def test_secondary_highway(self):
        # secondary highway
        self.assert_has_feature(
            7, 28, 47, 'roads',
            {'id': int, 'kind': 'major_road', 'kind_detail': 'primary'})

    def test_road(self):
        # road
        self.assert_has_feature(
            7, 71, 49, 'roads',
            {'id': int, 'kind': 'major_road', 'kind_detail': 'secondary'})

    def test_track(self):
        # track
        self.assert_has_feature(
            7, 113, 70, 'roads',
            {'id': int, 'kind': 'minor_road', 'kind_detail': 'tertiary'})

    def test_unknown(self):
        # unknown
        self.assert_has_feature(
            7, 107, 52, 'roads',
            {'id': int, 'kind': 'minor_road', 'kind_detail': 'tertiary'})
