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

    def test_eo57_grnational(self):
        # because EO looks a lot like ΕΟ, but it's not the same!
        import dsl

        z, x, y = (16, 37105, 24465)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/25562707
            dsl.way(25562707, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'layer': u'-1',
                'maxspeed': u'50',
                'name': u'Σήραγγα Ελληνοβουλγαρικής φιλίας',
                'oneway': u'no',
                'ref': u'EO57',
                'source': u'openstreetmap.org',
                'tunnel': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25562707,
                'network': u'GR:national',
                'shield_text': u'57',
                'all_networks': ['GR:national'],
                'all_shield_texts': [u'57'],
            })

    def test_a29_grmotorway(self):
        # because A looks a lot like Α, but it's not the same!
        import dsl

        z, x, y = (16, 36654, 24710)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/27016791
            dsl.way(27016791, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'info': u'correction based on GPS-tracking 2010-10-05',
                'int_name': u'Siatista - Krystallopigi',
                'lanes': u'2',
                'lit': u'no',
                'maxspeed': u'130',
                'name': u'Σιάτιστα - Κρυσταλλοπηγή',
                'oneway': u'yes',
                'ref': u'A29',
                'source': u'openstreetmap.org',
                'toll': u'no',
            }),
            dsl.relation(1, {
                'name': u'Aυτοκινητόδρομος 29 (Σιάτιστα - Κρυσταλλοπηγή)',
                'name:en': u'Motorway 29 (Siatista - Krystallopigi)',
                'ref': u'Α29',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[27016791]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 27016791,
                'network': u'GR:motorway',
                'shield_text': u'Α29',
                'all_networks': ['GR:motorway'],
                'all_shield_texts': [u'Α29'],
            })

    def test_5206_grprovincial52(self):
        # this should _ignore_ the ΕΠ6 ref on the way, as that's a local
        # designation. instead, should use the ref on the relation. see:
        # https://wiki.openstreetmap.org/wiki/WikiProject_Greece/Provincial_Road_Network
        # explicitly says to use "reg_ref" for ΕΠ6, although here it's
        # used in ref, so we should ignore it?

        import dsl

        z, x, y = (16, 37179, 24481)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/15463931
            dsl.way(15463931, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'name': u'Παρανέστι - Σιδηρόνερο',
                'note': u'this is the new route',
                'oneway': u'no',
                'ref': u'ΕΠ6',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'name': u'Παρανέστι - Σιδηρόνερο',
                'network': u'GR:provincial',
                'ref': u'5206',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[15463931]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 15463931,
                'network': u'GR:provincial',
                'shield_text': u'5206',
                'all_networks': [u'GR:provincial'],
                'all_shield_texts': [u'5206'],
            })

    def test_eo7_eo82(self):
        import dsl

        z, x, y = (16, 36785, 25495)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/25114417
            dsl.way(25114417, dsl.tile_diagonal(z, x, y), {
                'date': u'20110715',
                'highway': u'primary',
                'int_name': u'Megalopoli - Kalamata',
                'lanes': u'2',
                'maxspeed': u'70',
                'name': u'Μεγαλόπολη - Καλαμάτα',
                'name:fr': u'Mégalopolis - Kalamata',
                'ref': u'ΕΟ7;ΕΟ82',
                'source': u'openstreetmap.org',
                'source:ref': u'ΦΕΚ B 1932/26.9.2007',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Εθνική Οδός 7 (Κόρινθος - Καλαμάτα)',
                'name:en': u'National Highway 7 (Corinth - Kalamata)',
                'name:fr': u'Route Nationale 7 (Corinthe - Kalamata)',
                'network': u'GR:national',
                'ref': u'ΕΟ7',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q487890',
            }, ways=[25114417]),
            dsl.relation(2, {
                'int_name': u'Ethniki Odos 82 (Sparti - Kalamata - Pylos)',
                'name': u'Εθνική Οδός 82 (Σπάρτη - Καλαμάτα - Πύλος)',
                'name:en': u'National Highway 82 (Sparta - Kalamata - Pylos)',
                'name:fr': u'Route Nationale 82 (Sparte - Kalamata - Pylos)',
                'network': u'GR:national',
                'ref': u'ΕΟ82',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[25114417]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 25114417,
                'network': u'GR:national',
                'shield_text': u'7',
                'all_networks': ['GR:national', 'GR:national'],
                'all_shield_texts': ['7', '82'],
            })

    def test_8a_grnational(self):
        # checking that we keep the trailing alpha
        import dsl

        z, x, y = (16, 36730, 25214)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/19832532
            dsl.way(19832532, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'lanes': u'2',
                'lit': u'yes',
                'maxspeed': u'50',
                'name': u'Νέα Εθνική Οδός Πατρών - Αθηνών',
                'oneway': u'yes',
                'ref': u'ΕΟ8α',
                'smoothness': u'excellent',
                'source': u'openstreetmap.org',
                'source:ref': u'OKXE',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'int_name': u'Korinthos - Patra',
                'name': u'Εθνική Οδός 8α (Κόρινθος - Πάτρα)',
                'name:en': u'National Highway 8α (Korinthos - Patra)',
                'name:fr': u'Route nationale 8α (Corinthe - Patras)',
                'network': u'GR:national',
                'ref': u'ΕΟ8α',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[19832532]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 19832532,
                'network': u'GR:national',
                'shield_text': u'8α',
            })

    def test_eo3_eroad(self):
        # checking the sort order - e-roads last
        import dsl

        z, x, y = (16, 36710, 24650)

        self.generate_fixtures(
            dsl.is_in('GR', z, x, y),
            # https://www.openstreetmap.org/way/26934885
            dsl.way(26934885, dsl.tile_diagonal(z, x, y), {
                'date': u'20120711',
                'embankment': u'yes',
                'highway': u'trunk',
                'int_name': u'Florina - Edessa',
                'int_ref': u'E 65;E 86',
                'lanes': u'2',
                'layer': u'1',
                'maxspeed': u'90',
                'name': u'Φλώρινα - Έδεσσα',
                'official_name': u'Εθνική Οδός 3;Κοζάνη - Φλώρινα - Νίκη',
                'oneway': u'no',
                'ref': u'ΕΟ3',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'e-road:class': u'A-reference',
                'name': u'European Road 65 (Greece)',
                'name:bg': u'Европейски път Е65 (Гърция)',
                'name:cs': u'Evropská silnice E65 (Řecko)',
                'name:el': u'Ευρωπαϊκή Οδός 65 (Ελλάδα)',
                'name:fr': u'Route Européenne 65 (Grèce)',
                'name:mk': u'Европски пат Е65 (Грција)',
                'name:sq': u'Rruga evropiane E65 (Greqia)',
                'name:tr': u'Avrupa E-yolu E65 (Yunanistan)',
                'network': u'e-road',
                'note': u'Intricate relation. Do not autosort.',
                'ref': u'E 65',
                'route': u'road',
                'section': u'Greece',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q911135',
            }, ways=[26934885]),
            dsl.relation(2, {
                'name': u'Εθνική Οδός 3 (Ελευσίνα - Λάρισα - Νίκη)',
                'name:en': u'National Highway 3 (Elefsina - Larissa - Niki)',
                'name:fr': u'Route Nationale 3 (Éleusis - Larissa - Niki)',
                'network': u'GR:national',
                'note': u'Intricate relation - do not auto-sort.',
                'ref': u'ΕΟ3',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q528444',
            }, ways=[26934885]),
            dsl.relation(3, {
                'description': u'Krystallopigi - Florina - Edessa - Gefyra',
                'description:fr': u'E 86 Kristallopigí - Géfyra',
                'e-road:class': u'A-intermediate',
                'name': u'European Road 86 (Greece)',
                'name:bg': u'Европейски път Е86 (Гърция)',
                'name:el': u'Ευρωπαϊκή Οδός 86 (Ελλάδα)',
                'name:fr': u'Route européenne E 86',
                'name:mk': u'Европски пат Е86 (Грција)',
                'name:sq': u'Rruga evropiane E86 (Greqia)',
                'name:tr': u'Avrupa E-yolu E86 (Yunanistan)',
                'network': u'e-road',
                'ref': u'E 86',
                'route': u'road',
                'section': u'Greece',
                'source': u'openstreetmap.org',
                'type': u'route',
                'wikidata': u'Q1376023',
            }, ways=[26934885]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 26934885,
                'network': u'GR:national',
                'shield_text': '3',
                'all_networks': ['GR:national', 'e-road', 'e-road'],
                'all_shield_texts': ['3', 'E65', 'E86'],
            })
