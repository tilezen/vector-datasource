import unittest

from . import BROKEN
from . import FixtureTest


class ZoosAndOtherAttractionsTourism(FixtureTest):
    @unittest.skip(BROKEN)
    def test_tourism(self):
        # Sinclair Oil Apatosaurus, Windsor
        self._run_test(16, 17645, 24251, 786994983, 'artwork')
        # Walt Disney World Resort
        self._run_test(13, 2240, 3421, -1228099, 'theme_park')
        # Busch Gardens Williamsburg
        self._run_test(13, 2351, 3181, 362327591, 'theme_park')
        # Disneyland Resort
        self._run_test(14, 2825, 6555, -4795362, 'resort')
        # Aquarium of the Pacific
        self._run_test(14, 2812, 6557, 200068201, 'aquarium')

    def test_hut_also_building(self):
        # these are POIs, but also a buildings, so they won't show up in the
        # landuse layer.
        # Wendy Thompson Hut, BC
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/220084069'])

        self.assert_has_feature(
            15, 5236, 11051, 'pois',
            {'id': 220084069, 'kind': 'wilderness_hut'})

    def test_winery_building(self):
        # these are POIs, but also a buildings, so they won't show up in the
        # landuse layer.
        # Scharffenberger Winery
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/242899474'])

        self.assert_has_feature(
            16, 10296, 25030, 'pois',
            {'id': 242899474, 'kind': 'winery'})

    def test_trail_riding_station(self):
        # this is a POI, but also a point, so as it has no area, it won't
        # show up in the landuse layer.
        self.load_fixtures(
            ['http://www.openstreetmap.org/node/3095286850'])

        self.assert_has_feature(
            16, 34893, 21123, 'pois',
            {'id': 3095286850, 'kind': 'trail_riding_station'})

    def _run_test(self, z, x, y, osm_id, attraction):
        # expect these features in _both_ the landuse and POIs layers.
        typ = 'way' if osm_id >= 0 else 'relation'
        self.load_fixtures(
            ['https://www.openstreetmap.org/%s/%d' % (typ, abs(osm_id))])

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {'id': osm_id, 'kind': attraction})
