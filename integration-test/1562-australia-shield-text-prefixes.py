# -*- encoding: utf-8 -*-
from . import FixtureTest


class AustraliaShieldTextPrefixesTest(FixtureTest):

    def test_m(self):
        import dsl

        z, x, y = (16, 60295, 39334)

        self.generate_fixtures(
            dsl.is_in('AU', z, x, y),
            # https://www.openstreetmap.org/way/170318728
            dsl.way(170318728, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'no',
                'highway': u'motorway',
                'lanes': u'2',
                'layer': u'-1',
                'maxspeed': u'80',
                'name': u'Eastern Distributor',
                'old_network': u'MR',
                'old_ref': u'1',
                'oneway': u'yes',
                'ref': u'M1',
                'ref:start_date': u'2013-08',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'toll': u'yes',
            }),
            dsl.relation(1, {
                'addr:country': u'AU',
                'addr:state': u'NSW',
                'ref': u'M1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[170318728]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 170318728,
                'shield_text': 'M1',
                'network': 'AU:M-road',
            })

    def test_a(self):
        import dsl

        z, x, y = (16, 60290, 39332)

        self.generate_fixtures(
            dsl.is_in('AU', z, x, y),
            # https://www.openstreetmap.org/way/286361145
            dsl.way(286361145, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'4',
                'lit': u'yes',
                'maxspeed': u'50',
                'name': u'King Street',
                'parking:lane:both:parallel': u'on_street',
                'parking:lane:both:width': u'2',
                'ref': u'A36',
                'ref:start_date': u'2013-06',
                'sidewalk': u'both',
                'smoothness:lanes': u'|||intermediate',
                'source': u'openstreetmap.org',
                'surface': u'paved',
                'width': u'13.7',
            }),
            dsl.relation(1, {
                'addr:country': u'AU',
                'addr:state': u'NSW',
                'ref': u'A36',
                'ref:start_date': u'2013-06',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[286361145]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 286361145,
                'shield_text': 'A36',
                'network': 'AU:A-road',
            })
