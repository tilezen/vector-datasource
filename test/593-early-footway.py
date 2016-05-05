tiles = [
    [11, 344, 790],     # way 83076573   highway=footway, no name, route national (Pacific Crest Trail)
    [11, 345, 790],     # way 372066789  highway=footway, no name, route national (Pacific Crest Trail)
    [12, 654, 1582],    # way 239141479  highway=footway, with name, and route regional (Rodeo Valley Trail, Marin)
    [13, 1308, 3167],   # way 161702316  highway=footway, with designation (Ocean Beach north, SF)
    [13, 1308, 3166],   # way 28691787   highway=footway, with designation (Ocean Beach south, SF)
    [13, 1308, 3164],   # way 24526324   highway=footway, with name (Coastal Trail, Marin)
    [13, 1308, 3166],   # way 27553452   highway=footway, with name (Coastal Trail, SF)
    [13, 1309, 3165]    # way 69020102   highway=footway, with name (Lovers Lane, SF)
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'roads',
        {'highway': 'footway'})


#SF State, way/346093021
assert_no_matching_feature(
    14, 2617, 6335, 'roads',
    {'kind': 'path', 'footway': 'sidewalk'})

#SF State, way/346093021
assert_has_feature(
    15, 5235, 12671, 'roads',
    {'kind': 'path', 'footway': 'sidewalk'})

#SF in the Avenues, way/344205837
assert_no_matching_feature(
    14, 2617, 6333, 'roads',
    {'kind': 'path', 'footway': 'sidewalk'})

#SF in the Avenues, way/344205837
assert_has_feature(
    15, 5234, 12667, 'roads',
    {'kind': 'path', 'footway': 'crossing'})
