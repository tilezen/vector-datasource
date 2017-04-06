# Add ramp properties to paths in roads layer

# Steps with ramp:bicycle=yes in Copenhagen
# https://www.openstreetmap.org/way/91275149
assert_has_feature(
    15, 17527, 10257, 'roads',
    { 'id': 91275149, 'kind': 'path', 'kind_detail': 'steps', 'is_bicycle_related': True, 'ramp_bicycle': 'yes'})

# Footway with ramp=yes in San Francisco
# https://www.openstreetmap.org/way/346088008
assert_has_feature(
    15, 5235, 12671, 'roads',
    { 'id': 10273013, 'kind': 'path', 'kind_detail': 'footway', 'ramp': 'yes'})