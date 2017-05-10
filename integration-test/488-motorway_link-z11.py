locations = [
    (11, 327, 791) # SF  https://www.openstreetmap.org/way/8915478
]

for z, x, y in locations:
    test.assert_has_feature(
        z, x, y, 'roads',
        { 'kind': 'highway',
          'is_link': True,
          'kind_detail': 'motorway_link'})
    test.assert_no_matching_feature(
        z-1, x/2, y/2, 'roads',
        { 'kind': 'highway',
          'is_link': True,
          'kind_detail': 'motorway_link'})
