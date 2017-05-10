# http://www.openstreetmap.org/way/397268717
# http://www.openstreetmap.org/relation/2996736
test.assert_has_feature(
    16, 10484, 25339, 'roads',
    { 'is_bus_route': True, 'name': 'Industrial St.' })

# http://www.openstreetmap.org/way/32929419
# http://www.openstreetmap.org/relation/3412979
test.assert_has_feature(
    16, 10477, 25333, 'roads',
    { 'is_bus_route': True, 'name': 'Clayton St.' })

# http://www.openstreetmap.org/way/254756528
# http://www.openstreetmap.org/relation/3413068
test.assert_has_feature(
    16, 10477, 25326, 'roads',
    { 'is_bus_route': True, 'name': 'Union St.' })
