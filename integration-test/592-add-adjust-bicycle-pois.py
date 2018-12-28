# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class AddAdjustBicyclePois(FixtureTest):
    def test_bicycle_shop(self):
        # Valencia Cyclery in SF
        self.generate_fixtures(dsl.way(414269441, wkt_loads('POINT (-122.420868195558 37.75571996934519)'), {u'shop': u'bicycle', u'addr:housenumber': u'1077', u'source': u'openstreetmap.org', u'name': u'Valencia Cyclery', u'addr:street': u'Valencia Street'}))  # noqa

        self.assert_has_feature(
            16, 10481, 25335, 'pois',
            {'kind': 'bicycle', 'min_zoom': 17})

    def test_bicycle_rental(self):
        # San Francisco Bicycle Rentals
        self.generate_fixtures(dsl.way(3801412161, wkt_loads('POINT (-122.452439037061 37.76943920319768)'), {u'addr:housenumber': u'1816', u'amenity': u'bicycle_rental', u'name': u'San Francisco Bicycle Rentals', u'addr:state': u'CA', u'addr:city': u'San Francisco', u'source': u'openstreetmap.org', u'addr:street': u'Haight Street'}))  # noqa

        self.assert_has_feature(
            16, 10476, 25332, 'pois',
            {'kind': 'bicycle_rental', 'min_zoom': 16})

    def test_bicycle_rental_stations(self):
        # Citi Bike - Broadway & W 24 St, with network, operator
        self.generate_fixtures(dsl.way(3708656264, wkt_loads('POINT (-73.98911000496309 40.7427403594615)'), {u'website': u'http://citibikenyc.com', u'amenity': u'bicycle_rental', u'capacity': u'52', u'name': u'Citi Bike - Broadway & W 24 St', u'source': u'openstreetmap.org', u'operator': u'NYC Bike Share', u'network': u'Citi Bike'}))  # noqa

        self.assert_has_feature(
            16, 19298, 24633, 'pois',
            {'kind': 'bicycle_rental_station', 'min_zoom': 17,
             'capacity': 52, 'network': 'Citi Bike',
             'operator': 'NYC Bike Share'})

        # Alta Bike Share, Chattanooga, with network, operator, ref, capacity.
        self.generate_fixtures(dsl.way(1960994139, wkt_loads('POINT (-85.3072689456985 35.03690398638529)'), {u'amenity': u'bicycle_rental', u'capacity': u'19', u'name': u'Chattanooga Choo Choo', u'source': u'openstreetmap.org', u'alt_name': u'Market St & E 14th St', u'operator': u'Alta Bike Share', u'ref': u'5', u'network': u'Bike Chattanooga'}))  # noqa

        self.assert_has_feature(
            16, 17238, 25950, 'pois',
            {'kind': 'bicycle_rental_station', 'min_zoom': 17,
             'capacity': 19, 'network': 'Bike Chattanooga',
             'operator': 'Alta Bike Share', 'ref': '5'})

    def test_cycle_barrier(self):
        # Cycle barrier in Berkeley
        self.generate_fixtures(dsl.way(1993249660, wkt_loads('POINT (-122.251597299099 37.86592671972728)'), {u'source': u'openstreetmap.org', u'barrier': u'cycle_barrier'}))  # noqa

        self.assert_has_feature(
            16, 10512, 25310, 'pois',
            {'kind': 'cycle_barrier', 'min_zoom': 18})

    def test_bicycle_junction(self):
        # icn_ref=1
        self.generate_fixtures(dsl.way(3836406372, wkt_loads('POINT (-2.119868931472499 47.70661617865708)'), {u'information': u'guidepost', u'bicycle': u'yes', u'destination:Peillac': u'9', u'source': u'openstreetmap.org', u'destination:Malestroit': u'28', u'icn_ref': u'1', u'tourism': u'information'}))  # noqa

        self.assert_has_feature(
            16, 32382, 22860, 'pois',
            {'kind': 'bicycle_junction', 'min_zoom': 16, 'ref': '1',
             'bicycle_network': 'icn'})

        # No known examples in the world for nodes, and ways don't count
        # ncn_ref=1

        # rcn_ref=1
        self.generate_fixtures(dsl.way(340159623, wkt_loads('POINT (3.04793228555176 50.82669216681209)'), {u'source': u'openstreetmap.org', u'rcn_region': u'Leiestreek', u'rcn_ref': u'1'}))  # noqa

        self.assert_has_feature(
            16, 33322, 21990, 'pois',
            {'kind': 'bicycle_junction', 'min_zoom': 16, 'ref': '1',
             'bicycle_network': 'rcn'})

        # NOTE: this is strangely in Omaha, NE, USA
        # lcn_ref=1
        self.generate_fixtures(dsl.way(3269815503, wkt_loads('POINT (-95.95767492178869 41.26692741839979)'), {u'information': u'guidepost', u'bicycle': u'yes', u'network': u'lcn', u'lcn_ref': u'1', u'source': u'openstreetmap.org', u'lcn': u'yes', u'tourism': u'information'}))  # noqa

        self.assert_has_feature(
            16, 15299, 24506, 'pois',
            {'kind': 'bicycle_junction', 'min_zoom': 16, 'ref': '1',
             'bicycle_network': 'lcn'})

        # lcn_ref=2
        self.generate_fixtures(dsl.way(287609621, wkt_loads('POINT (-1.0858399471524 53.946398710662)'), {u'source': u'openstreetmap.org', u'lcn_ref': u'2'}))  # noqa

        self.assert_has_feature(
            16, 32570, 21058, 'pois',
            {'kind': 'bicycle_junction', 'min_zoom': 16, 'ref': '2',
             'bicycle_network': 'lcn'})

    def test_walking_junction(self):
        # No known examples in the world for nodes, and ways don't count
        # iwn_ref=1

        # No known examples in the world for nodes, and ways don't count
        # nwn_ref=1

        # rwn_ref=1
        self.generate_fixtures(dsl.way(300403808, wkt_loads('POINT (3.979695081634069 51.0373677006325)'), {u'rwn_ref': u'1', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 33492, 21929, 'pois',
            {'kind': 'walking_junction', 'min_zoom': 16, 'ref': '1',
             'walking_network': 'rwn'})

        # lwn_ref=1
        self.generate_fixtures(dsl.way(717593380, wkt_loads('POINT (9.975857256320671 53.42434618160578)'), {u'source': u'openstreetmap.org', u'lwn_ref': u'ST'}))  # noqa

        self.assert_has_feature(
            16, 34584, 21219, 'pois',
            {'kind': 'walking_junction', 'min_zoom': 16, 'ref': 'ST',
             'walking_network': 'lwn'})

    def test_bicycle_parking(self):
        # bicycle parking with capacity, covered & fee
        self.generate_fixtures(dsl.way(3161454672, wkt_loads('POINT (-112.004154808381 33.63944545280928)'), {u'amenity': u'bicycle_parking', u'fee': u'no', u'capacity': u'10', u'lit': u'yes', u'source': u'openstreetmap.org', u'covered': u'yes', u'bicycle_parking': u'lockers'}))  # noqa

        self.assert_has_feature(
            16, 12378, 26258, 'pois',
            {'kind': 'bicycle_parking',
             'capacity': 10, 'covered': True, 'fee': False})

        # bicycle parking with access, capacity, covered, fee & operator
        self.generate_fixtures(dsl.way(1618586234, wkt_loads('POINT (-122.798403968499 50.31816017249891)'), {u'website': u'http://www.pembertongatewayvillagesuites.com/index.php?option=com_content&view=article&id=46&Itemid=53', u'access': u'customers', u'amenity': u'bicycle_parking', u'fee': u'no', u'capacity': u'100', u'note': u'Free to guests of Pemberton Gateway Village Suites Hotel.', u'source': u'openstreetmap.org', u'operator': u'Pemberton Gateway Village Suites', u'covered': u'yes'}))  # noqa

        self.assert_has_feature(
            16, 10413, 22135, 'pois',
            {'kind': 'bicycle_parking',
             'capacity': 100, 'covered': True, 'fee': False,
             'access': 'customers',
             'operator': 'Pemberton Gateway Village Suites'})

        # bicycle parking with capacity, covered, fee, maxstay, operator
        self.generate_fixtures(dsl.way(1154262723, wkt_loads('POINT (-6.26408093525105 53.34149287895218)'), {u'amenity': u'bicycle_parking', u'fee': u'no', u'capacity': u'200', u'name': u'Drury Street Cycle Park', u'opening_hours': u'Mo-Fr 07:30-01:00; Sa-Su 11:00-19:00', u'source': u'openstreetmap.org', u'maxstay': u'2 days', u'operator': u'Dublin City Council', u'covered': u'yes', u'bicycle_parking': u'stands'}))  # noqa

        self.assert_has_feature(
            16, 31627, 21244, 'pois',
            {'kind': 'bicycle_parking',
             'capacity': 200, 'covered': True, 'fee': False,
             'maxstay': '2 days', 'operator': 'Dublin City Council'})

        # bicycle parking with capacity and cyclestreets ID.
        self.generate_fixtures(dsl.way(1116224894, wkt_loads('POINT (-0.12322559061534 51.51743826261948)'), {u'cyclestreets_id': u'27815', u'amenity': u'bicycle_parking', u'capacity': u'4', u'bicycle_parking': u'flower_pots', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 32745, 21789, 'pois',
            {'kind': 'bicycle_parking',
             'capacity': 4, 'cyclestreets_id': '27815'})

        # bicycle parking with access, capacity, covered, operator and
        # surveillance
        self.generate_fixtures(dsl.way(2921238315, wkt_loads('POINT (-86.1364513228567 39.94982195697919)'), {u'amenity': u'bicycle_parking', u'capacity': u'10', u'surveillance': u'yes', u'access': u'public', u'source': u'openstreetmap.org', u'operator': u'City of Carmel', u'covered': u'yes', u'bicycle_parking': u'rack'}))  # noqa

        self.assert_has_feature(
            16, 17087, 24822, 'pois',
            {'kind': 'bicycle_parking',
             'access': 'public', 'capacity': 10, 'covered': True,
             'operator': 'City of Carmel', 'surveillance': True})
