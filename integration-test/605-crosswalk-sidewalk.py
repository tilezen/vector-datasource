# http://www.openstreetmap.org/way/444491374
test.assert_has_feature(
    16, 10475, 25332, 'roads',
    { 'id': 444491374, 'kind': 'path', 'crossing': 'traffic_signals' })

# Way: The Embarcadero (397140734)
# http://www.openstreetmap.org/way/397140734
test.assert_has_feature(
    16, 10486, 25326, 'roads',
    { 'id': 397140734, 'kind': 'major_road', 'sidewalk': 'separate' })


# Way: Carrie Furnace Boulevard (438362919)
# http://www.openstreetmap.org/way/438362919
test.assert_has_feature(
    16, 18225, 24712, 'roads',
    { 'id': 438362919, 'kind': 'major_road',
      'sidewalk_left': 'sidepath', 'sidewalk_right': 'no' })
