tiles = [
    (16, 10484, 25332), # Fitness SF SOMA, leisure=fitness_centre
    (17, 20947, 50666), # Sunset gym, leisure=sports_centre + sport=fitness
    (17, 21028, 50668)  # Alameda Athletic Club, amenity=gym
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'fitness' })

# Pushup, fitness_station
assert_has_feature(
    17, 26332, 50542, 'pois',
    { 'kind': 'fitness_station' })
