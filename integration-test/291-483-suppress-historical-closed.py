# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class SuppressHistoricalClosed(FixtureTest):

    def test_cartoon_museum(self):
        # Cartoon Art Museum (closed)
        self.generate_fixtures(dsl.way(368173967, wkt_loads('POINT (-122.400856246311 37.78696485494709)'), {u'name': u'Cartoon Art Museum (closed)', u'gnis:reviewed': u'no', u'addr:state': u'CA', u'ele': u'7', u'source': u'openstreetmap.org', u'wikidata': u'Q1045990', u'gnis:import_uuid': u'57871b70-0100-4405-bb30-88b2e001a944', u'gnis:feature_id': u'1657282', u'tourism': u'museum', u'gnis:county_name': u'San Francisco'}))  # noqa

        # POI shouldn't be visible early
        self.assert_no_matching_feature(
            15, 5242, 12664, 'pois',
            {'id': 368173967})

        # but POI should be present at z17 and marked as closed
        self.assert_has_feature(
            16, 10485, 25328, 'pois',
            {'id': 368173967, 'kind': 'closed', 'min_zoom': 17})
