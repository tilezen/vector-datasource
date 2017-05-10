# all these places are in the south bay, near SF, CA.
# Foster City  http://www.openstreetmap.org/relation/2835016
# San Mateo    http://www.openstreetmap.org/relation/2835017
# Belmont      http://www.openstreetmap.org/node/150967056
# San Carlos   http://www.openstreetmap.org/node/150975918
# Redwood City http://www.openstreetmap.org/node/150946345
# Menlo Park   http://www.openstreetmap.org/node/150981209
test.assert_has_feature(
    11, 328, 793, 'places',
    { 'kind': 'locality',
      'kind_detail': {'city', 'town'},
      'population': int })

# Sacramento, CA http://www.openstreetmap.org/node/150959789
test.assert_has_feature(
    8, 41, 98, 'places',
    { 'kind': 'locality', 'kind_detail': 'city', 'region_capital': True,
      'population': int })
