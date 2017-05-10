tiles = [
    # highway=footway, no name, route national (Pacific Crest Trail)
    # https://www.openstreetmap.org/way/83076573
    # https://www.openstreetmap.org/relation/1225378
    [11, 344, 790],
    # highway=footway, no name, route national (Pacific Crest Trail)
    # https://www.openstreetmap.org/way/372066789
    # https://www.openstreetmap.org/relation/1225378
    [11, 345, 790],
    # highway=footway, with name, and route regional (Rodeo Valley Trail, Marin)
    # https://www.openstreetmap.org/way/239141479
    # https://www.openstreetmap.org/relation/2684235
    [12, 654, 1582],
    # highway=footway, with designation (Ocean Beach north, SF)
    # https://www.openstreetmap.org/way/161702316
    [13, 1308, 3167],
    # highway=footway, with designation (Ocean Beach south, SF)
    # https://www.openstreetmap.org/way/28691787
    [13, 1308, 3166],
    # highway=footway, with name (Coastal Trail, Marin)
    # https://www.openstreetmap.org/way/24526324
    [13, 1308, 3164],
    # highway=footway, with name (Coastal Trail, SF)
    # https://www.openstreetmap.org/way/27553452
    [13, 1308, 3166],
    # highway=footway, with name (Lovers Lane, SF)
    # https://www.openstreetmap.org/way/69020102
    [13, 1309, 3165]
]

for z, x, y in tiles:
    test.assert_has_feature(
        z, x, y, 'roads',
        {'kind_detail': 'footway'})


#SF State, way/346093021
test.assert_no_matching_feature(
    14, 2617, 6335, 'roads',
    {'kind': 'path', 'footway': 'sidewalk'})

#SF State, way/346093021
test.assert_has_feature(
    15, 5235, 12671, 'roads',
    {'kind': 'path', 'footway': 'sidewalk'})

#SF in the Avenues, way/344205837
test.assert_no_matching_feature(
    14, 2617, 6333, 'roads',
    {'id': 344205837, 'kind': 'path', 'footway': 'sidewalk'})

#SF in the Avenues, way/344205837
test.assert_has_feature(
    15, 5234, 12667, 'roads',
    {'kind': 'path', 'footway': 'crossing'})
