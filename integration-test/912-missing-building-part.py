# http://www.openstreetmap.org/way/287494678
z = 18
x = 77193
y = 98529
while z >= 16:
    assert_has_feature(
        z, x, y, 'buildings',
        { 'kind': 'building_part',
          'id': 287494678,
          'min_zoom': 16 })

    z -= 1
    x /= 2
    y /= 2
