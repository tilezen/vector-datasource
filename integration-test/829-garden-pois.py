# update gardens in pois

# garden with area in pois
# https://www.openstreetmap.org/way/120480164
test.assert_has_feature(
    13, 1309, 3166, 'pois',
    {'id': 120480164, 'kind': 'garden'})

# garden with area in landuse
# https://www.openstreetmap.org/way/120480164
test.assert_has_feature(
    13, 1309, 3166, 'landuse',
    {'id': 120480164, 'kind': 'garden'})

# garden without area in pois
# https://www.openstreetmap.org/node/2969748431
test.assert_has_feature(
    16, 10473, 25332, 'pois',
    {'id': 2969748431, 'kind': 'garden'})
