# http://www.openstreetmap.org/way/167274589
# area 300363008
assert_has_feature(
    4, 2, 5, 'landuse',
    { 'kind': 'national_park', 'id': 167274589, 'tier': 1,
      'min_zoom': 3 })
assert_has_feature(
    6, 10, 21, 'pois',
    { 'kind': 'national_park', 'id': 167274589, 'tier': 1,
      'min_zoom': 6.67 })

# http://www.openstreetmap.org/relation/921675
# area 30089300
assert_has_feature(
    8, 56, 115, 'landuse',
    { 'kind': 'national_park', 'id': -921675, 'tier': 1,
      'min_zoom': 8 })
assert_no_matching_feature(
    7, 28, 57, 'landuse',
    { 'kind': 'national_park', 'id': -921675 })
assert_has_feature(
    8, 56, 115, 'pois',
    { 'kind': 'national_park', 'id': -921675, 'tier': 1,
      'min_zoom': 8.33 })

# this is USFS, so demoted to tier 2 :-(
# http://www.openstreetmap.org/way/34416231
# area 86685400
assert_has_feature(
    8, 71, 98, 'landuse',
    { 'kind': 'national_park', 'id': 34416231,
      'tier': 2, 'min_zoom': 8 })
# this one is clipped by the polygon min_zoom, and so appears at the same
# level.
assert_has_feature(
    8, 71, 98, 'pois',
    { 'kind': 'national_park', 'id': 34416231,
      'tier': 2, 'min_zoom': 8 })
