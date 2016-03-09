assert_no_matching_feature(
    7, 20, 48, 'transit',
    {'kind': 'railway'})

# count the unique parameters - there should only be one, indicating that the
# rail routes have been merged.
with features_in_tile_layer(7, 20, 48, 'transit') as transit:
    seen_properties = set()
    railway_kinds = set(['train', 'subway', 'light_rail', 'tram'])

    for feature in transit:
        if feature['properties'].get('kind') in railway_kinds:
            props = frozenset(feature['properties'].items())
            if props in seen_properties:
                raise Exception("Duplicate properties %r in transit layer, but "
                                "properties should be unique."
                                % feature['properties'])
            seen_properties.add(props)
