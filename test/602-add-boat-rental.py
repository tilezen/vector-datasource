tiles = [
    [18, 66716, 99052], # node 2420432693 shop=boat_rental
    [18, 53293, 86717], # node 2911709060 amenity=boat_rental
    [18, 77832, 98089], # node 3466463119 shop=boat, rental=yes
    [18, 42014, 101241] # node 3509468126 rental=boat
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'pois',
        {'kind': 'boat_rental'})
