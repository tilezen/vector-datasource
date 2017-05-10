# Node: Gate G102 (1096088604)
# http://www.openstreetmap.org/node/1096088604
test.assert_has_feature(
    16, 10487, 25366, 'pois',
    { 'id': 1096088604, 'kind': 'aeroway_gate' })

# Node: Gate 1 (2618197593)
# http://www.openstreetmap.org/node/2618197593
# http://www.openstreetmap.org/way/320595943
test.assert_has_feature(
    16, 10309, 22665, 'pois',
    { 'id': 2618197593, 'kind': 'gate', 'aeroway': type(None) })

# Node: Lone Star Sports
# http://www.openstreetmap.org/node/2122898936
test.assert_has_feature(
    16, 13462, 24933, 'pois',
    { 'id': 2122898936, 'kind': 'ski_rental' })

# http://www.openstreetmap.org/way/52497271
test.assert_has_feature(
    16, 10566, 25429, 'landuse',
    { 'id': 52497271, 'kind': 'wood' })

# http://www.openstreetmap.org/way/207859675
test.assert_has_feature(
    16, 11306, 26199, 'landuse',
    { 'id': 207859675, 'kind': 'wood' })

# http://www.openstreetmap.org/way/417405367
test.assert_has_feature(
    16, 10480, 25323, 'landuse',
    { 'id': 417405367, 'kind': 'natural_wood' })

# http://www.openstreetmap.org/way/422270533
test.assert_has_feature(
    16, 10476, 25324, 'landuse',
    { 'id': 422270533, 'kind': 'forest' })

# http://www.openstreetmap.org/way/95360670
test.assert_has_feature(
    16, 17780, 27428, 'landuse',
    { 'id': 95360670, 'kind': 'natural_forest' })

# Way: Stables & Equestrian Area (393312618)
# http://www.openstreetmap.org/way/393312618
test.assert_has_feature(
    16, 10294, 25113, 'landuse',
    { 'id': 393312618, 'kind': 'park' })

# http://www.openstreetmap.org/way/469494860
test.assert_has_feature(
    16, 17612, 24209, 'landuse',
    { 'id': 469494860, 'kind': 'natural_park' })
