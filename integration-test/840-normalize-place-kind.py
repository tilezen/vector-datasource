# Node: California (671022)
# http://www.openstreetmap.org/node/671022
test.assert_has_feature(
    16, 11149, 25576, 'places',
    { 'id': 671022, 'kind': 'region', 'kind_detail': 'state' })

# Node: Saga Prefecture (1499608655)
# http://www.openstreetmap.org/node/1499608655
test.assert_has_feature(
    16, 56457, 26350, 'places',
    { 'id': 1499608655, 'kind': 'region', 'kind_detail': 'province' })

# Node: San Francisco (26819236)
# http://www.openstreetmap.org/node/26819236
test.assert_has_feature(
    16, 10482, 25330, 'places',
    { 'id': 26819236, 'kind': 'locality', 'kind_detail': 'city' })


# Node: Daly City (140983265)
# http://www.openstreetmap.org/node/140983265
test.assert_has_feature(
    16, 10474, 25346, 'places',
    { 'id': 140983265, 'kind': 'locality', 'kind_detail': 'town' })

# Node: Broadmoor (140983130)
# http://www.openstreetmap.org/node/140983130
test.assert_has_feature(
    16, 10470, 25350, 'places',
    { 'id': 140983130, 'kind': 'locality', 'kind_detail': 'village' })

# Node: Baden (150937258)
# http://www.openstreetmap.org/node/150937258
test.assert_has_feature(
    16, 10479, 25359, 'places',
    { 'id': 150937258, 'kind': 'locality', 'kind_detail': 'hamlet' })

# Node: McCovey Cove (317091394)
# http://www.openstreetmap.org/node/317091394
test.assert_has_feature(
    16, 10487, 25330, 'places',
    { 'id': 317091394, 'kind': 'locality', 'kind_detail': 'locality' })

# Node: Gilman Ranch (2682626694)
# http://www.openstreetmap.org/node/2682626694
test.assert_has_feature(
    16, 10592, 25477, 'places',
    { 'id': 2682626694, 'kind': 'locality', 'kind_detail': 'isolated_dwelling' })

# Node: Stevens Canyon Ranch (3219761323)
# http://www.openstreetmap.org/node/3219761323
test.assert_has_feature(
    16, 10539, 25446, 'places',
    { 'id': 3219761323, 'kind': 'locality', 'kind_detail': 'farm' })


# ne historic place
test.assert_has_feature(
    16, 38247, 21826, 'places',
    { 'id': int, 'name': 'Chernobyl',
      'kind': 'locality', 'kind_detail': 'hamlet'})

# ne scientific station
test.assert_has_feature(
    16, 22209, 47255, 'places',
    { 'id': int, 'name': 'Elephant Island',
      'kind': 'locality', 'kind_detail': 'scientific_station'})

# ne capitals
test.assert_has_feature(
    7, 109, 49, 'places',
    { 'id': int, 'name': 'Seoul',
      'kind': 'locality', 'country_capital': True})
test.assert_has_feature(
    7, 112, 50, 'places',
    { 'id': int, 'name': 'Kyoto',
      'kind': 'locality', 'country_capital': True})
test.assert_has_feature(
    7, 104, 55, 'places',
    { 'id': int, 'name': 'Hong Kong',
      'kind': 'locality', 'country_capital': True})


# ne state_capitals
test.assert_has_feature(
    7, 117, 76, 'places',
    { 'id': int, 'name': 'Sydney',
      'kind': 'locality', 'region_capital': True})
test.assert_has_feature(
    7, 112, 50, 'places',
    { 'id': int, 'name': 'Osaka',
      'kind': 'locality', 'region_capital': True})

# ne populated place
test.assert_has_feature(
    7, 20, 49, 'places',
    { 'id': int, 'name': 'San Francisco',
      'kind': 'locality', 'region_capital': type(None), 'country_capital': type(None)})
