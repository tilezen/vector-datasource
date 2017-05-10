# update kind to read urban_areas instead of urban areas.

# This is not an OSM feature it comes from Natural Earth
test.assert_has_feature(
    4, 2, 6, 'landuse',
    {'kind': 'urban_area'})
test.assert_no_matching_feature(
    4, 2, 6, 'landuse',
    {'kind': 'urban area'})

test.assert_has_feature(
    7, 20, 49, 'landuse',
    {'kind': 'urban_area'})
test.assert_no_matching_feature(
    7, 20, 49, 'landuse',
    {'kind': 'urban area'})

test.assert_has_feature(
    9, 81, 197, 'landuse',
    {'kind': 'urban_area'})
test.assert_no_matching_feature(
    9, 81, 197, 'landuse',
    {'kind': 'urban area'})