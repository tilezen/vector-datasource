# -*- encoding: utf-8 -*-
from . import FixtureTest


class NorwegianShieldTest(FixtureTest):
    def test_no_oslo_ring(self):
        # there's a different sign for the Store Ringvei (Oslo Ring-road). also
        # looks like in Norway they actually sign the E-roads.
        #
        # https://en.wikipedia.org/wiki/Ring_3_(Oslo)
        # https://en.wikipedia.org/wiki/Norwegian_national_road

        import dsl

        z, x, y = (16, 34736, 19062)

        self.generate_fixtures(
            dsl.is_in('NO', z, x, y),
            # https://www.openstreetmap.org/way/71218142
            dsl.way(71218142, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'E 06',
                'lanes': u'2',
                'maxspeed': u'70',
                'maxspeed:conditional': u'60 @ (Nov 01 - Apr 8)',
                'name': u'Adolf Hedins vei',
                'oneway': u'yes',
                'ref': u'E 6;Ring 3',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'nat_ref': u'E 6',
                'network': u'e-road',
                'ref': u'E 06',
                'route': u'road',
                'section': u'Norway (south-south)',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q921422',
                'wikipedia': u'de:Europastraße 6',
            }, ways=[71218142]),
            dsl.relation(2, {
                'name': u'Store ringvei',
                'ref': u'Ring 3',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[71218142]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 71218142,
                'network': u'NO:oslo:ring',
                'shield_text': 'Ring 3',
                'all_networks': ['NO:oslo:ring', 'e-road'],
                'all_shield_texts': ['Ring 3', 'E 6'],
            })

    def test_51_nofylkesvei(self):
        # interesting set of networks... but we should be able to normalise
        # them, or recover the network from the ref=Fv##
        import dsl

        z, x, y = (16, 34420, 18373)

        self.generate_fixtures(
            dsl.is_in('NO', z, x, y),
            # https://www.openstreetmap.org/way/26119489
            dsl.way(26119489, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'maxspeed': u'80',
                'name': u'Fjellvegen',
                'ref': u'51',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Fylkesvei 51',
                'network': u'no:Fylkesvei (Oppland);no:Fylkesvei (Buskerud)',
                'operator': u'Statens vegvesen',
                'ref': u'Fv51',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1770921',
                'wikipedia': u'no:Fylkesvei 51',
            }, ways=[26119489]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26119489,
                'network': u'NO:fylkesvei',
                'shield_text': u'51',
                'all_networks': [u'NO:fylkesvei'],
                'all_shield_texts': [u'51'],
            })

    def test_270_nofylkesvei(self):
        import dsl

        z, x, y = (16, 33734, 18885)

        self.generate_fixtures(
            dsl.is_in('NO', z, x, y),
            # https://www.openstreetmap.org/way/3648469
            dsl.way(3648469, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'50',
                'name': u'Tollbodallmenningen',
                'ref': u'270',
                'sidewalk': u'both',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Fylkesvei 270 (Hordaland)',
                'network': u'no:Fylkesvei (Hordaland)',
                'operator': u'Hordaland Fylkeskommune',
                'ref': u'270',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q6367270',
                'wikipedia': u'no:Fylkesvei 270 (Hordaland)',
            }, ways=[3648469]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 3648469,
                'network': u'NO:fylkesvei',
                'shield_text': u'270',
                'all_networks': [u'NO:fylkesvei'],
                'all_shield_texts': [u'270'],
            })
