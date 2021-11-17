import dsl
from . import FixtureTest


class EstimatePopulationsTest(FixtureTest):

    def validate_est_population(self, point, min_zoom_with_pop, est_pop, min_zoom_with_est_pop):
        z, x, y = (9, 259, 175)

        self.generate_fixtures(point)
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': point.fid,
                'population': int(point.features['population']),
                'min_zoom': min_zoom_with_pop
            })

        del point.properties['population']

        self.generate_fixtures(point)
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': point.fid,
                'population': est_pop,
                'min_zoom': min_zoom_with_est_pop
            })

    def test_city(self):
        # https://www.openstreetmap.org/node/26691955
        city = dsl.point(26691955, (2.2481797, 48.9479069),
                          {'addr:postcode': u'95100', 'capital': u'7', 'name': u'Argenteuil',
                           'place': u'city', 'population': u'104282',
                           'ref:SIREN': u'219500188', 'source': u'openstreetmap.org',
                           'source:population': u'INSEE 2007', 'wikidata': u'Q181946',
                           'wikipedia': u'fr:Argenteuil (Val-dOise)', })

        self.validate_est_population(city, 8, 10000, 9)

    def test_town(self):
        # https://www.openstreetmap.org/node/26691480
        town = dsl.point(26691480, (2.2303498, 48.986025), {
            'alt_name': u'Franconville',
            'name': u'Franconville-la-Garenne',
            'place': u'town',
            'population': u'33097',
            'source': u'openstreetmap.org',
            'source:population': u'INSEE 2013',
            'wikidata': u'Q237333',
        }),

        self.validate_est_population(town, 9, 5000, 10)
