locations = [
    (11, 327, 791), # SF
    (11, 603, 769)  # NYC
]

for z, x, y in locations:
    assert_has_feature(
        z, x, y, 'roads',
        { 'kind': 'highway',
          'is_link': 'yes',
          'highway': 'motorway_link'})
    assert_no_matching_feature(
        z-1, x/2, y/2, 'roads',
        { 'kind': 'highway',
          'is_link': 'yes',
          'highway': 'motorway_link'})
