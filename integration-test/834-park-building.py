# This test make sure park polygons with addresses still end up in the landuse layer
# Because it's a relation, it's ID will be negative.
# (Separately a address point is generated for the feature, but we don't test that here.)

# Way: Olympic Sculpture Park (239782410)
# http://www.openstreetmap.org/relation/7406606
# http://www.openstreetmap.org/way/239782410
# http://www.openstreetmap.org/way/508853912
# http://www.openstreetmap.org/way/508853910
# http://www.openstreetmap.org/way/508853909
test.assert_no_matching_feature(
    16, 10493, 22885, 'buildings',
    { 'id': -7406606 })

# Way: Olympic Sculpture Park (239782410)
# http://www.openstreetmap.org/relation/7406606
# http://www.openstreetmap.org/way/239782410
# http://www.openstreetmap.org/way/508853912
# http://www.openstreetmap.org/way/508853910
# http://www.openstreetmap.org/way/508853909
test.assert_has_feature(
    16, 10493, 22885, 'landuse',
    { 'id': -7406606, 'kind': 'park' })
