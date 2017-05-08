# mz_is_building is an internal tag and shouldn't be present on any output
# feature.
test.assert_no_matching_feature(
    12, 653, 1582, 'buildings',
    { 'mz_is_building': None })

test.assert_no_matching_feature(
    12, 653, 1582, 'landuse',
    { 'mz_is_building': None })
