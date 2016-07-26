# Set gate min zoom based on highway type

# Gate on secondary road
# https://www.openstreetmap.org/node/2784141829
assert_has_feature(
    15, 9237, 12635, 'pois',
    {'id': 2784141829, 'kind': 'gate'})

# Gate on minor road
# http://www.openstreetmap.org/node/2591034891
assert_has_feature(
    16, 19244, 24628, 'pois',
    {'id': 2591034891, 'kind': 'gate'})

assert_no_matching_feature(
    15, 9622, 12314, 'pois',
    {'id': 2591034891, 'kind': 'gate'})

# Gate on unclassified road
# http://www.openstreetmap.org/node/276321344
assert_has_feature(
    16, 10549, 25415, 'pois',
    {'id': 276321344, 'kind': 'gate'})

assert_no_matching_feature(
    15, 5274, 12707, 'pois',
    {'id': 276321344, 'kind': 'gate'})

# Gate on footway
# http://www.openstreetmap.org/node/302482019
assert_has_feature(
    16, 10466, 25328, 'pois',
    {'id': 302482019, 'kind': 'gate'})

assert_no_matching_feature(
    15, 5233, 12664, 'pois',
    {'id': 302482019, 'kind': 'gate'})

# Gate on a fence
# http://www.openstreetmap.org/node/4320045170
assert_has_feature(
    17, 20959, 50689, 'pois',
    {'id': 4320045170, 'kind': 'gate'})

assert_has_feature(
    16, 10479, 25344, 'pois',
    {'id': 4320045170, 'kind': 'gate', 'min_zoom': 17})
