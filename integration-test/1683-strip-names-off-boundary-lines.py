# -*- encoding: utf-8 -*-
from . import FixtureTest


class StripNamesOffBoundaryLinesTest(FixtureTest):

    def _setup(self, z, x, y, left_name, right_name):
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import LineString
        from ModestMaps.Core import Coordinate
        import dsl

        minx, miny, maxx, maxy = coord_to_bounds(
            Coordinate(zoom=z, column=x, row=y))

        # move the coordinate points slightly out of the tile, so that we
        # don't get borders along the sides of the tile.
        w = maxx - minx
        h = maxy - miny
        minx -= 0.5 * w
        miny -= 0.5 * h
        maxx += 0.5 * w
        maxy += 0.5 * h

        self.generate_fixtures(
            dsl.way(
                1,
                LineString([
                    [minx, miny],
                    [minx, maxy],
                    [maxx, maxy],
                    [minx, miny],
                ]), {
                    'boundary': 'administrative',
                    'admin_level': '2',
                    'name': left_name,
                    'mz_boundary_from_polygon': True,  # need this for hack
                }
            ),
            dsl.way(
                2,
                LineString([
                    [minx, miny],
                    [maxx, maxy],
                    [maxx, miny],
                    [minx, miny],
                ]), {
                    'boundary': 'administrative',
                    'admin_level': '2',
                    'name': right_name,
                    'mz_boundary_from_polygon': True,  # need this for hack
                }
            ),
        )

    def test_do_not_strip_short_names(self):
        z, x, y = (8, 128, 128)

        self._setup(z, x, y, 'Foo', 'Bar')

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'name': 'Foo - Bar',
            })

    def test_strip_long_names(self):
        z, x, y = (8, 128, 128)

        n = 16
        self._setup(z, x, y, 'Foo' * n, 'Bar' * n)

        # should have stripped all the names off with such a ridiculously long
        # name.
        self.assert_no_matching_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'name': None,
            })
