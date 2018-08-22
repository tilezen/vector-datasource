from . import FixtureTest


class ReturnOfTheZombieBuildings(FixtureTest):

    def _load_query(self, z, x, y, tag):
        from ModestMaps.Core import Coordinate
        from tilequeue.tile import coord_to_bounds

        coord = Coordinate(zoom=z, column=x, row=y)
        bounds = coord_to_bounds(coord)

        # have to reorder the bounds from conventional order to the unusual
        # scheme that overpass expects (south,west,north,east).
        bbox = "%f,%f,%f,%f" % (bounds[1], bounds[0], bounds[3], bounds[2])
        overpass = "http://overpass-api.de/api/interpreter?data="
        query = "way(" + bbox + ")[" + tag + "]%3B>%3B"

        self.load_fixtures([overpass + query])

    def test_building(self):
        # mz_is_building is an internal tag and shouldn't be present on any
        # output feature.
        self._load_query(12, 653, 1582, 'building')

        self.assert_no_matching_feature(
            12, 653, 1582, 'buildings',
            {'mz_is_building': None})

    def test_landuse(self):
        self._load_query(12, 653, 1582, 'landuse')

        self.assert_no_matching_feature(
            12, 653, 1582, 'landuse',
            {'mz_is_building': None})
