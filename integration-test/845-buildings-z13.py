# Earlier work in 845 dropped buildings from zoom 13

# http://www.openstreetmap.org/way/23654700
# http://www.openstreetmap.org/way/60500069
test.assert_has_feature(
    13, 1310, 3170, 'buildings',
    {'kind': 'building'})
