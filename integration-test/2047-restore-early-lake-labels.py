# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class BoundsTest(FixtureTest):
    def generate_fixtures(self, *objs):
        from dsl import Feature

        boundaries = []
        for feature in objs:
            if feature.shape.geom_type in ('Polygon', 'MultiPolygon'):
                props = feature.properties.copy()
                props['boundary'] = True
                boundary = Feature(
                    feature.fid,
                    feature.shape.boundary,
                    props)
                boundaries.append(boundary)

        new_objs = list(objs)
        new_objs.extend(boundaries)
        FixtureTest.generate_fixtures(self, *new_objs)


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

    def test_name_not_drop(self):
        import dsl

        for z in range(6, 13):
            x, y = (3, 4)
            area = 265548000

            self.generate_fixtures(
                dsl.way(1, dsl.box_area(z, x, y, area, include_boundary=True), {
                    'name': u'Clear Lake',
                    'natural': u'water',
                    'type': u'multipolygon',
                    'water': u'lake',
                    'wikidata': u'Q1099503',
                    'source': u'openstreetmap.org',
                }),
            )

            self.assert_has_feature(
                z, x, y, 'water', {
                    'kind': 'water',
                    'kind_detail': 'lake',
                    'name': 'Clear Lake',
                    'min_zoom': 6.0,
                })
