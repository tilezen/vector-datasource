from . import FixtureTest


class ZoosAndOtherAttractionsBarrier(FixtureTest):
    def test_fences_around_enclosures(self):
        # barrier=fence around enclosures
        self.load_fixtures(['https://www.openstreetmap.org/way/316623706'])

        self.assert_has_feature(
            16, 11458, 21855, 'landuse',
            {'kind': 'fence'})
