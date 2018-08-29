# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RangerStation(FixtureTest):
    def test_ranger_station_supersedes_tourism(self):
        # Big Basin Redwoods State Park Headquarters
        # Node with amenity=ranger_station, but also has tourism=information
        # set
        self.generate_fixtures(dsl.way(1996636138, wkt_loads('POINT (-122.22175526536 37.17244957017029)'), {u'information': u'office', u'amenity': u'ranger_station', u'name': u'Big Basin Redwoods State Park Headquarters', u'wheelchair': u'yes', u'source': u'openstreetmap.org', u'tourism': u'information'}))  # noqa

        self.assert_has_feature(
            14, 2629, 6367, 'pois',
            {'kind': 'ranger_station', 'min_zoom': 14})

        # Pantoll Ranger Station
        # Node with amenity=ranger_station, but also has tourism=information
        # set
        self.generate_fixtures(dsl.way(351892607, wkt_loads('POINT (-122.603770307802 37.90397806289519)'), {u'source': u'openstreetmap.org', u'amenity': u'ranger_station', u'tourism': u'information', u'name': u'Pantoll Ranger Station'}))  # noqa

        self.assert_has_feature(
            14, 2612, 6325, 'pois',
            {'kind': 'ranger_station', 'min_zoom': 14})

    def test_building_ranger_station(self):
        # Building with amenity=ranger_station
        self.generate_fixtures(dsl.way(361301773, wkt_loads('POLYGON ((-122.477381030419 37.83698367631209, -122.47725293066 37.83702865560479, -122.47713597001 37.83682106955531, -122.477264069769 37.83677609013608, -122.477381030419 37.83698367631209))'), {u'building': u'yes', u'addr:housenumber': u'T507', u'amenity': u'ranger_station', u'addr:city': u'Sausalito', u'building:levels': u'2', u'way_area': u'499.794', u'addr:state': u'CA', u'source': u'openstreetmap.org', u'addr:country': u'US', u'addr:street': u'McReynolds Road'}))  # noqa

        self.assert_has_feature(
            14, 2617, 6329, 'pois',
            {'kind': 'ranger_station', 'min_zoom': 14})

        # Entrance Yosemite Nationalpark
        # Building with amenity=ranger_station
        self.generate_fixtures(dsl.way(269908344, wkt_loads('POLYGON ((-119.731012377263 37.68609727879108, -119.730953896938 37.68613026461198, -119.730923533881 37.68610751577161, -119.730981565048 37.68607140197321, -119.731012377263 37.68609727879108))'), {u'building': u'yes', u'source': u'openstreetmap.org', u'amenity': u'ranger_station', u'way_area': u'38.727', u'name': u'Entrance Yosemite Nationalpark'}))  # noqa

        self.assert_has_feature(
            14, 2742, 6337, 'pois',
            {'kind': 'ranger_station', 'min_zoom': 14})
