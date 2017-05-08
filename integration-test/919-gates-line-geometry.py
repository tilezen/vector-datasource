# Add barrier:gates with line geometries in landuse

# Line barrier:ghate feature
# http://www.openstreetmap.org/way/391260223
test.assert_has_feature(
    16, 10482, 25335, 'landuse',
    { 'id': 391260223, 'kind': 'gate'})
