# this garden previously had a min_zoom of 12, but based on its size should be
# z16 instead.
#
# http://www.openstreetmap.org/way/273274870
assert_has_feature(
    16, 32182, 20422, 'landuse',
    { 'kind': 'garden', 'id': 273274870, 'min_zoom': 16, 'tier': 6 })
assert_has_feature(
    16, 32182, 20422, 'pois',
    { 'kind': 'garden', 'id': 273274870, 'min_zoom': 16, 'tier': 6 })
