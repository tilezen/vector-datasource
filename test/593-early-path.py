tiles = [
    [11, 345, 790],     # way 236361475  highway=path, with route national (Pacific Crest Trail)
    [12, 687, 1584],    # way 373491941  highway=path, with route regional (Merced Pass Trail)
    [12, 688, 1584],    # way 39996451   highway=path, with route regional (Merced Pass Trail)
    [13, 1374, 3166]   # way 162322353  highway=path, no route, but has name (Upper Yosemite Falls Trail)
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'roads',
        {'highway': 'path', 'name': None})
