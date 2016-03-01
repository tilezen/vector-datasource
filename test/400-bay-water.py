# osm_id: 43950409 name: San Pablo Bay
assert_has_feature(
    14, 2623, 6318, 'water',
    { 'kind': 'bay', 'label_placement': 'yes' })

# osm_id: -1019862, name: Sansum Narrows
assert_has_feature(
    11, 321, 705, 'water',
    { 'kind': 'strait', 'label_placement': 'yes' })

# None in North America?
# osm_id: -1451065 name: Horsens Fjord
#assert_has_feature(
#    14, 8645, 5114, 'water',
#    { 'kind': 'fjord', 'label_placement': 'yes' })
