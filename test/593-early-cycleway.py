tiles = [
    [12, 655, 1586]     # way 109993139  cycleway example south of SF, way/109993139, is member of regional cycling network
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'roads',
        {'highway': 'cycleway'})