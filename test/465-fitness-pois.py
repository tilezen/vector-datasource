tiles = [
    # Fitness SF SOMA, leisure=fitness_centre
    #https://www.openstreetmap.org/way/25371830
    (16, 10484, 25332),
    # Sunset gym, leisure=sports_centre + sport=fitness
    #https://www.openstreetmap.org/node/3674255652
    (17, 20947, 50666),
    # Alameda Athletic Club, amenity=gym
    #https://www.openstreetmap.org/node/310972983
    (17, 21028, 50668)
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'fitness' })

# Pushup, fitness_station
#https://www.openstreetmap.org/node/3658323774
assert_has_feature(
    17, 26332, 50542, 'pois',
    { 'kind': 'fitness_station' })
