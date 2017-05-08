#https://www.openstreetmap.org/way/32947245
test.assert_has_feature(
    15, 5242, 12663, 'pois',
    { 'kind': 'hotel', 'name': 'Ritz-Carlton' })

#http://www.openstreetmap.org/relation/1358120
test.assert_has_feature(
    16, 10483, 25323, 'pois',
    { 'kind': 'hotel', 'name': 'Hotel Zephyr' })
