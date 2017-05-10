# Example Stanislaus National Forest in California near Yosemite should be
# kind:forest.
#
# http://www.openstreetmap.org/relation/972008
test.assert_has_feature(
    11, 340, 788, 'landuse',
    { 'kind': 'forest', 'id': -972008 })

# But this other Humboldt forest in Nevada has protect_class 5 so that's not
# guaranteed, should be kind:forest.
#
# http://www.openstreetmap.org/relation/2389847
test.assert_has_feature(
    11, 369, 769, 'landuse',
    { 'kind': 'forest', 'id': -2389847 })

# leisure=nature_reserve in Smith River is already taken care of by operator
# (should be kind:forest).
#
# http://www.openstreetmap.org/relation/6213964
test.assert_has_feature(
    14, 2559, 6099, 'landuse',
    { 'kind': 'forest', 'id': -6213964 })

# Counter example is Mojave National Preserve which is operated by United
# States National Park Service so we don't want it to become a forest (it
# should be kind:national_park).
#
# http://www.openstreetmap.org/relation/175098
test.assert_has_feature(
    12, 733, 1617, 'landuse',
    { 'kind': 'national_park', 'id': -175098 })

# Point Reyes is also leisure=nature_reserve but without an operator but with
# a protect_class of 2 (it should be kind:national_park, but might need some
# data work?), until data is fixed I think it'd come thru as
# kind:nature_reserve?
#
# http://www.openstreetmap.org/relation/1250137
test.assert_has_feature(
    15, 5192, 12627, 'landuse',
    { 'kind': 'national_park', 'id': -1250137 })

# leisure=park in San Luis Reservoir State Recreational Area has
# boundary=national_park and leisure=park and park:type=state_recreational_area
# and no protect_class. This shouldn't be a kind national_park, just a
# kind:park!
#
# http://www.openstreetmap.org/relation/3004556
test.assert_has_feature(
    15, 5359, 12747, 'landuse',
    { 'kind': 'park', 'id': -3004556 })

# Example forest in Colorado that only gets demoted because of protect_class
# is present as 6 but operator is missing. Gets demoted to what, though?
# propose kind:park since there isn't an operator to say forest, and it's not
# a national park. Alternatively boundary:type=protected_area could give us
# kind: protected_area instead.
#
# This feature also has protection_title=National Forest, and the name is
# "Arapaho National Forest", so it should probably be classed as a forest.
#
# http://www.openstreetmap.org/relation/396026
test.assert_has_feature(
    13, 1683, 3103, 'landuse',
    { 'kind': 'forest', 'id': -396026 })

# leisure=nature_reserve in North Farallon Islands State Marine Reserve has
# boundary=protected_area with protect_class=4 in tile 11/323/791. It's
# operator=California Department of Fish & Wildlife so we'd just want this to
# be kind:nature_reserve.
#
# https://www.openstreetmap.org/way/436801947
test.assert_has_feature(
    11, 323, 791, 'landuse',
    { 'kind': 'nature_reserve', 'id': 436801947 })

# leisure=nature_reserve in Mount Tamalpais Watershed has
# boundary=national_park with boundary:type=protected_area and operator=Marin
# Municipal Water District and protect_class=4. It should just be
# kind:nature_reserve.
#
# https://www.openstreetmap.org/way/297463477
test.assert_has_feature(
    13, 1305, 3161, 'landuse',
    { 'kind': 'nature_reserve', 'id': 297463477 })

# leisure=common in Blithedale Summit Open Space Preserve with
# boundary=national_park and boundary:type=protected_area and protect_class=5
# and operator=Marin County Parks should just be kind:common.
#
# https://www.openstreetmap.org/way/297452972
test.assert_has_feature(
    15, 5229, 12648, 'landuse',
    { 'kind': 'common', 'id': 297452972 })

# leisure=nature_reserve in Glen Canyon National Recreation Area with
# boundary=national_park and boundary:type=protected_area and protect_class=5
# and protection_title=National Recreation Area which I think should default
# to kind:nature_reserve.
#
# http://www.openstreetmap.org/relation/5273153
test.assert_has_feature(
    12, 784, 1585, 'landuse',
    { 'kind': 'nature_reserve', 'id': -5273153 })

# leisure=nature_reserve in Parque Natural Sierra de Andújar with finally
# kind:nature_reserve.
#
# https://www.openstreetmap.org/way/373769670
test.assert_has_feature(
    13, 4003, 3151, 'landuse',
    { 'kind': 'nature_reserve', 'id': 373769670 })

# boundary=protected_area in Naturpark Steigerwald with protect_class=5
# should end up with kind: protected_area
#
# https://www.openstreetmap.org/relation/3875431
test.assert_has_feature(
    13, 4336, 2787, 'landuse',
    { 'kind': 'protected_area', 'id': -3875431 })

# boundary=national_park in Muir Woods National Monument with
# leisure=nature_reserve and operator=National Park Service and
# protect_class=3 should end up with kind:national_park
#
# https://www.openstreetmap.org/relation/6229828
test.assert_has_feature(
    16, 10452, 25302, 'landuse',
    { 'kind': 'national_park', 'id': -6229828 })

# leisure=park in Henry W. Coe State Park with boundary=protected_area and
# protect_class=5 should end up with kind:park.
#
# https://www.openstreetmap.org/relation/318202
test.assert_has_feature(
    13, 1332, 3184, 'landuse',
    { 'kind': 'park', 'id': -318202 })

# operator=United States National Park Service and protect_class=2 in
# Yosemite National Park with boundary=national_park and
# leisure=nature_reserve should end up with kind:national_park.
#
# https://www.openstreetmap.org/relation/1643367
test.assert_has_feature(
    13, 1371, 3164, 'landuse',
    { 'kind': 'national_park', 'id': -1643367 })

# operator=United States National Park Service and protect_class=2 in Redwood
# National Park with boundary=national_park and leisure=nature_reserve should
# end up with kind:national_park.
#
# https://www.openstreetmap.org/relation/215231
test.assert_has_feature(
    13, 1274, 3066, 'landuse',
    { 'kind': 'national_park', 'id': -215231 })

# operator=United States National Park Service and protect_class=2 in
# Yellowstone National Park with boundary=national_park and
# leisure=nature_reserve should end up with kind:national_park.
#
# https://www.openstreetmap.org/relation/1453306
test.assert_has_feature(
    13, 1591, 2972, 'landuse',
    { 'kind': 'national_park', 'id': -1453306 })

# boundary=national_park in Adirondack Park should end up with kind:park.
#
# https://www.openstreetmap.org/relation/1695394
test.assert_has_feature(
    13, 2410, 3001, 'landuse',
    { 'kind': 'park', 'id': -1695394 })

# operator=United States National Park Service and protect_class=2 in
# Shenandoah National Park with boundary=national_park and leisure=park should
# end up with kind:national_park.
#
# https://www.openstreetmap.org/relation/5548542
test.assert_has_feature(
    13, 2313, 3142, 'landuse',
    { 'kind': 'national_park', 'id': -5548542 })

# designation=national_park in Cairngorms National Park with
# boundary=national_park should end up with kind:national_park.
#
# https://www.openstreetmap.org/relation/1947603
test.assert_has_feature(
    13, 4014, 2512, 'landuse',
    { 'kind': 'national_park', 'id': -1947603 })

# boundary=national_park in North Wessex Downs AONB with
# designation=area_of_outstanding_natural_beauty should end up with kind:park.
#
# https://www.openstreetmap.org/relation/2904192
test.assert_has_feature(
    13, 4054, 2728, 'landuse',
    { 'kind': 'park', 'id': -2904192 })

# operator:en=Parks Canada and boundary=national_park in Riding Mountain
# National Park with leisure=nature_reserve.
#
# http://www.openstreetmap.org/way/185735773
test.assert_has_feature(
    13, 1812, 2748, 'landuse',
    { 'kind': 'national_park', 'id': 185735773 })
