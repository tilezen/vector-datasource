# Add source info in POIs

# http://www.openstreetmap.org/way/329133245
assert_has_feature(
    12, 2315, 1580, 'roads',
    {'id': 329133245, 'kind': 'minor_road'})

# http://www.openstreetmap.org/relation/4594226
assert_no_matching_feature(
    12, 2315, 1580, 'water',
    {'id': -4594226, 'kind': 'sea'})
