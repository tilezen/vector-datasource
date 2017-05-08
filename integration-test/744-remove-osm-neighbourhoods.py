# Node: Mount Pocono (158473043)
# http://www.openstreetmap.org/node/158473043
test.assert_no_matching_feature(
    16, 19048, 24541, 'places',
    { 'kind': 'borough', 'source': 'openstreetmap.org' })

# Node: Centerville District (150939391)
# http://www.openstreetmap.org/node/150939391
test.assert_no_matching_feature(
    16, 10558, 25381, 'places',
    { 'kind': 'suburb', 'source': 'openstreetmap.org' })

# Node: Northeast (2790349074)
# http://www.openstreetmap.org/node/2790349074
test.assert_no_matching_feature(
    16, 18754, 25065, 'places',
    { 'kind': 'quarter', 'source': 'openstreetmap.org' })
