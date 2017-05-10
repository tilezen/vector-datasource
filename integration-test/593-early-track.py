tiles = [
    # track example in Marin Headlands, a member of Bay Area Ridge Trail, a regional network
    # https://www.openstreetmap.org/way/12188550
    # https://www.openstreetmap.org/relation/2684235
    [12, 654, 1582]
]

for z, x, y in tiles:
    test.assert_has_feature(
        z, x, y, 'roads',
        {'kind_detail': 'track'})
