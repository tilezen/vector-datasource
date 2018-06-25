# -*- coding: utf-8 -*-
from . import FixtureTest


class BritishRoadShields(FixtureTest):
    def test_m25_gbmroad(self):
        import dsl

        z, x, y = (16, 32685, 21846)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/way/3256123
            dsl.way(3256123, dsl.tile_diagonal(z, x, y), {
                'active_traffic_management': u'yes',
                'bicycle': u'no',
                'carriageway_ref': u'B',
                'description': u'London Orbital Motorway',
                'foot': u'no',
                'highway': u'motorway',
                'highways_england:area': u'DBFO5',
                'horse': u'no',
                'lanes': u'3',
                'lit': u'yes',
                'maxspeed': u'70 mph',
                'maxspeed:type': u'GB:national',
                'maxspeed:variable': u'yes',
                'motor_vehicle': u'designated',
                'oneway': u'yes',
                'operator': u'Highways England',
                'ref': u'M25',
                'source': u'openstreetmap.org',
                'source:ref': u'local knowledge',
            }),
            dsl.relation(1, {
                'name': u'M25 motorway',
                'name:he': u'כביש הטבעת של לונדון',
                'operator': u'Highways England',
                'ref': u'M25',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q19872',
                'wikipedia': u'en:M25 motorway',
                'wikipedia:de': u'Motorway M25',
            }, ways=[3256123]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3256123,
                'network': u'GB:M-road',
                'shield_text': u'M25',
            })

    def test_a3_gbaroad(self):
        import dsl

        z, x, y = (16, 32685, 21846)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/way/152213939
            dsl.way(152213939, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'no',
                'highway': u'trunk',
                'highways_england:area': u'3',
                'lanes': u'2',
                'lit': u'yes',
                'maxspeed': u'70 mph',
                'maxspeed:type': u'UK:nsl_dual',
                'name': u'Portsmouth Road',
                'oneway': u'yes',
                'operator': u'Highways England',
                'ref': u'A3',
                'source': u'openstreetmap.org',
                'source:name': u'OS_OpenData_Locator',
                'source:ref': u'OS_OpenData_Locator',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 152213939,
                'network': u'GB:A-road-green',
                'shield_text': u'A3',
            })

    def test_a30_gbaroadgreen(self):
        import dsl

        z, x, y = (16, 32694, 21802)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/way/298766837
            dsl.way(298766837, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'lit': u'yes',
                'maxspeed': u'30 mph',
                'name': u'Great South West Road',
                'oneway': u'yes',
                'operator': u'Transport for London',
                'ref': u'A30',
                'sidewalk': u'separate',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 298766837,
                'network': u'GB:A-road-green',
                'shield_text': u'A30',
            })

    def test_a342_gbaroadwhite(self):
        import dsl

        z, x, y = (16, 32394, 21821)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/way/242656150
            dsl.way(242656150, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'2',
                'maxspeed': u'50 mph',
                'name': u'Devizes Road',
                'ref': u'A342',
                'source': u'openstreetmap.org',
                'source:name': u'OS_OpenData_Locator',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 242656150,
                'network': u'GB:A-road-white',
                'shield_text': u'A342',
            })

    def test_a329m_gbmroad(self):
        # although this ref begins with A, it's in fact an M-road. it _used_
        # to be an A-road, but it got upgraded and an "(m)" suffix.
        import dsl

        z, x, y = (16, 32621, 21819)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/way/186176850
            dsl.way(186176850, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'no',
                'carriageway_ref': u'A',
                'highway': u'motorway',
                'highways_england:area': u'3',
                'lanes': u'2',
                'lit': u'yes',
                'maxspeed': u'70 mph',
                'oneway': u'yes',
                'operator': u'Wokingham Borough Council',
                'ref': u'A329(M)',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 186176850,
                'network': u'GB:M-road',
                'shield_text': u'A329(M)',
            })

    def test_a312_gbaroadwhite(self):
        # the signage here is white. note that the road isn't actually the
        # A4090 - it's _leading to_ the A4090 (which is why it's parenthetical
        # on the signage). however, it's been (incorrectly) tagged as being
        # both the A312 and A4090.

        import dsl

        z, x, y = (16, 32702, 21778)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/way/306027724
            dsl.way(306027724, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'lanes': u'2',
                'lit': u'yes',
                'maxspeed': u'30 mph',
                'name': u'Petts Hill',
                'oneway': u'yes',
                'ref': u'A312;A4090',
                'sidewalk': u'separate',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 306027724,
                'network': u'GB:A-road-white',
                'shield_text': u'A312',
                'all_networks': ['GB:A-road-white', 'GB:A-road-white'],
                'all_shield_texts': ['A312', 'A4090'],
            })

    def test_a75_e18(self):
        # test that e-roads should sort after local refs
        import dsl

        z, x, y = (16, 31900, 20763)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/way/346973838
            dsl.way(346973838, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 18',
                'lanes': u'2',
                'lit': u'no',
                'maxspeed': u'60 mph',
                'maxspeed:type': u'GB:nsl_single',
                'operator': u'Transport Scotland',
                'ref': u'A75',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'E 18 England',
                'network': u'e-road',
                'ref': u'E 18',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[346973838]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 346973838,
                'network': u'GB:A-road-green',
                'shield_text': u'A75',
                'all_networks': ['GB:A-road-green', 'e-road'],
                'all_shield_texts': ['A75', 'E18'],
            })
