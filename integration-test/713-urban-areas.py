from . import OsmFixtureTest


class UrbanAreas(OsmFixtureTest):
    def test_urban_area_zooms(self):
        # update kind to read urban_areas instead of urban areas.
        # This is not an OSM feature it comes from Natural Earth
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_urban_areas/713-urban-areas.shp',
        ])

        self.assert_has_feature(
            4, 2, 6, 'landuse',
            {'kind': 'urban_area'})

        self.assert_no_matching_feature(
            4, 2, 6, 'landuse',
            {'kind': 'urban area'})

        self.assert_has_feature(
            7, 20, 49, 'landuse',
            {'kind': 'urban_area'})

        self.assert_no_matching_feature(
            7, 20, 49, 'landuse',
            {'kind': 'urban area'})

        self.assert_has_feature(
            9, 81, 197, 'landuse',
            {'kind': 'urban_area'})

        self.assert_no_matching_feature(
            9, 81, 197, 'landuse',
            {'kind': 'urban area'})
