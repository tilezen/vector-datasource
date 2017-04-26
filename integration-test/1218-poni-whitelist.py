# https://www.openstreetmap.org/node/2207370738
# 15/5230/12657
# aeroway"="helipad"
assert_has_feature(
    15, 5230, 12657, 'pois',
    {'id': 2207370738})

# https://www.openstreetmap.org/node/4113423533
# 15/5242/12668
# "amenity"="atm"
assert_has_feature(
    15, 5242, 12668, 'pois',
    {'id': 4113423533})

# https://www.openstreetmap.org/node/3951215438
# 15/5239/12672
# "amenity"="bench"
assert_has_feature(
    15, 5239, 12672, 'pois',
    {'id': 3951215438})

# https://www.openstreetmap.org/node/3509468129
# 15/5251/12655
# "amenity"="bicycle_rental"
assert_has_feature(
    15, 5251, 12655, 'pois',
    {'id': 3509468129})

# this is junk
# "amenity"="bus_stop"

# https://www.openstreetmap.org/node/4758733421
# 15/5266/12706
# "amenity"="car_sharing"
assert_has_feature(
    15, 5266, 12706, 'pois',
    {'id': 4758733421})

# https://www.openstreetmap.org/node/2059530671
# 15/5239/12671
# "amenity"="fuel"
assert_has_feature(
    15, 5239, 12671, 'pois',
    {'id': 2059530671})

# https://www.openstreetmap.org/node/4397690695
# 15/5239/12672
# "amenity"="post_box"
assert_has_feature(
    15, 5239, 12672, 'pois',
    {'id': 4397690695})

# https://www.openstreetmap.org/node/2338524067
# 15/5243/12666
# "amenity"="recycling"
assert_has_feature(
    15, 5243, 12666, 'pois',
    {'id': 2338524067})

# https://www.openstreetmap.org/node/4177497032
# 15/5250/12700
# "amenity"="shelter"
assert_has_feature(
    15, 5250, 12700, 'pois',
    {'id': 4177497032})

# https://www.openstreetmap.org/node/1241673617
# 15/5241/12670
# "amenity"="telephone"
assert_has_feature(
    15, 5241, 12670, 'pois',
    {'id': 1241673617})

# https://www.openstreetmap.org/node/4265260145
# 15/5240/12672
# "amenity"="waste_basket"
assert_has_feature(
    15, 5240, 12672, 'pois',
    {'id': 4265260145})

# https://www.openstreetmap.org/node/1229920715
# 15/5239/12672
# "highway"="bus_stop"
assert_has_feature(
    15, 5239, 12672, 'pois',
    {'id': 1229920715})

# https://www.openstreetmap.org/node/880807552
# 15/5767/13110
# "highway"="ford"
assert_has_feature(
    15, 5767, 13110, 'pois',
    {'id': 880807552})

# https://www.openstreetmap.org/node/110392851
# 15/5228/12650
# "highway"="mini_roundabout"
assert_has_feature(
    15, 5228, 12650, 'pois',
    {'id': 110392851})

# https://www.openstreetmap.org/node/1275126569
# 15/7539/11137
# "highway"="platform"
assert_has_feature(
    15, 7539, 11137, 'pois',
    {'id': 1275126569})

# https://www.openstreetmap.org/node/65329980
# 15/5242/12664
# "highway"="traffic_signals"
assert_has_feature(
    15, 5242, 12664, 'pois',
    {'id': 65329980})

# https://www.openstreetmap.org/node/675426915
# 15/9399/12418
# "waterway"="lock"
assert_has_feature(
    15, 9399, 12418, 'pois',
    {'id': 675426915})

# https://www.openstreetmap.org/node/3356570361
# 15/5265/12615
# "landuse"="quarry"
assert_has_feature(
    15, 5265, 12615, 'pois',
    {'id': 3356570361})
# Way:184367568 quarry in POIS
# http://www.openstreetmap.org/way/184367568
assert_no_matching_feature(
    12, 671, 1583, 'pois',
    {'id': 184367568})


# https://www.openstreetmap.org/node/1229112075
# 15/5235/12669
# "leisure"="dog_park"
assert_has_feature(
    15, 5235, 12669, 'pois',
    {'id': 1229112075})

# https://www.openstreetmap.org/node/2678961627
# 15/5238/12652
# "leisure"="slipway"
assert_has_feature(
    15, 5238, 12652, 'pois',
    {'id': 2678961627})

# https://www.openstreetmap.org/node/365485771
# 15/9527/11985
# "lock"="'yes'"
assert_has_feature(
    15, 9527, 11985, 'pois',
    {'id': 365485771})

# https://www.openstreetmap.org/node/4469596254
# 15/5626/12731
# "man_made"="adit"
assert_has_feature(
    15, 5626, 12731, 'pois',
    {'id': 4469596254})

# https://www.openstreetmap.org/node/1818064871
# 15/5378/12607
# "man_made"="mineshaft"
assert_has_feature(
    15, 5378, 12607, 'pois',
    {'id': 1818064871})

# originally from 657-natural-man_made.py
# unnamed rock
# node 1328665285
assert_no_matching_feature(
    15, 5293, 12734, 'pois',
    { 'id': 1328665285 })

# https://www.openstreetmap.org/node/4239915448
# 15/7549/13919
# "man_made"="offshore_platform"
assert_has_feature(
    15, 7549, 13919, 'pois',
    {'id': 4239915448})

# originally from 675-man_made-outdoor-landmarks.py
#http://www.openstreetmap.org/way/350328482
assert_no_matching_feature(
    13, 1942, 3395, 'pois',
    { 'id': 350328482 })

# there is only 1 of these in the world!?
# "man_made"="power_wind"

# https://www.openstreetmap.org/node/3310910810
# 15/5334/12510
# "man_made"="telescope"
assert_has_feature(
    15, 5334, 12510, 'pois',
    {'id': 3310910810})

# https://www.openstreetmap.org/node/1050825518
# 15/5178/12346
# "natural"="cave_entrance"
assert_has_feature(
    15, 5178, 12346, 'pois',
    {'id': 1050825518})

# https://www.openstreetmap.org/node/4719786091
# 15/5491/12694
# "natural"="waterfall"
assert_has_feature(
    15, 5491, 12694, 'pois',
    {'id': 4719786091})

# https://www.openstreetmap.org/node/2073000913
# 15/5238/12671
# "public_transport"="platform"
assert_has_feature(
    15, 5238, 12671, 'pois',
    {'id': 2073000913})

# https://www.openstreetmap.org/node/2991866242
# 15/5214/12588
# "public_transport"="stop_area"
assert_has_feature(
    15, 5214, 12588, 'pois',
    {'id': 2991866242})

# https://www.openstreetmap.org/node/2382580308
# 15/9545/12368
# "railway"="halt"
assert_has_feature(
    15, 9545, 12368, 'pois',
    {'id': 2382580308})

# https://www.openstreetmap.org/node/3987143106
# 15/9821/12242
# "railway"="platform"
assert_has_feature(
    15, 9821, 12242, 'pois',
    {'id': 3987143106})

# https://www.openstreetmap.org/node/1130268570
# 15/9381/12527
# "railway"="stop"
assert_has_feature(
    15, 9381, 12527, 'pois',
    {'id': 1130268570})

# originally from 661-historic-transit-stops.py
# public_transport=stop_position
# railway=stop
# http://www.openstreetmap.org/node/3721890342
assert_has_feature(
    13, 1316, 3176, 'pois',
    {'id': 3721890342})

# https://www.openstreetmap.org/node/3833748147
# 15/9367/12536
# "railway"="subway_entrance"
assert_has_feature(
    15, 9367, 12536, 'pois',
    {'id': 3833748147})

# https://www.openstreetmap.org/node/1719012916
# 15/5239/12670
# "railway"="tram_stop"
assert_has_feature(
    15, 5239, 12670, 'pois',
    {'id': 1719012916})

# https://www.openstreetmap.org/node/4665711307
# 15/5235/12667
# "railway=level_crossing" (but make min_zoom 18)
assert_has_feature(
    15, 5235, 12667, 'pois',
    {'id': 4665711307})

# weird one, only 1 node
# "tags->site"="stop_area"

# https://www.openstreetmap.org/node/4696619992
# 15/5362/12461
# "tags->whitewater"="egress"
assert_has_feature(
    15, 5362, 12461, 'pois',
    {'id': 4696619992})

# https://www.openstreetmap.org/node/4253919482
# 15/5387/12481
# "tags->whitewater"="hazard"
assert_has_feature(
    15, 5387, 12481, 'pois',
    {'id': 4253919482})

# https://www.openstreetmap.org/node/3688927027
# 15/5541/12666
# "tags->whitewater"="put_in"
assert_has_feature(
    15, 5541, 12666, 'pois',
    {'id': 3688927027})

# https://www.openstreetmap.org/node/4253919493
# 15/5385/12482
# "tags->whitewater"="rapid"
assert_has_feature(
    15, 5385, 12482, 'pois',
    {'id': 4253919493})

# https://www.openstreetmap.org/node/1076123765
# 15/5433/12607
# "tourism"="alpine_hut"
assert_has_feature(
    15, 5433, 12607, 'pois',
    {'id': 1076123765})

# https://www.openstreetmap.org/node/3065529317
# 15/5236/12667
# "tourism"="viewpoint"
assert_has_feature(
    15, 5236, 12667, 'pois',
    {'id': 3065529317})

# https://www.openstreetmap.org/node/1837443430
# 15/17100/11564
# "tourism"="wilderness_hut"
assert_has_feature(
    15, 17100, 11564, 'pois',
    {'id': 1837443430})

# https://www.openstreetmap.org/node/4319935813
# 15/5449/12526
# "waterway"="waterfall"
assert_has_feature(
    15, 5449, 12526, 'pois',
    {'id': 4319935813})

# originally from 927-normalize-operator-values.py
# information=guidepost
# operator=US Forest Service
# tourism=information
# http://www.openstreetmap.org/node/4216584100
assert_has_feature(
    16, 15995, 25090, 'pois',
    {'id': 4216584100})