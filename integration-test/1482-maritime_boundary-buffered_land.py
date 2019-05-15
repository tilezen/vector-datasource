from . import FixtureTest


# Adds tests for OSM features (but not NE features)
class MaritimeBoundary(FixtureTest):

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
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
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
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'maritime_boundary': True,
            })
