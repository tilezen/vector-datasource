# -*- encoding: utf-8 -*-
from . import FixtureTest


class RegionCapital(FixtureTest):

    def test_taichung(self):
        import dsl

        z, x, y = (10, 855, 441)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/60655918
            dsl.point(60655918, (120.6478282, 24.163162), {
                'name': u'臺中市',
                'name:en': u'Taichung',
                'place': u'city',
                'population': u'2767239',
                'source': u'openstreetmap.org',
                'wikidata': u'Q245023',
                'wikipedia': u'zh:臺中市',

                # these come from NE data joined on wikidataid
                'featurecla': 'Admin-1 capital',
                'fclass_cn': 'Populated place',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 60655918,
                'region_capital': type(True),
                'region_capital:cn': type(False),
            })
