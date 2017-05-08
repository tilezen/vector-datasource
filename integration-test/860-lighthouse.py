# update lighthouse zoom to 15 and if attraction zoom to 14

# lighthouse with tourism = attraction
# https://www.openstreetmap.org/way/423023928
test.assert_has_feature(
    14, 2615, 6330, 'pois',
    {'id': 423023928, 'kind': 'lighthouse'})

# lighthouse without tourism = attraction
# http://www.openstreetmap.org/node/1243877573
test.assert_no_matching_feature(
    14, 2617, 6329, 'pois',
    {'id': 1243877573, 'kind': 'lighthouse'})

test.assert_has_feature(
    15, 5235, 12659, 'pois',
    {'id': 1243877573, 'kind': 'lighthouse'})