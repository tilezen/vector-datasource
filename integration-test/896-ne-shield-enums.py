from . import OsmFixtureTest


class NeShieldEnums(OsmFixtureTest):

    def setUp(self):
        super(NeShieldEnums, self).setUp()
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_roads/896-ne-shield-enums.shp',
        ])

    def test_tch(self):
        # Trans-Canada Highway
        self.assert_has_feature(
            7, 20, 43, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'CA:??:primary',
             'kind': 'highway', 'shield_text': '1'})

    def test_i20(self):
        # I-20
        self.assert_has_feature(
            7, 35, 51, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'US:I',
             'kind': 'highway', 'shield_text': '20'})

    def test_us76(self):
        # US-76
        self.assert_has_feature(
            7, 35, 51, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'US:US',
             'kind': 'major_road', 'shield_text': '76'})

    def test_mex49(self):
        # MEX 49 (interstate)
        self.assert_has_feature(
            7, 27, 55, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'MX',
             'kind': 'highway', 'shield_text': '49'})

    def test_mex54(self):
        # MEX 54 (federal)
        self.assert_has_feature(
            7, 27, 55, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'MX:MX',
             'kind': 'major_road', 'shield_text': '54'})

    def test_e80(self):
        # E80 in Turkey
        self.assert_has_feature(
            7, 74, 47, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'e-road',
             'kind': 'highway', 'shield_text': '80'})

    def test_e30_m4(self):
        # E30 (M4) in UK
        self.assert_has_feature(
            7, 63, 42, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'e-road',
             'kind': 'highway', 'shield_text': '30'})

    def test_sh16(self):
        # SH16 in NZ
        self.assert_has_feature(
            7, 126, 78, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'NZ:SH',
             'kind': 'highway', 'shield_text': '16'})
