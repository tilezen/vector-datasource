from . import FixtureTest


class EarlyCycleway(FixtureTest):
    def test_cycleway(self):
        z, x, y = 12, 655, 1586
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/158622336',
             'https://www.openstreetmap.org/relation/2263205'],
            clip=self.tile_bbox(z, x, y))

        self.assert_has_feature(
            z, x, y, 'roads',
            {'kind_detail': 'cycleway'})
