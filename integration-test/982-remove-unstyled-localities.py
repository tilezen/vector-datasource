# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RemoveUnstyledLocalities(FixtureTest):
    def test_zoom_8(self):
        # zoom 8:
        # include only those localities with name and population and
        # kind_detail IN (city, town).
        # example: Arcata https://www.openstreetmap.org/node/141029389 with
        # population.
        self.generate_fixtures(dsl.way(141029389, wkt_loads('POINT (-124.082839865403 40.86651697352439)'), {u'gnis:ST_alpha': u'CA', u'gnis:County_num': u'023', u'name': u'Arcata', u'census:population': u'17231;2010', u'gnis:ST_num': u'06', u'wikipedia': u'en:Arcata, California', u'gnis:County': u'Humboldt', u'ele': u'7', u'source': u'openstreetmap.org', u'gnis:Class': u'Populated Place', u'place': u'town', u'population': u'17231', u'name:ru': u'\u0410\u0440\u043a\u0435\u0439\u0442\u0430', u'wikidata': u'Q631752', u'gnis:id': u'277471', u'import_uuid': u'bb7269ee-502a-5391-8056-e3ce0e66489c', u'is_in': u'Humboldt,California,Calif.,CA,USA'}))  # noqa

        self.assert_has_feature(
            8, 39, 96, 'places',
            {'kind': 'locality', 'kind_detail': 'town', 'name': 'Arcata',
             'id': 141029389, 'min_zoom': 8})

    def test_zoom_9_10(self):
        # zoom 9 and 10:
        # include only those localities with name and kind_detail IN
        # (city, town)
        # This drops the population requirement (cities or towns without
        # population are drawn but with smaller type size) .
        # example: Hoopa http://www.openstreetmap.org/node/4270230299 has no
        # population, is included starting at zoom 9.
        self.generate_fixtures(dsl.way(4270230299, wkt_loads('POINT (-123.685686862951 41.0640389635313)'), {u'wikidata': u'Q5898327', u'place': u'town', u'name': u'Hoopa', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_no_matching_feature(
            8, 40, 95, 'places',
            {'kind': 'locality', 'id': 4270230299})

        self.assert_has_feature(
            9, 80, 191, 'places',
            {'kind': 'locality', 'kind_detail': 'town', 'name': 'Hoopa',
             'id': 4270230299, 'min_zoom': 9})

    def test_zoom_11(self):
        # zoom 11:
        # include only those localities with name and kind_detail IN
        # (city, town)
        # This drops the population requirement (cities or towns without
        # population are drawn but with smaller type size) .
        # include only those localities with name and population and
        # kind_detail IN (village).
        # example: Fairfax http://www.openstreetmap.org/node/150949805 is
        # village with population
        self.generate_fixtures(dsl.way(150949805, wkt_loads('POINT (-122.587967324987 37.98729345716131)'), {u'gnis:ST_alpha': u'CA', u'gnis:County_num': u'041', u'name': u'Fairfax', u'census:population': u'7120;2006', u'gnis:ST_num': u'06', u'import_uuid': u'bb7269ee-502a-5391-8056-e3ce0e66489c', u'ele': u'35', u'source': u'openstreetmap.org', u'gnis:Class': u'Populated Place', u'place': u'village', u'population': u'7120', u'gnis:County': u'Marin', u'gnis:id': u'277511', u'is_in': u'Marin,California,Calif.,CA,USA'}))  # noqa

        self.assert_no_matching_feature(
            10, 163, 395, 'places',
            {'kind': 'locality', 'id': 150949805})

        self.assert_has_feature(
            11, 326, 790, 'places',
            {'kind': 'locality', 'kind_detail': 'village', 'name': 'Fairfax',
             'id': 150949805, 'min_zoom': 11})

    def test_zoom_12(self):
        # zoom 12:
        # include only those localities with name and kind_detail IN
        # (city, town, village)
        # This drops the population requirement (cities, towns, and villages
        # without population are drawn but with smaller type size) .
        # village with no population is Soquel 150933732 that is suddenly
        # visible include only those localities with name and population and
        # kind_detail IN (hamlet).
        # example: http://www.openstreetmap.org/node/150966610 - Duncans Mills,
        # is a hamlet with population.
        self.generate_fixtures(dsl.way(150966610, wkt_loads('POINT (-123.055001171706 38.4538029723741)'), {u'website': u'http://www.duncansmills.net/', u'gnis:ST_alpha': u'CA', u'gnis:County_num': u'097', u'name': u'Duncans Mills', u'gnis:ST_num': u'06', u'addr:postcode': u'95430', u'wikipedia': u'en:Duncans Mills, California', u'ele': u'7', u'source': u'openstreetmap.org', u'gnis:Class': u'Populated Place', u'place': u'hamlet', u'population': u'175', u'gnis:County': u'Sonoma', u'gnis:id': u'222722', u'import_uuid': u'bb7269ee-502a-5391-8056-e3ce0e66489c', u'is_in': u'Sonoma,California,Calif.,CA,USA'}))  # noqa

        self.assert_no_matching_feature(
            11, 323, 786, 'places',
            {'kind': 'locality', 'id': 150966610})

        self.assert_has_feature(
            12, 647, 1573, 'places',
            {'kind': 'locality', 'kind_detail': 'hamlet',
             'name': 'Duncans Mills', 'id': 150966610, 'min_zoom': 12})

    def test_zoom_13_and_up(self):
        # example: http://www.openstreetmap.org/node/150973394 - Inverness
        # hamlet with NO population should NOT show up at zoom 12
        self.generate_fixtures(dsl.way(150973394, wkt_loads('POINT (-122.856937563591 38.10103366949638)'), {u'gnis:ST_alpha': u'CA', u'gnis:County_num': u'041', u'name': u'Inverness', u'source': u'openstreetmap.org', u'gnis:ST_num': u'06', u'ele': u'13', u'import_uuid': u'bb7269ee-502a-5391-8056-e3ce0e66489c', u'gnis:Class': u'Populated Place', u'wikidata': u'Q3306123', u'place': u'hamlet', u'gnis:County': u'Marin', u'gnis:id': u'1658827', u'is_in': u'Marin,California,Calif.,CA,USA'}))  # noqa

        self.assert_no_matching_feature(
            12, 650, 1578, 'places',
            {'kind': 'locality', 'id': 150973394})

        # zoom 13+:
        # include only those localities with name and any kind IN (locality)
        # This drops the population requirement (cities, towns, and all the
        # other kind_details without population are drawn but with smaller
        # type size) .
        # example: Inverness 150973394 hamlet with no population should now
        # show up
        self.assert_has_feature(
            13, 1300, 3156, 'places',
            {'kind': 'locality', 'kind_detail': 'hamlet', 'name': 'Inverness',
             'id': 150973394, 'min_zoom': 13})
