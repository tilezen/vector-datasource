# highway=path, with route inter-national
# GR5-Grand Traverse de Jura between France and Switzerland
# https://www.openstreetmap.org/way/285975282
# https://www.openstreetmap.org/relation/6009161
test.assert_has_feature(
    9, 265, 179, 'roads',
    { 'kind': 'path', 'walking_network': 'iwn' } )

# highway=path, with route national (Pacific Crest Trail) at zoom 9
# https://www.openstreetmap.org/way/236361475
# https://www.openstreetmap.org/relation/1225378
test.assert_has_feature(
    9, 86, 197, 'roads',
    { 'kind': 'path', 'walking_network': 'nwn' } )

# highway=path, with route regional (Merced Pass Trail) at zoom 11
# https://www.openstreetmap.org/way/373491941
# https://www.openstreetmap.org/relation/5549623
test.assert_has_feature(
   11, 343, 792, 'roads',
   { 'kind': 'path', 'walking_network': 'rwn'  } )

# highway=unclassified, with route local (Grant Avenue) at zoom 12
# part of The Barbary Coast Trail in San Francisco
# https://www.openstreetmap.org/way/91181758
# https://www.openstreetmap.org/relation/6322028
test.assert_has_feature(
   12, 655, 1582, 'roads',
   { 'kind': 'minor_road', 'walking_network': 'lwn' } )


# Strøby Bygade secondary road part of international cycle network
# https://www.openstreetmap.org/way/378138944
# https://www.openstreetmap.org/relation/1737354
# https://www.openstreetmap.org/relation/28441
# https://www.openstreetmap.org/relation/2689634
# https://www.openstreetmap.org/relation/2749837
# https://www.openstreetmap.org/relation/36778
# https://www.openstreetmap.org/relation/721738
test.assert_has_feature(
    8, 136, 80, 'roads',
    { 'kind': 'major_road', 'kind_detail': 'secondary',
      'is_bicycle_related': True, 'bicycle_network': 'icn' })

# Sundbylillevej tertiary road part of national cycle network
# https://www.openstreetmap.org/way/28273516
# https://www.openstreetmap.org/relation/26863
test.assert_has_feature(
    8, 136, 79, 'roads',
    { 'kind': 'major_road', 'kind_detail': 'tertiary',
      'is_bicycle_related': True, 'bicycle_network': 'ncn' })

# Way: North Sea Cycle Route - part Netherlands (1977662)
# A really long highway=cycleway
# https://www.openstreetmap.org/way/35568189
# https://www.openstreetmap.org/relation/1977662
# https://www.openstreetmap.org/relation/1975739
# https://www.openstreetmap.org/relation/5294
# https://www.openstreetmap.org/relation/537418
test.assert_has_feature(
    8, 131, 83, 'roads',
    { 'kind': 'path', 'is_bicycle_related': True, 'bicycle_network': 'icn' })

# Ferry between Denmark and Germany, icn
# https://www.openstreetmap.org/way/128631318
# https://www.openstreetmap.org/relation/721738
test.assert_has_feature(
    8, 136, 81, 'roads',
    { 'kind': 'ferry', 'is_bicycle_related': True, 'bicycle_network': 'icn' })

# Søndervangsvej minor road in Denmark as national cycle route
# https://www.openstreetmap.org/way/149701891
# https://www.openstreetmap.org/relation/349521
test.assert_has_feature(
    8, 136, 79, 'roads',
    { 'kind': 'minor_road', 'is_bicycle_related': True, 'bicycle_network': 'ncn' })

# Part of Bay Trail in South (San Francisco) Bay
# way is marked rcn=yes, and part of a proper bike relation
# http://www.openstreetmap.org/way/44422697
# http://www.openstreetmap.org/relation/325779
test.assert_has_feature(
    10, 164, 396, 'roads',
    { 'kind': 'path', 'is_bicycle_related': True, 'bicycle_network': 'rcn' })

# Hyltebjerg Allé residential road with rcn in Copenhagen
# https://www.openstreetmap.org/way/2860759
# https://www.openstreetmap.org/relation/2087590
test.assert_has_feature(
    10, 547, 320, 'roads',
    { 'kind': 'minor_road', 'is_bicycle_related': True, 'bicycle_network': 'rcn' })

# lcn in Seattle (living street that would only be visible at zoom 13 otherwise) at zoom 11
# https://www.openstreetmap.org/way/6477775
# https://www.openstreetmap.org/relation/3541926
test.assert_has_feature(
    11, 327, 715, 'roads',
    { 'kind': 'minor_road', 'bicycle_network': 'lcn' })

# Kirkham Street lcn in San Francisco at zoom 11
# https://www.openstreetmap.org/way/89802424
# https://www.openstreetmap.org/relation/32313
test.assert_has_feature(
    11, 327, 791, 'roads',
    { 'kind': 'minor_road', 'bicycle_network': 'lcn' })

# Asiatisk Plads service road with lcn in Copenhagen
# https://www.openstreetmap.org/way/164049387
# https://www.openstreetmap.org/relation/6199242
test.assert_has_feature(
    11, 1095, 641, 'roads',
    { 'kind': 'minor_road', 'bicycle_network': 'lcn' })
