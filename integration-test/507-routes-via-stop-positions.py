stations = [
    # Stations and lines, etc... used in exploring the NYC Penn Station
    # object network.
    #https://www.openstreetmap.org/node/895371274
    #https://www.openstreetmap.org/relation/1359387
    #https://www.openstreetmap.org/relation/1377996
    #https://www.openstreetmap.org/relation/1377998
    #https://www.openstreetmap.org/relation/1377999
    #https://www.openstreetmap.org/relation/1380577
    #https://www.openstreetmap.org/relation/1590286
    #https://www.openstreetmap.org/relation/1809808
    #https://www.openstreetmap.org/relation/1834644
    #https://www.openstreetmap.org/relation/1897938
    #https://www.openstreetmap.org/relation/1900976
    #https://www.openstreetmap.org/relation/207401
    #https://www.openstreetmap.org/relation/2648181
    #https://www.openstreetmap.org/relation/2807121
    #https://www.openstreetmap.org/relation/4044002
    #https://www.openstreetmap.org/relation/4073816
    #https://www.openstreetmap.org/relation/4234377
    #https://www.openstreetmap.org/relation/4234911
    #https://www.openstreetmap.org/relation/4445771
    #https://www.openstreetmap.org/relation/4452779
    #https://www.openstreetmap.org/relation/4460896
    #https://www.openstreetmap.org/relation/4467189
    #https://www.openstreetmap.org/relation/4467190
    #https://www.openstreetmap.org/relation/4748609
    #https://www.openstreetmap.org/relation/4799100
    #https://www.openstreetmap.org/relation/4799101
    (13, 2412, 3078, 'Penn Station', 895371274L, 1, [
        '2100-2297', # Acela Express
        '68-69', # Adirondack
        '50-51', # Cardinal
        '79-80', # Carolinian
        '19-20', # Crescent
        '230-296', # Empire Service
        '600-674', # Keystone Service
        '63', # Maple Leaf (Northbound)
        '64', # Maple Leaf (Southbound)
        '89-90', # Palmetto
        '42-43', # Pennsylvanian
        '97-98', # Silver Meteor
        '91-92', # Silver Star
        '54-57', # Vermonter
    ]),
    #https://www.openstreetmap.org/node/1129957203
    #https://www.openstreetmap.org/node/1129957312
    #https://www.openstreetmap.org/node/845910705
    #https://www.openstreetmap.org/relation/1401995
    #https://www.openstreetmap.org/relation/1402004
    #https://www.openstreetmap.org/relation/1403277
    #https://www.openstreetmap.org/relation/1403278
    (13, 2352, 3122, 'Camden Station', 845910705L, 5, ['Camden Line']),
    #https://www.openstreetmap.org/node/297863017
    #https://www.openstreetmap.org/relation/2124174
    #https://www.openstreetmap.org/relation/3433312
    #https://www.openstreetmap.org/relation/3433314
    #https://www.openstreetmap.org/relation/3433316
    #https://www.openstreetmap.org/relation/3435875
    #https://www.openstreetmap.org/relation/63250
    #https://www.openstreetmap.org/relation/63572
    #https://www.openstreetmap.org/relation/91022
    #https://www.openstreetmap.org/way/256270166
    (13, 1309, 3166, 'Castro MUNI',    297863017L, 1, ['K', 'L', 'M', 'T']),
    #https://www.openstreetmap.org/node/2058688536
    #https://www.openstreetmap.org/node/2058688538
    #https://www.openstreetmap.org/node/3426208027
    #https://www.openstreetmap.org/node/3426249715
    #https://www.openstreetmap.org/node/3426249720
    #https://www.openstreetmap.org/node/3426249721
    #https://www.openstreetmap.org/relation/1269021
    #https://www.openstreetmap.org/relation/1359387
    #https://www.openstreetmap.org/relation/1388639
    #https://www.openstreetmap.org/relation/1388641
    #https://www.openstreetmap.org/relation/1388648
    #https://www.openstreetmap.org/relation/1390116
    #https://www.openstreetmap.org/relation/1390117
    #https://www.openstreetmap.org/relation/1390133
    #https://www.openstreetmap.org/relation/1402781
    #https://www.openstreetmap.org/relation/1405499
    #https://www.openstreetmap.org/relation/1590286
    #https://www.openstreetmap.org/relation/1809808
    #https://www.openstreetmap.org/relation/1897938
    #https://www.openstreetmap.org/relation/1900976
    #https://www.openstreetmap.org/relation/206515
    #https://www.openstreetmap.org/relation/2629937
    #https://www.openstreetmap.org/relation/2629938
    #https://www.openstreetmap.org/relation/2648181
    #https://www.openstreetmap.org/relation/2807121
    #https://www.openstreetmap.org/relation/4044002
    #https://www.openstreetmap.org/relation/4460896
    #https://www.openstreetmap.org/relation/4744254
    #https://www.openstreetmap.org/relation/4748609
    #https://www.openstreetmap.org/relation/4799100
    #https://www.openstreetmap.org/relation/4799101
    #https://www.openstreetmap.org/way/30953448
    #https://www.openstreetmap.org/way/32272623
    #https://www.openstreetmap.org/way/43352433
    #https://www.openstreetmap.org/way/60185604
    #https://www.openstreetmap.org/way/60185611
    (13, 2385, 3102, '30th Street',     32272623L, 1, [
        '2100-2297', # Acela Express
        '79-80', # Carolinian
        '19-20', # Crescent
        '600-674', # Keystone Service
        '82-198', # Northeast Regional (Boston/Springfield & Lynchburg)
        '89-90', # Palmetto
        'Chestnut Hill West Line', # SEPTA - Chestnut Hill West Line
        'Cynwyd Line', # SEPTA - Cynwyd Line
        'Media/Elwyn Line', # SEPTA - Media/Elwyn Line
        'Trenton Line', # SEPTA - Trenton Line
        'Wilmington/Newark Line', # SEPTA - Wilmington/Newark Line
        '91-92', # Silver Star
    ])
]

for z, x, y, name, osm_id, expected_rank, expected_routes in stations:
    with test.features_in_tile_layer(z, x, y, 'pois') as pois:
        found = False

        for poi in pois:
            props = poi['properties']
            if props['id'] == osm_id:
                found = True
                routes = list()
                for typ in ['train', 'subway', 'light_rail', 'tram']:
                    routes.extend(props.get('%s_routes' % typ, list()))
                rank = props['kind_tile_rank']

                if rank > expected_rank:
                    test.fail('Found %r, and was expecting a rank of %r or less, '
                         'but got %r.' % (name, expected_rank, rank))

                for r in expected_routes:
                    count = 0
                    for route in routes:
                        if r in route:
                            count = count + 1

                    if count == 0:
                        test.fail('Found %r, and was expecting at least one %r '
                             'route, but found none. Routes: %r' %
                             (name, r, routes))

        if not found:
            test.fail('Did not find %r (ID=%r) in tile.' % (name, osm_id))
