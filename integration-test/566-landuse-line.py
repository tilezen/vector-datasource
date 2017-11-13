from . import FixtureTest


class LanduseLine(FixtureTest):
    def test_tree_row(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/207142223'])

        self.assert_has_feature(
            16, 10454, 25310, 'landuse',
            {'kind': 'tree_row', 'sort_rank': 264})

    def test_hedge(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/205644321'])

        self.assert_has_feature(
            16, 10485, 25332, 'landuse',
            {'kind': 'hedge', 'sort_rank': 263})
