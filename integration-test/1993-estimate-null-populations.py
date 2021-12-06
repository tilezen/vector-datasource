import dsl

from . import FixtureTest


class EstimatePopulationsTest(FixtureTest):

    def validate_est_population(self, point, tile_coord, min_zoom_with_pop, min_zoom_with_est_pop, est_pop):
        z, x, y = tile_coord

        self.generate_fixtures(point)
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': point.fid,
                'population': int(point.properties['population']),
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
        z, x, y = (10, 518, 351)
        # https://www.openstreetmap.org/node/26691955
        city = dsl.point(26691955, (2.2481797, 48.9479069),
                         {'addr:postcode': u'95100', 'capital': u'7', 'name': u'Argenteuil',
                          'place': u'city', 'population': u'104282',
                          'ref:SIREN': u'219500188', 'source': u'openstreetmap.org',
                          'source:population': u'INSEE 2007', 'wikidata': u'Q181946',
                          'wikipedia': u'fr:Argenteuil (Val-dOise)', })

        self.validate_est_population(city, (z, x, y), 8, 9, 10000)

    def test_town(self):
        z, x, y = (11, 1036, 703)
        # https://www.openstreetmap.org/node/26691480
        town = dsl.point(26691480, (2.2303498, 48.986025), {
            'alt_name': u'Franconville',
            'name': u'Franconville-la-Garenne',
            'place': u'town',
            'population': u'33097',
            'source': u'openstreetmap.org',
            'source:population': u'INSEE 2013',
            'wikidata': u'Q237333',
        })
        self.validate_est_population(town, (z, x, y), 8, 10, 5000)

    def test_locality(self):
        z, x, y = (14, 8296, 5638)
        # https://www.openstreetmap.org/node/442197
        locality = dsl.point(442197, (2.2883604, 48.8326932),
                             {'name': u'Porte de Versailles', 'place': u'locality', 'population': u'1121',
                              'source': u'openstreetmap.org',
                              'unsigned': u'no', })
        self.validate_est_population(locality, (z, x, y), 13, 14, 1000)

    def test_village(self):
        z, x, y = (13, 4141, 2827)
        # https://www.openstreetmap.org/node/602470737
        village = dsl.point(602470737, (1.9878964, 48.5872266),
                            {'addr:postcode': u'78730', 'name': u'Rochefort-en-Yvelines', 'place': u'village',
                             'population': u'956', 'source': u'openstreetmap.org', })

        self.validate_est_population(village, (z, x, y), 12, 13, 2000)

    def test_hamlet(self):
        z, x, y = (15, 16563, 11302)
        # https://www.openstreetmap.org/node/534228360
        hamlet = dsl.point(534228360, (1.967011, 48.6425931),
                           {'name': u'Les Bordes', 'place': u'hamlet', 'population': u'816',
                            'source': u'openstreetmap.org', })
        self.validate_est_population(hamlet, (z, x, y), 13, 14, 200)

    def test_isolated_dwelling(self):
        z, x, y = (16, 33142, 22608)
        # https://www.openstreetmap.org/node/5111001636
        dwelling = dsl.point(5111001636, (2.0597882, 48.6321613),
                             {'name': u'La Maison Grise', 'place': u'isolated_dwelling', 'population': u'220',
                              'source': u'openstreetmap.org', })
        self.validate_est_population(dwelling, (z, x, y), 14, 15, 100)

    def test_farm(self):
        z, x, y = (16, 33137, 22614)
        # https://www.openstreetmap.org/node/5922383856
        farm = dsl.point(5922383856, (2.0303734, 48.6082567),
                         {'contact:website': u'https://www.fermedesclos.com/', 'name': u'Ferme des Clos',
                          'place': u'farm', 'population': u'91', 'source': u'openstreetmap.org', })
        self.validate_est_population(farm, (z, x, y), 14, 15, 50)
