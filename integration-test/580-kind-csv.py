#https://www.openstreetmap.org/node/1223019595
test.assert_has_feature(
    16, 10486, 25326, 'pois',
    { 'kind': 'post_office' })

#https://www.openstreetmap.org/node/317081601
test.assert_has_feature(
    16, 10485, 25329, 'pois',
    { 'kind': 'museum' })

#https://www.openstreetmap.org/node/3910307149
#https://www.openstreetmap.org/way/387798241
test.assert_has_feature(
    16, 10487, 25329, 'pois',
    { 'kind': 'gate' })

#https://www.openstreetmap.org/way/382798029
#https://www.openstreetmap.org/way/382798035
test.assert_has_feature(
    16, 10466, 25340, 'pois',
    { 'kind': 'enclosure' })

#http://www.openstreetmap.org/way/422270533
test.assert_has_feature(
    16, 10476, 25324, 'landuse',
    { 'id': 422270533, 'kind': 'forest' })

#https://www.openstreetmap.org/way/274459406
#https://www.openstreetmap.org/way/274459420
test.assert_has_feature(
    16, 10478, 25329, 'landuse',
    { 'kind': 'substation' })
