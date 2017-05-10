#http://www.openstreetmap.org/node/1996636138
# Big Basin Redwoods State Park Headquarters
# Node with amenity=ranger_station, but also has tourism=information set
test.assert_has_feature(
    14, 2629, 6367, 'pois',
    { 'kind': 'ranger_station', 'min_zoom': 14 })

#https://www.openstreetmap.org/node/351892607
# Pantoll Ranger Station
# Node with amenity=ranger_station, but also has tourism=information set
test.assert_has_feature(
    14, 2612, 6325, 'pois',
    { 'kind': 'ranger_station', 'min_zoom': 14 })

#http://www.openstreetmap.org/way/361301773
# Building with amenity=ranger_station
test.assert_has_feature(
    14, 2617, 6329, 'pois',
    { 'kind': 'ranger_station', 'min_zoom': 14 })

#https://www.openstreetmap.org/way/269908344
# Entrance Yosemite Nationalpark
# Building with amenity=ranger_station
test.assert_has_feature(
    14, 2742, 6337, 'pois',
    { 'kind': 'ranger_station', 'min_zoom': 14 })