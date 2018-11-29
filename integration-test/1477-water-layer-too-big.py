# -*- encoding: utf-8 -*-
from . import FixtureTest


class WaterLayerTooBigTest(FixtureTest):

    def test_drop_label(self):
        from tilequeue.tile import calc_meters_per_pixel_area
        from shapely.ops import transform
        from tilequeue.tile import reproject_mercator_to_lnglat
        import math
        import dsl

        for zoom in range(8, 16):
            area = 270.0 * calc_meters_per_pixel_area(zoom)
            radius = math.sqrt(area / math.pi)

            coord = 2 ** (zoom - 1)

            # larger feature should retain name
            shape = dsl.tile_centre_shape(
                zoom, coord, coord).buffer(radius * 1.1)
            shape_lnglat = transform(
                    reproject_mercator_to_lnglat, shape)

            self.generate_fixtures(
                dsl.way(1, shape_lnglat, {
                    'natural': 'water',
                    'name': 'Foo',
                }),
            )

            self.assert_has_feature(
                zoom, coord, coord, 'water', {
                    'kind': 'water',
                    'name': 'Foo',
                })

            # smaller shape should drop it
            shape = dsl.tile_centre_shape(
                zoom, coord, coord).buffer(radius / 1.1)
            shape_lnglat = transform(
                    reproject_mercator_to_lnglat, shape)

            self.generate_fixtures(
                dsl.way(1, shape_lnglat, {
                    'natural': 'water',
                    'name': 'Foo',
                }),
            )

            self.assert_has_feature(
                zoom, coord, coord, 'water', {
                    'kind': 'water',
                    'name': type(None),
                })
