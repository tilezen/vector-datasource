# Way: Hoopa Valley Tribe (174550914)
# http://www.openstreetmap.org/way/174550914
assert_has_feature(
    16, 10237, 24570, 'boundaries',
    {'id': 174550914, 'kind': 'aboriginal_lands', 'kind_detail': '4'})

# http://www.openstreetmap.org/way/286097885
assert_has_feature(
    16, 10483, 22987, 'boundaries',
    {'id': 286097885, 'kind': 'aboriginal_lands', 'kind_detail': type(None)})

# Way: Upper Sumas 6 (55602811)
# http://www.openstreetmap.org/way/55602811
assert_has_feature(
    16, 10523, 22492, 'boundaries',
    {'id': 55602811, 'kind': 'aboriginal_lands', 'kind_detail': type(None)})

# Way: United States of America (42298798)
# http://www.openstreetmap.org/way/42298798
assert_has_feature(
    16, 10417, 25370, 'boundaries',
    {'id': 42298798, 'kind': 'country', 'kind_detail': '2'})

# Relation: Wyoming (161991)
# http://www.openstreetmap.org/relation/161991
assert_has_feature(
    16, 12553, 24147, 'boundaries',
    {'id': -161991, 'kind': 'region', 'kind_detail': '4'})

# http://www.openstreetmap.org/way/395754575
assert_has_feature(
    16, 10484, 25346, 'boundaries',
    {'id': 395754575, 'kind': 'county', 'kind_detail': '6'})

# Relation: Brisbane (2834528)
# http://www.openstreetmap.org/relation/2834528
assert_has_feature(
    16, 10487, 25355, 'boundaries',
    {'id': -2834528, 'kind': 'locality', 'kind_detail': '8'})

# ne data

# Admin-1 boundary
assert_has_feature(
    7, 75, 70, 'boundaries',
    {'id': int, 'kind': 'region', 'kind_detail': '4'})
# Admin-1 statistical boundary
assert_has_feature(
    7, 101, 56, 'boundaries',
    {'id': int, 'kind': 'region', 'kind_detail': '4'})
# Admin-1 statistical meta bounds
assert_has_feature(
    7, 26, 52, 'boundaries',
    {'id': int, 'kind': 'region', 'kind_detail': '4'})

# Admin-1 region boundary
assert_has_feature(
    7, 99, 57, 'boundaries',
    {'id': int, 'kind': 'macroregion', 'kind_detail': '3'})

# Disputed (please verify)
assert_has_feature(
    7, 39, 71, 'boundaries',
    {'id': int, 'kind': 'disputed', 'kind_detail': '2'})

# Indefinite (please verify)
assert_has_feature(
    7, 20, 44, 'boundaries',
    {'id': int, 'kind': 'indefinite', 'kind_detail': '2'})

# Indeterminant frontier
assert_has_feature(
    7, 91, 50, 'boundaries',
    {'id': int, 'kind': 'indeterminate', 'kind_detail': '2'})

# International boundary (verify)
assert_has_feature(
    7, 67, 37, 'boundaries',
    {'id': int, 'kind': 'country', 'kind_detail': '2'})

# Lease limit
assert_has_feature(
    7, 86, 45, 'boundaries',
    {'id': int, 'kind': 'lease_limit', 'kind_detail': '2'})

# Line of control (please verify)
assert_has_feature(
    7, 90, 50, 'boundaries',
    {'id': int, 'kind': 'line_of_control', 'kind_detail': '2'})

# Overlay limit
assert_has_feature(
    7, 109, 49, 'boundaries',
    {'id': int, 'kind': 'overlay_limit', 'kind_detail': '2'})
