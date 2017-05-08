# Standardize operator values

# US National Park Service in POIS
# http://www.openstreetmap.org/node/4285104560
test.assert_has_feature(
    16, 15808, 25720, 'pois',
    {'id': 4285104560, 'operator': 'United States National Park Service'})

test.assert_no_matching_feature(
    16, 15808, 25720, 'pois',
    {'id': 4285104560, 'operator': 'US National Park Service'})

# National Park Service in landuse
# http://www.openstreetmap.org/way/368766687
test.assert_has_feature(
    16, 13163, 25153, 'landuse',
    {'id': 368766687, 'operator': 'United States National Park Service'})

test.assert_no_matching_feature(
    16, 13163, 25153, 'landuse',
    {'id': 368766687, 'operator': 'National Park Service'})

# US National Forest Service in POIS
# http://www.openstreetmap.org/node/796692690
test.assert_has_feature(
    16, 10542, 23271, 'pois',
    {'id': 796692690, 'operator': 'United States Forest Service'})

test.assert_no_matching_feature(
    16, 10542, 23271, 'pois',
    {'id': 796692690, 'operator': 'US National Forest Service'})

# US Forest Service in landuse
# http://www.openstreetmap.org/way/432302983
test.assert_has_feature(
    16, 11252, 25432, 'landuse',
    {'id': 432302983, 'operator': 'United States Forest Service'})

test.assert_no_matching_feature(
    16, 11252, 25432, 'landuse',
    {'id': 432302983, 'operator': 'US Forest Service'})

# NSW Parks and Wildlife Service in POIs
# http://www.openstreetmap.org/node/2514034066
test.assert_has_feature(
    16, 59800, 39773, 'pois',
    {'id': 2514034066, 'operator': 'National Parks & Wildife Service NSW'})

test.assert_no_matching_feature(
    16, 59800, 39773, 'pois',
    {'id': 2514034066, 'operator': 'NSW Parks and Wildlife Service'})

# Department of National Parks NSW in landuse
# http://www.openstreetmap.org/way/429280600
test.assert_has_feature(
    16, 60128, 39504, 'landuse',
    {'id': 429280600, 'operator': 'National Parks & Wildife Service NSW'})

test.assert_no_matching_feature(
    16, 60128, 39504, 'landuse',
    {'id': 429280600, 'operator': 'Department of National Parks NSW'})
