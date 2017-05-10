# these are tiles which have water boundaries, but only water-to-water
# boundaries. since we remove these, then we should have more than one water
# polygon, but zero water boundaries actually in the tile.
no_boundary_tiles = [
    # https://www.openstreetmap.org/relation/275011
    # https://www.openstreetmap.org/relation/1363854
    [16, 23768, 33616], # River Tocanis, Brasil
]

# these are tiles which do have a boundary, to check that the first condition
# isn't trivially fulfilled by having no boundaries whatsoever.
#
# each of these is close to the tests above, and so any data needed has already
# been pulled in by those.
boundary_tiles = [
    [16, 23775, 33616], # R. Tocanis, Brasil
]

for z, x, y in no_boundary_tiles:
    with test.features_in_tile_layer(z, x, y, 'water') as features:
        num_polygons = 0
        num_boundaries = 0

        for f in features:
            geom_type = f['geometry']['type']
            boundary = f['properties'].get('boundary', False)

            if geom_type in ['Polygon', 'MultiPolygon']:
                num_polygons += 1

            elif boundary == True:
                num_boundaries += 1

        if num_polygons < 2:
            test.fail('Expected at least 2 polygons in water boundary '
                 'test tile, but found only %d' % num_polygons)

        if num_boundaries > 0:
            test.fail('Expected an all-water tile with no land '
                 'boundaries, but found %d boundaries.' % num_boundaries)

for z, x, y in boundary_tiles:
    test.assert_has_feature(
        z, x, y, 'water',
        {'boundary': True})
