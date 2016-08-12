# Node:358830410 Grave_yard in POIs
# http://www.openstreetmap.org/node/358830410
assert_has_feature(
    17, 20950, 50703, 'pois',
    {'id': 358830410, 'kind': 'grave_yard'})

# Way:79457493 Grave_yard in POIS
# http://www.openstreetmap.org/way/79457493
assert_has_feature(
    15, 5240, 12666, 'pois',
    {'id': 79457493, 'kind': 'grave_yard'})

# Way:79457493 Grave_yard in landuse
# http://www.openstreetmap.org/way/79457493
assert_has_feature(
    15, 5240, 12666, 'landuse',
    {'id': 79457493, 'kind': 'grave_yard'})

# Label placement Grave_yard in landuse
assert_no_matching_feature(
    15, 5240, 12666, 'landuse',
    {'id': 79457493, 'kind': 'grave_yard', 'label_placement': True})

# Way:41654965 Cemetery in POIs
# http://www.openstreetmap.org/way/41654965
assert_has_feature(
    12, 1171, 1567, 'pois',
    {'id': 41654965, 'kind': 'cemetery', 'min_zoom': 12})

# Label placement Cemetery in landuse
# http://www.openstreetmap.org/way/44580948
assert_no_matching_feature(
    12, 683, 1622, 'landuse',
    {'id': 44580948, 'kind': 'cemetery', 'label_placement': True})

# Way:179213166 Farm in POIs
# http://www.openstreetmap.org/way/179213166
assert_has_feature(
    15, 6660, 12542, 'pois',
    {'id': 179213166, 'kind': 'farm'})

# Label placement farm in landuse
assert_no_matching_feature(
    15, 6660, 12542, 'landuse',
    {'id': 179213166, 'kind': 'farm', 'label_placement': True})

# Way:64296322 landuse: Forest in POIS
# http://www.openstreetmap.org/way/64296322
assert_has_feature(
    10, 163, 392, 'pois',
    {'id': 64296322, 'kind': 'forest'})

# Label placement forest in landuse
assert_no_matching_feature(
    10, 163, 392, 'landuse',
    {'id': 64296322, 'kind': 'forest', 'label_placement': True})

# Node:357559979 landuse: Forest in POIS
# http://www.openstreetmap.org/node/357559979
assert_has_feature(
    14, 2842, 6101, 'pois',
    {'id': 357559979, 'kind': 'forest', 'min_zoom': 14})

# Way:432810821 landuse: Forest protect class in POIS
# http://www.openstreetmap.org/way/432810821
assert_has_feature(
    8, 72, 94, 'pois',
    {'id': 432810821, 'kind': 'forest', 'protect_class': '6'})

# Way: natural: Forest in POIS
# http://www.openstreetmap.org/way/202680509
assert_has_feature(
    12, 1219, 1527, 'pois',
    {'id': 202680509, 'kind': 'natural_forest'})

# Label placement forest in landuse
assert_no_matching_feature(
    12, 1219, 1527, 'landuse',
    {'id': 202680509, 'kind': 'natural_forest', 'label_placement': True})

# Node:2148541212 natural: Forest in POIS
# http://www.openstreetmap.org/node/2148541212
assert_has_feature(
    14, 3942, 5901, 'pois',
    {'id': 2148541212, 'kind': 'natural_forest', 'min_zoom': 14})

# Way:30903221 Golf_course in POIS
# http://www.openstreetmap.org/way/30903221
assert_has_feature(
    12, 654, 1583, 'pois',
    {'id': 30903221, 'kind': 'golf_course'})

# Label placement Golf_course in landuse
assert_no_matching_feature(
    12, 654, 1583, 'landuse',
    {'id': 30903221, 'kind': 'golf_course', 'label_placement': True})

# Node:4035914099 Golf_course in POIS
# http://www.openstreetmap.org/node/4035914099
assert_has_feature(
    14, 2680, 6334, 'pois',
    {'id': 4035914099, 'kind': 'golf_course', 'min_zoom': 14})

# Way:330274727 Military in POIS
# http://www.openstreetmap.org/way/330274727
assert_has_feature(
    11, 327, 793, 'pois',
    {'id': 330274727, 'kind': 'military'})

# Label placement military in landuse
assert_no_matching_feature(
    11, 327, 793, 'landuse',
    {'id': 330274727, 'kind': 'military', 'label_placement': True})

# Node:369174053 Military in POIS
# http://www.openstreetmap.org/node/369174053
assert_has_feature(
    14, 2617, 6329, 'pois',
    {'id': 369174053, 'kind': 'military', 'min_zoom': 14})

# Way:296096756 national_park in POIS
# http://www.openstreetmap.org/way/296096756
assert_has_feature(
    10, 164, 397, 'pois',
    {'id': 296096756, 'kind': 'national_park'})

# Label placement national_park in landuse
assert_no_matching_feature(
    10, 164, 397, 'landuse',
    {'id': 296096756, 'kind': 'national_park', 'label_placement': True})

# Node:617506856 national_park in POIS
# http://www.openstreetmap.org/node/617506856
assert_has_feature(
    10, 210, 386, 'pois',
    {'id': 617506856, 'kind': 'national_park', 'min_zoom': 10})

# Way:40260866 nature_reserve in POIS
# http://www.openstreetmap.org/way/40260866
assert_has_feature(
    12, 720, 1638, 'pois',
    {'id': 40260866, 'kind': 'nature_reserve'})

# Label placement nature_reserve in landuse
assert_no_matching_feature(
    12, 720, 1638, 'landuse',
    {'id': 40260866, 'kind': 'nature_reserve', 'label_placement': True})

# Node:1262562806 nature_reserve in POIS
# http://www.openstreetmap.org/node/1262562806
assert_has_feature(
    10, 247, 388, 'pois',
    {'id': 1262562806, 'kind': 'nature_reserve', 'min_zoom': 10})

# Way:23871270 park in POIS
# http://www.openstreetmap.org/way/23871270
assert_has_feature(
    11, 327, 791, 'pois',
    {'id': 23871270, 'kind': 'park'})

# Label placement park in landuse
assert_no_matching_feature(
    11, 327, 791, 'landuse',
    {'id': 23871270, 'kind': 'park', 'label_placement': True})

# Node:4206408136 park in POIS
# http://www.openstreetmap.org/node/4206408136
assert_has_feature(
    14, 2619, 6333, 'pois',
    {'id': 4206408136, 'kind': 'park', 'min_zoom': 14})

# Way:26278098 plant in POIS
# http://www.openstreetmap.org/way/26278098
assert_has_feature(
    13, 1308, 3167, 'pois',
    {'id': 26278098, 'kind': 'plant'})

# Label placement plant in landuse
assert_no_matching_feature(
    13, 1308, 3167, 'landuse',
    {'id': 26278098, 'kind': 'plant', 'label_placement': True})

# Node:902365126 plant in POIS
# http://www.openstreetmap.org/node/902365126
assert_has_feature(
    14, 2777, 6374, 'pois',
    {'id': 902365126, 'kind': 'plant', 'min_zoom': 14})

# Node:2442093493 pitch in POIS
# http://www.openstreetmap.org/node/2442093493
assert_has_feature(
    16, 10910, 25062, 'pois',
    {'id': 2442093493, 'kind': 'pitch', 'min_zoom': 16})

# Way:296573403 protected_area in POIS
# http://www.openstreetmap.org/way/296573403
assert_has_feature(
    9, 82, 198, 'pois',
    {'id': 296573403, 'kind': 'protected_area'})

# Label placement protected_area in landuse
assert_no_matching_feature(
    9, 82, 198, 'landuse',
    {'id': 296573403, 'kind': 'protected_area', 'label_placement': True})

# Node:4076680383 protected_area in POIS
# http://www.openstreetmap.org/node/4076680383
assert_has_feature(
    14, 2809, 6074, 'pois',
    {'id': 4076680383, 'kind': 'protected_area', 'min_zoom': 14})

# Way:184367568 quarry in POIS
# http://www.openstreetmap.org/way/184367568
assert_has_feature(
    12, 671, 1583, 'pois',
    {'id': 184367568, 'kind': 'quarry', 'min_zoom': 12})

# Label placement quarry in landuse
assert_no_matching_feature(
    12, 671, 1583, 'landuse',
    {'id': 184367568, 'kind': 'quarry', 'label_placement': True})

# Node:585365655 quarry in POIS
# http://www.openstreetmap.org/node/585365655
assert_has_feature(
    14, 2622, 6334, 'pois',
    {'id': 585365655, 'kind': 'quarry', 'min_zoom': 14})

# Way:86285084 recreation_ground in POIS
# http://www.openstreetmap.org/way/86285084
assert_has_feature(
    14, 2619, 6334, 'pois',
    {'id': 86285084, 'kind': 'recreation_ground', 'min_zoom': 14})

# Label placement recreation_ground in landuse
assert_no_matching_feature(
    14, 2619, 6334, 'landuse',
    {'id': 86285084, 'kind': 'recreation_ground', 'label_placement': True})

# Node:1868204235 recreation_ground in POIS
# http://www.openstreetmap.org/node/1868204235
assert_has_feature(
    14, 2626, 6326, 'pois',
    {'id': 1868204235, 'kind': 'recreation_ground', 'min_zoom': 14})

# Node:4214350591 substation in POIS
# http://www.openstreetmap.org/node/4214350591
assert_has_feature(
    15, 5233, 12668, 'pois',
    {'id': 4214350591, 'kind': 'substation', 'min_zoom': 15})

# Way:28694608 village_green in POIS
# http://www.openstreetmap.org/way/28694608
assert_has_feature(
    14, 2618, 6334, 'pois',
    {'id': 28694608, 'kind': 'village_green', 'min_zoom': 14})

# Label placement village_green in landuse
assert_no_matching_feature(
    14, 2618, 6334, 'landuse',
    {'id': 28694608, 'kind': 'village_green', 'label_placement': True})

# Node:3199567035 village_green in POIS
# http://www.openstreetmap.org/node/3199567035
assert_has_feature(
    14, 4186, 6018, 'pois',
    {'id': 3199567035, 'kind': 'village_green', 'min_zoom': 14})

# Way:239634932 wastewater_plant in POIS
# http://www.openstreetmap.org/way/239634932
assert_has_feature(
    12, 655, 1583, 'pois',
    {'id': 239634932, 'kind': 'wastewater_plant', 'min_zoom': 12})

# Label placement wastewater_plant in landuse
assert_no_matching_feature(
    12, 655, 1583, 'landuse',
    {'id': 239634932, 'kind': 'wastewater_plant', 'label_placement': True})

# Node:2838226695 wastewater_plant in POIS
# http://www.openstreetmap.org/node/2838226695
assert_has_feature(
    14, 2615, 6325, 'pois',
    {'id': 2838226695, 'kind': 'wastewater_plant', 'min_zoom': 14})

# Way:93703732 water_works in POIS
# http://www.openstreetmap.org/way/93703732
assert_has_feature(
    14, 2620, 6330, 'pois',
    {'id': 93703732, 'kind': 'water_works', 'min_zoom': 14})

# Label placement water_works in landuse
assert_no_matching_feature(
    14, 2620, 6330, 'landuse',
    {'id': 93703732, 'kind': 'water_works', 'label_placement': True})

# Node:3367407023 water_works in POIS
# http://www.openstreetmap.org/node/3367407023
assert_has_feature(
    14, 2627, 6346, 'pois',
    {'id': 3367407023, 'kind': 'water_works', 'min_zoom': 14})

# Way:317721523 winter_sports in POIS
# http://www.openstreetmap.org/way/317721523
assert_has_feature(
    10, 170, 391, 'pois',
    {'id': 317721523, 'kind': 'winter_sports', 'min_zoom': 10})

# Label placement winter_sports in landuse
assert_no_matching_feature(
    10, 170, 391, 'landuse',
    {'id': 317721523, 'kind': 'winter_sports', 'label_placement': True})

# Node:4042754024 winter_sports in POIS
# http://www.openstreetmap.org/node/4042754024
assert_has_feature(
    13, 4238, 2938, 'pois',
    {'id': 4042754024, 'kind': 'winter_sports', 'min_zoom': 13})

# Way:207859675 landuse: wood in POIS
# http://www.openstreetmap.org/way/207859675
assert_has_feature(
    13, 1413, 3274, 'pois',
    {'id': 207859675, 'kind': 'wood'})

# Label placement landuse: wood in landuse
assert_no_matching_feature(
    13, 1413, 3274, 'landuse',
    {'id': 207859675, 'kind': 'wood', 'label_placement': True})

# Way:372445925 natural: wood in POIS
# http://www.openstreetmap.org/way/372445925
assert_has_feature(
    13, 1309, 3165, 'pois',
    {'id': 372445925, 'kind': 'natural_wood'})

# Label placement natural: wood in landuse
assert_no_matching_feature(
    13, 1309, 3165, 'landuse',
    {'id': 372445925, 'kind': 'natural_wood', 'label_placement': True})

# Node:369162231 natural: wood in POIS
# http://www.openstreetmap.org/node/369162231
assert_has_feature(
    14, 2612, 6298, 'pois',
    {'id': 369162231, 'kind': 'natural_wood', 'min_zoom': 14})

# Way:164878781 works in POIS
# http://www.openstreetmap.org/way/164878781
assert_has_feature(
    12, 714, 1623, 'pois',
    {'id': 164878781, 'kind': 'works', 'min_zoom': 12})

# Label placement works in landuse
assert_no_matching_feature(
    12, 714, 1623, 'landuse',
    {'id': 164878781, 'kind': 'works', 'label_placement': True})

# Node:1004981713 works in POIS
# http://www.openstreetmap.org/node/1004981713
assert_has_feature(
    14, 3293, 6329, 'pois',
    {'id': 1004981713, 'kind': 'works', 'min_zoom': 14})
