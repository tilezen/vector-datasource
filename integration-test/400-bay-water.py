# San Pablo Bay
# https://www.openstreetmap.org/way/43950409
assert_has_feature(
    14, 2623, 6318, 'water',
    { 'kind': 'bay', 'label_placement': True })

# Sansum Narrows
# https://www.openstreetmap.org/relation/1019862
assert_has_feature(
    11, 321, 705, 'water',
    { 'kind': 'strait', 'label_placement': True })

# Horsens Fjord
# https://www.openstreetmap.org/relation/1451065
assert_has_feature(
    14, 8645, 5114, 'water',
    { 'kind': 'fjord', 'label_placement': True })
