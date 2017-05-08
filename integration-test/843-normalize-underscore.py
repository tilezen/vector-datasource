# http://www.openstreetmap.org/way/219071307
test.assert_has_feature(
    16, 10478, 25338, 'roads',
    { 'id': 219071307, 'kind': 'minor_road', 'service': 'drive_through' })

# http://www.openstreetmap.org/way/258020271
test.assert_has_feature(
    16, 11077, 25458, 'roads',
    { 'id': 258020271, 'kind': 'aerialway', 'kind_detail': 't_bar' })

# http://www.openstreetmap.org/way/256717307
test.assert_has_feature(
    16, 18763, 24784, 'roads',
    { 'id': 256717307, 'kind': 'aerialway', 'kind_detail': 'j_bar' })

# http://www.openstreetmap.org/way/232074914
test.assert_has_feature(
    16, 13304, 24998, 'roads',
    { 'id': 232074914, 'kind': 'aerialway', 'kind_detail': type(None) })
