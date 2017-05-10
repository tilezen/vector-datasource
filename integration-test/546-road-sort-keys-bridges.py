# bridges
#https://www.openstreetmap.org/way/28412298
test.assert_has_feature(
    16, 10472, 25323, "roads",
    {"kind": "highway", "kind_detail": "motorway", "id": 28412298,
     "name": "Presidio Pkwy.", "is_bridge": True, "sort_rank": 443})

#https://www.openstreetmap.org/way/59801274
test.assert_has_feature(
    16, 10471, 25331, "roads",
    {"kind": "major_road", "kind_detail": "trunk", "id": 59801274,
     "name": "Crossover Dr.", "is_bridge": True, "sort_rank": 443})

#http://www.openstreetmap.org/way/399640204
test.assert_has_feature(
    16, 11265, 26221, "roads",
    {"kind": "major_road", "kind_detail": "primary", "id": 399640204,
     "name": "North Los Coyotes Diagonal", "is_bridge": True, "sort_rank": 430})

#https://www.openstreetmap.org/way/27613581
test.assert_has_feature(
    16, 10486, 25339, "roads",
    {"kind": "major_road", "kind_detail": "secondary", "id": 27613581,
     "name": "Oakdale Ave.", "is_bridge": True, "sort_rank": 429})

#https://www.openstreetmap.org/way/242940297
test.assert_has_feature(
    16, 10486, 25327, "roads",
    {"kind": "major_road", "kind_detail": "tertiary", "id": 242940297,
     "name": "Beale St.", "is_bridge": True, "sort_rank": 427})

#https://www.openstreetmap.org/way/162038104
test.assert_has_feature(
    16, 10738, 24989, "roads",
    {"kind": "minor_road", "kind_detail": "residential", "id": 162038104,
     "name": "Woodwardia Pl.", "sort_rank": 410})

#http://www.openstreetmap.org/way/232303398
test.assert_has_feature(
    16, 10482, 25363, "roads",
    {"id": 232303398, "kind": "minor_road", "kind_detail": "service",
     "is_bridge": True, "sort_rank": 408})
