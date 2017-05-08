# Add footway properties to pedestrian paths and piers

# Pedestrian path
# http://www.openstreetmap.org/way/8919991
test.assert_has_feature(
    13, 1309, 3165, 'roads',
    { 'id': 8919991, 'kind': 'path', 'is_bicycle_related': True, 'bicycle': 'designated'})

# Pier
# http://www.openstreetmap.org/way/133920164
test.assert_has_feature(
    13, 1304, 2933, 'roads',
    { 'id': 133920164, 'kind': 'path', 'is_bicycle_related': True, 'bicycle': 'yes'})
