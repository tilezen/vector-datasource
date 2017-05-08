# Relation: Hoopa Valley Tribe
# http://www.openstreetmap.org/relation/6214773
#
# Note: this is tagged as a "protected_area" rather than a political boundary,
# but it seems that some "protect_class" values indicate political "protection"
test.assert_has_feature(
    16, 10237, 24570, 'boundaries',
    {'id': -6214773, 'kind': 'aboriginal_lands', 'kind_detail': type(None)})

# use relation instead of way, as osm2pgsql treats the relation as superseding
# the way and removes its tags when both are present.
# http://www.openstreetmap.org/relation/3854097
test.assert_has_feature(
    16, 10483, 22987, 'boundaries',
    {'id': -3854097, 'kind': 'aboriginal_lands', 'kind_detail': type(None)})

# Way: Upper Sumas 6 (55602811)
# http://www.openstreetmap.org/way/55602811
# http://www.openstreetmap.org/relation/6791772
test.assert_has_feature(
    16, 10523, 22492, 'boundaries',
    {'id': -6791772, 'kind': 'aboriginal_lands', 'kind_detail': type(None)})

# Relation: United States of America
# https://www.openstreetmap.org/relation/148838
test.assert_has_feature(
    16, 10417, 25370, 'boundaries',
    {'id': -148838, 'kind': 'country', 'kind_detail': '2'})

# Relation: Wyoming (161991) & Idaho (162116)
# http://www.openstreetmap.org/relation/161991
# http://www.openstreetmap.org/relation/162116
test.assert_has_feature(
    16, 12553, 24147, 'boundaries',
    {'id': set([-161991,-162116]), 'kind': 'region', 'kind_detail': '4'})

# http://www.openstreetmap.org/relation/396487 -- SF City/County
# http://www.openstreetmap.org/relation/396498 -- San Mateo County
test.assert_has_feature(
    16, 10484, 25346, 'boundaries',
    {'id': set([-396487,-396498]), 'kind': 'county', 'kind_detail': '6'})

# Relation: Brisbane (2834528)
# http://www.openstreetmap.org/relation/2834528
test.assert_has_feature(
    16, 10487, 25355, 'boundaries',
    {'id': -2834528, 'kind': 'locality', 'kind_detail': '8'})

# ne data

# Admin-1 boundary
test.assert_has_feature(
    7, 75, 70, 'boundaries',
    {'id': int, 'kind': 'region', 'kind_detail': '4'})
# Admin-1 statistical boundary
test.assert_has_feature(
    7, 101, 56, 'boundaries',
    {'id': int, 'kind': 'region', 'kind_detail': '4'})
# Admin-1 statistical meta bounds
test.assert_has_feature(
    7, 26, 52, 'boundaries',
    {'id': int, 'kind': 'region', 'kind_detail': '4'})

# Admin-1 region boundary
test.assert_has_feature(
    7, 99, 57, 'boundaries',
    {'id': int, 'kind': 'macroregion', 'kind_detail': '3'})

# Disputed (please verify)
test.assert_has_feature(
    7, 39, 71, 'boundaries',
    {'id': int, 'kind': 'disputed', 'kind_detail': '2'})

# Indefinite (please verify)
test.assert_has_feature(
    7, 20, 44, 'boundaries',
    {'id': int, 'kind': 'indefinite', 'kind_detail': '2'})

# Indeterminant frontier
test.assert_has_feature(
    7, 91, 50, 'boundaries',
    {'id': int, 'kind': 'indeterminate', 'kind_detail': '2'})

# International boundary (verify)
test.assert_has_feature(
    7, 67, 37, 'boundaries',
    {'id': int, 'kind': 'country', 'kind_detail': '2'})

# Lease limit
test.assert_has_feature(
    7, 86, 45, 'boundaries',
    {'id': int, 'kind': 'lease_limit', 'kind_detail': '2'})

# Line of control (please verify)
test.assert_has_feature(
    7, 90, 50, 'boundaries',
    {'id': int, 'kind': 'line_of_control', 'kind_detail': '2'})

# Overlay limit
test.assert_has_feature(
    7, 109, 49, 'boundaries',
    {'id': int, 'kind': 'overlay_limit', 'kind_detail': '2'})
