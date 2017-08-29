from . import OsmFixtureTest


class BuildingsZ13(OsmFixtureTest):
    def test_buildings_exist_at_zoom_13(self):
        # Earlier work in 845 dropped buildings from zoom 13
        self.load_fixtures(['http://www.openstreetmap.org/way/23654700',
                            'http://www.openstreetmap.org/way/60500069'])

        self.assert_has_feature(
            13, 1310, 3170, 'buildings',
            {'kind': 'building'})
