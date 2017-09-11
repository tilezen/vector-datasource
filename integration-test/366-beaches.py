from . import FixtureTest


class Beaches(FixtureTest):
    def test_baker_beach(self):
        # Baker beach, SF
        self.load_fixtures(['https://www.openstreetmap.org/relation/6260732'])

        self.assert_has_feature(
            16, 10470, 25327, 'landuse', {'kind': 'beach'})
