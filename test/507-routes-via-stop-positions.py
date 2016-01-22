stations = [
    (17, 38596, 49262, 'Penn Station', 895371274L, [
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
    (17, 37639, 49960, 'Camden Station', 845910705L, ['Camden Line']),
    (17, 20958, 50667, 'Castro MUNI',    297863017L, ['K', 'L', 'M', 'T'])
]

for z, x, y, name, osm_id, expected_routes in stations:
    with features_in_tile_layer(z, x, y, 'pois') as pois:
        found = False

        for poi in pois:
            props = poi['properties']
            if props['id'] == osm_id:
                found = True
                routes = props.get('transit_routes', list())

                for r in expected_routes:
                    count = 0
                    for route in routes:
                        if r in route:
                            count = count + 1

                    if count == 0:
                        raise Exception("Found %r, and was expecting at "
                                        "least one %r route, but found "
                                        "none. Routes: %r"
                                        % (name, r, routes))

        if not found:
            raise Exception("Did not find %r (ID=%r) in tile." % (name, osm_id))
