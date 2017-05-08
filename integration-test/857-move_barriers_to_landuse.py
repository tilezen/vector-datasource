# update landuse to include barriers features and delete from boundaries

# city_wall in landuse
# http://www.openstreetmap.org/way/81522922
test.assert_has_feature(
    12, 2030, 1300, 'landuse',
    { 'kind': 'city_wall'})

# city_wall not in boundaries
test.assert_no_matching_feature(
    12, 2030, 1300, 'boundaries',
    { 'kind': 'city_wall'})

# citywalls in landuse
# http://www.openstreetmap.org/way/392978585
test.assert_has_feature(
    12, 2326, 1617, 'landuse',
    { 'kind': 'city_wall'})

# citywalls not in boundaries
test.assert_no_matching_feature(
    12, 2326, 1617, 'boundaries',
    { 'kind': 'city_wall'})

# dam in landuse
# http://www.openstreetmap.org/way/109629543
test.assert_has_feature(
    12, 740, 1606, 'landuse',
    { 'kind': 'dam'})

# dam not in boundaries
test.assert_no_matching_feature(
    12, 740, 1606, 'boundaries',
    { 'kind': 'dam'})

# fence in landuse
#http://www.openstreetmap.org/way/345599214
test.assert_has_feature(
    16, 19296, 24635, 'landuse',
    { 'kind': 'fence'})

# fence not in boundaries
test.assert_no_matching_feature(
    16, 19296, 24635, 'boundaries',
    { 'kind': 'fence'})

# retaining_wall in landuse
#http://www.openstreetmap.org/way/288896098
test.assert_has_feature(
    15, 9648, 12315, 'landuse',
    { 'kind': 'retaining_wall'})

# retaining_wall not in boundaries
test.assert_no_matching_feature(
    15, 9648, 12315, 'boundaries',
    { 'kind': 'retaining_wall'})

# snow_fence in landuse
#http://www.openstreetmap.org/way/356771680
test.assert_has_feature(
    15, 6788, 12264, 'landuse',
    { 'kind': 'snow_fence'})

# snow_fence not in boundaries
test.assert_no_matching_feature(
    15, 6788, 12264, 'boundaries',
    { 'kind': 'snow_fence'})
