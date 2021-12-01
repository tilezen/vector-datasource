from . import FixtureTest


class ZoosAndOtherAttractionsAttraction(FixtureTest):
    def test_attractions(self):
        # Sable Island Horse
        self._run_test(16, 21228, 23551, 342984911, 'animal')
        # Fun Mountain Water Park
        self._run_test(16, 15113, 22273, 243814268, 'water_slide')
        # Woodstock Express
        self._run_test(16, 18670, 25315, 235396958, 'roller_coaster')
        # Carousel
        self._run_test(16, 10555, 25516, 34300914, 'carousel')
        # White Water Canyon
        self._run_test(16, 18668, 25316, 235398104, 'amusement_ride')
        # Lawyers Farm Corn Maze
        self._run_test(16, 18681, 24907, 374883740, 'maze')

    def test_carousel_also_building(self):
        # This is a carousel, but also a building, which keeps it out of the
        # landuse layer. See
        # https://github.com/mapzen/vector-datasource/issues/201
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/325824281'])

        self.assert_has_feature(
            16, 17383, 25023, 'pois',
            {'id': 325824281,
             'kind': 'carousel'})

    def _run_test(self, z, x, y, osm_id, attraction):
        # expect these features in _both_ the landuse and POIs layers.
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/%d' % osm_id])

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {'id': osm_id, 'kind': attraction})
