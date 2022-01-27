# -*- encoding: utf-8 -*-
import dsl

from . import FixtureTest


class OSMNEJoinTest(FixtureTest):
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
                '__ne_pop_max': u'20000000'
            }),
        )

        # population is available directly from 'population' property
        # however the population_rank is calculated from '__ne_pop_max'
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                'population': 864816,
                'population_rank': 15
            })
        # __ne_pop_max shouldn't appear in the final result
        self.assert_no_matching_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                '__ne_pop_max': 20000000,
            })

    def test_ne_pop_min_override_estimate(self):
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
                '__ne_pop_min': u'50000000'
            }),
        )

        # population is not available from source but backfilled by
        # __ne_pop_min also __ne_pop_max is not available so
        # population_rank is still calculated by the value of the backfilled
        # population which is __ne_pop_min
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                'population': 50000000,
                'population_rank': 16
            })

        # __ne_pop_min shouldn't appear in the final result
        self.assert_no_matching_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                '__ne_pop_min': 50000000,
            })

    def test_ne_pop_max_override_estimate_pop_rank(self):
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
                '__ne_pop_max': u'20000000'
            }),
        )

        # population is not available from source but backfilled by
        # the estimate defined in tags_set_ne_pop_min_max_default
        # population_rank is still calculated by __ne_pop_max
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                'population': 10000,
                'population_rank': 15
            })
        # __ne_pop_max shouldn't appear in the final result
        self.assert_no_matching_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                '__ne_pop_max': 20000000,
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
                '__ne_min_zoom': 10,
            }),
        )

        # without __ne_min_zoom, the min_zoom should be 8 which is from the
        # https://github.com/tilezen/vector-datasource/blob/80799e74e0283a96b520c6fea8fa00455095e09b/yaml/places.yaml#L145
        # but with __ne_min_zoom override, it is 10
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                'min_zoom': 10,
            })

        # __ne_min_zoom shouldn't appear in the final result
        self.assert_no_matching_feature(
            z, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'kind_detail': 'city',
                'wikidata_id': 'Q62',
                '__ne_min_zoom': 10,
            })
