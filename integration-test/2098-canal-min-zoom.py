import dsl

from . import FixtureTest


class TestCanalMinZoom(FixtureTest):
    def test_canal(self):
    z, x, y = (16, 10483, 25332)
    self.generate_fixtures(
        dsl.way(76287073, dsl.tile_box(z, x, y), {
            'name': 'Ridenbaugh High Line Canal',
            'boat': 'no',
            'waterway': 'canal',
            'source': 'openstreetmap.org'
        })
    )

    self.assert_has_feature(
        z, x, y, 'water',
        {'id': 76287073,
         'name': 'Ridenbaugh High Line Canal'
         'kind_detail': 'canal',
         'min_zoom': '11',
         'source': 'openstreetmap.org'})

    def test_boat_canal(self):
    z, x, y = (16, 10483, 25332)
    self.generate_fixtures(
        dsl.way(85123623, dsl.tile_box(z, x, y), {
            'name': 'Canal de Bourgogne',
            'name:ja': 'ブルゴーニュ運河',
            'access': 'boat',
            'boat': 'yes',
            'fishing': 'yes',
            'waterway': 'canal',
            'source': 'openstreetmap.org'
        })
    )

    self.assert_has_feature(
        z, x, y, 'water',
        {'id': 85123623,
         'name': 'Canal de Bourgogne',
         'name:ja': 'ブルゴーニュ運河',
         'kind': 'canal',
         'boat': 'yes'
         'min_zoom': '9',
         'source': 'openstreetmap.org'})
