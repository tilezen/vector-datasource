# ne Admin-0 capital
assert_has_feature(
    3, 6, 3, 'places',
    { 'id': 7242, 'kind': 'locality', 'name': 'Seoul', 'capital': True})

assert_no_matching_feature(
    3, 6, 3, 'places',
    { 'id': 7242, 'kind': 'city', 'name': 'Seoul', 'capital': True})

# ne Admin-1 capital
assert_has_feature(
    3, 7, 4, 'places',
    { 'id': 7287, 'kind': 'locality', 'name': 'Sydney', 'region_capital': True})

assert_no_matching_feature(
    3, 7, 4, 'places',
    { 'id': 7287, 'kind': 'city', 'name': 'Sydney', 'region_capital': True})

# ne Populated place
assert_has_feature(
    3, 1, 3, 'places',
    { 'id': 7223, 'kind': 'locality', 'name': 'San Francisco'})

assert_no_matching_feature(
    3, 1, 3, 'places',
    { 'id': 7223, 'kind': 'city', 'name': 'San Francisco'})

# ne Scientific station
assert_has_feature(
    7, 44, 91, 'places',
    { 'id': 4831, 'kind': 'locality', 'kind_detail': 'scientific_station'})
