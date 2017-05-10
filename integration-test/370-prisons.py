tiles = [
    # Riker's Island - https://www.openstreetmap.org/relation/3955540
    (10, 301, 384, 'Rikers Island'),
    # SF County Jail - https://www.openstreetmap.org/way/103383866
    (14, 2621, 6332, 'SF County Jail')
]

for z, x, y, name in tiles:
    test.assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'prison',
          'name': name })

# Rikers Island also should have a landuse polygon
test.assert_has_feature(
    10, 301, 384, 'landuse',
    { 'kind': 'prison' })
