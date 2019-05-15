# -*- encoding: utf-8 -*-
from . import FixtureTest


class BoundaryIdTest(FixtureTest):

    def _setup(self, z, x, y, left_id, right_id):
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
                    'id': left_id,
                    'name': 'Left',
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
                    'id': right_id,
                    'name': 'Right',
                    'mz_boundary_from_polygon': True,  # need this for hack
                }
            ),
        )

    def test_have_ids_at_z13(self):
        z, x, y = (13, 100, 100)
        self._setup(z, x, y, 1, 2)
        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id:left': 1,
                'id:right': 2,
            })

    def test_dropped_at_z12(self):
        z, x, y = (12, 50, 50)
        self._setup(z, x, y, 1, 2)
        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id:left': type(None),
                'id:right': type(None),
            })
