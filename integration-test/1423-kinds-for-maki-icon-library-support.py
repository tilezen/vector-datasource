# -*- encoding: utf-8 -*-
from . import FixtureTest


class KindsForMakiIconSupportTest(FixtureTest):

    def test_airfield_node(self):
        import dsl

        z, x, y = (16, 40052, 53633)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/368396366
            dsl.point(368396366, (40.0168224, -74.591995), {
                'addr:state': u'NJ',
                'aerodrome:type': u'military',
                'ele': u'43',
                'gnis:county_name': u'Burlington',
                'gnis:created': u'08/01/1994',
                'gnis:feature_id': u'884993,2512291',
                'gnis:feature_type': u'Airport',
                'iata': u'WRI',
                'icao': u'KWRI',
                'is_in:iso_3166_2': u'US-NJ',
                'landuse': u'military',
                'military': u'airfield',
                'name': u'McGuire Air Force Base',
                'owner': u'US Air Force',
                'source': u'openstreetmap.org',
                'wikidata': u'Q10860392',
                'wikipedia': u'en:McGuire Air Force Base',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 368396366,
                'kind': u'airfield',
                'kind_detail': 'military',
            })

    def test_airfield_way(self):
        # NOTE: i think  this is probably _not_ actually a military airfield.
        # seems to be the site of the Radio Control Society of Marine Park
        # http://www.rcsmp.com/ - but useful as a test nonetheless.
        import dsl

        z, x, y = (16, 40157, 53181)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/468561706
            dsl.way(468561706, dsl.tile_box(z, x, y), {
                'military': u'airfield',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 468561706,
                'kind': u'airfield',
            })
