#http://www.openstreetmap.org/node/1230069003
test.assert_has_feature(
    15, 5285, 12654, 'pois',
    { 'kind': 'communications_tower', 'min_zoom': 15 })

#http://www.openstreetmap.org/node/747693102
# ideally the landuse would show up at zoom 13, but that's sparse coverage
# most features are buildings, some of which are incorrectly tagged (should be telescope)
test.assert_has_feature(
    15, 9504, 12490, 'pois',
    { 'kind': 'observatory', 'min_zoom': 15 })

#http://www.openstreetmap.org/node/258205070
test.assert_has_feature(
    16, 10623, 25430, 'pois',
    { 'kind': 'telescope', 'min_zoom': 16 })

#https://www.openstreetmap.org/way/53055408
# If someone took the time to digitize a building, promote it up
test.assert_has_feature(
    15, 5324, 12781, 'pois',
    { 'kind': 'telescope', 'min_zoom': 15 })

#http://www.openstreetmap.org/node/2622856034
test.assert_has_feature(
    13, 1409, 3281, 'pois',
    { 'kind': 'offshore_platform', 'min_zoom': 13 })

#http://www.openstreetmap.org/way/346405529
test.assert_has_feature(
    13, 1367, 3261, 'pois',
    { 'kind': 'offshore_platform', 'min_zoom': 13 })

#http://www.openstreetmap.org/way/446514311
test.assert_has_feature(
    13, 5399, 1881, 'pois',
    { 'kind': 'offshore_platform', 'min_zoom': 13, 'id': 446514311 })

#http://www.openstreetmap.org/node/1501843094
test.assert_has_feature(
    15, 5240, 12673, 'pois',
    { 'kind': 'water_tower', 'min_zoom': 15 })

#https://www.openstreetmap.org/node/3679715072
# This isn't part of the work, but because we split water_tower
# off from mast, we should test mast still shows up
test.assert_has_feature(
    16, 10588, 25442, 'pois',
    { 'kind': 'mast', 'min_zoom': 17 })
