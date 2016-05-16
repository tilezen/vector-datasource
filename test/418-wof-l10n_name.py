# Hollywood (wof neighbourhood)
# https://whosonfirst.mapzen.com/data/858/260/37/85826037.geojson
assert_has_feature(
    16, 11227, 26157, 'places',
    { 'id': 85826037, 'kind': 'neighbourhood',
      'source': "whosonfirst.mapzen.com",
      'name': 'Hollywood',
      'name:kor': '\xed\x97\x90\xeb\xa6\xac\xec\x9a\xb0\xeb\x93\x9c' })

# San Francisco (wof neighbourhood)
# https://whosonfirst.mapzen.com/data/858/826/41/85882641.geojson
assert_has_feature(
    16, 14893, 29234, 'places',
    { 'id': 85882641, 'kind': 'neighbourhood',
      'source': "whosonfirst.mapzen.com",
      'name': 'San Francisco',
      'name:spa': type(None) })

# San Francisco (osm city)
# https://whosonfirst.mapzen.com/data/858/826/41/85882641.geojson
assert_has_feature(
    16, 10482, 25330, 'places',
    { 'id': 26819236, 'kind': 'city',
      'source': "openstreetmap.org",
      'name': 'San Francisco',
      'name:zho': '\xe8\x88\x8a\xe9\x87\x91\xe5\xb1\xb1\xe5\xb8\x82\xe8\x88\x87\xe7\xb8\xa3' })
