# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class WindmillZoom(FixtureTest):
    def test_windmill_with_attraction(self):
        # update windmill zoom to 15 and if attraction zoom to 14
        # windmill with tourism = attraction
        self.generate_fixtures(dsl.way(287921407, wkt_loads('POLYGON ((-122.50950954605 37.77044960028441, -122.509500293403 37.77047580268178, -122.509480889793 37.77049817057459, -122.509461037025 37.770509816078, -122.509468493042 37.77057535750521, -122.509461126856 37.770575996587, -122.509454030166 37.7705140056184, -122.509453311513 37.77051436066419, -122.509420523006 37.77052259772597, -122.50938611753 37.77052195864368, -122.509353868011 37.7705125144261, -122.509327277879 37.77049540121677, -122.50930913191 37.77047232323118, -122.50930149623 37.77044576578648, -122.509305089492 37.7704187822768, -122.509319642199 37.77039407105399, -122.509343537386 37.77037461451069, -122.509374080105 37.77036218788359, -122.509408126255 37.7703583533811, -122.50943723167 37.77036268494871, -122.509432290936 37.7702980664548, -122.509441274089 37.77029771140798, -122.509446484317 37.7703654543115, -122.509471726977 37.770376886808, -122.509494364522 37.77039726647121, -122.509507479925 37.77042247475761, -122.50950954605 37.77044960028441))'), {u'building': u'yes', u'name': u'North Windmill', u'gnis:reviewed': u'no', u'wikipedia': u'en:Golden Gate Park windmills', u'way_area': u'433.646', u'man_made': u'windmill', u'addr:state': u'CA', u'height': u'13', u'source': u'openstreetmap.org', u'gnis:import_uuid': u'57871b70-0100-4405-bb30-88b2e001a944', u'gnis:feature_id': u'1655473', u'ele': u'11', u'tourism': u'attraction', u'gnis:county_name': u'San Francisco'}))  # noqa

        self.assert_has_feature(
            14, 2616, 6333, 'pois',
            {'id': 287921407, 'kind': 'windmill'})

    def test_windmill_without_attraction(self):
        # windmill without tourism = attraction
        self.generate_fixtures(dsl.way(2304462088, wkt_loads('POINT (-121.222603731272 36.38242898668528)'), {u'source': u'openstreetmap.org', u'man_made': u'windmill'}))  # noqa

        self.assert_no_matching_feature(
            14, 2675, 6412, 'pois',
            {'id': 2304462088, 'kind': 'windmill'})

        self.assert_has_feature(
            15, 5350, 12824, 'pois',
            {'id': 2304462088, 'kind': 'windmill'})
