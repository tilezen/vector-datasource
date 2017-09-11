from . import OsmFixtureTest


class AdjustTransitZoomRanges(OsmFixtureTest):
    def test_bart(self):
        # SFO-Pittsburg/Bay Point BART
        self.load_fixtures(['https://www.openstreetmap.org/relation/2827684'])

        self.assert_has_feature(
            8, 40, 98, 'transit',
            {'kind': 'subway'})

    def test_muni(self):
        # N-Judah Muni
        self.load_fixtures(['https://www.openstreetmap.org/relation/63223'])

        self.assert_has_feature(
            9, 81, 197, 'transit',
            {'kind': 'light_rail'})

    def test_tram(self):
        # F-Market & Wharves tram
        self.load_fixtures(['https://www.openstreetmap.org/relation/2007934'])

        self.assert_has_feature(
            9, 81, 197, 'transit',
            {'kind': 'tram'})
