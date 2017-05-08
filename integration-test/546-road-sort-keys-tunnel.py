# tunnels at level = 0
#https://www.openstreetmap.org/way/167952621
test.assert_has_feature(
    16, 10475, 25324, "roads",
    {"kind": "highway", "kind_detail": "motorway", "id": 167952621,
     "name": "Presidio Pkwy.", "is_tunnel": True, "sort_rank": 333})

# http://www.openstreetmap.org/way/259492789
test.assert_has_feature(
    16, 19266, 24635, "roads",
    {"kind": "major_road", "kind_detail": "trunk", "id": 259492789,
     "name": "McCarter Hwy.", "is_tunnel": True, "sort_rank": 331})

# http://www.openstreetmap.org/way/277441866
test.assert_has_feature(
    16, 17563, 25792, "roads",
    {"kind": "major_road", "kind_detail": "trunk", "id": 277441866,
     "name": "Gatlinburg Spur Road (north)", "is_tunnel": True, "sort_rank": 331})

#https://www.openstreetmap.org/way/117837633
test.assert_has_feature(
    16, 16808, 24434, "roads",
    {"kind": "major_road", "kind_detail": "primary", "id": 117837633,
     "name": "Dixie Hwy.", "is_tunnel": True, "sort_rank": 330})

#https://www.openstreetmap.org/way/57782075
test.assert_has_feature(
    16, 16812, 24391, "roads",
    {"kind": "major_road", "kind_detail": "secondary", "id": 57782075,
     "name": "S Halsted St.", "is_tunnel": True, "sort_rank": 329})

#https://www.openstreetmap.org/way/57708079
test.assert_has_feature(
    16, 16813, 24386, "roads",
    {"kind": "major_road", "kind_detail": "tertiary", "id": 57708079,
     "name": "W 74th St.", "is_tunnel": True, "sort_rank": 327})

#https://www.openstreetmap.org/way/56393654
test.assert_has_feature(
    16, 16808, 24362, "roads",
    {"kind": "minor_road", "kind_detail": "residential", "id": 56393654,
     "name": "S Paulina St.", "is_tunnel": True, "sort_rank": 310})

#https://www.openstreetmap.org/way/190835369
test.assert_has_feature(
    16, 16814, 24363, "roads",
    {"kind": "minor_road", "kind_detail": "service", "id": 190835369,
     "name": "S Wong Pkwy.", "is_tunnel": True, "sort_rank": 308})
