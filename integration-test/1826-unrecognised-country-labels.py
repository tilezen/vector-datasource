# -*- encoding: utf-8 -*-
from . import FixtureTest


class CountryTest(FixtureTest):

    def test_country_ne(self):
        import dsl

        z, x, y = 16, 0, 0
        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'place': 'country',
                'source': 'openstreetmap.org',
                'name': 'Foo',
                '__ne_min_zoom': 2,
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'kind': 'country',
                'min_zoom': 2,
            })

    def test_country_no_ne(self):
        import dsl

        z, x, y = 16, 0, 0
        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'place': 'country',
                'source': 'openstreetmap.org',
                'name': 'Foo',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'kind': 'country',
                'min_zoom': 6,
            })

    def test_region_no_ne(self):
        import dsl

        z, x, y = 16, 0, 0
        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'place': 'state',
                'source': 'openstreetmap.org',
                'name': 'Foo',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'kind': 'region',
                'min_zoom': 8,
            })
