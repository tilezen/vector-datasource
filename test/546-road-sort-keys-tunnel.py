# tunnels at level = 0
assert_has_feature(
    18, 41903, 101298, "roads",
    {"kind": "highway", "highway": "motorway", "id": 167952621,
     "name": "Presidio Pkwy.", "is_tunnel": "yes", "sort_key": 331})

# http://www.openstreetmap.org/way/89912879
assert_has_feature(
    16, 19829, 24234, "roads",
    {"kind": "major_road", "highway": "trunk", "id": 89912879,
     "name": "Sullivan Square Underpass", "is_tunnel": "yes", "sort_key": 329})

assert_has_feature(
    18, 67234, 97737, "roads",
    {"kind": "major_road", "highway": "primary", "id": 117837633,
     "name": "Dixie Hwy.", "is_tunnel": "yes", "sort_key": 328})

assert_has_feature(
    18, 67251, 97566, "roads",
    {"kind": "major_road", "highway": "secondary", "id": 57782075,
     "name": "S Halsted St.", "is_tunnel": "yes", "sort_key": 327})

assert_has_feature(
    18, 67255, 97547, "roads",
    {"kind": "major_road", "highway": "tertiary", "id": 57708079,
     "name": "W 74th St.", "is_tunnel": "yes", "sort_key": 326})

assert_has_feature(
    18, 67233, 97449, "roads",
    {"kind": "minor_road", "highway": "residential", "id": 56393654,
     "name": "S Paulina St.", "is_tunnel": "yes", "sort_key": 310})

assert_has_feature(
    18, 67258, 97452, "roads",
    {"kind": "minor_road", "highway": "service", "id": 190835369,
     "name": "S Wong Pkwy.", "is_tunnel": "yes", "sort_key": 308})
