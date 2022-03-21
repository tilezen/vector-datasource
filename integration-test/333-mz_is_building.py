from . import FixtureTest


class MzIsBuilding(FixtureTest):

    def test_buildings_around_san_francisco_state_university(self):
        # Buildings around San Francisco State University
        #
        # beware: overpass wants (south,west,north,east) coords for bbox,
        # in defiance of x, y coordinate ordering.
        #
        bbox = '37.72049,-122.48589,37.72918,-122.47472'
        overpass = 'http://overpass-api.de/api/interpreter?data='
        self.load_fixtures([
            overpass + 'way(' + bbox + ')[building]%3B>%3B',
            overpass + 'relation(' + bbox + ')[building]%3B>%3B',
        ], clip=self.tile_bbox(16, 10470, 25342))

        self.assert_no_matching_feature(
            16, 10470, 25342, 'landuse',
            {'mz_is_building': None})
