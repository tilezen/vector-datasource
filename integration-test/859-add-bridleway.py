# Add bridleway from osm

# http://www.openstreetmap.org/way/387216146
test.assert_has_feature(
    16, 19302, 24623, 'roads',
    { 'id': 387216146, 'kind': 'path', 'kind_detail': 'bridleway'})
