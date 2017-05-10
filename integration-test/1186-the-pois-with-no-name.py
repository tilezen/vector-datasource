# this is a collection of features which have no name and therefore should be
# excluded from being POIs.

# originally from 440-zoos-and-other-attractions-tourism.py
#https://www.openstreetmap.org/node/1589837084
# unnamed, CO
test.assert_no_matching_feature(
    16, 13686, 24901, 'pois',
    { 'id': 1589837084 })

# originally from 526-inclusive-pois.py
#https://www.openstreetmap.org/node/1460537343
test.assert_no_matching_feature(
    16, 10470, 25342, 'pois',
    { 'id': 1460537343 })

#https://www.openstreetmap.org/node/3879177193
test.assert_no_matching_feature(
    16, 10533, 22894, 'pois',
    { 'id': 3879177193 })

# originally from 602-add-boat-rental.py
#    [16, 16679, 24763], # node 2420432693 shop=boat_rental
#    [16, 13323, 21679], # node 2911709060 amenity=boat_rental
#    [16, 10503, 25310], # node 3509468126 rental=boat

# originally from 663-combo-outdoor-landuse-pois.py
#https://www.openstreetmap.org/relation/6328943
# Cox Stadium recreation track
test.assert_no_matching_feature(
    16, 10471, 25342, 'pois',
    { 'id': -6328943 })
#https://www.openstreetmap.org/node/3643451363
# unnamed running track
test.assert_no_matching_feature(
    16, 10962, 25007, 'pois',
    { 'id': 3643451363 })

# originally from 742-predictable-layers-pois.py
# Way:79457493 Grave_yard in POIS
# http://www.openstreetmap.org/way/79457493
test.assert_no_matching_feature(
    15, 5240, 12666, 'pois',
    {'id': 79457493})
# Way:64296322 landuse: Forest in POIS
# http://www.openstreetmap.org/way/64296322
test.assert_no_matching_feature(
    10, 163, 392, 'pois',
    {'id': 64296322})
# Node:2148541212 natural: Forest in POIS
# http://www.openstreetmap.org/node/2148541212
test.assert_no_matching_feature(
    14, 3942, 5901, 'pois',
    {'id': 2148541212})
# Node:4206408136 park in POIS
# http://www.openstreetmap.org/node/4206408136
test.assert_no_matching_feature(
    14, 2619, 6333, 'pois',
    {'id': 4206408136})
# Node:4076680383 protected_area in POIS
# http://www.openstreetmap.org/node/4076680383
test.assert_no_matching_feature(
    14, 2809, 6074, 'pois',
    {'id': 4076680383})
# Way:86285084 recreation_ground in POIS
# http://www.openstreetmap.org/way/86285084
test.assert_no_matching_feature(
    14, 2619, 6334, 'pois',
    {'id': 86285084})
# Node:582131344 recreation_ground in POIS
# http://www.openstreetmap.org/node/582131344
test.assert_no_matching_feature(
    14, 2621, 6331, 'pois',
    {'id': 582131344})
# Way:28694608 village_green in POIS
# http://www.openstreetmap.org/way/28694608
test.assert_no_matching_feature(
    14, 2618, 6334, 'pois',
    {'id': 28694608})
# Node:3367407023 water_works in POIS
# http://www.openstreetmap.org/node/3367407023
test.assert_no_matching_feature(
    14, 2627, 6346, 'pois',
    {'id': 3367407023})
# Way:207859675 landuse: wood in POIS
# http://www.openstreetmap.org/way/207859675
test.assert_no_matching_feature(
    14, 2826, 6549, 'pois',
    {'id': 207859675})
# Way:372445925 natural: wood in POIS
# http://www.openstreetmap.org/way/372445925
test.assert_no_matching_feature(
    14, 2618, 6330, 'pois',
    {'id': 372445925})
# Way:164878781 works in POIS
# http://www.openstreetmap.org/way/164878781
test.assert_no_matching_feature(
    13, 1429, 3247, 'pois',
    {'id': 164878781 })
