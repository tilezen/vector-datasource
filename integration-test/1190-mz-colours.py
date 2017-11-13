from . import FixtureTest


class MzColours(FixtureTest):
    def test_colour_property(self):
        self.load_fixtures(['http://www.openstreetmap.org/relation/366773'])

        self.assert_has_feature(
            16, 19310, 24645, 'transit',
            {'kind': 'subway', 'ref': 'Z',
             'colour': '#996633', 'colour_name': 'peru'})
