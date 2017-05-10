# https://www.openstreetmap.org/way/332223480
# Apple Store, SF
test.assert_has_feature(
    15, 5242, 12663, 'pois',
    { 'id': 332223480, 'min_zoom': 15.31 })

# Test that source and min_zoom are set properly for boundaries, roads, transit, and water
test.assert_has_feature(
    5, 9, 12, 'boundaries',
    { 'min_zoom': 2 , 'id': int,
    'source': 'naturalearthdata.com',
    'kind': 'region' })

test.assert_has_feature(
    7, 37, 48, 'roads',
    { 'min_zoom': 3 , 'id': int, 'shield_text': '95',
    'source': 'naturalearthdata.com' })

# There is no transit data from Natural Earth

test.assert_has_feature(
    7, 36, 50, 'water',
    { 'min_zoom': 0 , 'id': int,
    'source': 'naturalearthdata.com',
    'name': 'John H. Kerr Reservoir' })

# https://www.openstreetmap.org/relation/224951
# https://www.openstreetmap.org/relation/61320
test.assert_has_feature(
    9, 150, 192, 'boundaries',
    { 'min_zoom': 8, 'id':  -224951,
    'source': 'openstreetmap.org',
    'name': 'New Jersey - New York' })

# http://www.openstreetmap.org/relation/568499
test.assert_has_feature(
    9, 150, 192, 'roads',
    { 'min_zoom': 8, 'sort_rank':  381,
    'source': 'openstreetmap.org',
    'kind': 'major_road',
    'network': 'US:NJ:Hudson' })

# http://www.openstreetmap.org/relation/1359387
test.assert_has_feature(
    9, 150, 192, 'transit',
    { 'min_zoom': 5, 'ref':  '54-57',
    'source': 'openstreetmap.org',
    'name': 'Vermonter' })

test.assert_has_feature(
    9, 150, 192, 'water',
    { 'min_zoom': 0, 'id': int,
    'source': 'openstreetmapdata.com',
    'kind': 'ocean',
    'name': '' })
