from . import FixtureTest


class ZoosAndOtherAttractionsZoo(FixtureTest):
    def test_zoos(self):
        # Bear Enclosure (presumably + woods=yes?)
        self._run_test(16, 11458, 21855, 316623706, 'enclosure')
        # Oaklawn Farm Zoo
        self._run_test(16, 20963, 23573, 343269426, 'petting_zoo')
        # Budgie Buddies
        self._run_test(16, 10463, 22969, 370123970, 'aviary')
        # Shubenacadie Provincial Wildlife Park
        self._run_test(16, 21228, 23551, 84422829, 'wildlife_park')

    def test_aviary_also_building(self):
        # this is a building, so won't show up in landuse. still should be a
        # POI.
        # Wings of Asia
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/103256220'])

        self.assert_has_feature(
            16, 18131, 27942, 'pois',
            {'id': 103256220,
             'kind': 'aviary'})

    def _run_test(self, z, x, y, osm_id, attraction):
        # expect these features in _both_ the landuse and POIs layers.
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/%d' % osm_id])

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {'id': osm_id, 'kind': attraction})
