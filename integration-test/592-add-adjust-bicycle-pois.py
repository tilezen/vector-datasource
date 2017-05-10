# http://www.openstreetmap.org/node/414269441
# Valencia Cyclery in SF
test.assert_has_feature(
    15, 5240, 12667, 'pois',
    { 'kind': 'bicycle', 'min_zoom': 15 })

# http://www.openstreetmap.org/node/3801412161
# San Francisco Bicycle Rentals
test.assert_has_feature(
    16, 10476, 25332, 'pois',
    { 'kind': 'bicycle_rental', 'min_zoom': 16 })

# http://www.openstreetmap.org/node/3708656264
# Citi Bike - Broadway & W 24 St, with network, operator
test.assert_has_feature(
    16, 19298, 24633, 'pois',
    { 'kind': 'bicycle_rental_station', 'min_zoom': 17,
      'capacity': 52, 'network': 'Citi Bike', 'operator': 'NYC Bike Share' })

# http://www.openstreetmap.org/node/1960994139
# Alta Bike Share, Chattanooga, with network, operator, ref, capacity.
test.assert_has_feature(
    16, 17238, 25950, 'pois',
    { 'kind': 'bicycle_rental_station', 'min_zoom': 17,
      'capacity': 19, 'network': 'Bike Chattanooga',
      'operator': 'Alta Bike Share', 'ref': '5' })

# http://www.openstreetmap.org/node/1993249660
# Cycle barrier in Berkeley
test.assert_has_feature(
    16, 10512, 25310, 'pois',
    { 'kind': 'cycle_barrier', 'min_zoom': 18 })



# WARNING: this kind of feature is only available in Europe
# http://www.openstreetmap.org/node/3836406372
# icn_ref=1
test.assert_has_feature(
    16, 32382, 22860, 'pois',
    { 'kind': 'bicycle_junction', 'min_zoom': 16, 'ref': '1',
      'bicycle_network': 'icn' })

# No known examples in the world for nodes, and ways don't count
# ncn_ref=1

# WARNING: this kind of feature is only available in Europe
# http://www.openstreetmap.org/node/340159623
# rcn_ref=1
test.assert_has_feature(
    16, 33322, 21990, 'pois',
    { 'kind': 'bicycle_junction', 'min_zoom': 16, 'ref': '1',
      'bicycle_network': 'rcn' })

# NOTE: this is strangely in Omaha, NE, USA
# http://www.openstreetmap.org/node/3269815503
# lcn_ref=1
test.assert_has_feature(
    16, 15299, 24506, 'pois',
    { 'kind': 'bicycle_junction', 'min_zoom': 16, 'ref': '1',
      'bicycle_network': 'lcn' })

# http://www.openstreetmap.org/node/287609621
# lcn_ref=2
#    16, 32570, 21059, 'pois',
test.assert_has_feature(
    16, 32570, 21058, 'pois',
    { 'kind': 'bicycle_junction', 'min_zoom': 16, 'ref': '2',
      'bicycle_network': 'lcn' })


# No known examples in the world for nodes, and ways don't count
# iwn_ref=1

# No known examples in the world for nodes, and ways don't count
# nwn_ref=1

# WARNING: this kind of feature is only available in Europe
# http://www.openstreetmap.org/node/300403808
# rwn_ref=1
test.assert_has_feature(
    16, 33492, 21929, 'pois',
    { 'kind': 'walking_junction', 'min_zoom': 16, 'ref': '1',
      'walking_network': 'rwn' })

# WARNING: this kind of feature is only available in Europe
# http://www.openstreetmap.org/node/717593380
# lwn_ref=1
test.assert_has_feature(
    16, 34584, 21219, 'pois',
    { 'kind': 'walking_junction', 'min_zoom': 16, 'ref': 'ST',
      'walking_network': 'lwn' })


#http://www.openstreetmap.org/node/3161454672
# bicycle parking with capacity, covered & fee
test.assert_has_feature(
    16, 12378, 26258, 'pois',
    { 'kind': 'bicycle_parking',
      'capacity': 10, 'covered': True, 'fee': False })

#http://www.openstreetmap.org/node/1618586234
# bicycle parking with access, capacity, covered, fee & operator
test.assert_has_feature(
    16, 10413, 22135, 'pois',
    { 'kind': 'bicycle_parking',
      'capacity': 100, 'covered': True, 'fee': False, 'access': 'customers',
      'operator': 'Pemberton Gateway Village Suites' })

# WARNING - EXAMPLE IS IN EUROPE
#http://www.openstreetmap.org/node/1154262723
# bicycle parking with capacity, covered, fee, maxstay, operator
test.assert_has_feature(
    16, 31627, 21244, 'pois',
    { 'kind': 'bicycle_parking',
      'capacity': 200, 'covered': True, 'fee': False, 'maxstay': '2 days',
      'operator': 'Dublin City Council' })

# WARNING - EXAMPLE IS IN EUROPE
#http://www.openstreetmap.org/node/1116224894
# bicycle parking with capacity and cyclestreets ID.
test.assert_has_feature(
    16, 32745, 21789, 'pois',
    { 'kind': 'bicycle_parking',
      'capacity': 4, 'cyclestreets_id': '27815' })

#http://www.openstreetmap.org/node/2921238315
# bicycle parking with access, capacity, covered, operator and surveillance
test.assert_has_feature(
    16, 17087, 24822, 'pois',
    { 'kind': 'bicycle_parking',
      'access': 'public', 'capacity': 10, 'covered': True,
      'operator': 'City of Carmel', 'surveillance': True })
