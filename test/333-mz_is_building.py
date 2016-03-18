with features_in_tile_layer(16, 10470, 25342, 'landuse') as features:
    for feature in features:
        props = feature['properties']
        assert 'mz_is_building' not in props, 'mz_is_building detected'
