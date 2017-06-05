## Cartoon Art Museum (closed)
# https://www.openstreetmap.org/node/368173967

# POI shouldn't be visible early
test.assert_no_matching_feature(
    15, 5242, 12664, 'pois',
    {'id': 368173967})

# but POI should be present at z17 and marked as closed
test.assert_has_feature(
    16, 10485, 25328, 'pois',
    {'id': 368173967, 'kind': 'closed', 'min_zoom': 17})
