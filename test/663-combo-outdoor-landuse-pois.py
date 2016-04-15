#leisure=water_park
#(`"${GREATEST(13, LEAST(zoom + 6.32, 16))}"`). Around 8,000

#http://www.openstreetmap.org/way/31198945
# Waterworld in Concord
assert_has_feature(
    13, 1318, 3160, 'landuse',
    { 'kind': 'water_park', 'sort_key': 102 })

assert_has_feature(
    13, 1318, 3160, 'pois',
    { 'kind': 'water_park', 'min_zoom': 13 })

#http://www.openstreetmap.org/node/2753215890
# Antioch WaterPark
assert_has_feature(
    16, 10600, 25287, 'pois',
    { 'kind': 'water_park', 'min_zoom': 16 })



#leisure=beach_resort
#Needs to appear **before** tourism=hotel, but **after** natural=beach.
#(`"${GREATEST(14, LEAST(zoom + 5.32, 16))}"`), without even a name. Around 2000.

#http://www.openstreetmap.org/way/381817396
# Sandos Finisterra Los Cabos, extra large resort
assert_has_feature(
    14, 3189, 7122, 'pois',
    { 'kind': 'beach_resort', 'min_zoom': 14 })

#http://www.openstreetmap.org/node/2407351205
# Hilton Hawaiian Village – really this should be merged with its large AOI
assert_has_feature(
    16, 4034, 28801, 'pois',
    { 'kind': 'beach_resort', 'min_zoom': 16 })

#http://www.openstreetmap.org/node/3575812477
# Silver Gull Beach Club
assert_has_feature(
    16, 19314, 24677, 'pois',
    { 'kind': 'beach_resort', 'min_zoom': 16 })
  
#https://www.openstreetmap.org/node/1500943741
# Needs to appear **before** tourism=hotel
# Best Western Plus Blue Sea Lodge
assert_has_feature(
    16, 11422, 26443, 'pois',
    { 'kind': 'beach_resort', 'min_zoom': 16 })
  
#https://www.openstreetmap.org/way/257716817
# Needs to appear **after** natural=beach.
# Unnamed beach in Maskenthine Lake area
assert_has_feature(
    16, 15066, 24333, 'pois',
    { 'kind': 'beach', 'id': 257716817 })

#https://www.openstreetmap.org/way/257716817
# Needs to appear **after** natural=beach.
# Unnamed beach in Maskenthine Lake area
assert_has_feature(
    16, 15066, 24333, 'landuse',
    { 'kind': 'beach', 'id': 257716817 })




#leisure=summer_camp
#zoom 15 range up to zoom 13. Around 200.
#(`"${GREATEST(14, LEAST(zoom + 5.32, 17))}"`), without even a name. Around 2000.

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



#historic=battlefield
#zoom 14 up to zoom 11? POIs default zoom 17. Around 2000.

#https://www.openstreetmap.org/node/3992988013
# 2nd Battle of Kernstown
assert_has_feature(
    16, 18532, 25013, 'pois',
    { 'kind': 'battlefield', 'min_zoom': 17 })

#https://www.openstreetmap.org/node/3838356961
# Battle of Blackburn's Ford (1861)
assert_has_feature(
    16, 18668, 25092, 'pois',
    { 'kind': 'battlefield', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/231393152
# Antietam National Battlefield
assert_has_feature(
    11, 581, 779, 'pois',
    { 'kind': 'battlefield', 'min_zoom': 11 })

assert_has_feature(
    11, 581, 779, 'landuse',
    { 'kind': 'battlefield', 'sort_key': 25 })


#amenity=boat_storage
#zoom 17. Around 30 pois, 2500 landuse.

#https://www.openstreetmap.org/node/2117389172
# unnamed Boat Storage
assert_has_feature(
    16, 10563, 25453, 'pois',
    { 'kind': 'boat_storage', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/261064362
# in Tiburon, CA
assert_has_feature(
    16, 10476, 25304, 'pois',
    { 'kind': 'boat_storage' })



#historic=monument
# needs to sort **above** tourism=attraction
#zoom 17 up to zoom 16? Sometimes buildings. Around 38,000.

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
    { 'kind': 'monument', 'min_zoom': 16 })

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




# waterway=dam
# zoom 12 or zoom 13?. Around 120,000.

#https://www.openstreetmap.org/node/358811238
# Letts Valley 1-039 Dam
assert_has_feature(
    14, 2607, 6243, 'pois',
    { 'kind': 'dam', 'min_zoom': 13 })

#https://www.openstreetmap.org/way/189656737
# O'Shaughnessy Dam, Yosemite
assert_has_feature(
    13, 1370, 3161, 'landuse',
    { 'kind': 'dam', 'min_zoom': 12, 'sort_key': 221 })

#https://www.openstreetmap.org/way/169521202
# Dam line in front of Cherry Lake
assert_has_feature(
    12, 683, 1580, 'boundaries',
    { 'kind': 'dam', 'min_zoom': 12, "sort_key": 263 })



# leisure=dog_park
# similar zoom range to park, either 16 for landuse, with zoom 17 default for POIs. Around 4600.

#https://www.openstreetmap.org/node/3646717009
# Dog Run at Upper Noe Valley Rec Center, SF
assert_has_feature(
    16, 10480, 25338, 'pois',
    { 'kind': 'dog_park', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/375333476
# Dog park at Walter Hass Playground, SF
assert_has_feature(
    16, 10479, 25338, 'pois',
    { 'kind': 'dog_park', 'min_zoom': 16 })

assert_has_feature(
    16, 10479, 25338, 'landuse',
    { 'kind': 'dog_park', 'sort_key': 92 })



# leisure=track
# pois, same zoom range as sports. Around 50,000.

#https://www.openstreetmap.org/way/387242155
# Cox Stadium at SF State
assert_has_feature(
    15, 5235, 12671, 'landuse',
    { 'kind': 'recreation_track', 'sort_key': 57 })

assert_has_feature(
    16, 10471, 25342, 'pois',
    { 'kind': 'recreation_track', 'min_zoom': 16 })

#https://www.openstreetmap.org/node/3643451363
# unnamed running track
assert_has_feature(
    16, 10962, 25007, 'pois',
    { 'kind': 'recreation_track', 'min_zoom': 17 })

#https://www.openstreetmap.org/node/418185265
# cycle, Sand Pit
assert_has_feature(
    16, 10556, 25509, 'pois',
    { 'kind': 'recreation_track', 'min_zoom': 16 })

#https://www.openstreetmap.org/node/444949878
# motor, Mazda Raceway Laguna Seca
assert_has_feature(
    16, 10603, 25602, 'pois',
    { 'kind': 'recreation_track', 'min_zoom': 17 })



# leisure=fishing
# zoom 17 default for POIs, same zoom range as marina landuse; 
# LEAST(zoom + 1.76, 15)
# related: http://wiki.openstreetmap.org/wiki/Key:fishing, do we want to only allow yes and permissive values? Around 3500.

#https://www.openstreetmap.org/node/2613055910
# Unnamed fishing spot near Davis, CA
assert_has_feature(
    16, 10602, 25159, 'pois',
    { 'kind': 'fishing', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/62099107
# 
assert_has_feature(
#    16, 10471, 22459, 'pois',
    16, 10471, 22460, 'pois',
    { 'kind': 'fishing', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/234164554
# Alpine Lake
assert_has_feature(
    16, 12454, 24647, 'pois',
    { 'kind': 'fishing', 'min_zoom': 16 })



# leisure=swimming_area
# zoom 16 for landuse and POIs. Around 360.

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

#https://www.openstreetmap.org/node/3738168752
# Lake Arrowhead
assert_has_feature(
    16, 14857, 26232, 'pois',
    { 'kind': 'swimming_area', 'min_zoom': 16 })



# leisure=firepit
# pois, zoom 18, example . Around 4000 pois, 240 landuse.

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




# natural=stone
# 1500 landuse, pois covered elsewhere

#https://www.openstreetmap.org/way/329837642
# Old Man Boulder
assert_has_feature(
    16, 10442, 25304, 'landuse',
    { 'kind': 'stone', 'sort_key': 28 })

assert_has_feature(
    16, 10442, 25304, 'pois',
    { 'kind': 'stone', 'name': true })



# natural=rock
# 7000 landuse, pois covered elsewhere

#https://www.openstreetmap.org/way/377706598
# Goodrich Pinnacle
assert_has_feature(
    16, 11001, 25340, 'landuse',
    { 'kind': 'rock', 'sort_key': 27 })

assert_has_feature(
    16, 11001, 25340, 'pois',
    { 'kind': 'rock', 'name': true })


# tourism=caravan_site
# zoom 15 up to zoom 14? Around 16,000.

#https://www.openstreetmap.org/node/2246385222
# Redwood Acres RV Park, Eureka CA
assert_has_feature(
    15, 5085, 12312, 'pois',
    { 'kind': 'caravan_site', 'min_zoom': 15 })

#https://www.openstreetmap.org/way/291546386
# Pillar Point RV Park
assert_has_feature(
    14, 2618, 6348, 'landuse',
    { 'kind': 'caravan_site', 'sort_key': 56 })

assert_has_feature(
    14, 2618, 6348, 'pois',
    { 'kind': 'caravan_site', 'min_zoom': 14 })



# tourism=picnic_site
# zoom 16. weird one with a building tag? Around 85,000.

#https://www.openstreetmap.org/node/2401887217
# South Park, SF
assert_has_feature(
    16, 10486, 25329, 'pois',
    { 'kind': 'picnic_site', 'min_zoom': 16 })

#https://www.openstreetmap.org/node/3297410094
# Golden Gate Park, SF
assert_has_feature(
    16, 10472, 25332, 'pois',
    { 'kind': 'picnic_site', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/400701941
# Golden Gate Park, SF
assert_has_feature(
    16, 10474, 25332, 'landuse',
    { 'kind': 'picnic_site', 'sort_key': 103 })

assert_has_feature(
    16, 10474, 25332, 'pois',
    { 'kind': 'picnic_site', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/231863022
# building, South Park, SF
assert_has_feature(
    16, 10486, 25329, 'pois',
    { 'kind': 'picnic_site', 'min_zoom': 16, 'id': 231863022 })



# historic=fort
# zoom 15 range up to zoom 13 and zoom 17 for POIs. Around 2000.

#https://www.openstreetmap.org/node/1148222790
# Fort Strong
assert_has_feature(
    16, 19850, 24247, 'pois',
    { 'kind': 'fort', 'min_zoom': 17 })

#https://www.openstreetmap.org/way/265893625
# Battery 2
assert_has_feature(
    16, 19303, 24607, 'landuse',
    { 'kind': 'fort', 'sort_key': 45 })

assert_has_feature(
    16, 19303, 24607, 'pois',
    { 'kind': 'fort', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/345074546
# Fort Monroe
assert_has_feature(
    15, 9438, 12753, 'landuse',
    { 'kind': 'fort' })

assert_has_feature(
    15, 9438, 12753, 'pois',
    { 'kind': 'fort', 'min_zoom': 15 })