from . import OsmFixtureTest


class Funicular(OsmFixtureTest):
    def test_funicular(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/393550019'])

        self.assert_has_feature(
            16, 10481, 25345, 'roads',
            {'kind': 'rail', 'kind_detail': 'funicular'})
