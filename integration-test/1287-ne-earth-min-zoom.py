# -*- encoding: utf-8 -*-
from . import FixtureTest


class EarthMinZoomTest(FixtureTest):

    def test_min_zoom_ne(self):
        # NE data min zoom should be taken from NE itself.
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'source': 'naturalearthdata.com',
                'min_zoom': 1,
            }),
        )

        self.assert_has_feature(
            8, 0, 0, 'earth', {
                'min_zoom': 1,
            })

    def test_min_zoom_osmdata(self):
        # should stay at zero? (we don't use this below z8 at the moment, so
        # the min_zoom only really matters for consistency with NE. however,
        # there's no meaningful ID on osmdata polygons to match with NE...
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'source': 'osmdata.openstreetmap.de',
                'area': 1,
                'min_zoom': 1,
            }),
        )

        self.assert_has_feature(
            8, 0, 0, 'earth', {
                'id': 1,
                'min_zoom': 0,
            })
