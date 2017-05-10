# https://www.openstreetmap.org/way/431358377
test.assert_has_feature(
    16, 55897, 25449, 'buildings',
    { 'id': 431358377, 'kind': 'building', 'kind_detail': 'office' })

# http://www.openstreetmap.org/way/264768910
test.assert_has_feature(
    16, 19298, 24633, 'buildings',
    { 'id': 264768910, 'kind': 'building', 'kind_detail': 'apartments' })

# Way: Forest Hill (136822046)
# http://www.openstreetmap.org/way/136822046
test.assert_has_feature(
    16, 10474, 25337, 'buildings',
    { 'id': 136822046, 'kind': 'building', 'kind_detail': 'transportation' })

# http://www.openstreetmap.org/way/93817368
test.assert_has_feature(
    16, 10487, 25327, 'buildings',
    { 'id': 93817368, 'kind': 'building', 'kind_detail': type(None)})

# http://www.openstreetmap.org/way/132605515
test.assert_has_feature(
    16, 10482, 25331, 'buildings',
    { 'id': 132605515, 'kind': 'building_part', 'kind_detail': type(None) })

# http://www.openstreetmap.org/way/406710839
test.assert_has_feature(
    16, 10486, 25326, 'buildings',
    { 'id': 406710839, 'kind': 'building_part', 'kind_detail': type(None) })

# http://www.openstreetmap.org/way/257920199
test.assert_has_feature(
    16, 18743, 25070, 'buildings',
    { 'id': 257920199, 'kind': 'building_part', 'kind_detail': 'steps' })

# http://www.openstreetmap.org/way/352508405
test.assert_has_feature(
    16, 29704, 27412, 'buildings',
    { 'id': 352508405, 'kind': 'building_part', 'kind_detail': 'steps' })
