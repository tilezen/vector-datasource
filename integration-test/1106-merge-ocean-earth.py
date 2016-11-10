# There should be a single, merged feature in each of these tiles

# Natural Earth
assert_less_than_n_features(5, 11, 11, 'water', {'kind': 'ocean'}, 2)
assert_less_than_n_features(5, 8, 11, 'earth', {'kind': 'earth'}, 2)

# OpenStreetMap
assert_less_than_n_features(9, 167, 186, 'water', {'kind': 'ocean'}, 2)
assert_less_than_n_features(9, 170, 186, 'earth', {'kind': 'earth'}, 2)
