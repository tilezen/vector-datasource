# Way: I 81 (302933871)
# http://www.openstreetmap.org/way/302933871
#
# testing that it dropped oneway, but hasn't dropped is_bridge. note that
# the ID gets dropped due to a merge with the other carriageway.
test.assert_has_feature(
    14, 4496, 6381, 'roads',
    { 'kind': 'highway', 'oneway': type(None), 'is_bridge': True })

# http://www.openstreetmap.org/way/434308106
#
# note that the ID gets dropped due to merging with other pedestrian
# paths. best way to test this lacking the ID seems to be to assert the
# presence of a path, but the absence of any crossing.
test.assert_has_feature(
    14, 4933, 6066, 'roads',
    { 'kind': 'path' })
test.assert_no_matching_feature(
    14, 4933, 6066, 'roads',
    { 'kind': 'path', 'crossing': None })

# Way: The Embarcadero (397140734)
# http://www.openstreetmap.org/way/397140734
test.assert_has_feature(
    14, 2621, 6331, 'roads',
    { 'name': 'The Embarcadero', 'kind': 'major_road' })
test.assert_no_matching_feature(
    14, 2621, 6331, 'roads',
    { 'name': 'The Embarcadero', 'kind': 'major_road',
      'sidewalk': None })

# Way: Carrie Furnace Boulevard (438362919)
# http://www.openstreetmap.org/way/438362919
test.assert_has_feature(
    14, 4556, 6178, 'roads',
    { 'name': 'Carrie Furnace Blvd.', 'kind': 'major_road' })
test.assert_no_matching_feature(
    14, 4556, 6178, 'roads',
    { 'name': 'Carrie Furnace Blvd.', 'kind': 'major_road',
      'sidewalk_left': None, 'sidewalk_right': None })
