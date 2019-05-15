# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class MissingLocalizedNames(FixtureTest):
    def test_nj_ny_state_boundary(self):
        # New Jersey - New York state boundary
        self.generate_fixtures(
            dsl.way(37565051, wkt_loads(
                'LINESTRING (-74.05332209032987 40.65563874006117, '
                '-74.0557389479016 40.65175995493708)'), {
                    u'source': u'openstreetmap.org',
                    u'boundary': u'administrative',
                    u'maritime': u'yes',
                    u'admin_level': u'4',
            }),
            dsl.way(61603753, wkt_loads(
                'LINESTRING (-74.0557389479016 40.65175995493708, '
                '-74.058837890625 40.65177013430829)'), {
                    u'source': u'openstreetmap.org',
                    u'boundary': u'administrative',
                    u'maritime': u'yes',
                    u'admin_level': u'4',
            }),
            dsl.way(-224951, wkt_loads(
                'LINESTRING (-74.058837890625 40.65177013430829, '
                '-74.0557389479016 40.65175995493708, '
                '-74.05332209032987 40.65563874006117)'), {
                    u'ISO3166-2': u'US-NJ',
                    u'admin_level': u'4',
                    u'boundary': u'administrative',
                    u'is_in:country_code': u'US',
                    u'name': u'New Jersey',
                    u'name:es': u'Nueva Jersey',
                    u'name:lv': u'\u0145\u016bd\u017eersija',
                    u'ref': u'NJ',
                    u'ref:fips': u'34',
                    u'source': u'openstreetmap.org',
                    u'wikidata': u'Q1408',
                    u'wikipedia': u'en:New Jersey',
                    'mz_boundary_from_polygon': True,  # need this for hack
            }),
            dsl.way(-61320, wkt_loads(
                'LINESTRING (-74.058837890625 40.65177013430829, '
                '-74.0557389479016 40.65175995493708, '
                '-74.05332209032987 40.65563874006117)'), {
                    u'ISO3166-2': u'US-NY',
                    u'admin_level': u'4',
                    u'alt_name': u'New York State',
                    u'boundary': u'administrative',
                    u'is_in:country_code': u'US',
                    u'name': u'New York',
                    u'name:es': u'Nueva York',
                    u'name:lv': u'\u0145ujorka',
                    u'ref': u'NY',
                    u'ref:fips': u'36',
                    u'source': u'openstreetmap.org',
                    u'wikidata': u'Q1384',
                    u'wikipedia': u'en:New York',
                    'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            15, 9643, 12327, "boundaries",
            {"kind": "region", "name": "New Jersey - New York",
             "name:right": "New York", "name:left": "New Jersey",
             "name:right:es": "Nueva York", "name:left:es": "Nueva Jersey",
             "name:right:lv": u"Ņujorka", "name:left:lv": u"Ņūdžersija"})
