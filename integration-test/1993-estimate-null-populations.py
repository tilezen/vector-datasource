import dsl
from . import FixtureTest


class EstimatePopulationsTest(FixtureTest):

    def test_city(self):
        import dsl

        z, x, y = (9, 259, 175)

        # https://www.openstreetmap.org/node/26691955
        point = dsl.point(26691955, (2.2481797, 48.9479069),
                          {'addr:postcode': u'95100', 'capital': u'7', 'name': u'Argenteuil',
                           'place': u'city', 'population': u'104282',
                           'ref:SIREN': u'219500188', 'source': u'openstreetmap.org',
                           'source:population': u'INSEE 2007', 'wikidata': u'Q181946',
                           'wikipedia': u'fr:Argenteuil (Val-dOise)', })

        self.generate_fixtures(point)

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26691955,
                'population': 104282,
                'min_zoom': 8
            })

        del point.properties['population']

        self.generate_fixtures(point)

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 26691955,
                'population': 10000,
                'min_zoom': 9
            })
