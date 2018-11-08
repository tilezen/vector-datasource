# -*- encoding: utf-8 -*-
from . import FixtureTest


class MergeJunctionTest(FixtureTest):

    def test_junction(self):
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
            # should have merged into a single _feature_
            self.assertTrue(len(features) == 1)

            # the shape should be a multilinestring
            shape = asShape(features[0]['geometry'])
            self.assertTrue(shape.geom_type == 'MultiLineString')

            # with two internal linestrings
            self.assertTrue(len(shape.geoms) == 2)
