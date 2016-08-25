# http://www.openstreetmap.org/way/167274589
# area 300363008
assert_has_feature(
    16, 10818, 21900, 'landuse',
    { 'kind': 'national_park', 'id': 167274589, 'tier': 1,
      'min_zoom': 3 })

# http://www.openstreetmap.org/relation/921675
# area 30089300
assert_has_feature(
    16, 14579, 29651, 'landuse',
    { 'kind': 'national_park', 'id': -921675, 'tier': 1,
      'min_zoom': 8 })
assert_no_matching_feature(
    7, 28, 57, 'landuse',
    { 'kind': 'national_park', 'id': -921675 })

# this is USFS, so demoted to tier 2 :-(
# http://www.openstreetmap.org/way/34416231
# area 86685400
assert_has_feature(
    16, 18270, 25157, 'landuse',
    { 'kind': 'national_park', 'id': 34416231,
      'tier': 2, 'min_zoom': 8 })
