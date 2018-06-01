# -*- encoding: utf-8 -*-
from . import FixtureTest


class GreekShieldTest(FixtureTest):
    def test_8_grnational(self):
        import dsl

        z, x, y = (16, 37084, 25282)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/299496935
            dsl.way(299496935, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'int_name': u'Athinon',
                'lit': u'yes',
                'maxspeed': u'50',
                'name': u'Αθηνών',
                'nat_ref': u'ΕΟ8α',
                'oneway': u'yes',
                'ref': u'ΕΟ8',
                'source': u'openstreetmap.org',
                'source:ref': u'ΦΕΚ Β 319/23.07.1963',
                'wikipedia': u'en:Athinon Avenue',
            }),
            dsl.relation(1, {
                'name': u'Εθνική Οδός 8 (Αθήνα - Πάτρα)',
                'name:en': u'National Highway 8 (Athens - Patras)',
                'name:fr': u'Route Nationale 8 (Athènes - Patras)',
                'network': u'GR:national',
                'ref': u'ΕΟ8',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q959405',
            }, ways=[299496935]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 299496935,
                'network': u'GR:national',
                'shield_text': u'8',
            })

    def test_a6_grmotorway(self):
        import dsl

        z, x, y = (16, 37070, 25258)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/85601631
            dsl.way(85601631, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'no',
                'foot': u'no',
                'hazmat': u'no',
                'highway': u'motorway',
                'horse': u'no',
                'int_name': u'Autokinitodromos 6 (Attiki Odos)',
                'int_ref': u'E 94',
                'lanes': u'3',
                'lit': u'yes',
                'name': u'Αυτοκινητόδρομος 6 (Αττική Οδός)',
                'name:en': u'Motorway 6 (Attiki Odos)',
                'name:fr': u'Autoroute 6 (Attiki Odos)',
                'oneway': u'yes',
                'operator': u'Αττική Οδός',
                'ref': u'Α6',
                'smoothness': u'excellent',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'toll': u'yes',
            }),
            dsl.relation(1, {
                'description:fr': u'E 94 Corinthe - Athènes',
                'e-road:class': u'A-intermediate',
                'name': u'Ευρωπαική Οδός 94 (Κόρινθος - Αθήνα)',
                'name:en': u'European Route 94 (Corinth - Athens)',
                'name:fr': u'Route européenne E 94',
                'network': u'e-road',
                'ref': u'E 94',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q2586090',
            }, ways=[85601631]),
            dsl.relation(2, {
                'contact:website': u'http://www.aodos.gr/',
                'int_name': u'Autokinitodromos 6 (Attiki Odos)',
                'name': u'Αυτοκινητόδρομος 6 (Αττική Οδός)',
                'name:en': u'Motorway 6 (Attiki Odos)',
                'name:fr': u'Autoroute 6 (Attiki Odos)',
                'network': u'GR:motorway',
                'ref': u'Α6',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[85601631]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 85601631,
                'network': u'GR:motorway',
                # NOTE: the 'A' here is a capital Greek alpha, not Latin A
                'shield_text': u'Α6',
                'all_networks': ['GR:motorway', 'e-road'],
                # TODO: should the e-road have a E prefix?
                'all_shield_texts': [u'Α6', 'E94'],
            })
