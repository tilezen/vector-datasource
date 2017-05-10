# There should be a single, merged feature in each of these tiles

# Natural Earth
test.assert_less_than_n_features(5, 12, 11, 'water', {'kind': 'ocean'}, 2)
test.assert_less_than_n_features(5, 8, 11, 'earth', {'kind': 'earth'}, 2)

# OpenStreetMap
test.assert_less_than_n_features(9, 167, 186, 'water', {'kind': 'ocean'}, 2)
test.assert_less_than_n_features(9, 170, 186, 'earth', {'kind': 'earth'}, 2)
