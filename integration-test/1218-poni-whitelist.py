# aeroway=helipad
# https://www.openstreetmap.org/node/2207370738
assert_has_feature(
    15, 5230, 12657, 'pois',
    {'id': 2207370738})

# amenity=atm
# https://www.openstreetmap.org/node/4113423533
assert_has_feature(
    15, 5242, 12668, 'pois',
    {'id': 4113423533})

# amenity=bench
# https://www.openstreetmap.org/node/3951215438
assert_has_feature(
    15, 5239, 12672, 'pois',
    {'id': 3951215438})

# amenity=bicycle_rental
# https://www.openstreetmap.org/node/3509468129
assert_has_feature(
    15, 5251, 12655, 'pois',
    {'id': 3509468129})

# this is junk
# amenity=bus_stop

# amenity=car_sharing
# https://www.openstreetmap.org/node/4758733421
assert_has_feature(
    15, 5266, 12706, 'pois',
    {'id': 4758733421})

# amenity=fuel
# https://www.openstreetmap.org/node/2059530671
assert_has_feature(
    15, 5239, 12671, 'pois',
    {'id': 2059530671})

# amenity=post_box
# https://www.openstreetmap.org/node/4397690695
assert_has_feature(
    15, 5239, 12672, 'pois',
    {'id': 4397690695})

# amenity=recycling
# https://www.openstreetmap.org/node/2338524067
assert_has_feature(
    15, 5243, 12666, 'pois',
    {'id': 2338524067})

# amenity=shelter
# https://www.openstreetmap.org/node/4177497032
assert_has_feature(
    15, 5250, 12700, 'pois',
    {'id': 4177497032})

# amenity=telephone
# https://www.openstreetmap.org/node/1241673617
assert_has_feature(
    15, 5241, 12670, 'pois',
    {'id': 1241673617})

# amenity=waste_basket
# https://www.openstreetmap.org/node/4265260145
assert_has_feature(
    15, 5240, 12672, 'pois',
    {'id': 4265260145})

# highway=bus_stop
# https://www.openstreetmap.org/node/1229920715
assert_has_feature(
    15, 5239, 12672, 'pois',
    {'id': 1229920715})

# highway=ford
# https://www.openstreetmap.org/node/880807552
assert_has_feature(
    15, 5767, 13110, 'pois',
    {'id': 880807552})

# highway=mini_roundabout
# https://www.openstreetmap.org/node/110392851
assert_has_feature(
    15, 5228, 12650, 'pois',
    {'id': 110392851})

# highway=platform
# https://www.openstreetmap.org/node/1275126569
assert_has_feature(
    15, 7539, 11137, 'pois',
    {'id': 1275126569})

# highway=traffic_signals
# https://www.openstreetmap.org/node/65329980
assert_has_feature(
    15, 5242, 12664, 'pois',
    {'id': 65329980})

# waterway=lock
# https://www.openstreetmap.org/node/675426915
assert_has_feature(
    15, 9399, 12418, 'pois',
    {'id': 675426915})

# landuse=quarry
# https://www.openstreetmap.org/node/3356570361
assert_has_feature(
    15, 5265, 12615, 'pois',
    {'id': 3356570361})
# Way:184367568 quarry in POIS
# https://www.openstreetmap.org/way/184367568
assert_no_matching_feature(
    12, 671, 1583, 'pois',
    {'id': 184367568})

# leisure=dog_park
# https://www.openstreetmap.org/node/1229112075
assert_has_feature(
    15, 5235, 12669, 'pois',
    {'id': 1229112075})

# leisure=slipway
# https://www.openstreetmap.org/node/2678961627
assert_has_feature(
    15, 5238, 12652, 'pois',
    {'id': 2678961627})

# lock='yes'
# https://www.openstreetmap.org/node/365485771
assert_has_feature(
    15, 9527, 11985, 'pois',
    {'id': 365485771})

# man_made=adit
# https://www.openstreetmap.org/node/4469596254
assert_has_feature(
    15, 5626, 12731, 'pois',
    {'id': 4469596254})

# man_made=mineshaft
# https://www.openstreetmap.org/node/1818064871
assert_has_feature(
    15, 5378, 12607, 'pois',
    {'id': 1818064871})

# originally from 657-natural-man_made.py
# unnamed rock
# node 1328665285
assert_no_matching_feature(
    15, 5293, 12734, 'pois',
    { 'id': 1328665285 })

# man_made=offshore_platform
# https://www.openstreetmap.org/node/4239915448
assert_has_feature(
    15, 7549, 13919, 'pois',
    {'id': 4239915448})

# originally from 675-man_made-outdoor-landmarks.py
#https://www.openstreetmap.org/way/350328482
assert_no_matching_feature(
    13, 1942, 3395, 'pois',
    { 'id': 350328482 })

# there is only 1 of these in the world!?
# man_made=power_wind

# man_made=telescope
# https://www.openstreetmap.org/node/3310910810
assert_has_feature(
    15, 5334, 12510, 'pois',
    {'id': 3310910810})

# natural=cave_entrance
# https://www.openstreetmap.org/node/1050825518
assert_has_feature(
    15, 5178, 12346, 'pois',
    {'id': 1050825518})

# natural=waterfall
# https://www.openstreetmap.org/node/4719786091
assert_has_feature(
    15, 5491, 12694, 'pois',
    {'id': 4719786091})

# public_transport=platform
# https://www.openstreetmap.org/node/2073000913
assert_has_feature(
    15, 5238, 12671, 'pois',
    {'id': 2073000913})

# public_transport=stop_area
# https://www.openstreetmap.org/node/2991866242
assert_has_feature(
    15, 5214, 12588, 'pois',
    {'id': 2991866242})

# railway=halt
# https://www.openstreetmap.org/node/2382580308
assert_has_feature(
    15, 9545, 12368, 'pois',
    {'id': 2382580308})

# railway=platform
# https://www.openstreetmap.org/node/3987143106
assert_has_feature(
    15, 9821, 12242, 'pois',
    {'id': 3987143106})

# railway=stop
# https://www.openstreetmap.org/node/1130268570
assert_has_feature(
    15, 9381, 12527, 'pois',
    {'id': 1130268570})

# originally from 661-historic-transit-stops.py
# public_transport=stop_position
# railway=stop
# https://www.openstreetmap.org/node/3721890342
assert_has_feature(
    13, 1316, 3176, 'pois',
    {'id': 3721890342})

# railway=subway_entrance
# https://www.openstreetmap.org/node/3833748147
assert_has_feature(
    15, 9367, 12536, 'pois',
    {'id': 3833748147})

# railway=tram_stop
# https://www.openstreetmap.org/node/1719012916
assert_has_feature(
    15, 5239, 12670, 'pois',
    {'id': 1719012916})

# railway=level_crossing (but make min_zoom 18)
# https://www.openstreetmap.org/node/4665711307
assert_has_feature(
    15, 5235, 12667, 'pois',
    {'id': 4665711307})

# weird one, only 1 node
# tags->site=stop_area

# tags->whitewater=egress
# https://www.openstreetmap.org/node/4696619992
assert_has_feature(
    15, 5362, 12461, 'pois',
    {'id': 4696619992})

# tags->whitewater=hazard
# https://www.openstreetmap.org/node/4253919482
assert_has_feature(
    15, 5387, 12481, 'pois',
    {'id': 4253919482})

# tags->whitewater=put_in
# https://www.openstreetmap.org/node/3688927027
assert_has_feature(
    15, 5541, 12666, 'pois',
    {'id': 3688927027})

# tags->whitewater=rapid
# https://www.openstreetmap.org/node/4253919493
assert_has_feature(
    15, 5385, 12482, 'pois',
    {'id': 4253919493})

# tourism=alpine_hut
# https://www.openstreetmap.org/node/1076123765
assert_has_feature(
    15, 5433, 12607, 'pois',
    {'id': 1076123765})

# tourism=viewpoint
# https://www.openstreetmap.org/node/3065529317
assert_has_feature(
    15, 5236, 12667, 'pois',
    {'id': 3065529317})

# tourism=wilderness_hut
# https://www.openstreetmap.org/node/1837443430
assert_has_feature(
    15, 17100, 11564, 'pois',
    {'id': 1837443430})

# waterway=waterfall
# https://www.openstreetmap.org/node/4319935813
assert_has_feature(
    15, 5449, 12526, 'pois',
    {'id': 4319935813})

# originally from 927-normalize-operator-values.py
# information=guidepost
# operator=US Forest Service
# tourism=information
# https://www.openstreetmap.org/node/4216584100
assert_has_feature(
    16, 15995, 25090, 'pois',
    {'id': 4216584100})