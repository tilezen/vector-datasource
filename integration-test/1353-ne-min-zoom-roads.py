# note: uses existing fixture from 976-fractional-pois

# the road should be present at zoom 5
test.assert_has_feature(
    5, 9, 12, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'shield_text': '95' })

# but not at zoom 3 or 4
test.assert_no_matching_feature(
    3, 2, 3, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'shield_text': '95' })
test.assert_no_matching_feature(
    4, 4, 6, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'shield_text': '95' })
