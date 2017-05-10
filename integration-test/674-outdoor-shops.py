#http://www.openstreetmap.org/node/3056897308
test.assert_has_feature(
    16, 11111, 25360, 'pois',
    { 'kind': 'fishing', 'min_zoom': 16 })

#http://www.openstreetmap.org/node/1467729495
test.assert_has_feature(
    16, 10165, 24618, 'pois',
    { 'kind': 'hunting', 'min_zoom': 16 })

#http://www.openstreetmap.org/node/766201791
test.assert_has_feature(
    16, 10179, 24602, 'pois',
    { 'kind': 'outdoor', 'min_zoom': 16 })
    
#http://www.openstreetmap.org/way/35343322
# Smaller Sports Basement store in SF
# This should really be in 16, 10483, 25332, but is in zoom 15 now
test.assert_has_feature(
    15, 5241, 12666, 'pois',
    { 'kind': 'outdoor', 'id': 35343322 })
    
#http://www.openstreetmap.org/way/377630800
# Large Bass Pro building that should appear earlier
test.assert_has_feature(
    15, 6842, 12520, 'pois',
    { 'kind': 'outdoor', 'id': 377630800 })
    
#http://www.openstreetmap.org/way/290195878
# Large REI building that should appear earlier
test.assert_has_feature(
    15, 6207, 12321, 'pois',
    { 'kind': 'outdoor', 'id': 290195878 })

#http://www.openstreetmap.org/node/3931687122
test.assert_has_feature(
    16, 10467, 25309, 'pois',
    { 'kind': 'scuba_diving', 'min_zoom': 17 })

#http://www.openstreetmap.org/node/2135237099
test.assert_has_feature(
    16, 10558, 25443, 'pois',
    { 'kind': 'gas_canister', 'min_zoom': 18 })

#https://www.openstreetmap.org/node/3799971066
test.assert_has_feature(
    16, 10483, 25331, 'pois',
    { 'kind': 'motorcycle', 'min_zoom': 17 })
