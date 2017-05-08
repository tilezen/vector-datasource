#https://www.openstreetmap.org/way/32051122
test.assert_has_feature(
    16, 19321, 23740, "roads",
    {"kind": "aerialway", "kind_detail": "gondola", "id": 32051122,
     "sort_rank": 442})

#https://www.openstreetmap.org/way/384371038
test.assert_has_feature(
    16, 14894, 29232, "roads",
    {"kind": "aerialway", "kind_detail": "cable_car", "id": 384371038,
     "sort_rank": 442})

#https://www.openstreetmap.org/way/113791306
test.assert_has_feature(
    16, 10553, 25492, "roads",
    {"kind": "aerialway", "kind_detail": "chair_lift", "id": 113791306,
     "sort_rank": 441})

#https://www.openstreetmap.org/way/209129274
test.assert_has_feature(
    16, 10719, 25012, "roads",
    {"kind": "aerialway", "kind_detail": "rope_tow", "id": 209129274,
     "sort_rank": 440})
