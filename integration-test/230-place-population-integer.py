from . import OsmFixtureTest


class PlacePopulationInteger(OsmFixtureTest):

    def test_south_bay(self):
        # all these places are in the south bay, near SF, CA.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/2835016',  # Foster City
            'http://www.openstreetmap.org/relation/2835017',  # San Mateo
            'http://www.openstreetmap.org/node/150967056',  # Belmont
            'http://www.openstreetmap.org/node/150975918',  # San Carlos
            'http://www.openstreetmap.org/node/150946345',  # Redwood City
            'http://www.openstreetmap.org/node/150981209',  # Menlo Park
        ], clip=self.tile_bbox(11, 328, 793))
        self.assert_has_feature(
            11, 328, 793, 'places',
            {'kind': 'locality',
             'kind_detail': {'city', 'town'},
             'population': int})

    def test_sacramento(self):
        # Sacramento, CA
        self.load_fixtures([
            'http://www.openstreetmap.org/node/150959789',
        ])
        self.assert_has_feature(
            8, 41, 98, 'places',
            {'kind': 'locality', 'kind_detail': 'city',
             'region_capital': True, 'population': int})
