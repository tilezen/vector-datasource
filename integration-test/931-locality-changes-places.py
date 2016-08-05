# ne state capitals
assert_has_feature(
    9, 83, 196, 'places',
    { 'id': int, 'kind': 'locality'})

assert_no_matching_feature(
    9, 83, 196, 'places',
    { 'id': int, 'kind': 'city'})

assert_has_feature(
    9, 83, 196, 'places',
    { 'id': int, 'name': 'Sacramento', 'region_capital': True})

assert_no_matching_feature(
    9, 83, 196, 'places',
    { 'id': int, 'name': 'Sacramento', 'state_capital': True})

# ne country capitals
assert_has_feature(
    9, 289, 197, 'places',
    { 'id': int, 'kind': 'locality'})

assert_no_matching_feature(
    9, 289, 197, 'places',
    { 'id': int, 'kind': 'city'})

# ne populated place
assert_has_feature(
    8, 41, 98, 'places',
    { 'id': int, 'kind': 'locality'})

assert_no_matching_feature(
    8, 41, 98, 'places',
    { 'id': int, 'kind': 'city'})

# ne Scientific station
assert_has_feature(
    7, 41, 94, 'places',
    { 'id': int, 'kind': 'locality', 'kind_detail': 'scientific_station'})
