# -*- encoding: utf-8 -*-
from . import FixtureTest


class LanduseMergingTest(FixtureTest):

    def test_grass(self):
        # we'll generate a patchwork of completely contiguous shapes with
        # varying areas. this is to make sure that different min zooms are
        # calculated for all of them.

        from shapely.ops import transform
        from tilequeue.tile import coord_to_mercator_bounds
        from tilequeue.tile import reproject_mercator_to_lnglat
        from ModestMaps.Core import Coordinate
        from shapely.geometry import box
        import dsl

        z, x, y = (10, 528, 332)

        props = {
            'source': 'openstreetmap.org',
            'landuse': 'grass',
        }

        bounds = coord_to_mercator_bounds(Coordinate(zoom=z, column=x, row=y))

        # define tile-internal coordinate system. note that we're squashing
        # the features into a smaller square, since we want fairly small
        # features and don't want to fill the tile with them.
        ox = 0.5 * (bounds[2] + bounds[0])
        w = 0.1 * (bounds[2] - bounds[0])
        oy = 0.5 * (bounds[3] + bounds[1])
        h = 0.1 * (bounds[3] - bounds[1])

        way_id = 1
        ways = []
        splits = 8
        swidth = 2 ** splits

        for sx in xrange(splits):
            for sy in xrange(splits):
                minx = ox + w * (0.5 * float(1 << sx) / swidth)
                maxx = ox + w * (float(1 << sx) / swidth)
                miny = oy + h * (0.5 * float(1 << sy) / swidth)
                maxy = oy + h * (float(1 << sy) / swidth)

                merc_shape = box(minx, miny, maxx, maxy)
                latlng_shape = transform(
                    reproject_mercator_to_lnglat, merc_shape)

                ways.append(dsl.way(way_id, latlng_shape, props))
                way_id += 1

        self.generate_fixtures(*ways)

        with self.features_in_tile_layer(z, x, y, 'landuse') as features:
            # have to use assertTrue here rather than the more natural
            # assertEqual so that when this is run as --download-only the test
            # case class can skip this test.
            self.assertTrue(len(features) == 1)
