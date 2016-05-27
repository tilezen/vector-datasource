#http://www.openstreetmap.org/way/107817218
# Arizona Canal Diversion Channel (ACDC) 
assert_has_feature(
    16, 12353, 26272, 'water',
    { 'kind': 'river', 'intermittent': True })

#http://www.openstreetmap.org/way/96528126
# 10th Street Wash
assert_has_feature(
    16, 12368, 26272, 'water',
    { 'kind': 'drain', 'intermittent': True })

#http://www.openstreetmap.org/way/61954975
# Unnamed drain
assert_has_feature(
    16, 12372, 26272, 'water',
    { 'kind': 'drain', 'intermittent': True })

#http://www.openstreetmap.org/way/321690441
# Unnamed stream
assert_has_feature(
    16, 12492, 26279, 'water',
    { 'kind': 'stream', 'intermittent': True })

#http://www.openstreetmap.org/way/68709904
# Unnamed water (lake)
assert_has_feature(
    16, 12349, 26257, 'water',
    { 'kind': 'water', 'intermittent': True })
