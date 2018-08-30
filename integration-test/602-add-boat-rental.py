# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class AddBoatRental(FixtureTest):
    def test_shop_boat_rental(self):
        # shop=boat_rental
        self.generate_fixtures(dsl.way(1306277961, wkt_loads('POINT (-79.3866958699203 43.63838899063068)'), {u'shop': u'boat_rental', u'phone': u'4162033000', u'website': u'www.qqy.ca', u'name': u'Harbourfront Centre Sailing / Powerboating', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 18316, 23921, 'pois',
            {'kind': 'boat_rental'})

    def test_amenity_boat_rental(self):
        # amenity=boat_rental
        self.generate_fixtures(dsl.way(4362555638, wkt_loads('POINT (-119.691422275218 34.40824461340819)'), {u'source': u'openstreetmap.org', u'amenity': u'boat_rental', u'name': u'SEA Landing'}))  # noqa

        self.assert_has_feature(
            16, 10978, 26089, 'pois',
            {'kind': 'boat_rental'})

    def test_shop_boat_rental_yes(self):
        # shop=boat, rental=yes
        self.generate_fixtures(dsl.way(3466463119, wkt_loads('POINT (-73.11327613880708 41.2023199639785)'), {u'shop': u'boat', u'source': u'openstreetmap.org', u'rental': u'yes', u'name': u'Boardwalk Marina Boat Sales and Rentals'}))  # noqa

        self.assert_has_feature(
            16, 19458, 24522, 'pois',
            {'kind': 'boat_rental'})

    def test_rental_boat(self):
        # rental=boat
        self.generate_fixtures(dsl.way(2425308146, wkt_loads('POINT (4.63301616208223 46.84542196190339)'), {u'website': u'http://www.locaboat.com/fr/102/saint-leger-sur-dheune.html', u'source': u'openstreetmap.org', u'rental': u'boat', u'name': u'Locaboat Holydays'}))  # noqa

        self.assert_has_feature(
            16, 33611, 23091, 'pois',
            {'kind': 'boat_rental'})
