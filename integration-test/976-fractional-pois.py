# https://www.openstreetmap.org/way/147689077
# Apple Store, SF
assert_has_feature(
    15, 5242, 12664, 'pois',
    { 'id': 147689077, 'min_zoom': 15.68 })

# Test that source and min_zoom are set properly for boundaries, roads, transit, and water
assert_has_feature(
    5, 9, 12, 'boundaries',
    { 'min_zoom': 0 , 'id': int,
    'source': 'naturalearthdata.com',
    'name': 'New Jersey - Pennsylvania' })

assert_has_feature(
    5, 9, 12, 'roads',
    { 'min_zoom': 8 , 'id': int, 'name': '611',
    'source': 'naturalearthdata.com' })

# There is no transit data from Natural Earth

assert_has_feature(
    5, 9, 12, 'water',
    { 'min_zoom': 0 , 'id': 1144,
    'source': 'naturalearthdata.com',
    'name': 'John H. Kerr Reservoir' })

# https://www.openstreetmap.org/relation/224951
# https://www.openstreetmap.org/relation/61320
assert_has_feature(
    9, 150, 192, 'boundaries',
    { 'min_zoom': 8, 'id':  -224951,
    'source': 'openstreetmap.org',
    'name': 'New Jersey - New York' })

assert_has_feature(
    9, 150, 192, 'roads',
    { 'min_zoom': 8, 'sort_key':  381,
    'source': 'openstreetmap.org',
    'kind': 'major_road',
    'network': 'US:NJ:Hudson' })

assert_has_feature(
    9, 150, 192, 'transit',
    { 'min_zoom': 5, 'ref':  '54-57',
    'source': 'openstreetmap.org',
    'name': 'Vermonter' })

assert_has_feature(
    9, 150, 192, 'water',
    { 'min_zoom': 0, 'id':  10613,
    'source': 'openstreetmapdata.com',
    'kind': 'ocean',
    'name': '' })
