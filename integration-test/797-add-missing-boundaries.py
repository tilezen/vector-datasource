from . import OsmFixtureTest


class AddMissingBoundaries(OsmFixtureTest):
    def test_statistical(self):
        # NE data - no OSM elements
        # boundary between NV and CA is _also_ a "statistical" boundary
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_admin_1_states_provinces_lines/'
            '797-ne_10m_admin_1_states_provinces_lines-nv-ca.shp',
        ])

        self.assert_has_feature(
            7, 21, 49, 'boundaries',
            {'kind': 'region'})

    def test_statistical_meta(self):
        # boundary between MT and ND is _also_ a "statistical meta" boundary
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_admin_1_states_provinces_lines/'
            '797-ne_10m_admin_1_states_provinces_lines-mt-nd.shp',
        ])

        self.assert_has_feature(
            7, 27, 44, 'boundaries',
            {'kind': 'region'})
