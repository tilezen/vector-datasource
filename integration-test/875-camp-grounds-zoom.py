# update landuse to include campground features and fix label zoom

# large campground in landuse zoom 16
# http://www.openstreetmap.org/way/431725967
assert_has_feature(
    16, 10959, 25337, 'landuse',
    { 'kind': 'camp_site'})

# large campground in point zoom 16
# http://www.openstreetmap.org/way/431725967
assert_has_feature(
    16, 10959, 25337, 'pois',
    { 'kind': 'camp_site'})

# large campground in landuse zoom 13
# http://www.openstreetmap.org/way/431725967
assert_has_feature(
    13, 1369, 3167, 'landuse',
    { 'kind': 'camp_site'})

# large campground in point zoom 13
# http://www.openstreetmap.org/way/431725967
assert_has_feature(
    13, 1369, 3167, 'pois',
    { 'kind': 'camp_site'})

# small campground in landuse zoom 16
# http://www.openstreetmap.org/way/417405356
assert_has_feature(
    16, 10471, 25326, 'landuse',
    { 'kind': 'camp_site'})

# small campground in point zoom 16
# http://www.openstreetmap.org/way/417405356
assert_has_feature(
    16, 10471, 25326, 'pois',
    { 'kind': 'camp_site'})

# small campground in landuse zoom 13
# http://www.openstreetmap.org/way/417405356
assert_has_feature(
    13, 1308, 3165, 'landuse',
    { 'kind': 'camp_site'})

# small campground in point zoom 13
# http://www.openstreetmap.org/way/417405356
assert_no_matching_feature(
    13, 1308, 3165, 'pois',
    { 'kind': 'camp_site'})
