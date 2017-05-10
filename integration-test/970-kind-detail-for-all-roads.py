# kind: ferry
# http://www.openstreetmap.org/way/98752535 - Alameda <-> SF Ferry bldg
test.assert_has_feature(
    16, 10487, 25326, 'roads',
    { 'kind': 'ferry', 'id': 98752535 })

# http://www.openstreetmap.org/way/98752545 - SF Pier 41 <-> SF Ferry bldg
test.assert_has_feature(
    16, 10487, 25326, 'roads',
    { 'kind': 'ferry', 'id': 98752545 })

# http://www.openstreetmap.org/way/289694213 - South SF <-> SF Ferry bldg
test.assert_has_feature(
    16, 10487, 25326, 'roads',
    { 'kind': 'ferry', 'id': 289694213 })
