# The landuse for a pier
# http://www.openstreetmap.org/way/82206919
test.assert_no_matching_feature(
    14, 2620, 6330, 'landuse',
    {'id': 82206919, 'kind': 'pier', 'label_placement': True})

test.assert_has_feature(
    15, 5240, 12661, 'landuse',
    {'id': 82206919, 'kind': 'pier', 'label_placement': True})


# The building known as 650 California Street
# http://www.openstreetmap.org/way/260520160
test.assert_no_matching_feature(
    15, 5242, 12663, 'buildings',
    {'id': 260520160, 'kind': 'building', 'label_placement': True})

test.assert_has_feature(
    16, 10484, 25326, 'buildings',
    {'id': 260520160, 'kind': 'building', 'label_placement': True})

