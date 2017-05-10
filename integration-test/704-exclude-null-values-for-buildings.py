# way 128245373 - alcatraz prison main building
test.assert_has_feature(
    16, 10481, 25319, 'buildings',
    { 'kind': 'building' })

# but that same building should not have any "null" values in it
with test.features_in_tile_layer(16, 10481, 25319, 'buildings') as features:
    for f in features:
        for k, v in f['properties'].items():
            if v is None:
                test.fail('%r is null, but there should be no null values in '
                     'feature %r' % (k, f['properties']))
