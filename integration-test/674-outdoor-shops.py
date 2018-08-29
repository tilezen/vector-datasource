# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class OutdoorShops(FixtureTest):
    def test_fishing(self):
        self.generate_fixtures(dsl.way(3056897308, wkt_loads('POINT (-118.965276301823 37.64610896194417)'), {u'shop': u'fishing', u'source': u'openstreetmap.org', u'name': u'The Trout Fitter'}))  # noqa

        self.assert_has_feature(
            16, 11111, 25360, 'pois',
            {'kind': 'fishing', 'min_zoom': 16})

    def test_hunting(self):
        # http://www.openstreetmap.org/node/1467729495
        self.generate_fixtures(dsl.way(1467729495, wkt_loads('POINT (-124.156607540242 40.80332877487159)'), {u'shop': u'hunting', u'addr:housenumber': u'1327', u'addr:city': u'Eureka', u'addr:postcode': u'95501', u'name': u'Old West Shootery & Supply', u'source': u'openstreetmap.org', u'addr:country': u'US', u'addr:street': u'5th Street'}))  # noqa

        self.assert_has_feature(
            16, 10165, 24618, 'pois',
            {'kind': 'hunting', 'min_zoom': 16})

    def test_outdoor(self):
        self.generate_fixtures(dsl.way(766201791, wkt_loads('POINT (-124.084844635623 40.86953316699248)'), {u'shop': u'outdoor', u'addr:housenumber': u'650', u'name': u"Adventure's Edge", u'opening_hours': u'Mo-Sa 09:00-18:00; Su 10:00-17:00', u'source': u'openstreetmap.org', u'addr:street': u'10th Street'}))  # noqa

        self.assert_has_feature(
            16, 10179, 24602, 'pois',
            {'kind': 'outdoor', 'min_zoom': 16})

    def test_small_outdoor(self):
        # Smaller Sports Basement store in SF
        # This should really be in 16, 10483, 25332, but is in zoom 15 now
        self.generate_fixtures(dsl.way(35343322, wkt_loads('POLYGON ((-122.411503438384 37.76727108830107, -122.410791613353 37.76720071510631, -122.410771041933 37.76699456599798, -122.411464092175 37.7669514613754, -122.411469302404 37.76699378486008, -122.411503438384 37.76727108830107))'), {u'shop': u'outdoor', u'building': u'yes', u'addr:full': u'1590 Bryant St, San Francisco, CA 94103', u'addr:city': u'San Francisco', u'addr:postcode': u'94013', u'way_area': u'2888.38', u'addr:state': u'CA', u'height': u'14.98', u'source': u'openstreetmap.org', u'addr:housenumber': u'1590', u'addr:street': u'Bryant Street', u'name': u'Sports Basement'}))  # noqa

        self.assert_has_feature(
            15, 5241, 12666, 'pois',
            {'kind': 'outdoor', 'id': 35343322})

    def test_large_outdoor(self):
        # http://www.openstreetmap.org/way/377630800
        # Large Bass Pro building that should appear earlier
        self.generate_fixtures(dsl.way(377630800, wkt_loads('POLYGON ((-104.827294994284 39.02406511310399, -104.826632037605 39.02437706682608, -104.826394792538 39.02407285962249, -104.826073285498 39.0242241608225, -104.82564496877 39.02367478517689, -104.82595291125 39.0235299033882, -104.825856611851 39.0234063767732, -104.826482198615 39.02311200569858, -104.826618562875 39.0232869675069, -104.826799932731 39.0232016850202, -104.827087303791 39.0235703112002, -104.826957137906 39.0236315858692, -104.827294994284 39.02406511310399))'), {u'shop': u'outdoor', u'building': u'retail', u'way_area': u'18864.9', u'name': u'Bass Pro Shop', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            15, 6842, 12520, 'pois',
            {'kind': 'outdoor', 'id': 377630800})

        # Large REI building that should appear earlier
        self.generate_fixtures(dsl.way(290195878, wkt_loads('POLYGON ((-111.802024167649 40.70123485563938, -111.802023987986 40.7014723988414, -111.8015969289 40.70146919800679, -111.801545365603 40.7014105614151, -111.800970443821 40.70141709929548, -111.800970443821 40.70153416810739, -111.800824467587 40.70153416810739, -111.800807309766 40.70066878023668, -111.801682807841 40.70066878023668, -111.801777220778 40.70074035716837, -111.801785844605 40.70123485563938, -111.802024167649 40.70123485563938))'), {u'shop': u'outdoor', u'building': u'yes', u'name': u'REI', u'addr:postcode': u'84109', u'way_area': u'13133', u'addr:housenumber': u'3285', u'addr:city': u'Salt Lake City', u'source': u'openstreetmap.org', u'opening_hours': u'Mo-Fr 10:00-21:00;Sa 9:00-19:00;Su 11:00-18:00', u'internet_access': u'wlan', u'addr:street': u'3300 S'}))  # noqa

        self.assert_has_feature(
            15, 6207, 12321, 'pois',
            {'kind': 'outdoor', 'id': 290195878})

    def test_scuba_diving(self):
        self.generate_fixtures(dsl.way(3931687122, wkt_loads('POINT (-122.498863431955 37.86810888775278)'), {u'shop': u'scuba_diving', u'addr:housenumber': u'200', u'addr:city': u'Sausalito', u'addr:postcode': u'94965', u'addr:state': u'CA', u'name': u'Harbor Dive Center', u'source': u'openstreetmap.org', u'addr:street': u'Harbor Drive'}))  # noqa

        self.assert_has_feature(
            16, 10467, 25309, 'pois',
            {'kind': 'scuba_diving', 'min_zoom': 17})

    def test_gas_canister(self):
        self.generate_fixtures(dsl.way(2135237099, wkt_loads('POINT (-121.999360877607 37.28441996256068)'), {u'shop': u'gas', u'source': u'openstreetmap.org', u'name': u'Valero'}))  # noqa

        self.assert_has_feature(
            16, 10558, 25443, 'pois',
            {'kind': 'gas_canister', 'min_zoom': 18})

    def test_motorcycle(self):
        self.generate_fixtures(dsl.way(3799971066, wkt_loads('POINT (-122.412868069132 37.77455850560839)'), {u'shop': u'motorcycle', u'addr:housenumber': u'220', u'addr:city': u'San Francisco', u'addr:postcode': u'94103', u'addr:state': u'CA', u'name': u'Desmoto Sport', u'source': u'openstreetmap.org', u'addr:street': u'9th Street'}))  # noqa

        self.assert_has_feature(
            16, 10483, 25331, 'pois',
            {'kind': 'motorcycle', 'min_zoom': 17})
