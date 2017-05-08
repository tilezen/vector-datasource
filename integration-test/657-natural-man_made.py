# http://www.openstreetmap.org/node/4305375025
test.assert_has_feature(
    15, 10394, 19077, 'pois',
    { 'kind': 'mineshaft' })

# node 369156437
test.assert_has_feature(
    16, 11932, 25298, 'pois',
    { 'kind': 'adit' })

# node 2794798164
test.assert_has_feature(
    16, 10549, 25431, 'pois',
    { 'kind': 'water_well', 'min_zoom': 17 })

# node 966585438
test.assert_has_feature(
    14, 2764, 6333, 'pois',
    { 'kind': 'saddle' })

# node 358832354
test.assert_has_feature(
    15, 5224, 12570, 'pois',
    { 'kind': 'geyser' })

# node 4020311689
test.assert_has_feature(
    16, 10805, 25827, 'pois',
    { 'kind': 'hot_spring' })

# http://www.openstreetmap.org/node/1804644217
test.assert_has_feature(
    16, 27431, 36586, 'pois',
    { 'kind': 'rock', 'min_zoom': 17 })
