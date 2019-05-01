# -*- encoding: utf-8 -*-
from . import FixtureTest


class OSMMinZoomTests(FixtureTest):
    def test_motorway_min_zoom(self):
        import dsl

        z, x, y = (16, 33186, 22554)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/16108247
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'highway': 'motorway',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 1,
                'min_zoom': 5,
            })

    def test_trunk_min_zoom(self):
        import dsl

        z, x, y = (16, 33186, 22554)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/16108247
            dsl.way(2, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'highway': 'trunk',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 2,
                'min_zoom': 6,
            })

    def test_primary_min_zoom(self):
        import dsl

        z, x, y = (16, 33186, 22554)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/16108247
            dsl.way(3, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'highway': 'primary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3,
                'min_zoom': 8,
            })
