##
## A selection of very tall peaks which should be visible at zoom 9.
##

#http://www.openstreetmap.org/node/358915477
# Mount Elbert, CO
test.assert_has_feature(
    9, 104, 195, 'pois',
    { 'kind': 'peak', 'id': 358915477, 'elevation': 4397 })

# http://www.openstreetmap.org/node/1744903493
# Mount Rainier, WA (volcano)
test.assert_has_feature(
    9, 82, 180, 'pois',
    { 'kind': 'volcano', 'id': 1744903493, 'elevation': 4392 })

##
## Some smaller ones which should be visible at a range of zooms
##

def assert_feature_min_zoom(z, x, y, layer, props):
    test.assert_has_feature(z, x, y, layer, props)
    test.assert_no_matching_feature(z-1, x/2, y/2, layer, props)

# http://www.openstreetmap.org/node/358792071
# San Gorgonio Mountain
assert_feature_min_zoom(
    10, 179, 408, 'pois',
    { 'kind': 'peak', 'id': 358792071, 'elevation': 3502 })

#https://www.openstreetmap.org/node/358793535
# Toro Peak
assert_feature_min_zoom(
    11, 361, 821, 'pois',
    { 'kind': 'peak', 'id': 358793535, 'elevation': 2650 })

#https://www.openstreetmap.org/node/549642731
# Ventana Double Cone
assert_feature_min_zoom(
    12, 663, 1604, 'pois',
    { 'kind': 'peak', 'id': 549642731, 'elevation': 1477 })

#https://www.openstreetmap.org/node/358796064
# Chamisal Mountain
assert_feature_min_zoom(
    13, 1274, 3100, 'pois',
    { 'kind': 'peak', 'id': 358796064, 'elevation': 785 })
