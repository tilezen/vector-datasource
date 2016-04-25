# http://www.openstreetmap.org/node/414269441
# Valencia Cyclery in SF
assert_has_feature(
    15, 5240, 12667, 'pois',
    { 'kind': 'bicycle', 'min_zoom': 15 })

# http://www.openstreetmap.org/node/3801412161
# San Francisco Bicycle Rentals
assert_has_feature(
    16, 10476, 25332, 'pois',
    { 'kind': 'bicycle_rental', 'min_zoom': 16 })

# http://www.openstreetmap.org/node/3708656264
# Citi Bike - Broadway & W 24 St, with network, operator
assert_has_feature(
    16, 19298, 24633, 'pois',
    { 'kind': 'bicycle_rental_station', 'min_zoom': 17, 'capacity': 52, 'network': 'Citi Bike' })

# http://www.openstreetmap.org/node/1993249660
# Cycle barrier in Berkeley
assert_has_feature(
    16, 10512, 25310, 'pois',
    { 'kind': 'cycle_barrier', 'min_zoom': 18 })



# WARNING: this kind of feature is only available in Europe
# http://www.openstreetmap.org/node/3836406372
# icn_ref=1
assert_has_feature(
    16, 32382, 22860, 'pois',
    { 'kind': 'bicycle_guidepost', 'min_zoom': 16, 'ref': '1', 'bicycle_network': 'icn' })

# No known examples in the world for nodes, and ways don't count
# ncn_ref=1

# WARNING: this kind of feature is only available in Europe
# http://www.openstreetmap.org/node/340159623
# rcn_ref=1
assert_has_feature(
    16, 33322, 21990, 'pois',
    { 'kind': 'bicycle_guidepost', 'min_zoom': 16, 'ref': '1', 'bicycle_network': 'rcn' })

# NOTE: this is strangely in Omaha, NE, USA
# http://www.openstreetmap.org/node/3269815503
# lcn_ref=1
assert_has_feature(
    16, 15299, 24506, 'pois',
    { 'kind': 'bicycle_guidepost', 'min_zoom': 16, 'ref': '1', 'bicycle_network': 'lcn' })

# http://www.openstreetmap.org/node/287609621
# lcn_ref=2
#    16, 32570, 21059, 'pois',
assert_has_feature(
    16, 32570, 21058, 'pois',
    { 'kind': 'bicycle_guidepost', 'min_zoom': 16, 'ref': '2', 'bicycle_network': 'lcn' })


# No known examples in the world for nodes, and ways don't count
# iwn_ref=1

# No known examples in the world for nodes, and ways don't count
# nwn_ref=1

# WARNING: this kind of feature is only available in Europe
# http://www.openstreetmap.org/node/300403808
# rwn_ref=1
assert_has_feature(
    16, 33492, 21929, 'pois',
    { 'kind': 'walking_guidepost', 'min_zoom': 16, 'ref': '1', 'walking_network': 'rwn' })

# WARNING: this kind of feature is only available in Europe
# http://www.openstreetmap.org/node/717593380
# lwn_ref=1
assert_has_feature(
    16, 34584, 21219, 'pois',
    { 'kind': 'walking_guidepost', 'min_zoom': 16, 'ref': 'ST', 'walking_network': 'lwn' })