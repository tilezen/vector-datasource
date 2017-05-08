# San Francisco International
# https://www.openstreetmap.org/way/23718192
test.assert_has_feature(
    13, 1311, 3170, 'pois',
    { 'kind': 'aerodrome',
      'iata': 'SFO' })

# Oakland airport
# https://www.openstreetmap.org/way/54363486
test.assert_has_feature(
    13, 1314, 3167, 'pois',
    { 'kind': 'aerodrome',
      'iata': 'OAK' })
