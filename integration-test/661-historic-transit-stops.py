# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class HistoricTransitStops(FixtureTest):
    def test_historic_railway_stop(self):
        # Check if historic stops are shown in pois and in transit layers.
        # Historic railway stop
        self.generate_fixtures(dsl.way(3039734894, wkt_loads('POINT (-73.9832352026681 40.6727968999414)'), {u'name': u'Third Street', u'end_date': u'1940-05-31', u'tram': u'no', u'source': u'openstreetmap.org', u'historic': u'yes', u'train': u'no', u'light_rail': u'no', u'operator': u'Brooklyn-Manhattan Transit Company', u'railway': u'stop', u'subway': u'yes', u'public_transport': u'stop_position'}))  # noqa

        self.assert_no_matching_feature(
            13, 2412, 3081, 'pois',
            {'id': 3039734894})

    def test_historic_tram_stop(self):
        # Historic tram stop
        self.generate_fixtures(dsl.way(413573669, wkt_loads('POINT (-121.949906465259 36.97554418488439)'), {u'name': u'Capitola Village/Depot Hill', u'railway:proposed': u'tram_stop', u'note': u'Noted as a Secondary Station', u'source': u'openstreetmap.org', u'historic': u'yes', u'railway': u'tram_stop', u'ref': u'11'}))  # noqa

        self.assert_no_matching_feature(
            13, 1320, 3189, 'pois',
            {'id': 413573669})

    def test_historic_railway_halt(self):
        # Historic railway halt
        self.generate_fixtures(dsl.way(708144563, wkt_loads('POINT (14.8139903286339 59.15514209522067)'), {u'historic:railway': u'halt', u'historic': u'yes', u'disused': u'yes', u'name': u'Kvistbro', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_no_matching_feature(
            13, 4433, 2416, 'pois',
            {'id': 708144563})

        self.generate_fixtures(dsl.way(2468597590, wkt_loads('POINT (9.147960458165631 46.24711157299198)'), {u'source': u'openstreetmap.org', u'railway': u'halt', u'historic': u'railway_station', u'name': u'Grono'}))  # noqa

        self.assert_no_matching_feature(
            13, 4304, 2906, 'pois',
            {'id': 2468597590})

    def test_historic_railway_station(self):
        # Historic railway station
        self.generate_fixtures(dsl.way(985085275, wkt_loads('POINT (7.88296176838984 50.62061888904539)'), {u'name': u'Alter Verladebahnhof', u'note': u'disused since 2001', u'source': u'openstreetmap.org', u'historic': u'yes', u'railway': u'station', u'ruins': u'yes'}))  # noqa

        self.assert_no_matching_feature(
            13, 4275, 2756, 'pois',
            {'id': 985085275})

    def test_historic_tram_stop_2(self):
        # Historic tram stop
        self.generate_fixtures(dsl.way(3367033945, wkt_loads('POINT (-122.333631091518 47.78397268711019)'), {u'name': u'Lake Ballenger (Historic)', u'source': u'openstreetmap.org', u'historic': u'tram_stop', u'crossing': u'uncontrolled', u'railway': u'tram_stop', u'highway': u'crossing'}))  # noqa

        self.assert_no_matching_feature(
            13, 1312, 2854, 'pois',
            {'id': 3367033945})

    def test_current_railway_stop(self):
        # Current railway stop
        self.generate_fixtures(dsl.way(2986320002, wkt_loads('POINT (-73.94815608065468 40.67836252093279)'), {u'name': u'Nostrand Avenue', u'source': u'openstreetmap.org', u'train': u'yes', u'public_transport': u'stop_position', u'operator': u'Long Island Rail Road', u'railway': u'stop', u'railway:position': u'1.6', u'network': u'Long Island Rail Road'}))  # noqa

        self.assert_has_feature(
            16, 19306, 24648, 'pois',
            {'id': 2986320002, 'min_zoom': 16})

    def test_current_tram_stop(self):
        # Current tram stop
        self.generate_fixtures(dsl.way(257074010, wkt_loads('POINT (-122.413997610771 37.77939210258558)'), {u'name': u'Civic Center', u'wikipedia': u'en:Civic Center / UN Plaza Station', u'source': u'openstreetmap.org', u'operator': u'San Francisco Municipal Railway', u'railway': u'tram_stop', u'network': u'Muni'}))  # noqa

        self.assert_has_feature(
            16, 10483, 25330, 'pois',
            {'id': 257074010, 'kind': 'tram_stop', 'min_zoom': 16})

    def test_current_railway_halt(self):
        # Current railway halt
        import dsl

        z, x, y = (16, 35826, 22751)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/302735255
            dsl.point(302735255, (16.8020704, 48.1080027), {
                'name': u'Wildungsmauer',
                'network': u'VOR',
                'operator': u'ÖBB-Infrastruktur AG',
                'public_transport': u'stop_position',
                'railway': u'halt',
                'railway:platform_height': u'38',
                'railway:platform_length': u'142',
                'railway:position': u'38.0',
                'railway:position:exact': u'37.985',
                'railway:ref': u'Reg H1',
                'ref': u'1',
                'source': u'openstreetmap.org',
                'train': u'yes',
                'uic_name': u'Wildungsmauer',
                'uic_ref': u'8101787',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 302735255,
                'kind': u'halt',
                'min_zoom': 16,
            })
