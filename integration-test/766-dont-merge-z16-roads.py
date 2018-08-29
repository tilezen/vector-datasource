# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class DontMergeZ16Roads(FixtureTest):
    def test_roads_not_merged(self):
        # if we're merging, then only one of these will be in tiles. if
        # both exist then it's more likely that no merging is happening.
        self.generate_fixtures(dsl.way(89911760, wkt_loads('LINESTRING (-71.0727023957791 42.38242551026689, -71.07199631996571 42.3812520084956)'), {u'layer': u'-1', u'lanes': u'2', u'name': u'Sullivan Square Underpass', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'width': u'19.5', u'condition': u'fair', u'oneway': u'yes', u'attribution': u'Office of Geographic and Environmental Information (MassGIS)', u'massgis:way_id': u'139891', u'ref': u'MA 99', u'highway': u'trunk'}),dsl.way(89912879, wkt_loads('LINESTRING (-71.0719030748393 42.38128558481939, -71.0726063658752 42.3824638635311)'), {u'layer': u'-1', u'lanes': u'2', u'name': u'Sullivan Square Underpass', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'width': u'19.5', u'condition': u'fair', u'oneway': u'yes', u'attribution': u'Office of Geographic and Environmental Information (MassGIS)', u'massgis:way_id': u'139891', u'ref': u'MA 99', u'highway': u'trunk'}))  # noqa

        self.assert_has_feature(
            16, 19829, 24234, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 89912879})

        self.assert_has_feature(
            16, 19829, 24234, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 89911760})
