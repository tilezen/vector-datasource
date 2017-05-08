# New York, NY (amenity=ice_cream)
#https://www.openstreetmap.org/node/2782000317
test.assert_has_feature(
    16, 19299, 24629, 'pois',
    { 'kind': 'ice_cream' })

# Oakland, CA (shop=ice_cream)
#https://www.openstreetmap.org/node/661742947
test.assert_has_feature(
    16, 10512, 25314, 'pois',
    { 'kind': 'ice_cream' })
