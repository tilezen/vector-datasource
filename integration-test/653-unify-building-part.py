# http://www.openstreetmap.org/way/264768910
# Way: One Madison
test.assert_has_feature(
    16, 19298, 24633, 'buildings',
    { 'id': 264768910, 'kind': 'building', 'root_id': type(None) })

# http://www.openstreetmap.org/way/160967738
test.assert_has_feature(
    16, 19298, 24633, 'buildings',
    { 'id': 160967738, 'kind': 'building_part', 'root_id': 264768910 })

#http://www.openstreetmap.org/way/160967739
test.assert_has_feature(
    16, 19298, 24633, 'buildings',
    { 'id': 160967739, 'kind': 'building_part', 'root_id': 264768910 })


# http://www.openstreetmap.org/relation/6062613
# Relation: Ferry Building
test.assert_has_feature(
    16, 10486, 25326, 'buildings',
    { 'id': 24460886, 'kind': 'building', 'root_id': type(None) })

# http://www.openstreetmap.org/way/404449724
test.assert_has_feature(
    16, 10486, 25326, 'buildings',
    { 'id': 404449724, 'kind': 'building_part', 'root_id': 24460886 })


# http://www.openstreetmap.org/relation/1242762
# Relation: Waterloo (tube and rail)
# http://www.openstreetmap.org/relation/238793
# Relation: Waterloo (tube station)
# http://www.openstreetmap.org/relation/238792
# Relation: London Waterloo
test.assert_has_feature(
    16, 32747, 21793, 'pois',
    { 'id': 3638795617, 'root_id': 1242762, 'root_relation_id': type(None) })
test.assert_has_feature(
    16, 32747, 21793, 'pois',
    { 'id': 3638795618, 'root_id': 1242762, 'root_relation_id': type(None) })
