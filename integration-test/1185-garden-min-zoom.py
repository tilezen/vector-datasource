# this garden previously had a min_zoom of 12, but based on its size should be
# z16 instead.
#
# http://www.openstreetmap.org/way/273274870
test.assert_has_feature(
    16, 32182, 20422, 'landuse',
    { 'kind': 'garden', 'id': 273274870, 'min_zoom': 16, 'tier': 6 })
# shouldn't be a POI now as it has no name.
test.assert_no_matching_feature(
    16, 32182, 20422, 'pois',
    { 'kind': 'garden' })

# instead, here's a small, named garden
# http://www.openstreetmap.org/way/162235630
test.assert_has_feature(
    16, 19303, 24647, 'pois',
    { 'kind': 'garden', 'id': 162235630, 'min_zoom': 16, 'tier': 6 })
