# ne Admin-0 capital
assert_has_feature(
    3, 6, 3, 'places',
    { 'kind': 'locality', 'name': 'Seoul', 'capital': True})

assert_no_matching_feature(
    3, 6, 3, 'places',
    { 'kind': 'city', 'name': 'Seoul', 'capital': True})

# ne Admin-1 capital
assert_has_feature(
    3, 7, 4, 'places',
    { 'kind': 'locality', 'name': 'Sydney', 'region_capital': True})

assert_no_matching_feature(
    3, 7, 4, 'places',
    { 'kind': 'city', 'name': 'Sydney', 'state_capital': True})

# ne Populated place
assert_has_feature(
    3, 1, 3, 'places',
    { 'kind': 'locality', 'name': 'San Francisco'})

assert_no_matching_feature(
    3, 1, 3, 'places',
    { 'kind': 'city', 'name': 'San Francisco'})

# ne Scientific station
assert_has_feature(
    9, 164, 377, 'places',
    { 'kind': 'locality', 'name': 'Palmer Station', 'kind_detail': 'scientific_station'})
