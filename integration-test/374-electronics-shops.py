tiles = [
    # https://www.openstreetmap.org/way/25821942
    (17, 20966, 50665, 'Best Buy'),
    # https://www.openstreetmap.org/way/143811375
    (15, 5236, 12676, 'Best Buy'),
    # https://www.openstreetmap.org/way/25821942
    (15, 5241, 12666, 'Best Buy'),
    # https://www.openstreetmap.org/way/332223480
    (16, 10484, 25327, 'Apple Store, Union Square')
]

for z, x, y, name in tiles:
    assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'electronics',
          'name': name })
