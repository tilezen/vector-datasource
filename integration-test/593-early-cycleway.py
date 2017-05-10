tiles = [
    # cycleway example south of SF is member of regional cycling network
    #https://www.openstreetmap.org/way/158622336
    #https://www.openstreetmap.org/relation/2263205
    [12, 655, 1586]
]

for z, x, y in tiles:
    test.assert_has_feature(
        z, x, y, 'roads',
        {'kind_detail': 'cycleway'})
