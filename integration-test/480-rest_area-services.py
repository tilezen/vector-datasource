# node: Tiffin River
# http://www.openstreetmap.org/node/200412620
test.assert_has_feature(
    16, 17401, 24424, 'pois',
    { 'kind': 'service_area', 'id': 200412620, 'min_zoom': 11 })

# http://www.openstreetmap.org/node/159773030
test.assert_has_feature(
    16, 18798, 24573, 'pois',
    { 'kind': 'rest_area', 'id': 159773030, 'min_zoom': 11 })

# Way: Crystal Springs Rest Area (97057565)
# http://www.openstreetmap.org/way/97057565
test.assert_has_feature(
    16, 10492, 25385, 'landuse',
    { 'kind': 'rest_area', 'id': 97057565, 'sort_rank': 41 })

# Way: Nicole Driveway (274732386)
# http://www.openstreetmap.org/way/274732386
test.assert_has_feature(
    16, 10900, 25256, 'landuse',
    { 'kind': 'service_area', 'id': 274732386, 'sort_rank': 42 })
