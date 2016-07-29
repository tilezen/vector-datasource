# Standardize operator values

# US National Park Service in POIS
# http://www.openstreetmap.org/node/4285104560
assert_has_feature(
    16, 15808, 25720, 'pois',
    {'id': 4285104560, 'operator': 'National Park Service'})

assert_no_matching_feature(
    16, 15808, 25720, 'pois',
    {'id': 4285104560, 'operator': 'US National Park Service'})

# United States National Park Service in landuse
# http://www.openstreetmap.org/way/220076368
assert_has_feature(
    13, 1730, 3194, 'landuse',
    {'id': 220076368, 'operator': 'National Park Service'})

assert_no_matching_feature(
    13, 1730, 3194, 'landuse',
    {'id': 220076368, 'operator': 'United States National Park Service'})

# US National Forest Service in POIS
# http://www.openstreetmap.org/node/4216584100
assert_has_feature(
    16, 15995, 25090, 'pois',
    {'id': 4216584100, 'operator': 'United States Forest Service'})

assert_no_matching_feature(
    16, 15995, 25090, 'pois',
    {'id': 4216584100, 'operator': 'US National Forest Service'})

# National Forest Service in landuse
# http://www.openstreetmap.org/way/260686310
assert_has_feature(
    16, 12331, 25369, 'landuse',
    {'id': 260686310, 'operator': 'United States Forest Service'})

assert_no_matching_feature(
    16, 12331, 25369, 'landuse',
    {'id': 260686310, 'operator': 'National Forest Service'})

# NSW Parks and Wildlife Service in POIs
# http://www.openstreetmap.org/node/2514034066
assert_has_feature(
    16, 59800, 39773, 'pois',
    {'id': 2514034066, 'operator': 'National Parks & Wildife Service NSW'})

assert_no_matching_feature(
    16, 59800, 39773, 'pois',
    {'id': 2514034066, 'operator': 'NSW Parks and Wildlife Service'})

# Department of National Parks NSW in landuse
# http://www.openstreetmap.org/way/429280600
assert_has_feature(
    16, 60128, 39504, 'landuse',
    {'id': 429280600, 'operator': 'National Parks & Wildife Service NSW'})

assert_no_matching_feature(
    16, 60128, 39504, 'landuse',
    {'id': 429280600, 'operator': 'Department of National Parks NSW'})
