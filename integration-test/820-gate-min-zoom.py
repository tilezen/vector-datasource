# Set gate min zoom based on highway type

# Gate on secondary road
# http://www.openstreetmap.org/node/3608363612
# http://www.openstreetmap.org/way/83473200
test.assert_has_feature(
    15, 5528, 12649, 'pois',
    {'id': 3608363612, 'kind': 'gate', 'min_zoom': 15})

# Gate on minor road
# http://www.openstreetmap.org/node/2591034891
# http://www.openstreetmap.org/way/11621900
test.assert_has_feature(
    16, 19244, 24628, 'pois',
    {'id': 2591034891, 'kind': 'gate', 'min_zoom': 16})

test.assert_no_matching_feature(
    15, 9622, 12314, 'pois',
    {'id': 2591034891, 'kind': 'gate'})

# Gate on unclassified road
# http://www.openstreetmap.org/node/276321344
# http://www.openstreetmap.org/way/70807512
test.assert_has_feature(
    16, 10549, 25415, 'pois',
    {'id': 276321344, 'kind': 'gate', 'min_zoom': 16})

test.assert_no_matching_feature(
    15, 5274, 12707, 'pois',
    {'id': 276321344, 'kind': 'gate'})

# Gate on footway
# http://www.openstreetmap.org/node/302482019
# http://www.openstreetmap.org/way/27553445
test.assert_has_feature(
    16, 10466, 25328, 'pois',
    {'id': 302482019, 'kind': 'gate', 'min_zoom': 16})

test.assert_no_matching_feature(
    15, 5233, 12664, 'pois',
    {'id': 302482019, 'kind': 'gate'})

# Gate on a fence
# http://www.openstreetmap.org/node/4320045170
# http://www.openstreetmap.org/way/427290222
test.assert_has_feature(
    16, 10479, 25344, 'pois',
    {'id': 4320045170, 'kind': 'gate', 'min_zoom': 17})
