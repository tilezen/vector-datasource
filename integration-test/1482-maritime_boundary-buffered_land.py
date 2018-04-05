from . import FixtureTest


# Adds tests for OSM features (but not NE features)
class MaritimeBoundary(FixtureTest):

    def test_usa_canada_country_boundary(self):
        # country boundary of USA and Canada
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/148838',
            'https://www.openstreetmap.org/relation/1428125',
        ], clip=self.tile_bbox(8, 44, 87, padding=0.1))
        self.assert_has_feature(
            8, 44, 87, "boundaries",
            {"kind": "country", "maritime_boundary": false})

    def test_washington_idaho_region_boundary(self):
        # region boundary between Washington - Idaho
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/165479',
            'https://www.openstreetmap.org/relation/162116',
        ], clip=self.tile_bbox(8, 44, 88, padding=0.1))
        self.assert_has_feature(
            8, 44, 88, "boundaries",
            {"kind": "region", "maritime_boundary": false})
