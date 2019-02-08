# -*- encoding: utf-8 -*-
from . import FixtureTest


class BridgeTest(FixtureTest):

    def test_viaduct(self):
        import dsl

        z, x, y = (16, 36399, 22206)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/365016934
            dsl.way(365016934, dsl.tile_diagonal(z, x, y), {
                'bicycle': 'use_sidepath',
                'bridge': 'viaduct',
                'dual_carriageway': 'yes',
                'highway': 'primary',
                'lanes': '2',
                'layer': '1',
                'maxspeed': '70',
                'name': 'Wita Stwosza',
                'oneway': 'yes',
                'source': 'openstreetmap.org',
                'source:maxspeed': 'sign',
                'surface': 'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 365016934,
                'is_bridge': True,
            })

    def test_boardwalk(self):
        import dsl

        z, x, y = (16, 10535, 25399)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/521108473
            dsl.way(521108473, dsl.tile_diagonal(z, x, y), {
                'access': u'private',
                'bridge': u'boardwalk',
                'highway': u'footway',
                'layer': u'1',
                'operator': u'PG&E',
                'source': u'openstreetmap.org',
                'surface': u'wood',
                'width': u'1',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 521108473,
                'is_bridge': True,
            })

    def test_no(self):
        import dsl

        z, x, y = (16, 10541, 25410)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/518869401
            dsl.way(518869401, dsl.tile_diagonal(z, x, y), {
                'access': u'permissive',
                'bicycle': u'permissive',
                'bridge': u'no',
                'foot': u'permissive',
                'highway': u'footway',
                'horse': u'no',
                'lit': u'yes',
                'motor_vehicle': u'no',
                'source': u'openstreetmap.org',
                'surface': u'concrete',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 518869401,
                'is_bridge': type(None),
            })
