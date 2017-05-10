## Best buy (closed)
# https://www.openstreetmap.org/way/241643507

# building should be present at z15
test.assert_has_feature(
    15, 5232, 12654, 'buildings',
    {'id': 241643507, 'kind': 'building', 'kind_detail': 'retail'})

# but POI shouldn't
test.assert_no_matching_feature(
    15, 5232, 12654, 'pois',
    {'id': 241643507})

# but POI should be present at z17 and marked as closed
test.assert_has_feature(
    16, 10465, 25308, 'pois',
    {'id': 241643507, 'kind': 'closed', 'min_zoom': 17})
