# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class BasicOutdoorPois(FixtureTest):
    def test_bbq(self):
        self.generate_fixtures(dsl.way(1387024181, wkt_loads('POINT (-122.043111437058 37.9185297983412)'), {u'source': u'openstreetmap.org', u'amenity': u'bbq'}))  # noqa

        self.assert_has_feature(
            16, 10550, 25297, 'pois',
            {'kind': 'bbq', 'min_zoom': 18})

    def test_bicycle_repair_station(self):
        # Node: Valencia Cyclery (3443701422)
        self.generate_fixtures(dsl.way(3443701422, wkt_loads('POINT (-122.420883736413 37.7559216043955)'), {u'website': u'http://www.valenciacyclery.com', u'addr:housenumber': u'1077', u'amenity': u'bicycle_repair_station', u'fee': u'yes', u'name': u'Valencia Cyclery', u'source': u'openstreetmap.org', u'addr:postcode': u'94110', u'service:bicycle:pump': u'yes', u'addr:state': u'CA', u'phone': u'4155506601', u'addr:street': u'Valencia Street', u'addr:city': u'San Francisco'}))  # noqa

        self.assert_has_feature(
            16, 10481, 25335, 'pois',
            {'id': 3443701422, 'kind': 'bicycle_repair_station',
             'min_zoom': 18})

    def test_dive_centre(self):
        self.generate_fixtures(dsl.way(2910259124, wkt_loads('POINT (-120.682905520547 35.24858062361431)'), {u'shop': u'scuba_diving', u'website': u'http://www.depthperceptions.net/', u'amenity': u'dive_centre', u'addr:city': u'San Luis Obispo', u'addr:postcode': u'93405', u'name': u'Depth Perceptions', u'source': u'openstreetmap.org', u'addr:housenumber': u'12322', u'addr:street': u'Los Osos Valley Road'}))  # noqa

        self.assert_has_feature(
            16, 10798, 25903, 'pois',
            {'kind': 'dive_centre', 'min_zoom': 16})

    def test_life_ring(self):
        self.generate_fixtures(dsl.way(2844159164, wkt_loads('POINT (-79.42727771203799 43.75376437111998)'), {u'source': u'openstreetmap.org', u'amenity': u'life_ring'}))  # noqa

        self.assert_has_feature(
            16, 18308, 23892, 'pois',
            {'kind': 'life_ring', 'min_zoom': 18})

    def test_lifeguard_tower(self):
        self.generate_fixtures(dsl.way(4083762008, wkt_loads('POINT (-120.64533707705 35.14172262312749)'), {u'source': u'openstreetmap.org', u'name': u'Pismo Lifeguard Tower 4', u'emergency': u'lifeguard_tower'}))  # noqa

        self.assert_has_feature(
            16, 10805, 25927, 'pois',
            {'kind': 'lifeguard_tower', 'min_zoom': 17})

    def test_picnic_table(self):
        self.generate_fixtures(dsl.way(696801847, wkt_loads('POINT (-121.785774381382 38.54985189949681)'), {u'source': u'openstreetmap.org', u'amenity': u'picnic_table', u'tourism': u'picnic_site', u'name': u'Picnic Tables'}))  # noqa

        self.assert_has_feature(
            16, 10597, 25151, 'pois',
            {'kind': 'picnic_table', 'min_zoom': 18})

    def test_shower(self):
        self.generate_fixtures(dsl.way(1128776802, wkt_loads('POINT (-122.504145615657 37.59650072368881)'), {u'source': u'openstreetmap.org', u'amenity': u'shower'}))  # noqa

        self.assert_has_feature(
            16, 10466, 25372, 'pois',
            {'kind': 'shower', 'min_zoom': 18})

    def test_waste_disposal(self):
        self.generate_fixtures(dsl.way(2287784170, wkt_loads('POINT (-122.244492793011 38.10185261522749)'), {u'source': u'openstreetmap.org', u'amenity': u'waste_disposal', u'waste': u'trash'}))  # noqa

        self.assert_has_feature(
            16, 10514, 25255, 'pois',
            {'kind': 'waste_disposal', 'min_zoom': 18})

    def test_watering_place(self):
        self.generate_fixtures(dsl.way(2640323071, wkt_loads('POINT (-122.306777034078 37.94991920607908)'), {u'source': u'openstreetmap.org', u'amenity': u'watering_place'}))  # noqa

        self.assert_has_feature(
            16, 10502, 25290, 'pois',
            {'kind': 'watering_place', 'min_zoom': 18})

    def test_water_point(self):
        self.generate_fixtures(dsl.way(3954505509, wkt_loads('POINT (-124.110018304493 43.92884831271299)'), {u'source': u'openstreetmap.org', u'amenity': u'water_point'}))  # noqa

        self.assert_has_feature(
            16, 10174, 23848, 'pois',
            {'kind': 'water_point', 'min_zoom': 18})

        self.generate_fixtures(dsl.way(3984333433, wkt_loads('POINT (-112.165685191532 37.63484157316341)'), {u'source': u'openstreetmap.org', u'amenity': u'water_point'}))  # noqa

        self.assert_has_feature(
            16, 12348, 25363, 'pois',
            {'kind': 'water_point', 'min_zoom': 18})

    def test_pylon(self):
        self.generate_fixtures(dsl.way(1978323412, wkt_loads('POINT (-120.241505998775 39.19449800774999)'), {u'source': u'openstreetmap.org', u'aerialway': u'pylon'}))  # noqa

        self.assert_has_feature(
            16, 10878, 25000, 'pois',
            {'kind': 'pylon', 'min_zoom': 17})

    def test_power_pole(self):
        self.generate_fixtures(dsl.way(2398019418, wkt_loads('POINT (-121.955094595351 37.76424341812228)'), {u'source': u'openstreetmap.org', u'power': u'pole'}))  # noqa

        self.assert_has_feature(
            16, 10566, 25333, 'pois',
            {'kind': 'power_pole', 'min_zoom': 18})

    def test_power_tower(self):
        self.generate_fixtures(dsl.way(1378418272, wkt_loads('POINT (-122.429615181311 37.6809742037058)'), {u'source': u'openstreetmap.org', u'power': u'tower'}))  # noqa

        self.assert_has_feature(
            16, 10480, 25352, 'pois',
            {'kind': 'power_tower', 'min_zoom': 16})

    def test_petroleum_well(self):
        self.generate_fixtures(dsl.way(2890101480, wkt_loads('POINT (-119.13405572999 34.17119825946398)'), {u'source': u'openstreetmap.org', u'man_made': u'petroleum_well', u'method': u'pumpjack'}))  # noqa

        self.assert_has_feature(
            16, 11080, 26141, 'pois',
            {'kind': 'petroleum_well', 'min_zoom': 17})
