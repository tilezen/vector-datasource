def assert_is_linestring(z, x, y, layer, name, max_coords, max_count):
    with features_in_tile_layer(z, x, y, layer) as features:
        count = 0
        total_coords = 0
        for feature in features:
            props = feature['properties']
            if props.get('name') == name:
                # should have been merged to become a single linestring.
                geom_type = feature['geometry']['type']
                if geom_type != 'LineString':
                    raise Exception('Expected linestring, got %r' % geom_type)
                count += 1
                coords = feature['geometry']['coordinates']
                if len(coords) > max_coords:
                    raise Exception(
                        'Single feature exceeded max coords: %d > %d' %
                        (len(coords), max_coords))
                total_coords += len(coords)
        if count > max_count:
            raise Exception('Expected at most %d features, found %d' %
                            (max_count, count))
        if total_coords > max_coords:
            raise Exception(
                'Expected at most %d coordinates, found %d in total' %
                (max_coords, total_coords))


# Pitkin Ave, NYC
#
# all of these are teriary roads, so we'd expect them to be merged
#
# http://www.openstreetmap.org/way/183794629
# http://www.openstreetmap.org/way/221583055
# http://www.openstreetmap.org/way/279918415
# http://www.openstreetmap.org/way/279918410
# http://www.openstreetmap.org/way/473433733
# http://www.openstreetmap.org/way/219606150
#
# note that there are 2 Pitkin Ave.s due to cycle path differences
assert_is_linestring(12, 1207, 1540, 'roads', 'Pitkin Ave.', 8, 2)
assert_is_linestring(11, 603, 770, 'roads', 'Pitkin Ave.', 8, 2)

# Linden Blvd, NYC
#
# many segments, one road?
#
# http://www.openstreetmap.org/way/183794593
# http://www.openstreetmap.org/way/221698693
# http://www.openstreetmap.org/way/420314185
# http://www.openstreetmap.org/way/420314186
# http://www.openstreetmap.org/way/420314187
# http://www.openstreetmap.org/way/420314188
# http://www.openstreetmap.org/way/420314189
# http://www.openstreetmap.org/way/420314190
# http://www.openstreetmap.org/way/420314194
# http://www.openstreetmap.org/way/420314195
# http://www.openstreetmap.org/way/420314197
# http://www.openstreetmap.org/way/420314198
# http://www.openstreetmap.org/way/420314200
# http://www.openstreetmap.org/way/420314201
# http://www.openstreetmap.org/way/420314202
# http://www.openstreetmap.org/way/420314203
# http://www.openstreetmap.org/way/420314205
# http://www.openstreetmap.org/way/420314206
# http://www.openstreetmap.org/way/420314208
# http://www.openstreetmap.org/way/420314209
# http://www.openstreetmap.org/way/420314213
# http://www.openstreetmap.org/way/420314215
# http://www.openstreetmap.org/way/420314217
# http://www.openstreetmap.org/way/420908360
# http://www.openstreetmap.org/way/420908361
# http://www.openstreetmap.org/way/420908362
# http://www.openstreetmap.org/way/420908363
# http://www.openstreetmap.org/way/420910104
# http://www.openstreetmap.org/way/420910105
# http://www.openstreetmap.org/way/420910106
# http://www.openstreetmap.org/way/420910107
# http://www.openstreetmap.org/way/421092462
# http://www.openstreetmap.org/way/421092463
# http://www.openstreetmap.org/way/421092464
# http://www.openstreetmap.org/way/421092465
# http://www.openstreetmap.org/way/421092466
# http://www.openstreetmap.org/way/421092467
# http://www.openstreetmap.org/way/421092468
# http://www.openstreetmap.org/way/421092472
# http://www.openstreetmap.org/way/421092475
# http://www.openstreetmap.org/way/421092476
# http://www.openstreetmap.org/way/421092482
# http://www.openstreetmap.org/way/421092484
# http://www.openstreetmap.org/way/421092485
# http://www.openstreetmap.org/way/421092487
assert_is_linestring(13, 2413, 3081, 'roads', 'Linden Blvd.', 8, 1)
