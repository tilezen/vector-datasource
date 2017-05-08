# NE data - no OSM elements
# boundary between NV and CA is _also_ a "statistical" boundary
test.assert_has_feature(
    7, 21, 49, 'boundaries',
    { 'kind': 'region' })

# boundary between MT and ND is _also_ a "statistical meta" boundary
test.assert_has_feature(
    7, 27, 44, 'boundaries',
    { 'kind': 'region' })
