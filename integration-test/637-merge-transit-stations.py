# Do not merge transit relations in zoom 15

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

assert_has_feature(
    14, 8186, 5448, 'pois',
    { 'id': 3638795618, 'kind': 'station'})

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
