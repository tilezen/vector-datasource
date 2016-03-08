## Best buy (closed)

# building should be present at z15
assert_has_feature(
    15, 5232, 12654, 'buildings',
    {'id': 241643507, 'kind': 'retail'})

# but POI shouldn't
assert_no_matching_feature(
    15, 5232, 12654, 'pois',
    {'id': 241643507})

# but POI should be present at z17 and marked as closed
assert_has_feature(
    17, 20931, 50616, 'pois',
    {'id': 241643507, 'kind': 'closed', 'min_zoom': 17})

## US Naval Hospital (historical)

# original polygon should be present at z15
assert_has_feature(
    15, 5266, 12666, 'landuse',
    {'id': -317369, 'kind': 'hospital'})

# but POI should not be present
assert_no_matching_feature(
    15, 5266, 12666, 'pois',
    {'id': -317369})

# but it should be present at z17
assert_has_feature(
    17, 21063, 50665, 'pois',
    {'id': -317369, 'kind': 'historical'})
