from . import FixtureTest


class ClipBuildings(FixtureTest):

    def test_high_line(self):
        from ModestMaps.Core import Coordinate
        from shapely.geometry import box
        from shapely.geometry import shape
        from tilequeue.tile import coord_to_mercator_bounds

        # this is mid way along the High Line in NYC, which is a huge long
        # "building". we should be clipping it to the bounds of the tile.
        #
        # NOTE: we _don't_ clip the fixture, that has to happen in the
        # query.
        #
        # NOTE: https://github.com/tilezen/vector-datasource/issues/1142
        # we want to clip all buildings to the bounding box of the tile, so
        # that there are no overlaps.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/7141751',
        ])
        coord = Coordinate(zoom=16, column=19295, row=24631)
        with self.features_in_tile_layer(
                coord.zoom, coord.column, coord.row, 'buildings') as buildings:
            # tile bounds as a box
            tile_bounds = coord_to_mercator_bounds(coord)
            bbox = box(*tile_bounds)

            # need to check that we at least saw the high line
            saw_the_high_line = False

            for building in buildings:
                building_bounds = shape(building['geometry']).bounds
                building_box = box(*building_bounds)

                if building['properties']['id'] == -7141751:
                    saw_the_high_line = True

                self.assertTrue(
                    building_box.within(bbox),
                    'feature %r extends outside of the bounds of the '
                    'tile (%r not within %r).' %
                    (building['properties']['id'], building_bounds,
                     tile_bounds))

        self.assertTrue(
            saw_the_high_line,
            "Expected to see the High Line in this tile, but didn't.")
