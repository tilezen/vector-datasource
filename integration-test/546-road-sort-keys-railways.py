# Railways
#https://www.openstreetmap.org/way/8920472
assert_has_feature(
    18, 41948, 101333, "roads",
    {"kind": "rail", "kind_detail": "rail", "id": 8920472, "sort_key": 382})

#https://www.openstreetmap.org/way/95623728
assert_has_feature(
    18, 41947, 101306, "roads",
    {"kind": "rail", "kind_detail": "tram", "id": 95623728, "sort_key": 382})

#https://www.openstreetmap.org/way/160279679
assert_has_feature(
    18, 41914, 101365, "roads",
    {"kind": "rail", "kind_detail": "light_rail", "id": 160279679,
     "sort_key": 382})

#https://www.openstreetmap.org/way/105574666
assert_has_feature(
    18, 76864, 99113, "roads",
    {"kind": "rail", "kind_detail": "narrow_gauge", "id": 105574666,
     "sort_key": 382})

#https://www.openstreetmap.org/way/296530703
assert_has_feature(
    18, 70859, 97816, "roads",
    {"kind": "rail", "kind_detail": "monorail", "id": 296530703,
     "sort_key": 382})

# spurs, sidings, etc...
#https://www.openstreetmap.org/way/106087318
assert_has_feature(
    18, 41967, 101369, "roads",
    {"kind": "rail", "kind_detail": "rail", "service": "spur", "id": 106087318,
     "sort_key": 361})

#https://www.openstreetmap.org/way/148018328
assert_has_feature(
    18, 41943, 101326, "roads",
    {"kind": "rail", "kind_detail": "rail", "service": "siding", "id": 148018328,
     "sort_key": 361})

#https://www.openstreetmap.org/way/119709585
assert_has_feature(
    18, 41943, 101326, "roads",
    {"kind": "rail", "kind_detail": "rail", "service": "yard", "id": 119709585,
     "sort_key": 359})

#https://www.openstreetmap.org/way/119695339
assert_has_feature(
    18, 41941, 101390, "roads",
    {"kind": "rail", "kind_detail": "rail", "service": "crossover",
     "id": 119695339, "sort_key": 357})
