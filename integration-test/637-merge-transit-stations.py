# Do not merge transit relations in zoom 15

# Add all Waterloo station relations
# https://www.openstreetmap.org/relation/1242762
# https://www.openstreetmap.org/relation/238793
# https://www.openstreetmap.org/relation/238792
# https://www.openstreetmap.org/relation/102762
# https://www.openstreetmap.org/relation/102767
# https://www.openstreetmap.org/relation/173090
# https://www.openstreetmap.org/relation/4859971
# https://www.openstreetmap.org/relation/238792
# https://www.openstreetmap.org/node/70867643
# https://www.openstreetmap.org/node/178805960
# https://www.openstreetmap.org/node/492095642
# https://www.openstreetmap.org/node/3638795618
# https://www.openstreetmap.org/node/1802706032
# https://www.openstreetmap.org/node/344521109
# https://www.openstreetmap.org/node/492098585
# https://www.openstreetmap.org/node/492098466
# https://www.openstreetmap.org/node/495741652
# https://www.openstreetmap.org/node/495742107
# https://www.openstreetmap.org/node/492098125
# https://www.openstreetmap.org/node/3638795617
# https://www.openstreetmap.org/way/40551344
# https://www.openstreetmap.org/way/249695786
# https://www.openstreetmap.org/way/40781754
# https://www.openstreetmap.org/way/4245075

# https://www.openstreetmap.org/node/3638795617
assert_has_feature(
    16, 32747, 21793, 'pois',
    { 'id': 3638795617, 'kind': 'station'})

assert_has_feature(
    15, 16373, 10896, 'pois',
    { 'id': 3638795617, 'kind': 'station'})

assert_has_feature(
    14, 8186, 5448, 'pois',
    { 'id': 3638795617, 'kind': 'station'})

# https://www.openstreetmap.org/node/3638795618
assert_has_feature(
    16, 32747, 21793, 'pois',
    { 'id': 3638795618, 'kind': 'station'})

assert_has_feature(
    15, 16373, 10896, 'pois',
    { 'id': 3638795618, 'kind': 'station'})

assert_no_matching_feature(
    14, 8186, 5448, 'pois',
    { 'id': 3638795618, 'kind': 'station'})

# https://www.openstreetmap.org/node/1802706032
assert_has_feature(
    16, 32747, 21793, 'pois',
    { 'id': 1802706032, 'kind': 'stop_position'})

assert_has_feature(
    15, 16373, 10896, 'pois',
    { 'id': 1802706032, 'kind': 'stop_position'})

assert_no_matching_feature(
    14, 8186, 5448, 'pois',
    { 'id': 1802706032, 'kind': 'stop_position'})

# https://www.openstreetmap.org/node/70867643
assert_has_feature(
    16, 32747, 21793, 'pois',
    { 'id': 70867643, 'kind': 'stop'})

assert_has_feature(
    15, 16373, 10896, 'pois',
    { 'id': 70867643, 'kind': 'stop'})

assert_no_matching_feature(
    14, 8186, 5448, 'pois',
    { 'id': 70867643, 'kind': 'stop'})

# https://www.openstreetmap.org/node/492095642
assert_has_feature(
    16, 32747, 21793, 'pois',
    { 'id': 492095642, 'kind': 'stop_position'})

assert_has_feature(
    15, 16373, 10896, 'pois',
    { 'id': 492095642, 'kind': 'stop_position'})

assert_no_matching_feature(
    14, 8186, 5448, 'pois',
    { 'id': 492095642, 'kind': 'stop_position'})

# http://www.openstreetmap.org/node/178805960
assert_has_feature(
    16, 32747, 21793, 'pois',
    { 'id': 178805960, 'kind': 'stop_position'})

assert_has_feature(
    15, 16373, 10896, 'pois',
    { 'id': 178805960, 'kind': 'stop_position'})

assert_no_matching_feature(
    14, 8186, 5448, 'pois',
    { 'id': 178805960, 'kind': 'stop_position'})
