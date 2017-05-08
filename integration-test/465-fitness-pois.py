tiles = [
    # Fitness SF SOMA, leisure=fitness_centre
    #https://www.openstreetmap.org/way/25371830
    (16, 10484, 25332),
    # Sunset gym, leisure=sports_centre + sport=fitness
    #https://www.openstreetmap.org/node/3674255652
    (16, 10473, 25333),
    # Alameda Athletic Club, amenity=gym
    #https://www.openstreetmap.org/node/310972983
    (16, 10514, 25334)
]

for z, x, y in tiles:
    test.assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'fitness' })

# Pushup, fitness_station
#https://www.openstreetmap.org/node/3658323774
test.assert_has_feature(
    16, 13166, 25271, 'pois',
    { 'kind': 'fitness_station' })
