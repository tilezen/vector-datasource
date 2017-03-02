tiles = [
    [16, 16679, 24763], # node 2420432693 shop=boat_rental
    [16, 13323, 21679], # node 2911709060 amenity=boat_rental
    [16, 19458, 24522], # node 3466463119 shop=boat, rental=yes
    [16, 10503, 25310], # node 3509468126 rental=boat
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'pois',
        {'kind': 'boat_rental'})
