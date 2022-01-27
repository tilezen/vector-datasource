# -*- encoding: utf-8 -*-
import dsl

from . import FixtureTest


class OSMNEJoinTest(FixtureTest):
    # test that the population_rank is overridden by __ne_pop_max
    def test_ne_pop_max_override(self):
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
                '__ne_pop_max': u'1000000000'
            }),
        )

        # population is directly from 'population' property
        # however the population_rank is calculated from '__ne_pop_max'
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                'population': 864816,
                'population_rank': 18
            })

    # test that the population is overridden by __ne_pop_min
    def test_ne_pop_min_override(self):
        z, x, y = (16, 10482, 25330)
        self.generate_fixtures(
            # https://www.openstreetmap.org/node/26819236
            dsl.point(26819236, (-122.4199061, 37.7790262), {
                'name': u'San Francisco',
                'place': u'city',
                'rank': u'10',
                'short_name': u'SF',
                'source': u'openstreetmap.org',
                'wikidata': u'Q62',
                'wikipedia': u'en:San Francisco',
                '__ne_pop_min': u'50000000',
            }),
        )

        # population is not available from 'population' property
        # however '__ne_pop_min' should backfill it and be used to calculate
        # population_rank
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                'population': 50000000,
                'population_rank': 16
            })

    # test that the min_zoom is overridden by __ne_min_zoom
    def test_ne_min_zoom(self):
        z, x, y = (16, 10482, 25330)
        self.generate_fixtures(
            # https://www.openstreetmap.org/node/26819236
            dsl.point(26819236, (-122.4199061, 37.7790262), {
                'name': u'San Francisco',
                'place': u'city',
                'rank': u'10',
                'short_name': u'SF',
                'source': u'openstreetmap.org',
                'wikidata': u'Q62',
                'wikipedia': u'en:San Francisco',
            }),
        )

        # without __ne_min_zoom, the min_zoom should be 8 which is from the
        # yaml/places.yaml file
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                'min_zoom': 8,
            })
