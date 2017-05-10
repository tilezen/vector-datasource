tiles = [
    # Bayonne Municipal Pool, amenity=swimming_pool
    # https://www.openstreetmap.org/way/361100118
    (16, 19273, 24652),
    # McCarren Park Swimming Pool, leisure=swimming_pool
    # https://www.openstreetmap.org/way/118987681
    (16, 19305, 24638)
]

for z, x, y in tiles:
    test.assert_has_feature(
        z, x, y, 'water',
        { 'kind': 'swimming_pool' })
