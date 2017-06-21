#  Way: The Embarcadero (24335490)
# http://www.openstreetmap.org/way/24335490
# http://www.openstreetmap.org/relation/32386
test.assert_has_feature(
    16, 10487, 25327, 'roads',
    { 'id': 24335490, 'kind': 'major_road', 'cycleway_right': 'lane', 'bicycle_network': 'lcn' })

# Way: King Street (8920394) http://www.openstreetmap.org/way/8920394
test.assert_has_feature(
    16, 10487, 25329, 'roads',
    { 'id': 8920394, 'kind': 'major_road', 'cycleway_right': 'lane', 'bicycle_network': 'lcn'})

# Way: King Street (397270776) http://www.openstreetmap.org/way/397270776
test.assert_has_feature(
    16, 10487, 25329, 'roads',
    { 'id': 397270776, 'kind': 'major_road', 'cycleway_right': 'lane', 'bicycle_network': 'lcn'})

# Way: Clara-Immerwahr-Straße (287167007) http://www.openstreetmap.org/way/287167007
test.assert_has_feature(
    16, 34494, 21846, 'roads',
    { 'id': 287167007, 'kind': 'minor_road', 'bicycle_network': 'icn'})

# Way: 198th Street (138388021) http://www.openstreetmap.org/way/138388021
test.assert_has_feature(
    16, 10435, 22457, 'roads',
    { 'id': 138388021, 'kind': 'major_road', 'bicycle_network': 'icn', 'cycleway': 'shared_lane'})

# Way: 232603515 http://www.openstreetmap.org/way/232603515
test.assert_has_feature(
    16, 18735, 25114, 'roads',
    { 'id': 232603515, 'kind': 'minor_road', 'bicycle_network': 'ncn', 'oneway': 'yes'})

# Way: Longleaf Trace (165276857) http://www.openstreetmap.org/way/165276857
test.assert_has_feature(
    16, 16505, 26756, 'roads',
    { 'id': 165276857, 'kind': 'path', 'bicycle_network': 'ncn'})

# http://www.openstreetmap.org/way/44422697
test.assert_has_feature(
    16, 10509, 25377, 'roads',
    { 'id': 44422697, 'kind': 'path', 'bicycle_network': 'rcn'})

# Way: Cabrini Boulevard.
# http://www.openstreetmap.org/way/5669719
# rcn_ref=9, but not part of any relation.
test.assert_has_feature(
    16, 19307, 24607, 'roads',
    { 'id': 5669719, 'kind': 'minor_road', 'bicycle_network': 'rcn'})

# Way: 11th Street (27029204) http://www.openstreetmap.org/way/27029204#map=16/37.7700/-122.4117
test.assert_has_feature(
    16, 10483, 25332, 'roads',
    { 'id': 27029204, 'kind': 'major_road', 'bicycle_network': 'lcn', 'cycleway': 'lane'})

# Way: Boulge Road
# http://www.openstreetmap.org/way/50835689
# http://www.openstreetmap.org/relation/2767188
test.assert_has_feature(
    16, 33002, 21613, 'roads',
    { 'id': 50835689, 'kind': 'minor_road', 'bicycle_network': 'icn'})

# Way: West National Ave (95578389)
# http://www.openstreetmap.org/way/95578389
# http://www.openstreetmap.org/relation/3318923
test.assert_has_feature(
    16, 16842, 24939, 'roads',
    { 'id': 95578389, 'kind': 'major_road', 'bicycle_network': 'ncn'})

# Way: Kananaskis Trail (385652955)
# http://www.openstreetmap.org/way/385652955
# http://www.openstreetmap.org/relation/5737942
test.assert_has_feature(
    16, 11818, 22039, 'roads',
    { 'id': 385652955, 'kind': 'major_road', 'bicycle_network': 'rcn'})

# Way: Foothill Expressway (173846425)
# http://www.openstreetmap.org/way/173846425
# http://www.openstreetmap.org/relation/1204994
test.assert_has_feature(
    16, 10535, 25419, 'roads',
    { 'id': 173846425, 'kind': 'major_road', 'bicycle_network': 'lcn'})

# http://www.openstreetmap.org/way/255652148
test.assert_has_feature(
    16, 10487, 25333, 'roads',
    { 'id': 255652148, 'kind': 'path', 'segregated': True})

# http://www.openstreetmap.org/way/215528939
test.assert_no_matching_feature(
    16, 10486, 25331, 'roads', { 'segregated': 'no'})

# Way: Post Street (28841123) http://www.openstreetmap.org/way/28841123
test.assert_has_feature(
    16, 10484, 25327, 'roads',
    { 'id': 28841123, 'is_bicycle_related': True })

# Way: 301442215 http://www.openstreetmap.org/way/301442215
test.assert_has_feature(
    16, 34748, 22664, 'roads',
    { 'id': 301442215, 'is_bicycle_related': True })

# Way: 428306786 http://www.openstreetmap.org/way/428306786
test.assert_has_feature(
    16, 18649, 25417, 'roads',
    { 'id': 428306786, 'is_bicycle_related': True })
