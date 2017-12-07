from . import FixtureTest


class RoadShieldCleanup(FixtureTest):
    def _check_network_relation(
            self, way_id, rel_id, tile, expected_shield_text):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/%d' % (way_id,),
            'https://www.openstreetmap.org/relation/%d' % (rel_id,),
        ], clip=self.tile_bbox(*tile))

        z, x, y = tile
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': way_id, 'shield_text': expected_shield_text})

    def test_A151(self):
        self._check_network_relation(
            way_id=208288552, rel_id=1159812, tile=(16, 32949, 22362),
            expected_shield_text='A151')

    def test_E402(self):
        self._check_network_relation(
            way_id=121496753, rel_id=88503, tile=(16, 32975, 22371),
            expected_shield_text='E402')

    def test_A52(self):
        self._check_network_relation(
            way_id=358261897, rel_id=5715176, tile=(16, 32416, 21339),
            expected_shield_text='A52')

    def test_M1(self):
        self._check_network_relation(
            way_id=3109799, rel_id=2332838, tile=(16, 32531, 21377),
            expected_shield_text='M1')
