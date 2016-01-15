tiles = [
    (16, 19273, 24652), # Bayonne Municipal Pool, amenity=swimming_pool
    (16, 19305, 24638)  # McCarren Park Swimming Pool, leisure=swimming_pool
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'water',
        { 'kind': 'swimming_pool' })
