# Check if historic stops are shown in pois and in transit layers.

# Historic railway stop
# https://www.openstreetmap.org/node/3039734894
test.assert_no_matching_feature(
    13, 2412, 3081, 'pois',
    {'id': 3039734894})

# Historic tram stop
# http://www.openstreetmap.org/node/413573669
test.assert_no_matching_feature(
    13, 1320, 3189, 'pois',
    {'id': 413573669})

# Historic railway halt
# http://www.openstreetmap.org/node/708144563
test.assert_no_matching_feature(
    13, 4433, 2416, 'pois',
    {'id': 708144563})

# Historic railway halt
# http://www.openstreetmap.org/node/2468597590
test.assert_no_matching_feature(
    13, 4304, 2906, 'pois',
    {'id': 2468597590})

# Historic railway station
# http://www.openstreetmap.org/node/985085275
test.assert_no_matching_feature(
    13, 4275, 2756, 'pois',
    {'id': 985085275})

# Historic tram stop
# http://www.openstreetmap.org/node/3367033945
test.assert_no_matching_feature(
    13, 1312, 2854, 'pois',
    {'id': 3367033945})

# Current railway stop
# http://www.openstreetmap.org/node/2986320002
test.assert_has_feature(
    16, 19306, 24648, 'pois',
    {'id': 2986320002, 'min_zoom': 13})

# Current tram stop
# http://www.openstreetmap.org/node/257074010
test.assert_has_feature(
	13, 1310, 3166, 'pois',
    {'id': 257074010})

# Current railway halt
# http://www.openstreetmap.org/node/302735255
test.assert_has_feature(
	13, 4478, 2843, 'pois',
    {'id': 302735255})
