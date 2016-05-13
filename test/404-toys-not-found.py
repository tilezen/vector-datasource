tiles = [
    (17, 20946, 50678), # https://www.openstreetmap.org/way/215472849
    (17, 20959, 50673), # https://www.openstreetmap.org/node/1713279804
    (17, 20961, 50675), # https://www.openstreetmap.org/node/3188857553
    (17, 20969, 50656), # https://www.openstreetmap.org/node/3396659022
    (17, 21013, 50637), # https://www.openstreetmap.org/node/1467717312
    (17, 21019, 50617), # https://www.openstreetmap.org/node/2286100659
    (17, 21028, 50645), # https://www.openstreetmap.org/node/3711137981
    (17, 38597, 49266), # https://www.openstreetmap.org/node/3810578539
    (17, 38598, 49259), # http://www.openstreetmap.org/node/2678466844
    (17, 38600, 49261), # https://www.openstreetmap.org/node/1429062988
    (17, 38601, 49258), # https://www.openstreetmap.org/node/1058296287
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'toys' })
