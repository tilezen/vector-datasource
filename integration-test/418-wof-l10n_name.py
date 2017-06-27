# Hollywood (wof neighbourhood)
# https://whosonfirst.mapzen.com/data/858/260/37/85826037.geojson
test.assert_has_feature(
    16, 11227, 26157, 'places',
    { 'id': 85826037, 'kind': 'neighbourhood',
      'source': "whosonfirst.mapzen.com",
      'name': 'Hollywood',
      'name:ko': '\xed\x97\x90\xeb\xa6\xac\xec\x9a\xb0\xeb\x93\x9c' })

# San Francisco (wof neighbourhood)
# https://whosonfirst.mapzen.com/data/858/826/41/85882641.geojson
test.assert_has_feature(
    16, 14893, 29234, 'places',
    { 'id': 85882641, 'kind': 'neighbourhood',
      'source': "whosonfirst.mapzen.com",
      'name': 'San Francisco',
      'name:es': type(None) })

# San Francisco (osm city)
# http://www.openstreetmap.org/node/26819236
#
# note: presence of Chinese name tested, but not its value, as that can and
# does change.
test.assert_has_feature(
    16, 10482, 25330, 'places',
    { 'id': 26819236, 'kind': 'locality', 'kind_detail': 'city',
      'source': "openstreetmap.org",
      'name': 'San Francisco',
      'name:zh': None })

# Node: Londonderry/Derry (267762522)
# http://www.openstreetmap.org/node/267762522
test.assert_has_feature(
    16, 31436, 20731, 'places',
    { 'id': 267762522, 'name:en_GB': 'Londonderry'})

# Node: Jerusalem (29090735)
# http://www.openstreetmap.org/node/29090735
#
# note: presence of Chinese name tested, but not its value, as that can and
# does change.
test.assert_has_feature(
    16, 39180, 26661, 'places',
    { 'id': 29090735,
      'name:zh-min-nan': None,
      'name:zh': None,
      'name:zh-yue': None,
      })
