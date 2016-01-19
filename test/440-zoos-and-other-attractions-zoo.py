# expect these features in _both_ the landuse and POIs layers.
for layer in ['pois', 'landuse']:

    # whitelist zoo values
    zoo_values = [
        (17, 22916, 43711, 316623706, 'enclosure'), # Bear Enclosure (presumably + woods=yes?)
        (17, 41926, 47147, 343269426, 'petting_zoo'), # Oaklawn Farm Zoo
        (17, 20927, 45938, 370123970, 'aviary'), # Budgie Buddies
        (17, 42457, 47102, 84422829, 'wildlife_park') # Shubenacadie Provincial Wildlife Park
    ]

    for z, x, y, osm_id, zoo in zoo_values:
        assert_has_feature(
            z, x, y, layer,
            { 'id': osm_id,
              'kind': zoo })

# this is a building, so won't show up in landuse. still should be a POI.
# Wings of Asia
assert_has_feature(
    17, 36263, 55884, 'pois',
    { 'id': 103256220,
      'kind': 'aviary' })
