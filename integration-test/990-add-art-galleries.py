from . import FixtureTest


class AddArtGalleries(FixtureTest):
    def test_node(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2026996113'])

        self.assert_has_feature(
            16, 10485, 25328, 'pois',
            {'id': 2026996113, 'kind': 'gallery', 'min_zoom': 17})

    def test_way(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/83488820'])

        self.assert_has_feature(
            15, 16370, 10894, 'pois',
            {'id': 83488820, 'kind': 'gallery'})
