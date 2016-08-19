# tunnels at level = 0
#https://www.openstreetmap.org/way/167952621
assert_has_feature(
    18, 41903, 101298, "roads",
    {"kind": "highway", "kind_detail": "motorway", "id": 167952621,
     "name": "Presidio Pkwy.", "is_tunnel": True, "sort_key": 333})

# http://www.openstreetmap.org/way/259492762
assert_has_feature(
    16, 19267, 24634, "roads",
    {"kind": "major_road", "kind_detail": "trunk", "id": 259492762,
     "name": "Raymond Blvd.", "is_tunnel": True, "sort_key": 331})

# http://www.openstreetmap.org/way/277441866
assert_has_feature(
    16, 17563, 25792, "roads",
    {"kind": "major_road", "kind_detail": "trunk", "id": 277441866,
     "name": "Gatlinburg Spur Road (north)", "is_tunnel": True, "sort_key": 331})

#https://www.openstreetmap.org/way/117837633
assert_has_feature(
    18, 67234, 97737, "roads",
    {"kind": "major_road", "kind_detail": "primary", "id": 117837633,
     "name": "Dixie Hwy.", "is_tunnel": True, "sort_key": 330})

#https://www.openstreetmap.org/way/57782075
assert_has_feature(
    18, 67251, 97566, "roads",
    {"kind": "major_road", "kind_detail": "secondary", "id": 57782075,
     "name": "S Halsted St.", "is_tunnel": True, "sort_key": 329})

#https://www.openstreetmap.org/way/57708079
assert_has_feature(
    18, 67255, 97547, "roads",
    {"kind": "major_road", "kind_detail": "tertiary", "id": 57708079,
     "name": "W 74th St.", "is_tunnel": True, "sort_key": 327})

#https://www.openstreetmap.org/way/56393654
assert_has_feature(
    18, 67233, 97449, "roads",
    {"kind": "minor_road", "kind_detail": "residential", "id": 56393654,
     "name": "S Paulina St.", "is_tunnel": True, "sort_key": 310})

#https://www.openstreetmap.org/way/190835369
assert_has_feature(
    18, 67258, 97452, "roads",
    {"kind": "minor_road", "kind_detail": "service", "id": 190835369,
     "name": "S Wong Pkwy.", "is_tunnel": True, "sort_key": 308})
