with test.layers_in_tile(16, 10486, 25325) as layers:
    test.assertTrue('landuse_labels' not in layers)
