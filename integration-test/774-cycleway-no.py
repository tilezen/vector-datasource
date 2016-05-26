#  Way: Grant Avenue (184956229) http://www.openstreetmap.org/way/184956229
assert_no_matching_feature(
    16, 10484, 25327, 'roads',
    { 'cycleway': 'no' })

# Way: Wedge Parkway (263563960) http://www.openstreetmap.org/way/263563960
assert_no_matching_feature(
    16, 10966, 24952, 'roads',
    { 'cycleway_left': 'no' })
assert_has_feature(
    16, 10966, 24952, 'roads',
    { 'cycleway_right': 'lane' })

# Way: Wedge Parkway (263563950) http://www.openstreetmap.org/way/263563950
assert_no_matching_feature(
    16, 10965, 24952, 'roads',
    { 'cycleway_right': 'no' })
assert_has_feature(
    16, 10965, 24952, 'roads',
    { 'cycleway_left': 'lane' })
