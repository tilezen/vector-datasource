# regular roads
#https://www.openstreetmap.org/way/26765956
assert_has_feature(
    18, 41888, 101295, "roads",
    {"kind": "highway", "kind_detail": "motorway", "id": 26765956,
     "name": "Presidio Pkwy.", "sort_rank": 383})

#https://www.openstreetmap.org/way/89802409
assert_has_feature(
    18, 41887, 101348, "roads",
    {"kind": "major_road", "kind_detail": "trunk", "id": 89802409,
     "name": "19th Ave.", "sort_rank": 381})

#https://www.openstreetmap.org/way/160842753
assert_has_feature(
    18, 41952, 101346, "roads",
    {"kind": "major_road", "kind_detail": "primary", "id": 160842753,
     "name": "3rd St.", "sort_rank": 380})

#https://www.openstreetmap.org/way/25337673
assert_has_feature(
    18, 41928, 101328, "roads",
    {"kind": "major_road", "kind_detail": "secondary", "id": 25337673,
     "name": "Mission St.", "sort_rank": 379})

#https://www.openstreetmap.org/way/255330035
assert_has_feature(
    18, 41941, 101298, "roads",
    {"kind": "major_road", "kind_detail": "tertiary", "id": 255330035,
     "name": "Battery St.", "sort_rank": 377})

#https://www.openstreetmap.org/way/123456285
assert_has_feature(
    18, 41890, 101390, "roads",
    {"kind": "highway", "kind_detail": "motorway_link", "id": 123456285,
     "name": "Junipero Serra Blvd.", "is_link": True, "sort_rank": 374})

#https://www.openstreetmap.org/way/8919312
assert_has_feature(
    18, 41942, 101379, "roads",
    {"kind": "minor_road", "kind_detail": "residential", "id": 8919312,
     "name": "Racine Ln.", "sort_rank": 360})

#https://www.openstreetmap.org/way/59161514
assert_has_feature(
    18, 41908, 101294, "roads",
    {"kind": "minor_road", "kind_detail": "service", "id": 59161514,
     "name": "Yacht Rd.", "sort_rank": 358})

# service roads
#https://www.openstreetmap.org/way/147002738
assert_has_feature(
    18, 41885, 101367, "roads",
    {"kind": "minor_road", "kind_detail": "service", "service": "parking_aisle",
     "id": 147002738, "sort_rank": 356})

#https://www.openstreetmap.org/way/242769687
assert_has_feature(
    18, 41949, 101316, "roads",
    {"kind": "minor_road", "kind_detail": "service", "service": "driveway",
     "id": 242769687, "sort_rank": 356})
