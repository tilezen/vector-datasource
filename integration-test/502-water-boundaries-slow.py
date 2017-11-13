from . import FixtureTest


class WaterBoundariesSlow(FixtureTest):

    def test_boundaries(self):
        from shapely.ops import unary_union

        # River Tocanis, Brasil

        # these are tiles which have water boundaries, but only
        # water-to-water boundaries. since we remove these, then we should
        # have more than one water polygon, but zero water boundaries
        # actually in the tile.
        no_boundary_tiles = [
            [16, 23768, 33616],
        ]

        # these are tiles which do have a boundary, to check that the first
        # condition isn't trivially fulfilled by having no boundaries
        # whatsoever.
        boundary_tiles = [
            [16, 23775, 33616],
        ]

        all_tiles = no_boundary_tiles + boundary_tiles
        all_boxes = [self.tile_bbox(*t, padding=2) for t in all_tiles]

        self.load_fixtures([
            'https://www.openstreetmap.org/relation/275011',
            'https://www.openstreetmap.org/relation/1363854',
        ], clip=unary_union(all_boxes))

        for z, x, y in no_boundary_tiles:
            with self.features_in_tile_layer(z, x, y, 'water') as features:
                num_polygons = 0
                num_boundaries = 0

                for f in features:
                    geom_type = f['geometry']['type']
                    boundary = f['properties'].get('boundary', False)

                    if geom_type in ['Polygon', 'MultiPolygon']:
                        num_polygons += 1

                    elif boundary is True:
                        num_boundaries += 1

                self.assertFalse(
                    num_polygons < 2,
                    'Expected at least 2 polygons in water boundary test '
                    'tile, but found only %d' % num_polygons)

                self.assertFalse(
                    num_boundaries > 0,
                    'Expected an all-water tile with no land boundaries, '
                    'but found %d boundaries.' % num_boundaries)

        for z, x, y in boundary_tiles:
            self.assert_has_feature(
                z, x, y, 'water',
                {'boundary': True})
