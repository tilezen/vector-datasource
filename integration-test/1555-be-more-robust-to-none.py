# -*- encoding: utf-8 -*-
from . import FixtureTest


class RobustToNoneTest(FixtureTest):

    def test_fake_rel_with_ref_none(self):
        # this starts with real data, but i've removed the ref from the
        # relation to inject a None into the network "fixup" code.

        import dsl

        z, x, y = (16, 36334, 21769)

        self.generate_fixtures(
            dsl.is_in('PL', z, x, y),
            # https://www.openstreetmap.org/way/367163748
            dsl.way(367163748, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'int_ref': u'E 67;E 75',
                'name': u'Autostrada Bursztynowa',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Autostrada A1',
                'network': u'pl:motorways',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[367163748]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 367163748,
                'network': 'PL:motorway',
            })

    def test_es_ref_no_digits(self):
        import dsl
        z, x, y = (16, 32360, 24673)
        self.generate_fixtures(
            dsl.is_in('ES', z, x, y),
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'motorway',
                'source': 'openstreetmap.org',
            }),
            dsl.relation(1, {
                # NOTE: no "ref" on the relation.
                'network': 'ES:A-road',
                'route': 'road',
                'type': 'route',
                'source': 'openstreetmap.org',
            }, ways=[1]),
        )

        # can't figure out network or shield_text for this!
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 1,
                'network': type(None),
                'shield_text': type(None),
            })
