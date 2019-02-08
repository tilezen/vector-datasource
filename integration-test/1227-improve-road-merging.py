# -*- encoding: utf-8 -*-
from . import FixtureTest


class MergeJunctionTest(FixtureTest):

    def test_junction_x(self):
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import LineString, asShape
        from ModestMaps.Core import Coordinate
        import dsl

        z, x, y = (12, 2048, 2048)

        minx, miny, maxx, maxy = coord_to_bounds(
            Coordinate(zoom=z, column=x, row=y))
        midx = 0.5 * (minx + maxx)
        midy = 0.5 * (miny + maxy)

        road_props = dict(
            highway='residential',
            source='openstreetmap.org',
        )

        # make a tile with 4 roads in an X shape, as below.
        #
        #  \    /
        #   1  2
        #    \/
        #    /\
        #   3  4
        #  /    \
        #
        # these should get merged into two lines 1->4 & 2->3.
        self.generate_fixtures(
            dsl.way(1, LineString([[minx, maxy], [midx, midy]]), road_props),
            dsl.way(2, LineString([[maxx, maxy], [midx, midy]]), road_props),
            dsl.way(3, LineString([[minx, miny], [midx, midy]]), road_props),
            dsl.way(4, LineString([[maxx, miny], [midx, midy]]), road_props),
        )

        with self.features_in_tile_layer(z, x, y, 'roads') as features:
            # multilinestrings which contain lines which cross (as in the X
            # above) are "non-simple", and many geometry operations start by
            # forcing multilinestrings to be simple. we don't want this, as
            # it introduces an extra coordinate where the lines cross.
            # instead, we split into features which are individually simple,
            # which means we'll need 2 in this example.
            self.assertTrue(len(features) == 2)

            # when the test suite runs in "download only mode", an empty
            # set of features is passed into this block. the assertion
            # is shorted out, so we need this additional check which is
            # trivially satisfied in the case we're doing real testing.
            if len(features) == 2:
                for i in (0, 1):
                    # the shapes should be single linestrings in this example.
                    shape = asShape(features[i]['geometry'])
                    self.assertTrue(shape.geom_type == 'LineString')

                    # consisting of _only two_ points. (i.e: one didn't get
                    # inserted into the middle)
                    self.assertTrue(len(shape.coords) == 2)

    def test_junction_hash(self):
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import LineString, asShape
        from ModestMaps.Core import Coordinate
        import dsl

        z, x, y = (12, 2048, 2048)

        minx, miny, maxx, maxy = coord_to_bounds(
            Coordinate(zoom=z, column=x, row=y))
        midl = minx + (maxx - minx) / 3
        midr = minx + 2 * (maxx - minx) / 3
        midd = miny + (maxy - miny) / 3
        midu = miny + 2 * (maxy - miny) / 3

        road_props = dict(
            highway='residential',
            source='openstreetmap.org',
        )

        # make a tile with 4 roads in a # shape, as below.
        #
        #      |     |
        #      1     2
        #      |     |
        # --7--+--8--+--9--
        #      |     |
        #      3     4
        #      |     |
        # -10--+-11--+-12--
        #      |     |
        #      5     6
        #      |     |
        #
        # these should get merged into two features, one with 1->3->5 and
        # 2->4->6 and the other with 7->8->9 and 10->11->12.
        self.generate_fixtures(
            dsl.way(1, LineString([[midl, maxy], [midl, midu]]), road_props),
            dsl.way(2, LineString([[midr, maxy], [midr, midu]]), road_props),
            dsl.way(3, LineString([[midl, midu], [midl, midd]]), road_props),
            dsl.way(4, LineString([[midr, midu], [midr, midd]]), road_props),
            dsl.way(5, LineString([[midl, midd], [midl, miny]]), road_props),
            dsl.way(6, LineString([[midr, midd], [midr, miny]]), road_props),

            dsl.way(7, LineString([[minx, midu], [midl, midu]]), road_props),
            dsl.way(8, LineString([[minx, midd], [midl, midd]]), road_props),
            dsl.way(9, LineString([[midl, midu], [midr, midu]]), road_props),
            dsl.way(10, LineString([[midl, midd], [midr, midd]]), road_props),
            dsl.way(11, LineString([[midr, midu], [maxx, midu]]), road_props),
            dsl.way(12, LineString([[midr, midd], [maxx, midd]]), road_props),
        )

        class ApproxCoordSet(object):
            def __init__(self, coords, tolerance):
                self.coords = coords
                self.tolerance = tolerance

            def check_and_remove(self, item):
                x, y = item

                for ex, ey in self.coords:
                    if abs(x - ex) < self.tolerance and \
                       abs(y - ey) < self.tolerance:
                        self.coords.remove((ex, ey))
                        return True

                return False

        # scale from the coordinates within the tile to the coords in the
        # generated tile.
        scale = 20026376.39 / 180.0
        tolerance = scale * 1.0e-4

        with self.features_in_tile_layer(z, x, y, 'roads') as features:
            self.assertTrue(len(features) == 2,
                            "expected 2 features, got %d" % (len(features),))

            expected_coords = ApproxCoordSet([
                (midl * scale, maxy * scale),
                (midl * scale, miny * scale),
                (midr * scale, maxy * scale),
                (midr * scale, miny * scale),
                (minx * scale, midu * scale),
                (minx * scale, midd * scale),
                (maxx * scale, midu * scale),
                (maxx * scale, midd * scale),
            ], tolerance)

            if len(features) == 2:
                for i in (0, 1):
                    # the shapes should be multilinestrings with two lines.
                    shape = asShape(features[i]['geometry'])
                    self.assertTrue(shape.geom_type == 'MultiLineString')
                    self.assertTrue(
                        len(shape.geoms) == 2,
                        "expected 2 geometries in the MultiLineString, but "
                        "there are %d" % (len(shape.geoms),))

                    for line_i in (0, 1):
                        # each line should consist of only two points
                        line = shape.geoms[line_i]
                        self.assertTrue(
                            len(line.coords) == 2,
                            "expected 2 points, but line has %d" %
                            (len(line.coords),))

                        for coord_i in (0, 1):
                            coord = line.coords[coord_i]
                            self.assertTrue(
                                expected_coords.check_and_remove(coord),
                                "%r not in expected set %r" %
                                (coord, expected_coords.coords))
