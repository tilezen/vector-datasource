# http://www.openstreetmap.org/relation/3948946
test.assert_has_feature(
    16, 63085, 15623, 'roads',
    { 'id': 425415345, 'shield_text': u'77\u041a' })
test.assert_has_feature(
    16, 63085, 15623, 'roads',
    { 'id': -3948946, 'osm_relation': type(True), 'shield_text': u'77\u041a' })
