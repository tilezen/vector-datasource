# https://www.openstreetmap.org/node/1426311638
test.assert_has_feature(
    16, 19298, 24629, 'pois',
    { 'id': 1426311638, 'kind': 'restaurant', 'kind_detail': 'seafood' })

# https://www.openstreetmap.org/way/280288213
test.assert_has_feature(
    16, 19319, 24634, 'pois',
    { 'id': 280288213, 'kind': 'restaurant', 'kind_detail': 'japanese' })

# https://www.openstreetmap.org/node/4305351592
test.assert_has_feature(
    16, 19336, 24608, 'pois',
    { 'id': 4305351592, 'kind': 'pitch', 'kind_detail': 'baseball' })

# https://www.openstreetmap.org/way/326894220
test.assert_has_feature(
    16, 19321, 24634, 'pois',
    { 'id': 326894220, 'kind': 'pitch', 'kind_detail': 'basketball' })

