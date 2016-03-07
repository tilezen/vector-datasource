import sys

def assert_no_repeated_points(coords):
    last_coord = coords[0]
    for i in range(1, len(coords)):
        coord = coords[i]
        if coord == last_coord:
            raise Exception("Coordinate %r (at %d) == %r (at %d), but "
                            "coordinates should not be repeated." %
                            (coord, i, last_coord, i-1))


with features_in_tile_layer(16, 17885, 27755, 'roads') as features:
    for feature in features:
        gtype = feature['geometry']['type']

        if gtype == 'LineString':
            assert_no_repeated_points(feature['geometry']['coordinates'])

        elif gtype == 'MultiLineString':
            for linestring in feature['geometry']['coordinates']:
                assert_no_repeated_points(linestring)
