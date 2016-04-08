# ne_10m_lakes gid 1298
assert_has_feature(
    8, 47, 95, 'water',
    { 'kind': 'lake', 'alkaline': 'yes' })

# way ​386662458
assert_has_feature(
    16, 10481, 25324, 'water',
    { 'kind': 'lake', 'reservoir': 'yes' })
