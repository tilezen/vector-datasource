# Add bicycle properties to roads

# Road with bicycle=yes in Washington, DC
# http://www.openstreetmap.org/way/281677984
assert_has_feature(
    15, 9379, 12539, 'roads',
    { 'id': 281677984, 'kind': 'major_road', 'is_bicycle_related': True, 'bicycle': 'yes'})

# Road with bicycle=designated in Eureka, California
# http://www.openstreetmap.org/way/10273013
assert_has_feature(
    15, 5081, 12311, 'roads',
    { 'id': 10273013, 'kind': 'major_road', 'is_bicycle_related': True, 'bicycle': 'designated'})