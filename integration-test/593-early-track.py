from . import OsmFixtureTest


class EarlyTrack(OsmFixtureTest):
    def test_track(self):
        # track example in Marin Headlands, a member of Bay Area Ridge Trail,
        # a regional network
        z, x, y = 12, 654, 1582

        self.load_fixtures([
            'https://www.openstreetmap.org/way/12188550',
            'https://www.openstreetmap.org/relation/2684235',
        ], clip=self.tile_bbox(z, x, y))

        self.assert_has_feature(
            z, x, y, 'roads',
            {'kind_detail': 'track'})
