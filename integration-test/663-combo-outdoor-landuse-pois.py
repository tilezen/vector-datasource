#http://www.openstreetmap.org/way/31198945
# Waterworld in Concord
assert_has_feature(
    13, 1318, 3160, 'landuse',
    { 'kind': 'water_park', 'sort_key': 107 })

assert_has_feature(
    13, 1318, 3160, 'pois',
    { 'kind': 'water_park', 'min_zoom': 13 })

#http://www.openstreetmap.org/node/2753215890
# Antioch WaterPark
assert_has_feature(
    16, 10600, 25287, 'pois',
    { 'kind': 'water_park', 'min_zoom': 15 })



#http://www.openstreetmap.org/way/381817396
# Sandos Finisterra Los Cabos, extra large resort
assert_has_feature(
    14, 3189, 7122, 'pois',
    { 'kind': 'beach_resort', 'min_zoom': 14 })

#http://www.openstreetmap.org/node/2407351205
# Hilton Hawaiian Village
# really this should be merged with its large AOI!
assert_has_feature(
    16, 4034, 28801, 'pois',
    { 'kind': 'beach_resort', 'min_zoom': 16 })

#http://www.openstreetmap.org/node/3575812477
# Silver Gull Beach Club
assert_has_feature(
    16, 19314, 24677, 'pois',
    { 'kind': 'beach_resort', 'min_zoom': 16 })

# https://www.openstreetmap.org/way/381817391
# Terrasol Beach Resort
# Needs to appear **before** tourism=hotel
assert_has_feature(
    16, 12760, 28488, 'pois',
    { 'id': 381817391, 'kind': 'beach_resort'})


#https://www.openstreetmap.org/way/257716817
# Needs to appear **after** natural=beach.
# Unnamed beach in Maskenthine Lake area
assert_has_feature(
    16, 15066, 24333, 'landuse',
    { 'kind': 'beach', 'id': 257716817 })



#https://www.openstreetmap.org/node/3655879348
# Camp Ahmek
assert_has_feature(
    15, 9219, 11714, 'pois',
    { 'kind': 'summer_camp', 'min_zoom': 15 })

#https://www.openstreetmap.org/node/4050178586
# Camp Goodtimes
assert_has_feature(
    15, 5225, 11211, 'pois',
    { 'kind': 'summer_camp', 'min_zoom': 15 })



#https://www.openstreetmap.org/node/3838356961
# Battle of Blackburn's Ford (1861)
assert_has_feature(
    16, 18668, 25092, 'pois',
    { 'kind': 'battlefield', 'min_zoom': 17 })

#https://www.openstreetmap.org/node/3992988013
# 2nd Battle of Kernstown
assert_has_feature(
    16, 18532, 25013, 'pois',
    { 'kind': 'battlefield', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/231393152
# Antietam National Battlefield
assert_has_feature(
    10, 290, 389, 'pois',
    { 'kind': 'battlefield', 'min_zoom': 10 })

assert_has_feature(
    10, 290, 389, 'landuse',
    { 'kind': 'battlefield', 'sort_key': 25 })


#http://www.openstreetmap.org/way/316054549
# White Oak Road Battlefield
assert_has_feature(
    11, 582, 796, 'pois',
    { 'kind': 'battlefield', 'min_zoom': 10.0683 })

assert_has_feature(
    11, 582, 796, 'landuse',
    { 'kind': 'battlefield', 'sort_key': 25 })



#https://www.openstreetmap.org/node/2117389172
# unnamed Boat Storage
assert_has_feature(
    16, 10563, 25453, 'pois',
    { 'kind': 'boat_storage', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/261064362
# in Tiburon, CA
assert_has_feature(
    16, 10476, 25304, 'pois',
    { 'kind': 'boat_storage', 'min_zoom': 17 })



#https://www.openstreetmap.org/node/3314950786
# Red Cross monument in DC
assert_has_feature(
    16, 18742, 25070, 'pois',
    { 'kind': 'monument', 'min_zoom': 17 })

#https://www.openstreetmap.org/node/2316449632
# Major General James B. McPherson in DC
assert_has_feature(
    16, 18744, 25069, 'pois',
    { 'kind': 'monument', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/41273627
# polygon but no landuse / Netherlands Carillon near DC
assert_has_feature(
    16, 18737, 25072, 'pois',
    { 'kind': 'monument', 'min_zoom': (lambda z: z >= 16 and z < 17) })

#https://www.openstreetmap.org/way/248460669
# building, Jefferson Monument
assert_has_feature(
    15, 9371, 12537, 'pois',
    { 'kind': 'monument', 'min_zoom': 15 })

#https://www.openstreetmap.org/way/66418767
# building, and tourism=attraction, National World War II Memorial
assert_has_feature(
    15, 9371, 12536, 'pois',
    { 'kind': 'monument', 'min_zoom': 15 })



#https://www.openstreetmap.org/node/358811238
# Letts Valley 1-039 Dam
assert_has_feature(
    14, 2607, 6243, 'pois',
    { 'kind': 'dam', 'min_zoom': 14 })

#https://www.openstreetmap.org/way/189656737
# O'Shaughnessy Dam, Yosemite
# 13, 1370, 3161
assert_has_feature(
    12, 685, 1580, 'landuse',
    { 'kind': 'dam', 'sort_key': 223 })

assert_has_feature(
    12, 685, 1580, 'pois',
    { 'kind': 'dam', 'min_zoom': 12 })

#https://www.openstreetmap.org/way/62201624
# Named dam line in front of Cherry Lake
# Should be labeled in the stylesheet, no POI generate
assert_has_feature(
    12, 683, 1580, 'landuse',
    { 'kind': 'dam', "sort_key": 265 })


#http://www.openstreetmap.org/node/262220409
# Indian Lake Dog Exercise Area, near Madison, WI
assert_has_feature(
    16, 16450, 24033, 'pois',
    { 'kind': 'dog_park', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/417184097
# Dog Run at Upper Noe Valley Rec Center, SF
assert_has_feature(
    16, 10480, 25338, 'pois',
    { 'kind': 'dog_park', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/375333476
# Dog park at Walter Hass Playground, SF
assert_has_feature(
    16, 10479, 25338, 'pois',
    { 'kind': 'dog_park', 'min_zoom': 16 })

assert_has_feature(
    16, 10479, 25338, 'landuse',
    { 'kind': 'dog_park', 'sort_key': 97 })


#https://www.openstreetmap.org/relation/6328943
# Cox Stadium recreation track
assert_has_feature(
    15, 5235, 12671, 'landuse',
    { 'id': -6328943, 'kind': 'recreation_track', 'sort_key': 59 })

# Cox Stadium recreation track
assert_has_feature(
    16, 10471, 25342, 'pois',
    { 'id': -6328943, 'kind': 'recreation_track', 'min_zoom': 16 })

#https://www.openstreetmap.org/node/3643451363
# unnamed running track
assert_has_feature(
    16, 10962, 25007, 'pois',
    { 'kind': 'recreation_track', 'min_zoom': 17 })

#https://www.openstreetmap.org/node/418185265
# cycle, Sand Pit
assert_has_feature(
    16, 10556, 25509, 'pois',
    { 'kind': 'recreation_track', 'min_zoom': 17 })

#https://www.openstreetmap.org/node/444949878
# motor, Mazda Raceway Laguna Seca
assert_has_feature(
    16, 10603, 25602, 'pois',
    { 'kind': 'recreation_track', 'min_zoom': 17 })



#https://www.openstreetmap.org/node/2613055910
# Unnamed fishing spot near Davis, CA
assert_has_feature(
    16, 10602, 25159, 'pois',
    { 'kind': 'fishing_area', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/62099107
#    16, 10471, 22459, 'pois',
assert_has_feature(
    16, 10471, 22460, 'pois',
    { 'kind': 'fishing_area', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/234164554
# Alpine Lake
assert_has_feature(
    16, 12454, 24647, 'pois',
    { 'kind': 'fishing_area', 'min_zoom': 16 })



#https://www.openstreetmap.org/node/3733554139
# Seneca Rocks
assert_has_feature(
    16, 18319, 25083, 'pois',
    { 'kind': 'swimming_area', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/368533731
# Pine Lake Swimming Beach
assert_has_feature(
#    16, 10551, 22893, 'pois',
    16, 10551, 22892, 'pois',
    { 'kind': 'swimming_area', 'min_zoom': 16 })

#https://www.openstreetmap.org/node/3733554139
# Swimming hole at Seneca Rocks
assert_has_feature(
    16, 18319, 25083, 'pois',
    { 'kind': 'swimming_area', 'min_zoom': 16 })



#https://www.openstreetmap.org/node/3795571179
# UC Berkeley area
assert_has_feature(
    16, 10509, 25309, 'pois',
    { 'kind': 'firepit', 'min_zoom': 18 })

#https://www.openstreetmap.org/way/349337076
# Bloomfield area
assert_has_feature(
    16, 10742, 24971, 'pois',
    { 'kind': 'firepit', 'min_zoom': 18 })




#https://www.openstreetmap.org/way/329837642
# Old Man Boulder
assert_has_feature(
    16, 10442, 25304, 'landuse',
    { 'kind': 'stone', 'sort_key': 28 })

assert_has_feature(
    16, 10442, 25304, 'pois',
    { 'kind': 'stone', 'min_zoom': 17, 'name': 'Old Man Boulder' })



#https://www.openstreetmap.org/way/377706598
# Goodrich Pinnacle
assert_has_feature(
    16, 11001, 25340, 'landuse',
    { 'kind': 'rock', 'sort_key': 27 })

assert_has_feature(
    16, 11001, 25340, 'pois',
    { 'kind': 'rock', 'min_zoom': 17, 'name': 'Goodrich Pinnacle' })



#https://www.openstreetmap.org/node/2246385222
# Redwood Acres RV Park, Eureka CA
assert_has_feature(
    15, 5085, 12312, 'pois',
    { 'kind': 'caravan_site', 'min_zoom': 15 })

#https://www.openstreetmap.org/way/291546386
# Pillar Point RV Park
assert_has_feature(
    14, 2618, 6348, 'landuse',
    { 'kind': 'caravan_site', 'sort_key': 58 })

assert_has_feature(
    14, 2618, 6348, 'pois',
    { 'kind': 'caravan_site', 'min_zoom': 14 })



#https://www.openstreetmap.org/node/2401887217
# South Park, SF
assert_has_feature(
    16, 10486, 25329, 'pois',
    { 'kind': 'picnic_site', 'min_zoom': 16 })

#https://www.openstreetmap.org/node/3297410094
# Why is this missing?
# Golden Gate Park, SF
assert_has_feature(
    16, 10472, 25332, 'pois',
    { 'kind': 'picnic_site', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/400701941
# Golden Gate Park, SF
assert_has_feature(
    16, 10474, 25332, 'landuse',
    { 'kind': 'picnic_site', 'sort_key': 108 })

assert_has_feature(
    16, 10474, 25332, 'pois',
    { 'kind': 'picnic_site', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/231863022
# building, South Park, SF
assert_has_feature(
    16, 10486, 25329, 'pois',
    { 'kind': 'picnic_site', 'min_zoom': 16, 'id': 231863022 })



#https://www.openstreetmap.org/node/1148222790
# Fort Strong
assert_has_feature(
    16, 19850, 24247, 'pois',
    { 'kind': 'fort', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/265893625
# Battery 2
assert_has_feature(
    16, 19303, 24607, 'landuse',
    { 'kind': 'fort', 'sort_key': 47 })

assert_has_feature(
    16, 19303, 24607, 'pois',
    { 'kind': 'fort', 'min_zoom': (lambda z: z >= 15 and z < 16) })

#https://www.openstreetmap.org/way/51064272
# Fort Monroe
assert_has_feature(
    13, 2359, 3188, 'landuse',
    { 'kind': 'fort' })

assert_has_feature(
    13, 2359, 3188, 'pois',
	{ 'kind': 'fort', 'min_zoom': 13, 'name': 'Fort Monroe' })
