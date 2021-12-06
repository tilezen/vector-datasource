from . import FixtureTest


class DuplicatePoints(FixtureTest):

    def _assert_no_repeated_points(self, coords):
        last_coord = coords[0]
        for i in range(1, len(coords)):
            coord = coords[i]
            self.assertFalse(
                coord == last_coord,
                'Coordinate %r (at %d) == %r (at %d), but coordinates should '
                'not be repeated.' % (coord, i, last_coord, i - 1))

    def test_road_no_repeated_points(self):
        from ModestMaps.Core import Coordinate
        from tilequeue.tile import coord_to_bounds

        z, x, y = 16, 17885, 27755
        coord = Coordinate(zoom=z, column=x, row=y)
        bounds = coord_to_bounds(coord)

        # have to reorder the bounds from conventional order to the unusual
        # scheme that overpass expects (south,west,north,east).
        bbox = '%f,%f,%f,%f' % (bounds[1], bounds[0], bounds[3], bounds[2])
        overpass = 'http://overpass-api.de/api/interpreter?data='
        query = 'way(' + bbox + ')[highway]%3B>%3B'

        self.load_fixtures([overpass + query])

        num_tested = 0
        with self.features_in_tile_layer(z, x, y, 'roads') as features:
            for feature in features:
                gtype = feature['geometry']['type']

                if gtype == 'LineString':
                    self._assert_no_repeated_points(
                        feature['geometry']['coordinates'])
                    num_tested += 1

                elif gtype == 'MultiLineString':
                    for linestring in feature['geometry']['coordinates']:
                        self._assert_no_repeated_points(linestring)
                    num_tested += 1

        self.assertTrue(num_tested != 0,
                        'Expected at least one testable feature.')
