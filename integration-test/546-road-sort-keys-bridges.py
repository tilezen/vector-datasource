# bridges
#https://www.openstreetmap.org/way/28412298
assert_has_feature(
    18, 41888, 101295, "roads",
    {"kind": "highway", "highway": "motorway", "id": 28412298,
     "name": "Presidio Pkwy.", "is_bridge": True, "sort_key": 443})

#https://www.openstreetmap.org/way/59801274
assert_has_feature(
    18, 41885, 101327, "roads",
    {"kind": "major_road", "highway": "trunk", "id": 59801274,
     "name": "Crossover Dr.", "is_bridge": True, "sort_key": 443})

#https://www.openstreetmap.org/way/370954791
assert_has_feature(
    18, 41903, 101329, "roads",
    {"kind": "major_road", "highway": "primary", "id": 370954791,
     "name": "Alvord Lake Bridge", "is_bridge": True, "sort_key": 428})

#https://www.openstreetmap.org/way/27613581
assert_has_feature(
    18, 41946, 101358, "roads",
    {"kind": "major_road", "highway": "secondary", "id": 27613581,
     "name": "Oakdale Ave.", "is_bridge": True, "sort_key": 427})

#https://www.openstreetmap.org/way/242940297
assert_has_feature(
    18, 41946, 101309, "roads",
    {"kind": "major_road", "highway": "tertiary", "id": 242940297,
     "name": "Beale St.", "is_bridge": True, "sort_key": 426})

#https://www.openstreetmap.org/way/162038104
assert_has_feature(
    18, 42955, 99957, "roads",
    {"kind": "minor_road", "highway": "residential", "id": 162038104,
     "name": "Woodwardia Pl.", "sort_key": 410})

#http://www.openstreetmap.org/way/232303398
assert_has_feature(
    16, 10482, 25363, "roads",
    {"id": 232303398, "kind": "minor_road", "highway": "service",
     "is_bridge": True, "sort_key": 408})
