# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads
from tilequeue.tile import deg2num

from . import FixtureTest


class WaterKinds(FixtureTest):
    def test_water_reservoir(self):
        self.generate_fixtures(dsl.way(1, wkt_loads(
            'POLYGON ((-122.421611012467 37.80395991667648, '
            '-122.420227786592 37.80413210674329, -122.420159873957 '
            '37.80408277780808, -122.420117832801 37.80383748120349, '
            '-122.42154480663 37.80365748294528, -122.421611012467 '
            '37.80395991667648))'),
            {
            u'way_area': u'6936.45',
            u'natural': u'water',
            u'source': u'openstreetmap.org',
            u'water': u'reservoir',
            u'name': u'Francisco Reservoir',
            u'covered': u'no'}))

        self.assert_has_feature(
            16, 10481, 25324, 'water',
            {
                'kind': 'water',
                'reservoir': True,
                'kind_detail': 'lake'
            })

    def test_water_lagoon(self):
        self.generate_fixtures(dsl.way(1, wkt_loads(
            'POLYGON ((-122.421611012467 37.80395991667648, '
            '-122.420227786592 37.80413210674329, -122.420159873957 '
            '37.80408277780808, -122.420117832801 37.80383748120349, '
            '-122.42154480663 37.80365748294528, -122.421611012467 '
            '37.80395991667648))'),
            {
            u'natural': u'water',
            u'way_area': u'6936.45',
            u'source': u'openstreetmap.org',
            u'water': u'lagoon',
            u'name': u'Francisco Reservoir',
            u'covered': u'no'}))

        self.assert_has_feature(
            16, 10481, 25324, 'water',
            {
                'kind': 'water',
                'alkaline': True,
                'kind_detail': 'lake'
            })

    def test_water_ditch(self):
        self.generate_fixtures(dsl.way(1, wkt_loads(
            'POLYGON ((-122.421611012467 37.80395991667648, -122.420227786592 37.80413210674329, -122.420159873957 37.80408277780808, -122.420117832801 37.80383748120349, -122.42154480663 37.80365748294528, -122.421611012467 37.80395991667648))'),
            {
            u'natural': u'water',
            u'way_area': u'6936.45',
            u'source': u'openstreetmap.org',
            u'water': u'ditch',
            u'name': u'Francisco Reservoir',
            u'covered': u'no'}))

        self.assert_has_feature(
            16, 10481, 25324, 'water',
            {
                'kind': 'water',
                'kind_detail': 'ditch'
            })

    def test_prop_drop(self):
        import dsl

        lon, lat = (-122.417169, 37.769196)

        for z in range(0, 16):
            x, y = deg2num(lat, lon, z)
            # without remapping min_zoom this area would result in min_zoom of 6,
            # but after remapping it'd be 9
            area = 265548000
            self.generate_fixtures(
                dsl.way(1, dsl.box_area(z, x, y, area), {
                    'name': u'Clear Lake',
                    'natural': u'water',
                    'water': u'lake',
                    'wikidata': u'Q1099503',
                    'source': u'openstreetmap.org',
                }),
            )

            if z < 6:
                self.assert_no_matching_feature(z, x, y, 'water',
                                                {
                                                    'kind': 'water',
                                                })
            if 6 <= z <= 14:
                with self.features_in_tile_layer(z, x, y, 'water') as features:
                    for f in features:
                        if f['geometry']['type'] == 'Polygon':
                            assert f['id'] is None
                            assert f['properties']['min_zoom'] == 6
                            assert 'name' not in f['properties']
                            assert 'old_name' not in f['properties']
            if z == 15:
                with self.features_in_tile_layer(z, x, y, 'water') as features:
                    for f in features:
                        if f['geometry']['type'] == 'Polygon':
                            assert f['id'] is None
                            assert f['properties']['name'] == 'Clear Lake'
                            assert f['properties']['kind'] == 'water'
                            assert f['properties']['kind_detail'] == 'lake'

            if z < 9:
                self.assert_no_matching_feature(z, x, y, 'water',
                                                {
                                                    'kind': 'water',
                                                    'label_placement': True,
                                                })

            if z >= 9:
                self.assert_has_feature(z, x, y, 'water', {
                    'kind': 'water',
                    'name': 'Clear Lake',
                    'kind_detail': 'lake',
                    'label_placement': True,
                    'min_zoom': 9.0,
                })
