from . import FixtureTest


class Prisons(FixtureTest):
    def test_rikers_island(self):
        self.load_fixtures(['https://www.openstreetmap.org/relation/3955540'])

        self.assert_has_feature(
            10, 301, 384, 'pois',
            {'kind': 'prison', 'name': 'Rikers Island'})

    def test_sf_county_jail(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/103383866'])

        self.assert_has_feature(
            14, 2621, 6332, 'pois',
            {'kind': 'prison', 'name': 'SF County Jail'})

    def test_rikers_island_landuse(self):
        # Rikers Island also should have a landuse polygon
        self.load_fixtures(['https://www.openstreetmap.org/relation/3955540'])

        self.assert_has_feature(
            10, 301, 384, 'landuse',
            {'kind': 'prison'})
