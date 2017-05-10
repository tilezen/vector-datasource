# Ways used in this test.
#https://www.openstreetmap.org/way/342984911
#https://www.openstreetmap.org/way/243814268
#https://www.openstreetmap.org/way/235398095
#https://www.openstreetmap.org/way/235037260
#https://www.openstreetmap.org/way/235398104
#https://www.openstreetmap.org/way/374883740
#https://www.openstreetmap.org/way/342984911
#https://www.openstreetmap.org/way/243814268
#https://www.openstreetmap.org/way/235398095
#https://www.openstreetmap.org/way/235037260
#https://www.openstreetmap.org/way/235398104
#https://www.openstreetmap.org/way/374883740
#https://www.openstreetmap.org/way/325824281

# expect these features in _both_ the landuse and POIs layers.
for layer in ['pois', 'landuse']:

    # whitelist attraction values
    attraction_values = [
        (16, 21228, 23551, 342984911, 'animal'), # Sable Island Horse
        (16, 15113, 22273, 243814268, 'water_slide'), # Fun Mountain Water Park
        (16, 18670, 25316, 235398095, 'roller_coaster'), # Intimidator 305
        (16, 18669, 25316, 235037260, 'carousel'), # Carousel
        (16, 18668, 25316, 235398104, 'amusement_ride'), # White Water Canyon
        (16, 18681, 24907, 374883740, 'maze') # Lawyers Farm Corn Maze
    ]

    for z, x, y, osm_id, attraction in attraction_values:
        test.assert_has_feature(
            z, x, y, layer,
            { 'id': osm_id,
              'kind': attraction })

# This is a carousel, but also a building, which keeps it out of the landuse
# layer. See https://github.com/mapzen/vector-datasource/issues/201
test.assert_has_feature(
    16, 17383, 25023, 'pois',
    { 'id': 325824281,
      'kind': 'carousel' })
