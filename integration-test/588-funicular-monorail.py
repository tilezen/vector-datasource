# https://www.openstreetmap.org/relation/6043603
test.assert_has_feature(
    16, 10486, 25367, 'transit',
    { 'kind': 'monorail' })

# https://www.openstreetmap.org/relation/6060405
test.assert_has_feature(
    16, 18201, 24705, 'transit',
    { 'kind': 'funicular' })
