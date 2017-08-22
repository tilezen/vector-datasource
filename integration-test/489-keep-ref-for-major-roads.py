from . import OsmFixtureTest


class KeepRefForMajorRoads(OsmFixtureTest):
    def test_I495(self):
        # just checks that there is at least one major_road with a ref set.
        self.load_fixtures(['https://www.openstreetmap.org/relation/1876662'])

        self.assert_has_feature(
            9, 151, 192, 'roads',
            {'kind': 'major_road',
             'ref': None})
