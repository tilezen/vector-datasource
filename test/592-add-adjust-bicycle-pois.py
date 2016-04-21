#http://www.openstreetmap.org/node/414269441
# Valencia Cyclery in SF
assert_has_feature(
    15, 5240, 12667, 'pois',
    { 'kind': 'bicycle', 'min_zoom': 15 })

#http://www.openstreetmap.org/node/3801412161
# San Francisco Bicycle Rentals
assert_has_feature(
    16, 10476, 25332, 'pois',
    { 'kind': 'bicycle_rental', 'min_zoom': 16 })

#http://www.openstreetmap.org/node/3708656264
# Citi Bike - Broadway & W 24 St, with network, operator
assert_has_feature(
    16, 19298, 24633, 'pois',
    { 'kind': 'bicycle_rental', 'min_zoom': 17, 'capacity': 52, 'network': 'Citi Bike' })

#http://www.openstreetmap.org/node/1993249660
# Cycle barrier in Berkeley
assert_has_feature(
    16, 10512, 25310, 'pois',
    { 'kind': 'cycle_barrier', 'min_zoom': 18 })

# WARNING: this kind of feature is only available in Europe
#http://www.openstreetmap.org/node/340159623
# rcn_ref=1
assert_has_feature(
    16, 33322, 21990, 'pois',
    { 'kind': 'bicycle_signpost', 'min_zoom': 16, 'ref': 1 })

# WARNING: this kind of feature is only available in Europe
#http://www.openstreetmap.org/node/300403808
# rwn_ref=1
assert_has_feature(
    16, 33492, 21929, 'pois',
    { 'kind': 'walking_signpost', 'min_zoom': 16, 'ref': 1 })
