# http://www.openstreetmap.org/node/2026996113
test.assert_has_feature(
    16, 10485, 25328, 'pois',
    { 'id': 2026996113, 'kind': 'gallery', 'min_zoom': 17 })

# https://www.openstreetmap.org/way/83488820
test.assert_has_feature(
    15, 16370, 10894, 'pois',
    { 'id': 83488820, 'kind': 'gallery' })
