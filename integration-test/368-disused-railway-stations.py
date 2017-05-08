# Old South Ferry (1) (disused=yes)
test.assert_no_matching_feature(
    16, 19294, 24643, 'pois',
    {'kind': 'station', 'id': 2086974744})

# Valle, AZ (disused=station)
test.assert_no_matching_feature(
    16, 12342, 25813, 'pois',
    {'id': 366220389})

# Sadly, we seem to be lacking a disused=no object in
# North America to use for testing.
