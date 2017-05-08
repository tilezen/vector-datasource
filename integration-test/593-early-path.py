# highway=path, with route national (Pacific Crest Trail)
# https://www.openstreetmap.org/way/236361475
# https://www.openstreetmap.org/relation/1225378
test.assert_has_feature(
11, 345, 790, 'roads',
{ 'walking_network': 'nwn',
  'walking_shield_text': 'PCT' })

# highway=path, with route regional (Merced Pass Trail)
# https://www.openstreetmap.org/way/373491941
# https://www.openstreetmap.org/relation/5549623
test.assert_has_feature(
	12, 687, 1584, 'roads',
	{'kind_detail': 'path', 'name': None, 'walking_network': None})

# highway=path, with route regional (Merced Pass Trail)
# https://www.openstreetmap.org/way/39996451
# https://www.openstreetmap.org/relation/5549623
test.assert_has_feature(
	12, 688, 1584, 'roads',
	{'kind_detail': 'path', 'name': None, 'walking_network': None})

# highway=path, no route, but has name (Upper Yosemite Falls Trail)
# https://www.openstreetmap.org/way/162322353
test.assert_has_feature(
	13, 1374, 3166, 'roads',
	{'kind_detail': 'path', 'name': None})
