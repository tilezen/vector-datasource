def assert_add_place(z, x, y, name):
    test.assert_has_feature(
        z, x, y, 'places',
        { 'kind': 'locality', 'name': name,
          'source': 'naturalearthdata.com',
          'min_zoom': z })
    test.assert_no_matching_feature(
        z-1, x/2, y/2, 'places',
        { 'kind': 'locality', 'name': name,
          'source': 'naturalearthdata.com' })

def assert_remove_place(z, x, y, name):
    test.assert_no_matching_feature(
        z, x, y, 'places',
        { 'kind': 'locality', 'name': name,
          'source': 'naturalearthdata.com' })
    test.assert_has_feature(
        z-1, x/2, y/2, 'places',
        { 'kind': 'locality', 'name': name,
          'source': 'naturalearthdata.com' })

# z2: Add New York City
assert_add_place(2, 1, 1, 'New York')

# z3: Add San Francisco
assert_add_place(3, 1, 3, 'San Francisco')

# z4: Add Seattle
assert_add_place(4, 2, 5, 'Seattle')

# z5: Add Eureka, California
assert_add_place(5, 4, 12, 'Eureka')

# z6: Add Medford, Oregon
assert_add_place(6, 10, 23, 'Medford')

# z7: Add Arcata, California
assert_add_place(7, 19, 48, 'Arcata')
assert_add_place(7, 20, 48, 'Ukiah')

# z8: Remainder Ukiah, California
assert_remove_place(8, 75, 96, 'New York')
assert_remove_place(8, 40, 94, 'Medford')

# z9: Remainder Mendocino, California
assert_add_place(9, 79, 195, 'Mendocino')

# z10: Remainder Harnosand, Sweden (62.6339970391, 17.9340036175)
assert_add_place(10, 563, 281, 'Harnosand')
assert_remove_place(10, 159, 384, 'Arcata')
assert_remove_place(10, 161, 390, 'Ukiah')

# z11 Mendocino should still be here
test.assert_has_feature(
    9, 79, 195, 'places',
    { 'kind': 'locality', 'name': 'Mendocino',
      'source': 'naturalearthdata.com' })
