# Buildings around San Francisco State University
#
# beware: overpass wants (south,west,north,east) coords for bbox, in defiance
# of x, y coordinate ordering.
#
# RAW QUERY: way(37.72049,-122.48589,37.72918,-122.47472)[building];>;
# RAW QUERY: relation(37.72049,-122.48589,37.72918,-122.47472)[building];>;
#
with test.features_in_tile_layer(16, 10470, 25342, 'landuse') as features:
    for feature in features:
        props = feature['properties']
        test.assertTrue('mz_is_building' not in props, 'mz_is_building detected')
