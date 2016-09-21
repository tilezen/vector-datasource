# http://www.openstreetmap.org/way/367477828
assert_has_feature(
    16, 10471, 25331, 'roads',
    { 'id': 367477828, 'kind': 'path', 'crossing': 'zebra' })

# Way: The Embarcadero (397140734)
# http://www.openstreetmap.org/way/397140734
assert_has_feature(
    16, 10486, 25326, 'roads',
    { 'id': 397140734, 'kind': 'major_road', 'sidewalk': 'separate' })


# Way: Carrie Furnace Boulevard (438362919)
# http://www.openstreetmap.org/way/438362919
assert_has_feature(
    16, 18225, 24712, 'roads',
    { 'id': 438362919, 'kind': 'major_road',
      'sidewalk_left': 'sidepath', 'sidewalk_right': 'no' })
