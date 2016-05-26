# Old South Ferry (1) (disused=yes)
assert_no_matching_feature(
    19, 154354, 197144, 'pois',
    {'kind': 'station', 'id': 2086974744})

# Valle, AZ (disused=station)
assert_no_matching_feature(
    19, 98740, 206504, 'pois',
    {'id': 366220389})

# Sadly, we seem to be lacking a disused=no object in
# North America to use for testing.
