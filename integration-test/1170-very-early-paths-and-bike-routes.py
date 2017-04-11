# highway=path, with route national (Pacific Crest Trail) at zoom 9
# https://www.openstreetmap.org/way/236361475
# https://www.openstreetmap.org/relation/1225378
assert_has_feature(
    9, 86, 197, 'roads',
    { 'kind': 'path', 'walking_network': 'nwn'})

# highway=path, with route regional (Merced Pass Trail) at zoom 10
# https://www.openstreetmap.org/way/373491941
# https://www.openstreetmap.org/relation/5549623
#assert_has_feature(
#    10, 171, 396, 'roads',
#    { 'kind': 'path', 'walking_network': 'rwn'})

# highway=path, with route regional (Merced Pass Trail) at zoom 10
# https://www.openstreetmap.org/way/39996451
# https://www.openstreetmap.org/relation/5549623
#assert_has_feature(
#    10, 172, 396, 'roads',
#    { 'kind': 'path', 'walking_network': 'rwn'})

# highway=unclassified, with route local (Grant Avenue) at zoom 12
# part of The Barbary Coast Trail in San Francisco
# https://www.openstreetmap.org/way/91181758
# https://www.openstreetmap.org/relation/6322028
#assert_has_feature(
#    12, 688, 1584, 'roads',
#    { 'kind': 'minor_road', 'walking_network': 'lwn'})

# Way: Clara-Immerwahr-Straße (287167007)
# icn=yes is marked on the way
# http://www.openstreetmap.org/way/287167007
# assert_has_feature(
#     8, 134, 85, 'roads',
#     { 'kind': 'minor_road', 'bicycle_network': 'icn'})

# Ferry between Denmark and Germany, icn
# https://www.openstreetmap.org/way/128631318
# https://www.openstreetmap.org/relation/721738
#assert_has_feature(
#     8, 136, 81, 'roads',
#     { 'kind': 'ferry', 'bicycle_network': 'icn'})

# Søndervangsvej minor road in Denmark as national cycle route
# https://www.openstreetmap.org/way/149701891
# https://www.openstreetmap.org/relation/349521
assert_has_feature(
    8, 136, 79, 'roads',
    { 'kind': 'minor_road', 'bicycle_network': 'ncn'})

# Part of Bay Trail in South (San Francisco) Bay
# way is marked rcn=yes, and part of a proper bike relation
# http://www.openstreetmap.org/way/44422697
# http://www.openstreetmap.org/relation/325779
assert_has_feature(
    10, 164, 396, 'roads',
    { 'kind': 'path', 'bicycle_network': 'rcn'})

# Hyltebjerg Allé residential road with rcn in Copenhagen
# https://www.openstreetmap.org/way/2860759
# https://www.openstreetmap.org/relation/2087590
assert_has_feature(
    10, 1095, 641, 'roads',
    { 'kind': 'minor_road', 'bicycle_network': 'rcn'})

# lcn in Seattle (living street that would only be visible at zoom 13 otherwise) at zoom 11
# https://www.openstreetmap.org/way/6477775
# https://www.openstreetmap.org/relation/3541926
assert_has_feature(
    11, 327, 715, 'roads',
    { 'kind': 'minor_road', 'bicycle_network': 'lcn'})

# Kirkham Street lcn in San Francisco at zoom 11
# https://www.openstreetmap.org/way/89802424
# https://www.openstreetmap.org/relation/32313
assert_has_feature(
    11, 327, 791, 'roads',
    { 'kind': 'minor_road', 'bicycle_network': 'lcn'})

# Asiatisk Plads service road with lcn in Copenhagen
# https://www.openstreetmap.org/way/164049387
# https://www.openstreetmap.org/relation/6199242
assert_has_feature(
    11, 1095, 641, 'roads',
    { 'kind': 'minor_road', 'bicycle_network': 'lcn'})
