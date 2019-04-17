# -*- encoding: utf-8 -*-
from . import FixtureTest


class OSMTest(FixtureTest):

    def test_place(self):
        import dsl

        z, x, y = (16, 10482, 25330)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/26819236
            dsl.point(26819236, (-122.4199061, 37.7790262), {
                'name': u'San Francisco',
                'place': u'city',
                'population': u'864816',
                'rank': u'10',
                'short_name': u'SF',
                'source': u'openstreetmap.org',
                'wikidata': u'Q62',
                'wikipedia': u'en:San Francisco',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
            })

    def test_poi(self):
        import dsl

        z, x, y = (16, 10482, 25330)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1901905716
            dsl.point(1901905716, (-122.4185377, 37.7789014), {
                'historic': u'memorial',
                'name': u'Abraham Lincoln',
                'source': u'openstreetmap.org',
                'wikidata': u'Q20011487',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1901905716,
                'kind': u'memorial',
                'wikidata_id': u'Q20011487',
            })

    def test_water(self):
        import dsl

        z, x, y = (16, 10752, 32895)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/305640005
            dsl.way(305640005, dsl.tile_centre_shape(z, x, y), {
                'name': u'Pacific Ocean',
                'place': u'ocean',
                'source': u'openstreetmap.org',
                'wikidata': u'Q98',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 305640005,
                'kind': u'ocean',
                'wikidata_id': u'Q98',
            })


class WOFTest(FixtureTest):

    def test_place(self):
        import dsl

        z, x, y = (16, 10483, 25328)

        self.generate_fixtures(
            dsl.point(85865903, (-122.414102, 37.785926), {
                "max_zoom": 18.0,
                "min_zoom": 15.0,
                "name": "Tenderloin",
                "placetype": "neighbourhood",
                "source": "whosonfirst.org",
                "wikidata": "Q7464",
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 85865903,
                'kind': 'neighbourhood',
                'wikidata_id': 'Q7464',
            })
