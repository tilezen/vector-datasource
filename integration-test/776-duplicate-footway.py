from . import OsmFixtureTest


# we used to duplicate footway features between the roads and landuse layers.
# this test exists to make sure we don't backslide.
# see https://github.com/tilezen/vector-datasource/issues/776 for more info.
class DuplicateFootway(OsmFixtureTest):

    def test_pedestrian(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/128534087'])

        self.assert_has_feature(
            16, 10482, 25330, 'roads',
            {'id': 128534087})

        self.assert_no_matching_feature(
            16, 10482, 25330, 'landuse',
            {'id': 128534087})

    def test_footway(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/367756094'])

        self.assert_has_feature(
            16, 10465, 25331, 'roads',
            {'id': 367756094})

        self.assert_no_matching_feature(
            16, 10465, 25331, 'landuse',
            {'id': 367756094})
