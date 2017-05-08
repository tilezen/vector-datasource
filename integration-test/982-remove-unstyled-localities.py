# zoom 8:
# include only those localities with name and population and kind_detail IN
# (city, town).
# example: Arcata https://www.openstreetmap.org/node/141029389 with population.
test.assert_has_feature(
    8, 39, 96, 'places',
    { 'kind': 'locality', 'kind_detail': 'town', 'name': 'Arcata',
      'id': 141029389, 'min_zoom': 8 })

# zoom 9 and 10:
# include only those localities with name and kind_detail IN (city, town)
# This drops the population requirement (cities or towns without population are
# drawn but with smaller type size) .
# example: Hoopa http://www.openstreetmap.org/node/4270230299 has no population,
# is included starting at zoom 9.
test.assert_no_matching_feature(
    8, 40, 95, 'places',
    { 'kind': 'locality', 'id': 4270230299 })
test.assert_has_feature(
    9, 80, 191, 'places',
    { 'kind': 'locality', 'kind_detail': 'town', 'name': 'Hoopa',
      'id': 4270230299, 'min_zoom': 9 })

# zoom 11:
# include only those localities with name and kind_detail IN (city, town)
# This drops the population requirement (cities or towns without population are
# drawn but with smaller type size) .
# include only those localities with name and population and kind_detail IN
# (village).
# example: Fairfax http://www.openstreetmap.org/node/150949805 is village with
# population
test.assert_no_matching_feature(
    10, 163, 395, 'places',
    { 'kind': 'locality', 'id': 150949805 })
test.assert_has_feature(
    11, 326, 790, 'places',
    { 'kind': 'locality', 'kind_detail': 'village', 'name': 'Fairfax',
      'id': 150949805, 'min_zoom': 11 })

# zoom 12:
# include only those localities with name and kind_detail IN (city, town,
# village)
# This drops the population requirement (cities, towns, and villages without
# population are drawn but with smaller type size) .
# village with no population is Soquel 150933732 that is suddenly visible
# include only those localities with name and population and kind_detail IN
# (hamlet).
# example: http://www.openstreetmap.org/node/150966610 - Duncans Mills, is
# a hamlet with population.
test.assert_no_matching_feature(
    11, 323, 786, 'places',
    { 'kind': 'locality', 'id': 150966610 })
test.assert_has_feature(
    12, 647, 1573, 'places',
    { 'kind': 'locality', 'kind_detail': 'hamlet', 'name': 'Duncans Mills',
      'id': 150966610, 'min_zoom': 12 })

# example: http://www.openstreetmap.org/node/150973394 - Inverness
# hamlet with NO population should NOT show up
test.assert_no_matching_feature(
    12, 650, 1578, 'places',
    { 'kind': 'locality', 'id': 150973394 })

# zoom 13+:
# include only those localities with name and any kind IN (locality)
# This drops the population requirement (cities, towns, and all the other
# kind_details without population are drawn but with smaller type size) .
# example: Inverness 150973394 hamlet with no population should now show up
test.assert_has_feature(
    13, 1300, 3156, 'places',
    { 'kind': 'locality', 'kind_detail': 'hamlet', 'name': 'Inverness',
      'id': 150973394, 'min_zoom': 13 })
