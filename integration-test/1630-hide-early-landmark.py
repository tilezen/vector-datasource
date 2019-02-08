# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlyLandmarkTest(FixtureTest):

    def test_prison_rikers_island(self):
        import dsl

        z, x, y = (13, 2414, 3077)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/3955540
            dsl.way(3955540, dsl.box_area(z, x, y, 2919251), {
                'amenity': 'prison',
                'ele': '8',
                'gnis:county_id': '005',
                'gnis:created': '01/23/1980',
                'gnis:edited': '10/27/2005',
                'gnis:feature_id': '962524',
                'gnis:state_id': '36',
                'name': 'Rikers Island',
                'place': 'island',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wikidata': 'Q120119',
                'wikipedia': 'en:Rikers Island',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3955540,
                'kind': 'prison',
                'min_zoom': 13,
            })

    def test_museum_petit_palais(self):
        import dsl

        z, x, y = (12, 2074, 1408)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/2778854
            dsl.way(2778854, dsl.box_area(z, x, y, 20111), {
                'addr:city': 'Paris',
                'addr:postcode': '75008',
                'addr:street': 'Avenue Winston Churchill',
                'architect': 'Charles Girault',
                'building': 'yes',
                'heritage': '3',
                'heritage:operator': 'mhs',
                'internet_access': 'wlan',
                'internet_access:fee': 'no',
                'internet_access:operator': 'Mairie de Paris',
                'name': 'Petit Palais',
                'opening_hours': 'Tu-Su 10:00-18:00',
                'phone': '+33 153 434 000',
                'ref:mhs': 'PA00088878',
                'source': 'openstreetmap.org',
                'source:internet_access': 'Paris Open Data',
                'start_date': '1900',
                'tourism': 'museum',
                'type': 'multipolygon',
                'website': 'http://www.petitpalais.paris.fr/',
                'wikidata': 'Q820892',
                'wikipedia': 'fr:Petit Palais',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2778854,
                'kind': 'museum',
                'min_zoom': 12,
            })

    def test_landmark_ghirardelli_square(self):
        import dsl

        z, x, y = (12, 655, 1582)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/27104863
            dsl.way(27104863, dsl.box_area(z, x, y, 18245), {
                'area': 'yes',
                'historic': 'landmark',
                'landuse': 'retail',
                'name': 'Ghirardelli Square',
                'name:ko': u'\uae30\ub77c\ub378\ub9ac \uc2a4\ud018\uc5b4',
                'opening_hours': '11:00-21:00',
                'source': 'openstreetmap.org',
                'tourism': 'attraction',
                'wikidata': 'Q5556730',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 27104863,
                'kind': 'landmark',
                'min_zoom': 12,
            })
