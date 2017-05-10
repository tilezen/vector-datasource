tiles = [
    [16, 18316, 23921], # node 1306277961 shop=boat_rental
    [16, 10978, 26089], # node 4362555638 amenity=boat_rental
    [16, 19458, 24522], # node 3466463119 shop=boat, rental=yes
    [16, 33611, 23091], # node 2425308146 rental=boat
]

for z, x, y in tiles:
    test.assert_has_feature(
        z, x, y, 'pois',
        {'kind': 'boat_rental'})
