#https://www.openstreetmap.org/way/32947245
assert_has_feature(
    15, 5242, 12663, 'pois',
    { 'kind': 'hotel', 'name': 'Ritz-Carlton' })

#https://www.openstreetmap.org/relation/3827943
assert_has_feature(
    16, 10484, 25327, 'pois',
    { 'kind': 'hotel', 'name': 'The Stanford Court Renaissance' })
