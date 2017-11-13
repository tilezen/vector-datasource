from . import FixtureTest


class NeMinZoomRoads(FixtureTest):
    def setUp(self):
        super(NeMinZoomRoads, self).setUp()

        # note: uses existing fixture from 976-fractional-pois
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_roads/976-fractional-pois.shp',
        ])

    def test_roads_present_at_zoom_5(self):
        # the road should be present at zoom 5
        self.assert_has_feature(
            5, 9, 12, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'shield_text': '95'})

    def test_roads_not_present_at_zoom_3(self):
        # but not at zoom 3 or 4
        self.assert_no_matching_feature(
            3, 2, 3, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'shield_text': '95'})

    def test_roads_not_present_at_zoom_4(self):
        self.assert_no_matching_feature(
            4, 4, 6, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'shield_text': '95'})
