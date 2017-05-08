# Adds tests for OSM features (but not NE features)

# country boundary of USA
#https://www.openstreetmap.org/relation/148838
test.assert_has_feature(
    8, 39, 95, "boundaries",
    {"kind": "country", "sort_rank": 262})

# region boundary between Nevada - California
#https://www.openstreetmap.org/relation/165473
#https://www.openstreetmap.org/relation/165475
test.assert_has_feature(
    8, 42, 96, "boundaries",
    {"kind": "region", "sort_rank": 256})

# county boundary between Mendocino County - Humboldt County
#https://www.openstreetmap.org/relation/396458
#https://www.openstreetmap.org/relation/396489
test.assert_has_feature(
    10, 159, 387, "boundaries",
    {"kind": "county", "sort_rank": 254})

# locality boundary between San Francisco - Daly City
#https://www.openstreetmap.org/relation/111968
#https://www.openstreetmap.org/relation/112271
test.assert_has_feature(
    10, 163, 396, "boundaries",
    {"kind": "locality", "sort_rank": 252})
