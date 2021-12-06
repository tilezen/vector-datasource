# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class SourceInPoi(FixtureTest):
    def test_poi_has_source(self):
        # Add source info in POIs
        self.generate_fixtures(dsl.way(4227424520, wkt_loads('POINT (-122.529578178992 37.81559717375449)'), {u'source': u'openstreetmap.org', u'entrance': u'yes'}),dsl.way(4227424524, wkt_loads('POINT (-122.52952338176 37.81562250855571)'), {u'source': u'openstreetmap.org', u'entrance': u'yes'}),dsl.way(423023928, wkt_loads('POLYGON ((-122.529608542049 37.8155831934824, -122.529578178992 37.81559717375449, -122.52952338176 37.81562250855571, -122.529489964431 37.81563790813641, -122.529467057391 37.81560689607419, -122.52958572484 37.81555218139718, -122.529608542049 37.8155831934824))'), {u'website': u'https://www.nps.gov/goga/pobo.htm', u'building': u'lighthouse', u'name': u'Point Bonita Lighthouse', u'source': u'openstreetmap.org', u'opening_hours': u'Mo-Su 12:30-15:30; Tu off; We off; Th off; Fr off', u'way_area': u'77.3216', u'man_made': u'lighthouse', u'source:opening_hours': u'https://www.nps.gov/goga/pobo.htm', u'wikidata': u'Q2100738', u'source:start_date': u'https://www.nps.gov/goga/upload/sb-pobo.pdf', u'tourism': u'attraction', u'start_date': u'1877'}))

        self.assert_has_feature(
            14, 2615, 6330, 'pois',
            {'id': 423023928, 'kind': 'lighthouse',
             'source': 'openstreetmap.org'})
