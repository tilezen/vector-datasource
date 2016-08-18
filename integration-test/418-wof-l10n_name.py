# Hollywood (wof neighbourhood)
# https://whosonfirst.mapzen.com/data/858/260/37/85826037.geojson
assert_has_feature(
    16, 11227, 26157, 'places',
    { 'id': 85826037, 'kind': 'neighbourhood',
      'source': "whosonfirst.mapzen.com",
      'name': 'Hollywood',
      'name:ko': '\xed\x97\x90\xeb\xa6\xac\xec\x9a\xb0\xeb\x93\x9c' })

# San Francisco (wof neighbourhood)
# https://whosonfirst.mapzen.com/data/858/826/41/85882641.geojson
assert_has_feature(
    16, 14893, 29234, 'places',
    { 'id': 85882641, 'kind': 'neighbourhood',
      'source': "whosonfirst.mapzen.com",
      'name': 'San Francisco',
      'name:es': type(None) })

# San Francisco (osm city)
# http://www.openstreetmap.org/node/26819236
assert_has_feature(
    16, 10482, 25330, 'places',
    { 'id': 26819236, 'kind': 'locality', 'kind_detail': 'city',
      'source': "openstreetmap.org",
      'name': 'San Francisco',
      'name:zh': '\xe8\x88\x8a\xe9\x87\x91\xe5\xb1\xb1\xe5\xb8\x82\xe8\x88\x87\xe7\xb8\xa3' })

# Node: Londonderry/Derry (267762522)
# http://www.openstreetmap.org/node/267762522
assert_has_feature(
    16, 31436, 20731, 'places',
    { 'id': 267762522, 'name:en_GB': 'Londonderry'})

# Node: Jerusalem (29090735)
# http://www.openstreetmap.org/node/29090735
assert_has_feature(
    16, 39180, 26661, 'places',
    { 'id': 29090735,
      'name:zh-min-nan': 'I\xc3\xa2-l\xc5\x8d\xcd\x98-sat-l\xc3\xa9ng',
      'name:zh': '\xe8\x80\xb6\xe8\xb7\xaf\xe6\x92\x92\xe5\x86\xb7',
      'name:zh-yue': '\xe8\x80\xb6\xe8\xb7\xaf\xe6\x92\x92\xe5\x86\xb7',
      })
