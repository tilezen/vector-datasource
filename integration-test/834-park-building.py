# Way: Olympic Sculpture Park (239782410)
# http://www.openstreetmap.org/way/239782410
test.assert_no_matching_feature(
    16, 10493, 22885, 'buildings',
    { 'id': 239782410 })

# Way: Olympic Sculpture Park (239782410)
# http://www.openstreetmap.org/way/239782410
test.assert_has_feature(
    16, 10493, 22885, 'landuse',
    { 'id': 239782410, 'kind': 'park' })
