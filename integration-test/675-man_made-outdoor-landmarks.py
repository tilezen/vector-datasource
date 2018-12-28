# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class ManMadeOutdoorLandmarks(FixtureTest):
    def test_communications_tower(self):
        self.generate_fixtures(dsl.way(1230069003, wkt_loads('POINT (-121.92892226938 37.8670382002752)'), {u'source': u'openstreetmap.org', u'man_made': u'communications_tower'}))  # noqa

        self.assert_has_feature(
            15, 5285, 12654, 'pois',
            {'kind': 'communications_tower', 'min_zoom': 15})

    def test_observatory(self):
        # ideally the landuse would show up at zoom 13, but that's sparse
        # coverage most features are buildings, some of which are incorrectly
        # tagged (should be telescope)
        self.generate_fixtures(dsl.way(747693102, wkt_loads('POINT (-75.58143133824321 39.27851040008478)'), {u'website': u'www.DASEF.org', u'amenity': u'university', u'man_made': u'observatory', u'observatory:type': u'astronomical', u'source': u'openstreetmap.org', u'addr:street': u'ITEC Loop'}))  # noqa

        self.assert_has_feature(
            15, 9504, 12490, 'pois',
            {'kind': 'observatory', 'min_zoom': 15})

    def test_telescope_node(self):
        self.generate_fixtures(dsl.way(258205070, wkt_loads('POINT (-121.642976117694 37.34109930263988)'), {u'name': u'James Lick Telescope', u'telescope:diameter': u'0.9144', u'man_made': u'telescope', u'telescope:type': u'optical', u'source': u'openstreetmap.org', u'alt_name': u'Great Lick Refractor; Lick Refractor', u'operator': u'University of California'}))  # noqa

        self.assert_has_feature(
            16, 10623, 25430, 'pois',
            {'kind': 'telescope', 'min_zoom': 16})

    def test_telescope_way(self):
        # If someone took the time to digitize a building, promote it up
        self.generate_fixtures(dsl.way(53055408, wkt_loads('POLYGON ((-121.498736237637 36.76031996576698, -121.498625026205 36.76032039757599, -121.498624397384 36.7601999947297, -121.498735608816 36.76019956292, -121.498736237637 36.76031996576698))'), {u'building': u'yes', u'name': u'Fremont Peak Observatory', u'way_area': u'207.122', u'man_made': u'telescope', u'source': u'openstreetmap.org', u'landuse': u'observatory'}))  # noqa

        self.assert_has_feature(
            15, 5324, 12781, 'pois',
            {'kind': 'telescope', 'min_zoom': 15})

    def test_offshore_platform_node(self):
        self.generate_fixtures(dsl.way(2622856034, wkt_loads('POINT (-118.044507537345 33.6623171776256)'), {u'man_made': u'offshore_platform', u'type': u'oil', u'name': u'Platform Emmy', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            13, 1409, 3281, 'pois',
            {'kind': 'offshore_platform', 'min_zoom': 13})

    def test_offshore_platform_way(self):
        self.generate_fixtures(dsl.way(346405529, wkt_loads('POLYGON ((-119.906535907426 34.3897671631719, -119.906489105199 34.3899948169202, -119.905999703033 34.38992632070937, -119.906022879567 34.38981349457748, -119.905964219579 34.3898052661218, -119.905994133478 34.38965967421188, -119.906246110915 34.38969496025808, -119.906239822708 34.38972579847117, -119.906535907426 34.3897671631719))'), {u'building': u'industrial', u'source': u'openstreetmap.org', u'way_area': u'1944.96', u'man_made': u'offshore_platform', u'name': u'Platform Holly'}))  # noqa

        self.assert_has_feature(
            13, 1367, 3261, 'pois',
            {'kind': 'offshore_platform', 'min_zoom': 13})

        self.generate_fixtures(dsl.way(446514311, wkt_loads('POLYGON ((57.28399280807089 69.26576040721967, 57.28402739320939 69.2669031049751, 57.2874108078955 69.26689028887759, 57.287376222757 69.26574749503671, 57.28399280807089 69.26576040721967))'), {u'source': u'openstreetmap.org', u'way_area': u'135352', u'man_made': u'offshore_platform', u'name': u'\u041c\u041b\u0421\u041f \xab\u041f\u0440\u0438\u0440\u0430\u0437\u043b\u043e\u043c\u043d\u0430\u044f\xbb'}))  # noqa

        self.assert_has_feature(
            13, 5399, 1881, 'pois',
            {'kind': 'offshore_platform', 'min_zoom': 13, 'id': 446514311})

    def test_water_tower(self):
        self.generate_fixtures(dsl.way(1501843094, wkt_loads('POINT (-122.428099094606 37.70762977463859)'), {u'source': u'openstreetmap.org', u'man_made': u'water_tower'}))  # noqa

        self.assert_has_feature(
            16, 10480, 25346, 'pois',
            {'kind': 'water_tower', 'min_zoom': 17})

    def test_mast(self):
        # This isn't part of the work, but because we split water_tower
        # off from mast, we should test mast still shows up
        self.generate_fixtures(dsl.way(3679715072, wkt_loads('POINT (-121.833830835485 37.2910862055756)'), {u'source': u'openstreetmap.org', u'man_made': u'mast'}))  # noqa

        self.assert_has_feature(
            16, 10588, 25442, 'pois',
            {'kind': 'mast', 'min_zoom': 17})
