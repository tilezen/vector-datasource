# Add footway properties to pedestrian paths and piers

# Pedestrian path
# http://www.openstreetmap.org/way/8919991
assert_has_feature(
    13, 1309, 3165, 'roads',
    { 'id': 8919991, 'kind': 'path', 'bicycle': 'designated'})

# Pier
# http://www.openstreetmap.org/way/133920164
assert_has_feature(
    13, 1304, 2933, 'roads',
    { 'id': 133920164, 'kind': 'path', 'bicycle': 'yes'})
