from . import FixtureTest


class NoNaturalPois(FixtureTest):

    def test_unnamed_natural_wood_hyde_park_london(self):
        # example from ticket: an unnamed natural=wood in Hyde Park, London
        # since this is unnamed, it might already get dropped as a POI, and
        # won't have a landuse label, so this checks for the polygon.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/1756198',
        ])

        self.assert_has_feature(
            16, 32737, 21792, 'landuse',
            {'id': -1756198, 'kind': 'natural_wood'})

        self.assert_no_matching_feature(
            16, 32737, 21792, 'pois',
            {'id': -1756198, 'kind': 'natural_wood'})

    def test_named_area_mt_cydonia_ponds(self):
        # named area, should get a label placement. note that we currently
        # only add landuse label placements at zoom 15+.
        # Mt. Cydonia Ponds Natural Area
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/6366946',
        ])

        self.assert_has_feature(
            15, 9327, 12418, 'landuse',
            {'id': -6366946, 'kind': 'natural_wood',
             'label_placement': True})

        self.assert_no_matching_feature(
            15, 9327, 12418, 'pois',
            {'id': -6366946, 'kind': 'natural_wood'})
