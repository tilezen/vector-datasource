import dsl

from . import FixtureTest


class TestNEName(FixtureTest):
    def test_use_ne_name_country(self):
        z, x, y = (16, 10482, 25333)

        self.generate_fixtures(
            dsl.point(10200326532, (-122.4195493, 37.7653381), {
                u'place': u'country',
                u'name': u'Schweiz/Suisse/Svizzera/Svizra',
                u'name:en': u'Switzerland',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q30',
                u'ne_name_en': u'Test'
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 10200326532,
                'name:en': u'Test'
            })

    def test_use_ne_name_hamlet(self):
        z, x, y = (16, 10482, 25333)

        self.generate_fixtures(
            dsl.point(10200326532, (-122.4195493, 37.7653381), {
                u'place': u'hamlet',
                u'name': u'Schweiz/Suisse/Svizzera/Svizra',
                u'name:en': u'Switzerland',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q30',
                u'ne_name_en': u'Test'
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 10200326532,
                'name:en': u'Test'
            })


    def test_no_ne_name(self):
        z, x, y = (16, 10482, 25333)

        self.generate_fixtures(
            dsl.point(10200326532, (-122.4195493, 37.7653381), {
                u'place': u'country',
                u'name': u'Schweiz/Suisse/Svizzera/Svizra',
                u'name:en': u'Switzerland',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q30',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 10200326532,
                'name:en': u'Switzerland'
            })
