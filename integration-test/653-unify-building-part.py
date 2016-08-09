# http://www.openstreetmap.org/way/264768910
# Way: One Madison
assert_has_feature(
    16, 19298, 24633, 'buildings',
    { 'id': 264768910, 'kind': 'building', 'root_id': type(None) })

# http://www.openstreetmap.org/way/160967738
assert_has_feature(
    16, 19298, 24633, 'buildings',
    { 'id': 160967738, 'kind': 'building_part', 'root_id': 264768910 })

#http://www.openstreetmap.org/way/160967739
assert_has_feature(
    16, 19298, 24633, 'buildings',
    { 'id': 160967739, 'kind': 'building_part', 'root_id': 264768910 })


# http://www.openstreetmap.org/relation/6062613
# Relation: Ferry Building
assert_has_feature(
    16, 10486, 25326, 'buildings',
    { 'id': 24460886, 'kind': 'building', 'root_id': type(None) })

# http://www.openstreetmap.org/way/404449724
assert_has_feature(
    16, 10486, 25326, 'buildings',
    { 'id': 404449724, 'kind': 'building_part', 'root_id': 24460886 })
