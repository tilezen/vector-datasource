# There should be a single (merged) ocean feature in this tile
assert_less_than_n_features(9, 167, 186, 'water', {'kind': 'ocean'}, 2)
# There should be a single (merged) earth feature in this tile
assert_less_than_n_features(9, 170, 186, 'earth', {'kind': 'earth'}, 2)
