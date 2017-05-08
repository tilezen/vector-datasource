# Railways
#https://www.openstreetmap.org/way/8920472
test.assert_has_feature(
    16, 10487, 25333, "roads",
    {"kind": "rail", "kind_detail": "rail", "id": 8920472, "sort_rank": 382})

#https://www.openstreetmap.org/way/95623728
test.assert_has_feature(
    16, 10486, 25326, "roads",
    {"kind": "rail", "kind_detail": "tram", "id": 95623728, "sort_rank": 382})

#https://www.openstreetmap.org/way/160279679
test.assert_has_feature(
    16, 10478, 25341, "roads",
    {"kind": "rail", "kind_detail": "light_rail", "id": 160279679,
     "sort_rank": 382})

#https://www.openstreetmap.org/way/105574666
test.assert_has_feature(
    16, 19216, 24778, "roads",
    {"kind": "rail", "kind_detail": "narrow_gauge", "id": 105574666,
     "sort_rank": 382})

#https://www.openstreetmap.org/way/296530703
test.assert_has_feature(
    16, 17714, 24454, "roads",
    {"kind": "rail", "kind_detail": "monorail", "id": 296530703,
     "sort_rank": 382})

# spurs, sidings, etc...
#https://www.openstreetmap.org/way/135403703
test.assert_has_feature(
    16, 13353, 25941, "roads",
    {"kind": "rail", "kind_detail": "rail", "service": "spur", "id": 135403703,
     "sort_rank": 361})

#https://www.openstreetmap.org/way/148018328
test.assert_has_feature(
    16, 10485, 25331, "roads",
    {"kind": "rail", "kind_detail": "rail", "service": "siding", "id": 148018328,
     "sort_rank": 361})

#https://www.openstreetmap.org/way/119709585
test.assert_has_feature(
    16, 10485, 25331, "roads",
    {"kind": "rail", "kind_detail": "rail", "service": "yard", "id": 119709585,
     "sort_rank": 359})

#https://www.openstreetmap.org/way/119695339
test.assert_has_feature(
    16, 10485, 25347, "roads",
    {"kind": "rail", "kind_detail": "rail", "service": "crossover",
     "id": 119695339, "sort_rank": 357})
