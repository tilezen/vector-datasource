import dsl

from . import FixtureTest


class TestPlaceUnrecognized(FixtureTest):
    def test_place_unrecognized_into_kind(self):

        z, x, y = 16, 0, 0
        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'place': 'unrecognized',
                'source': 'openstreetmap.org',
                'name': 'Foo'
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'kind': 'unrecognized',
                'min_zoom': 8,
            })
