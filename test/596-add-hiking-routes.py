# https://www.openstreetmap.org/way/12188550
assert_has_feature(
    12, 654, 1582, 'roads',
    { 'kind': 'path', 'highway': 'track' })

# https://www.openstreetmap.org/way/109993139
# NOTE: part of *cycle* network, not walking network.
#assert_has_feature(
#    12, 655, 1586, 'roads',
#    { 'kind': 'path', 'highway': 'cycleway' })

# https://www.openstreetmap.org/way/25292070
assert_has_feature(
    14, 2620, 6334, 'roads',
    { 'kind': 'path', 'highway': 'steps', 'name': 'Esmeralda Ave.' })

# https://www.openstreetmap.org/way/346093021
assert_has_feature(
    15, 5235, 12671, 'roads',
    { 'kind': 'path', 'highway': 'footway' })

# http://www.openstreetmap.org/way/344205837
assert_has_feature(
    15, 5234, 12667, 'roads',
    { 'kind': 'path', 'highway': 'footway' })
