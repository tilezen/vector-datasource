# ne Admin-0 capital
test.assert_has_feature(
    3, 6, 3, 'places',
    { 'kind': 'locality', 'name': 'Seoul', 'country_capital': True})

test.assert_no_matching_feature(
    3, 6, 3, 'places',
    { 'kind': 'city', 'name': 'Seoul', 'country_capital': True})

# ne Admin-1 capital
test.assert_has_feature(
    3, 7, 4, 'places',
    { 'kind': 'locality', 'name': 'Sydney', 'region_capital': True})

test.assert_no_matching_feature(
    3, 7, 4, 'places',
    { 'kind': 'city', 'name': 'Sydney', 'state_capital': True})

# ne Populated place
test.assert_has_feature(
    3, 1, 3, 'places',
    { 'kind': 'locality', 'name': 'San Francisco'})

test.assert_no_matching_feature(
    3, 1, 3, 'places',
    { 'kind': 'city', 'name': 'San Francisco'})

# ne Scientific station
test.assert_has_feature(
    9, 164, 377, 'places',
    { 'kind': 'locality', 'name': 'Palmer Station', 'kind_detail': 'scientific_station'})

# http://www.openstreetmap.org/node/158368533
# Washington (158368533)
# no region_capital false
test.assert_has_feature(
    8, 73, 97, 'places',
    { 'id': 158368533, 'region_capital': type(None) })

# http://www.openstreetmap.org/node/3441540432
# Node: Deerfield, Nova Scotia (3441540432)
# no country_capital when falsey
test.assert_has_feature(
    16, 20752, 23846, 'places',
    { 'id': 3441540432, 'country_capital': type(None) })
