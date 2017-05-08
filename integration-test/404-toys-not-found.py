tiles = [
    (16, 10473, 25339), # https://www.openstreetmap.org/way/215472849
    (16, 10479, 25336), # https://www.openstreetmap.org/node/1713279804
    (16, 10480, 25337), # https://www.openstreetmap.org/node/3188857553
    (16, 10484, 25328), # https://www.openstreetmap.org/node/3396659022
    (16, 10506, 25318), # https://www.openstreetmap.org/node/1467717312
    (16, 10509, 25308), # https://www.openstreetmap.org/node/2286100659
    (16, 10514, 25322), # https://www.openstreetmap.org/node/3711137981
    (16, 19298, 24633), # https://www.openstreetmap.org/node/3810578539
    (16, 19300, 24630), # https://www.openstreetmap.org/node/1429062988
    (16, 19300, 24629), # https://www.openstreetmap.org/node/1058296287
]

for z, x, y in tiles:
    test.assert_has_feature(
        z, x, y, 'pois',
        { 'kind': 'toys' })
