#  Way: 128534087 http://www.openstreetmap.org/way/128534087
test.assert_has_feature(
    16, 10482, 25330, 'roads',
    { 'id': 128534087 })
test.assert_no_matching_feature(
    16, 10482, 25330, 'landuse',
    { 'id': 128534087 })

# Way: 367756094 http://www.openstreetmap.org/way/367756094
test.assert_has_feature(
    16, 10465, 25331, 'roads',
    { 'id': 367756094 })
test.assert_no_matching_feature(
    16, 10465, 25331, 'landuse',
    { 'id': 367756094 })
