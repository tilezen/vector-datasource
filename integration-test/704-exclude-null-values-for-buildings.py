# way 128245373 - alcatraz prison main building
assert_has_feature(
    16, 10481, 25319, 'buildings',
    { 'kind': 'building' })

# but that same building should not have any "null" values in it
with features_in_tile_layer(16, 10481, 25319, 'buildings') as features:
    for f in features:
        for k, v in f['properties'].items():
            if v is None:
                raise AssertionError(
                    "%r is null, but there should be no null values in "
                    "feature %r" % (k, f['properties']))
