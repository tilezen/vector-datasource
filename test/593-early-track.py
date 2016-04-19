tiles = [
    [12, 654, 1582]     # way/12188550 track example in Marin Headlands, a member of Bay Area Ridge Trail, a regional network
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'roads',
        {'highway': 'track'})