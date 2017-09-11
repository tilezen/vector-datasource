from . import OsmFixtureTest


class MultilineEncoded(OsmFixtureTest):
    def test_multiline_encoded(self):
        # Way: Big Bear Boulevard (325846175)
        self.load_fixtures(['http://www.openstreetmap.org/way/325846175'])

        self.assert_feature_geom_type(16, 11473, 26126, 'roads',
                                      325846175, 'LineString')
