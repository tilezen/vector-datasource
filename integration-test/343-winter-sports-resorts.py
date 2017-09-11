from . import FixtureTest


class WinterSportsResorts(FixtureTest):
    def test_heavenly_mountain_resort(self):
        # Heavenly Mountain Resort NV/CA
        self.load_fixtures(['https://www.openstreetmap.org/way/317721523'])

        self.assert_has_feature(
            15, 5467, 12531, 'landuse',
            {'kind': 'winter_sports',
             'sort_rank': 36})
