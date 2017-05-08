# update windmill zoom to 15 and if attraction zoom to 14

# windmill with tourism = attraction
# http://www.openstreetmap.org/way/287921407
test.assert_has_feature(
    14, 2616, 6333, 'pois',
    {'id': 287921407, 'kind': 'windmill'})

# windmill without tourism = attraction
# http://www.openstreetmap.org/node/2304462088
test.assert_no_matching_feature(
    14, 2675, 6412, 'pois',
    {'id': 2304462088, 'kind': 'windmill'})

test.assert_has_feature(
    15, 5350, 12824, 'pois',
    {'id': 2304462088, 'kind': 'windmill'})