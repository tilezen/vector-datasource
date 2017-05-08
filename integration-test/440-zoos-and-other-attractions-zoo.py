# Features used in this test:
#https://www.openstreetmap.org/way/316623706
#https://www.openstreetmap.org/way/343269426
#https://www.openstreetmap.org/way/370123970
#https://www.openstreetmap.org/way/84422829
#https://www.openstreetmap.org/way/316623706
#https://www.openstreetmap.org/way/343269426
#https://www.openstreetmap.org/way/370123970
#https://www.openstreetmap.org/way/84422829
#https://www.openstreetmap.org/way/103256220

# expect these features in _both_ the landuse and POIs layers.
for layer in ['pois', 'landuse']:

    # whitelist zoo values
    zoo_values = [
        (16, 11458, 21855, 316623706, 'enclosure'), # Bear Enclosure (presumably + woods=yes?)
        (16, 20963, 23573, 343269426, 'petting_zoo'), # Oaklawn Farm Zoo
        (16, 10463, 22969, 370123970, 'aviary'), # Budgie Buddies
        (16, 21228, 23551, 84422829, 'wildlife_park') # Shubenacadie Provincial Wildlife Park
    ]

    for z, x, y, osm_id, zoo in zoo_values:
        test.assert_has_feature(
            z, x, y, layer,
            { 'id': osm_id,
              'kind': zoo })

# this is a building, so won't show up in landuse. still should be a POI.
# Wings of Asia
test.assert_has_feature(
    16, 18131, 27942, 'pois',
    { 'id': 103256220,
      'kind': 'aviary' })
