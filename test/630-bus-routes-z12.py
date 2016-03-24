z, x, y = (16, 10484, 25329)

# test that at least one is present in tiles up to z12
while z >= 12:
    assert_has_feature(
        z, x, y, 'roads',
        { 'is_bus_route': True })
    z, x, y = (z-1, x/2, y/2)

# but that none are present in the parent tile at z11
assert_no_matching_feature(
    z, x, y, 'roads',
    { 'is_bus_route': True })
