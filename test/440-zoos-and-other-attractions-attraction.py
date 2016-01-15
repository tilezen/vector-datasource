# expect these features in _both_ the landuse and POIs layers.
for layer in ['pois', 'landuse']:

    # whitelist attraction values
    attraction_values = [
        (17, 42456, 47103, 342984911, 'animal'), # Sable Island Horse
        (17, 30227, 44547, 243814268, 'water_slide'), # Fun Mountain Water Park
        (17, 37341, 50633, 235398095, 'roller_coaster'), # Intimidator 305
        (17, 37339, 50633, 235037260, 'carousel'), # Carousel
        (17, 37337, 50632, 235398104, 'amusement_ride'), # White Water Canyon
        (17, 37363, 49814, 374883740, 'maze') # Lawyers Farm Corn Maze
    ]

    for z, x, y, osm_id, attraction in attraction_values:
        assert_has_feature(
            z, x, y, layer,
            { 'id': osm_id,
              'kind': attraction })

# This is a carousel, but also a building, which keeps it out of the landuse
# layer. See https://github.com/mapzen/vector-datasource/issues/201
assert_has_feature(
    17, 34766, 50047, 'pois',
    { 'id': 325824281,
      'kind': 'carousel' })
