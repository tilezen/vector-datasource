# Best Buy, SF
assert_has_feature(
    17, 20966, 50665, 'pois',
    { 'kind': 'electronics',
      'name': 'Best Buy' })

tiles = [
    (15, 5236, 12676, 'Best Buy'),
    (15, 5241, 12666, 'Best Buy'),
    (16, 10484, 25328, 'Apple Store')
]

for z, x, y, name in tiles:
    assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'electronics',
          'name': name })
