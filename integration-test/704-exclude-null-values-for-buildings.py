# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class ExcludeNullValuesForBuildings(FixtureTest):

    def test_alcatraz(self):
        # way 128245373 - alcatraz prison main building
        self.generate_fixtures(dsl.way(128245373, wkt_loads('POLYGON ((-122.423257444719 37.82664991474569, -122.423191867704 37.82669851905227, -122.423154767282 37.82672675920409, -122.422982739905 37.82686079334499, -122.422942405549 37.82689236831889, -122.422807029436 37.82678245896928, -122.422727977691 37.82684617661089, -122.42232652059 37.82653000033398, -122.422618742552 37.82630507159251, -122.422648297125 37.8262838558809, -122.42277495958 37.82639369501761, -122.422865689424 37.82632579060928, -122.423257444719 37.82664991474569))'), {u'building': u'yes', u'source': u'openstreetmap.org', u'way_area': u'4693.31', u'name': u'Main Prison', u'alt_name': u'Cellhouse'}))  # noqa

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
