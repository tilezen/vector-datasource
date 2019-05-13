# -*- encoding: utf-8 -*-
from . import FixtureTest

# https://www.openstreetmap.org/relation/3694102
SAN_ANSELMO = {
    'boundary': 'administrative',
    'admin_level': '8',
    'name': 'San Anselmo',
    'official_name': 'Town of San Anselmo',
    'source': 'openstreetmap.org',
    'mz_boundary_from_polygon': True,  # need this for hack
}

# https://www.openstreetmap.org/relation/112679
SAN_RAFAEL = {
    'boundary': 'administrative',
    'admin_level': '8',
    'name': 'San Rafael',
    'source': 'openstreetmap.org',
    'mz_boundary_from_polygon': True,  # need this for hack
}


class LocalityTest(FixtureTest):

    def _setup(self, z, x, y, left_props, right_props):
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
                ]),
                left_props,
            ),
            dsl.way(
                2,
                LineString([
                    [minx, miny],
                    [maxx, maxy],
                    [maxx, miny],
                    [minx, miny],
                ]),
                right_props,
            ),
        )

    def test_name_stripped_at_z11(self):
        z, x, y = (11, 326, 790)
        self._setup(z, x, y, SAN_ANSELMO, SAN_RAFAEL)

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'locality',
                'name': type(None),
                'name:left': type(None),
                'name:right': type(None),
                'official_name:left': type(None),
            })

    def test_name_stripped_at_z12(self):
        z, x, y = (12, 653, 1580)
        self._setup(z, x, y, SAN_ANSELMO, SAN_RAFAEL)

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'locality',
                'name': type(None),
                'name:left': type(None),
                'name:right': type(None),
                'official_name:left': type(None),
            })

    def test_name_not_stripped_at_z13(self):
        z, x, y = (13, 1307, 3160)
        self._setup(z, x, y, SAN_ANSELMO, SAN_RAFAEL)

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'locality',
                'name': 'San Anselmo - San Rafael',
                'name:left': 'San Anselmo',
                'name:right': 'San Rafael',
                'official_name:left': 'Town of San Anselmo',
            })
