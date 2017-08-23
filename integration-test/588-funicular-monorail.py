from . import OsmFixtureTest


class FunicularMonorail(OsmFixtureTest):
    def test_monorail(self):
        self.load_fixtures(['https://www.openstreetmap.org/relation/6043603'])

        self.assert_has_feature(
            16, 10486, 25367, 'transit',
            {'kind': 'monorail'})

    def test_funicular(self):
        self.load_fixtures(['https://www.openstreetmap.org/relation/6060405'])

        self.assert_has_feature(
            16, 18201, 24705, 'transit',
            {'kind': 'funicular'})
