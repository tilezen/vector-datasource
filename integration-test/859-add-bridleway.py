from . import FixtureTest


class AddBridleway(FixtureTest):
    def test_bridleway(self):
        # Add bridleway from osm
        self.load_fixtures(['http://www.openstreetmap.org/way/387216146'])

        self.assert_has_feature(
            16, 19302, 24623, 'roads',
            {'id': 387216146, 'kind': 'path', 'kind_detail': 'bridleway'})
