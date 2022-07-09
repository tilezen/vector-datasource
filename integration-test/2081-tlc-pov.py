import dsl

from . import FixtureTest


class TestTLCPOV(FixtureTest):
    def test_tlc_ne_place(self):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'name': 'Foo',
                'featurecla': 'Admin-0 capital',
                'fclass_iso': 'Admin-1 capital',
                'fclass_tlc': 'Admin-0 capital',
                'scalerank': 4,
                'min_zoom': 4,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'kind': 'locality',
                'country_capital': type(True),
                'country_capital:iso': type(False),
                'region_capital:iso': type(True),
                'country_capital:tlc': type(True),
            })

    def test_tlc_ne_boundary(self):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'name': 'Foo',
                'featurecla': 'Admin-1 region boundary',
                'fclass_iso': 'Admin-1 region boundary',
                'fclass_tlc': 'International boundary (verify)',
                'scalerank': 4,
                'min_zoom': 4,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'macroregion',
                'kind:iso': 'macroregion',
                'kind:tlc': 'country',
            })

    def test_osm_admin_level_viewpoint_tlc(self):
        z, x, y = (16, 39109, 26572)

        self.generate_fixtures(
            dsl.way(726514231, dsl.tile_diagonal(z, x, y), {
                'admin_level': '4',
                'admin_level:ISO': '8',
                'admin_level:TLC': '8',
                'boundary': 'disputed',
                'name': 'Viewpoints on Disputed Administrative Boundaries',
                'type': 'linestring',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 726514231,
                'kind': 'disputed_reference_line',
                'kind:iso': 'locality',
                'kind:tlc': 'locality',
            })

    def test_osm_places_with_viewpoint_tlc(self):
        import dsl

        z, x, y = (10, 856, 441)

        self.generate_fixtures(
            dsl.point(432425099, (120.9820179, 23.9739374), {
                'name': 'Test place',
                'place': 'country',
                'place:ISO': 'state',
                'place:TLC': 'district',
                'source': 'openstreetmap.org',
                'source:sqkm': 'CIA World Factbook',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 432425099,
                'kind': 'country',
                'kind:iso': 'region',
                'kind:tlc': 'county'
            })
