#https://www.openstreetmap.org/way/32947245
assert_has_feature(
    15, 5242, 12663, 'pois',
    { 'kind': 'hotel', 'name': 'Ritz-Carlton' })

#https://www.openstreetmap.org/relation/6480430
assert_has_feature(
    16, 10484, 25327, 'pois',
    { 'kind': 'hotel', 'name': 'Stanford Court San Francisco Hotel' })

#http://www.openstreetmap.org/relation/1358120
assert_has_feature(
    16, 10483, 25323, 'pois',
    { 'kind': 'hotel', 'name': 'Hotel Zephyr' })
