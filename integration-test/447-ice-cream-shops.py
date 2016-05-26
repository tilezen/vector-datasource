# New York, NY (amenity=ice_cream)
#https://www.openstreetmap.org/node/2782000317
assert_has_feature(
    18, 77196, 98518, 'pois',
    { 'kind': 'ice_cream' })

# Oakland, CA (shop=ice_cream)
#https://www.openstreetmap.org/node/661742947
assert_has_feature(
    18, 42050, 101257, 'pois',
    { 'kind': 'ice_cream' })
