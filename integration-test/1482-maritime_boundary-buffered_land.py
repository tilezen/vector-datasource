from . import FixtureTest


# Adds tests for OSM features (but not NE features)
class MaritimeBoundary(FixtureTest):

    def test_usa_canada_country_boundary(self):
        # country boundary of USA and Canada
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/148838',
            'https://www.openstreetmap.org/relation/1428125',
            'file://integration-test/fixtures/buffered_land/'
            '1482-buffered_land-usa-can-wash-idaho.shp',
        ], clip=self.tile_bbox(8, 44, 87, padding=0.1))
        self.assert_has_feature(
            8, 44, 87, "boundaries",
            {"kind": "country"})

    def test_usa_canada_country_boundary_not_maritime_boundary(self):
        # country boundary of USA and Canada
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/148838',
            'https://www.openstreetmap.org/relation/1428125',
            'file://integration-test/fixtures/buffered_land/'
            '1482-buffered_land-usa-can-wash-idaho.shp',
        ], clip=self.tile_bbox(8, 44, 87, padding=0.1))
        self.assert_no_matching_feature(
            8, 44, 87, "boundaries",
            {"kind": "country", "maritime_boundary": 1})

    def test_washington_idaho_region_boundary(self):
        # region boundary between Washington - Idaho
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/165479',
            'https://www.openstreetmap.org/relation/162116',
            'file://integration-test/fixtures/buffered_land/'
            '1482-buffered_land-usa-can-wash-idaho.shp',
        ], clip=self.tile_bbox(8, 44, 88, padding=0.1))
        self.assert_has_feature(
            8, 44, 88, "boundaries",
            {"kind": "region"})

    def test_washington_idaho_region_boundary_not_maritime_boundary(self):
        # region boundary between Washington - Idaho
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/165479',
            'https://www.openstreetmap.org/relation/162116',
            'file://integration-test/fixtures/buffered_land/'
            '1482-buffered_land-usa-can-wash-idaho.shp',
        ], clip=self.tile_bbox(8, 44, 88, padding=0.1))
        self.assert_no_matching_feature(
            8, 44, 88, "boundaries",
            {"kind": "region", "maritime_boundary": 1})

    # this test is to state the properties explicitly, so that we can make sure
    # they don't get changed unintentionally.
    def test_generative_non_maritime(self):
        import dsl

        z, x, y = (8, 44, 88)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'source': 'tilezen.org',
                'maritime_boundary': True,
                'min_zoom': 0,
                'kind': 'maritime',
            }),
            dsl.way(2, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'boundary': 'administrative',
                'admin_level': '2',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 2,
                'kind': 'country',
                'maritime_boundary': type(None),
            })

    def test_generative_maritime(self):
        import dsl

        z, x, y = (8, 44, 88)

        self.generate_fixtures(
            dsl.way(2, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'boundary': 'administrative',
                'admin_level': '2',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 2,
                'kind': 'country',
                'maritime_boundary': True,
            })
