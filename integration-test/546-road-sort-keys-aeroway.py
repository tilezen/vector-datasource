#https://www.openstreetmap.org/way/214484985
test.assert_has_feature(
    16, 18957, 24538, "roads",
    {"kind": "aeroway", "kind_detail": "runway", "id": 214484985,
     "sort_rank": 62})

#https://www.openstreetmap.org/way/115434129
test.assert_has_feature(
    16, 18981, 24490, "roads",
    {"kind": "aeroway", "kind_detail": "taxiway", "id": 115434129,
     "sort_rank": 61})
