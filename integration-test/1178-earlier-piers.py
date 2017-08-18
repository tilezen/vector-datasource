from . import OsmFixtureTest


class EarlierPiers(OsmFixtureTest):

    def test_very_large_pier(self):
        # a very, very large pier which alters the coastline visually, so
        # should be kept until z11.
        self.load_fixtures(['http://www.openstreetmap.org/way/377915546'])

        self.assert_has_feature(
            11, 1714, 876, 'landuse',
            {'id': 377915546, 'kind': 'pier', 'min_zoom': 11})

    def test_cruise_terminal(self):
        # zoom 11 for Cruise Terminal with area 53,276
        self.load_fixtures(['http://www.openstreetmap.org/way/275609726'])

        self.assert_has_feature(
            11, 357, 826, 'landuse',
            {'id': 275609726, 'kind': 'pier', 'min_zoom': 11.22})

    def test_broadway_pier(self):
        # zoom 12 for Broadway Pier with area 17,856
        self.load_fixtures(['http://www.openstreetmap.org/way/275609725'])

        self.assert_has_feature(
            12, 714, 1653, 'landuse',
            {'id': 275609725, 'kind': 'pier', 'min_zoom': 12})

    def test_smaller_unnamed_pier(self):
        # zoom 12 for unnamed pier with area 4,734
        self.load_fixtures(['http://www.openstreetmap.org/way/275609722'])

        self.assert_has_feature(
            12, 714, 1653, 'landuse',
            {'id': 275609722, 'kind': 'pier', 'min_zoom': 12.96})
