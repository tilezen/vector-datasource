# example from ticket: an unnamed natural=wood in Hyde Park, London
# http://www.openstreetmap.org/relation/1756198
# since this is unnamed, it might already get dropped as a POI, and won't have
# a landuse label, so this checks for the polygon.
test.assert_has_feature(
    16, 32737, 21792, 'landuse',
    { 'id': -1756198, 'kind': 'natural_wood' })
test.assert_no_matching_feature(
    16, 32737, 21792, 'pois',
    { 'id': -1756198, 'kind': 'natural_wood' })

# named area, should get a label placement. note that we currently only add
# landuse label placements at zoom 15+.
# Mt. Cydonia Ponds Natural Area
# http://www.openstreetmap.org/relation/6366946
test.assert_has_feature(
    15, 9327, 12418, 'landuse',
    { 'id': -6366946, 'kind': 'natural_wood', 'label_placement': True })
test.assert_no_matching_feature(
    15, 9327, 12418, 'pois',
    { 'id': -6366946, 'kind': 'natural_wood' })

# same, but for a forest
# Liebesinsel, nr. Berlin, Germany
# http://www.openstreetmap.org/way/316516905
test.assert_has_feature(
    16, 35199, 21454, 'landuse',
    { 'id': 316516905, 'kind': 'natural_forest', 'label_placement': True })
test.assert_no_matching_feature(
    16, 35199, 21454, 'pois',
    { 'id': 316516905, 'kind': 'natural_forest' })
