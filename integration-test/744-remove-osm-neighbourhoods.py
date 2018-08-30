# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RemoveOsmNeighbourhoods(FixtureTest):
    def test_no_borough(self):
        # Node: Mount Pocono (158473043)
        self.generate_fixtures(dsl.way(158473043, wkt_loads('POINT (-75.36462806481801 41.12203367097907)'), {u'gnis:ST_alpha': u'PA', u'gnis:County_num': u'089', u'name': u'Mount Pocono', u'census:population': u'3001;2006', u'gnis:ST_num': u'42', u'import_uuid': u'bb7269ee-502a-5391-8056-e3ce0e66489c', u'ele': u'562', u'source': u'openstreetmap.org', u'gnis:Class': u'Populated Place', u'place': u'borough', u'population': u'3001', u'gnis:County': u'Monroe', u'gnis:id': u'1181833', u'is_in': u'Monroe,Pennsylvania,Pa.,PA,USA'}))  # noqa

        self.assert_no_matching_feature(
            16, 19048, 24541, 'places',
            {'kind': 'borough', 'source': 'openstreetmap.org'})

    def test_no_suburb(self):
        # Node: Centerville District (150939391)
        self.generate_fixtures(dsl.way(150939391, wkt_loads('POINT (-121.999127674959 37.5541029557231)'), {u'gnis:ST_alpha': u'CA', u'gnis:County_num': u'001', u'name': u'Centerville District', u'source': u'openstreetmap.org', u'gnis:ST_num': u'06', u'ele': u'16', u'import_uuid': u'bb7269ee-502a-5391-8056-e3ce0e66489c', u'gnis:Class': u'Populated Place', u'place': u'suburb', u'gnis:County': u'Alameda', u'gnis:id': u'1658251', u'is_in': u'Fremont,California,Calif.,CA,USA'}))  # noqa

        self.assert_no_matching_feature(
            16, 10558, 25381, 'places',
            {'kind': 'suburb', 'source': 'openstreetmap.org'})

    def test_no_quarter(self):
        # Node: Northeast (2790349074)
        self.generate_fixtures(dsl.way(2790349074, wkt_loads('POINT (-76.98003089067129 38.91991558011007)'), {u'source': u'openstreetmap.org', u'place': u'quarter', u'name': u'Northeast'}))  # noqa

        self.assert_no_matching_feature(
            16, 18754, 25065, 'places',
            {'kind': 'quarter', 'source': 'openstreetmap.org'})
