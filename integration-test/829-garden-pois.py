# update gardens in pois

# garden with area in pois
# https://www.openstreetmap.org/way/120480164
assert_has_feature(
    12, 654, 1583, 'pois',
    {'id': 120480164, 'kind': 'garden'})

# garden with area in landuse
# https://www.openstreetmap.org/way/120480164
assert_has_feature(
    11, 327, 791, 'landuse',
    {'id': 120480164, 'kind': 'garden'})

# garden without area in pois
# https://www.openstreetmap.org/node/2969748431
assert_has_feature(
    16, 10473, 25332, 'pois',
    {'id': 2969748431, 'kind': 'garden'})