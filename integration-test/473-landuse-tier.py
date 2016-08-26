# http://www.openstreetmap.org/way/167274589
# area 300363008
assert_has_feature(
    16, 10818, 21900, 'landuse',
    { 'kind': 'national_park', 'id': 167274589, 'tier': 1,
      'min_zoom': 3 })
# POI should be visible at zoom 6, although polygon is at 3
# NOTE: when https://github.com/tilezen/vector-datasource/pull/989
# gets merged, this should be 6, until then we need to use 7.
#assert_has_feature(
#    6, 10, 21, 'pois',
#    { 'kind': 'national_park', 'id': 167274589, 'tier': 1,
#      'min_zoom': 6.67 })
assert_has_feature(
    7, 21, 42, 'pois',
    { 'kind': 'national_park', 'id': 167274589, 'tier': 1,
      'min_zoom': 6.67493 })

# http://www.openstreetmap.org/relation/921675
# area 30089300
assert_has_feature(
    16, 14579, 29651, 'landuse',
    { 'kind': 'national_park', 'id': -921675, 'tier': 1,
      'min_zoom': 8 })
assert_no_matching_feature(
    7, 28, 57, 'landuse',
    { 'kind': 'national_park', 'id': -921675 })
# POI should be visible at zoom 6, although polygon is at 3
# NOTE: when https://github.com/tilezen/vector-datasource/pull/989
# gets merged, this should be 6, until then we need to use 7.
#assert_has_feature(
#    8, 56, 115, 'pois',
#    { 'kind': 'national_park', 'id': -921675, 'tier': 1,
#      'min_zoom': 8.33 })
assert_has_feature(
    9, 113, 231, 'pois',
    { 'kind': 'national_park', 'id': -921675, 'tier': 1,
      'min_zoom': 8.33463 })

# this is USFS, so demoted to tier 2 :-(
# http://www.openstreetmap.org/way/34416231
# area 86685400
assert_has_feature(
    16, 18270, 25157, 'landuse',
    { 'kind': 'national_park', 'id': 34416231,
      'tier': 2, 'min_zoom': 8 })
# this one is clipped by the polygon min_zoom, and so appears at the same
# level.
assert_has_feature(
    8, 71, 98, 'pois',
    { 'kind': 'national_park', 'id': 34416231,
      'tier': 2, 'min_zoom': 8 })
