# count the unique parameters - there should only be one, indicating that the
# roads have been merged.
with features_in_tile_layer(8, 41, 99, 'roads') as roads:
    features = set()

    for road in roads:
        props = frozenset(road['properties'].items())
        if props in features:
            raise Exception("Duplicate properties %r in roads layer, but "
                            "properties should be unique."
                            % road['properties'])
        features.add(props)
