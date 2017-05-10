# http://www.openstreetmap.org/relation/2307408
# ref="N 4", route=road, but no network=*
# so we should get something that has no network, but a shield text of '4'
test.assert_has_feature(
    11, 1038, 705, 'roads',
    { 'kind': 'major_road', 'shield_text': '4', 'network': type(None) })
