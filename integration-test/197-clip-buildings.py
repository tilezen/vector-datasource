from . import FixtureTest


class ClipBuildings(FixtureTest):

    def test_high_line(self):
        from shapely.geometry import shape

        # this is mid way along the High Line in NYC, which is a huge long
        # "building". we should be clipping it to the bounds of the tile.
        #
        # NOTE: we _don't_ clip the fixture, that has to happen in the
        # query.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/7141751',
        ])
        with self.features_in_tile_layer(16, 19295, 24631, 'buildings') \
                as buildings:
            # max width and height in mercator meters as the size of the
            # above tile
            max_w = 611.5
            max_h = 611.5

            # need to check that we at least saw the high line
            saw_the_high_line = False

            for building in buildings:
                bounds = shape(building['geometry']).bounds
                w = bounds[2] - bounds[0]
                h = bounds[3] - bounds[1]

                if building['properties']['id'] == -7141751:
                    saw_the_high_line = True

                self.assertFalse(
                    w > max_w or h > max_h,
                    'feature %r is %rx%r, larger than the allowed '
                    '%rx%r.' % (building['properties']['id'], w, h,
                                max_w, max_h))

        self.assertTrue(
            saw_the_high_line,
            "Expected to see the High Line in this tile, but didn't.")
