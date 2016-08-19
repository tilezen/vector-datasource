tiles = [
    # highway=path, with route national (Pacific Crest Trail)
    # https://www.openstreetmap.org/way/236361475
    # https://www.openstreetmap.org/relation/1225378
    [11, 345, 790],
    # highway=path, with route regional (Merced Pass Trail)
    # https://www.openstreetmap.org/way/373491941
    # https://www.openstreetmap.org/relation/5549623
    [12, 687, 1584],
    # highway=path, with route regional (Merced Pass Trail)
    # https://www.openstreetmap.org/way/39996451
    # https://www.openstreetmap.org/relation/5549623
    [12, 688, 1584],
    # highway=path, no route, but has name (Upper Yosemite Falls Trail)
    # https://www.openstreetmap.org/way/162322353
    [13, 1374, 3166]
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'roads',
        {'kind_detail': 'path', 'name': None})
