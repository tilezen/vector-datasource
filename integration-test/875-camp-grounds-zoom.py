# update landuse to include campground features and fix label zoom

# large campground in landuse zoom 16
# http://www.openstreetmap.org/way/237314510
test.assert_has_feature(
    16, 10599, 25679, 'landuse',
    { 'kind': 'camp_site', 'sort_rank': 92})

# large campground in point zoom 16
# http://www.openstreetmap.org/way/237314510
test.assert_has_feature(
    16, 10599, 25679, 'pois',
    { 'kind': 'camp_site'})

# large campground in landuse zoom 13
# http://www.openstreetmap.org/way/237314510
test.assert_has_feature(
    13, 1324, 3209, 'landuse',
    { 'kind': 'camp_site', 'sort_rank': 92})

# large campground in point zoom 13
# http://www.openstreetmap.org/way/237314510
test.assert_has_feature(
    13, 1324, 3209, 'pois',
    { 'kind': 'camp_site'})

# small campground in landuse zoom 16
# http://www.openstreetmap.org/way/417405356
test.assert_has_feature(
    16, 10471, 25326, 'landuse',
    { 'kind': 'camp_site', 'sort_rank': 92})

# small campground in point zoom 16
# http://www.openstreetmap.org/way/417405356
test.assert_has_feature(
    16, 10471, 25326, 'pois',
    { 'kind': 'camp_site'})

# small campground in landuse zoom 13
# http://www.openstreetmap.org/way/417405356
test.assert_has_feature(
    13, 1308, 3165, 'landuse',
    { 'kind': 'camp_site', 'sort_rank': 92})

# small campground in point zoom 13
# http://www.openstreetmap.org/way/417405356
test.assert_no_matching_feature(
    13, 1308, 3165, 'pois',
    { 'kind': 'camp_site'})
