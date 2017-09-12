from . import FixtureTest


class PierLines(FixtureTest):
    def test_pier_in_roads_layer(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/23783924'])

        self.assert_has_feature(
            16, 10467, 25308, 'roads',
            {'kind': 'path',
             'kind_detail': 'pier'})
