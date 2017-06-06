# layer 5
#https://www.openstreetmap.org/way/122189460
test.assert_has_feature(
    16, 18819, 24980, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
     "id": 122189460, "sort_rank": 447})

# layer 4
#https://www.openstreetmap.org/way/8918870
test.assert_has_feature(
    16, 10483, 25340, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
     "id": 8918870, "sort_rank": 446})

# layer 3
#https://www.openstreetmap.org/way/29394019
test.assert_has_feature(
    16, 10479, 25341, "roads",
    {"kind": "highway", "kind_detail": "motorway_link", "is_bridge": True,
     "id": 29394019, "sort_rank": 445})

# layer 2
#https://www.openstreetmap.org/way/27651523
test.assert_has_feature(
    16, 10480, 25365, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
     "id": 27651523, "sort_rank": 444})

# layer 1
#https://www.openstreetmap.org/way/28412298
test.assert_has_feature(
    16, 10472, 25323, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
     "id": 28412298, "sort_rank": 443})

# layer -1
#https://www.openstreetmap.org/way/43685501
test.assert_has_feature(
    16, 10472, 25323, "roads",
    {"kind": "minor_road", "kind_detail": "service", "is_tunnel": True,
     "id": 43685501, "sort_rank": 304})

# layer -2
#https://www.openstreetmap.org/way/50691047
test.assert_has_feature(
    16, 10491, 25323, "roads",
    {"kind": "highway", "kind_detail": "motorway", "is_tunnel": True,
     "id": 50691047, "sort_rank": 303})
