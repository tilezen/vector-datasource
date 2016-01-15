tiles = [
    (10, 301, 384, 'Rikers Island'),
    (14, 2621, 6332, 'SF County Jail')
]

for z, x, y, name in tiles:
    assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'prison',
          'name': name })

# Rikers Island also should have a landuse polygon
assert_has_feature(
    10, 301, 384, 'landuse',
    { 'kind': 'prison' })
