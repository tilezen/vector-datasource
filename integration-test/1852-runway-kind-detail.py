# -*- encoding: utf-8 -*-
from . import FixtureTest


class RunwayTest(FixtureTest):

    def _check(self, aerodrome_type, runway_kind_detail):
        import dsl
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import LineString
        from shapely.geometry import CAP_STYLE
        from ModestMaps.Core import Coordinate

        z, x, y = (16, 0, 0)

        bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))

        # runway line that runs from a quarter to three quarters of the
        # tile diagonal. this is so that we can buffer it without it
        # going outside the tile boundary.
        runway_line = LineString([
            [bounds[0] + 0.25 * (bounds[2] - bounds[0]),
             bounds[1] + 0.25 * (bounds[3] - bounds[1])],
            [bounds[0] + 0.75 * (bounds[2] - bounds[0]),
             bounds[1] + 0.75 * (bounds[3] - bounds[1])],
        ])

        # runway polygon which has the runway line as a centreline.
        runway_poly = runway_line.buffer(
            0.1 * (bounds[2] - bounds[0]),  # width 1/10th of a tile
            cap_style=CAP_STYLE.flat,
        )

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'aeroway': 'aerodrome',
                'aerodrome:type': aerodrome_type,
                'name': 'Fake Aerodrome',
                'source': 'openstreetmap.org',
            }),
            # runway line
            dsl.way(2, runway_line, {
                'aeroway': 'runway',
                'source': 'openstreetmap.org',
            }),
            # runway polygon
            dsl.way(3, runway_poly, {
                'area:aeroway': 'runway',
                'source': 'openstreetmap.org',
            })
        )

        # runway line ends up in roads layer
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 2,
                'kind': 'aeroway',
                'kind_detail': 'runway',
                'aerodrome_kind_detail': runway_kind_detail,
            })

        # runway polygon is in landuse
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 3,
                'kind': 'runway',
                'kind_detail': runway_kind_detail,
            })

    def test_public(self):
        self._check('public', 'public')
