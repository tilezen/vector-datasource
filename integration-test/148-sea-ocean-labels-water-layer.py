# ocean and sea labels should be in the water layer rather than the places
# layer.

## Gulf of California: http://www.openstreetmap.org/node/305639734
test.assert_has_feature(
    9, 97, 215, 'water',
    {'kind': 'sea', 'name': 'Gulf of California', 'label_placement': True})
test.assert_no_matching_feature(
    9, 97, 215, 'places',
    {'kind': 'sea', 'name': 'Gulf of California'})

## Greenland Sea: http://www.openstreetmap.org/node/305639396
test.assert_has_feature(
    9, 241, 90, 'water',
    {'kind': 'sea', 'name': 'Greenland Sea', 'label_placement': True})
test.assert_no_matching_feature(
    9, 241, 90, 'places',
    {'kind': 'sea', 'name': 'Greenland Sea'})

## NOTE: No ocean points in the North America extract :-(
