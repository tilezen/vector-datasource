from . import OsmFixtureTest


class GardenMinZoom(OsmFixtureTest):
    def test_very_small_garden(self):
        # this garden previously had a min_zoom of 12, but based on its size
        # should be z16 instead.
        self.load_fixtures(['http://www.openstreetmap.org/way/273274870'])

        self.assert_has_feature(
            16, 32182, 20422, 'landuse',
            {'kind': 'garden', 'id': 273274870, 'min_zoom': 16, 'tier': 6})

        # shouldn't be a POI now as it has no name.
        self.assert_no_matching_feature(
            16, 32182, 20422, 'pois',
            {'kind': 'garden'})

    def test_small_named_garden(self):
        # instead, here's a small, named garden
        self.load_fixtures(['http://www.openstreetmap.org/way/162235630'])

        self.assert_has_feature(
            16, 19303, 24647, 'pois',
            {'kind': 'garden', 'id': 162235630, 'min_zoom': 16, 'tier': 6})
