from . import OsmFixtureTest


# I think we should remove for v1 (and never should be been included at zoom
# less than 7 anyhow):
#
# Remove properties:
#  * level
#  * namealt
#  * namealtt
class NeShieldEnums2(OsmFixtureTest):

    def setUp(self):
        super(NeShieldEnums2, self).setUp()
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_roads/896-ne-shield-enums.shp',
        ])

    def test_remove_level(self):
        # E30 (M4) in UK
        self.assert_no_matching_feature(
            7, 63, 42, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'level': None})

    def test_remove_namealt(self):
        self.assert_no_matching_feature(
            7, 63, 42, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'namealt': None})

    def test_remove_namealtt(self):
        self.assert_no_matching_feature(
            7, 63, 42, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'namealtt': None})

    def test_network_and_shield(self):
        # network & shield text should stay on highways at lower zooms.
        # E30 (M4) in UK
        for z in range(5, 6):
            # tile 7/63/42 was tested in 896-ne-shield-enums.py
            x = 63 >> (7 - z)
            y = 42 >> (7 - z)
            self.assert_has_feature(
                z, x, y, 'roads',
                {'source': 'naturalearthdata.com', 'network': 'e-road',
                 'kind': 'highway', 'shield_text': '30'})
            # but not name, ref or all_*
            for prop in ['name', 'ref', 'all_networks', 'all_shield_texts']:
                self.assert_no_matching_feature(
                    z, x, y, 'roads', {prop: None})
