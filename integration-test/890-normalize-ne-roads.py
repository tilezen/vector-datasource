# ferry
test.assert_has_feature(
    7, 37, 48, 'roads',
    {'id': int, 'kind': 'ferry', 'type': type(None)})

# expressway
test.assert_has_feature(
    7, 37, 48, 'roads',
    {'id': int, 'kind': 'highway', 'kind_detail': 'motorway', 'type': type(None)})

# major highway
test.assert_has_feature(
    7, 108, 61, 'roads',
    {'id': int, 'kind': 'highway', 'kind_detail': 'trunk'})
# beltway
test.assert_has_feature(
    7, 30, 48, 'roads',
    {'id': int, 'kind': 'highway', 'kind_detail': 'trunk'})
# bypass
test.assert_has_feature(
    7, 34, 50, 'roads',
    {'id': int, 'kind': 'highway', 'kind_detail': 'trunk'})

# secondary highway
test.assert_has_feature(
    7, 28, 47, 'roads',
    {'id': int, 'kind': 'major_road', 'kind_detail': 'primary'})

# road
test.assert_has_feature(
    7, 71, 49, 'roads',
    {'id': int, 'kind': 'major_road', 'kind_detail': 'secondary'})

# track
test.assert_has_feature(
    7, 113, 70, 'roads',
    {'id': int, 'kind': 'minor_road', 'kind_detail': 'tertiary'})
# unknown
test.assert_has_feature(
    7, 107, 52, 'roads',
    {'id': int, 'kind': 'minor_road', 'kind_detail': 'tertiary'})
