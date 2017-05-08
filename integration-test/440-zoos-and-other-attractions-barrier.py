# barrier=fence around enclosures
# https://www.openstreetmap.org/way/316623706
test.assert_has_feature(
    16, 11458, 21855, 'landuse',
    { 'kind': 'fence' })
