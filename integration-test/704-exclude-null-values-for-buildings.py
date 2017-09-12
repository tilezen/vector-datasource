from . import FixtureTest


class ExcludeNullValuesForBuildings(FixtureTest):

    def test_alcatraz(self):
        # way 128245373 - alcatraz prison main building
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/128245373'])

        self.assert_has_feature(
            16, 10481, 25319, 'buildings',
            {'kind': 'building'})

        # but that same building should not have any "null" values in it
        with self.features_in_tile_layer(
                16, 10481, 25319, 'buildings') as features:
            for f in features:
                for k, v in f['properties'].items():
                    self.assertFalse(
                        v is None,
                        '%r is null, but there should be no null values in '
                        'feature %r' % (k, f['properties']))
