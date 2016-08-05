# ne state capitals
assert_has_feature(
    9, 83, 196, 'places',
    { 'id': 6779, 'kind': 'locality', 'name': 'Sacramento', 'region_capital': True})

assert_no_matching_feature(
    9, 83, 196, 'places',
    { 'id': 6779, 'kind': 'city', 'name': 'Sacramento', 'region_capital': True})

# ne country capitals
assert_has_feature(
    9, 289, 197, 'places',
    { 'id': 7252, 'kind': 'locality'})

assert_no_matching_feature(
    9, 289, 197, 'places',
    { 'id': 7252, 'kind': 'city'})

# ne populated place
assert_has_feature(
    8, 41, 98, 'places',
    { 'id': 608, 'kind': 'locality'})

assert_no_matching_feature(
    8, 41, 98, 'places',
    { 'id': 608, 'kind': 'city'})

# ne Scientific station
assert_has_feature(
    7, 41, 94, 'places',
    { 'id': 4825, 'kind': 'locality', 'kind_detail': 'scientific_station'})
