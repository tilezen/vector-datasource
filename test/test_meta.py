# -*- coding: utf-8 -*-

import unittest


def memoize(f):
    result = {}

    def wrapped(*args, **kwargs):
        cache_key = tuple(args)
        if not result:
            result[cache_key] = f(*args, **kwargs)
        return result[cache_key]

    return wrapped


@memoize
def parse_layers_props(yaml_path):
    from vectordatasource.meta.python import parse_layers, output_kind, \
        make_function_name_props
    return parse_layers(yaml_path, output_kind, make_function_name_props)


@memoize
def parse_layers_min_zoom(yaml_path):
    from vectordatasource.meta.python import parse_layers, output_min_zoom, \
        make_function_name_min_zoom
    return parse_layers(
        yaml_path, output_min_zoom, make_function_name_min_zoom)


@memoize
def find_yaml_path():
    from vectordatasource.meta import find_yaml_path
    return find_yaml_path()


@memoize
def make_layer_data_props():
    yaml_path = find_yaml_path()
    layer_data = parse_layers_props(yaml_path)
    by_name = {}
    for layer_datum in layer_data:
        by_name[layer_datum.layer] = layer_datum
    return layer_data, by_name


@memoize
def make_layer_data_min_zoom():
    yaml_path = find_yaml_path()
    layer_data = parse_layers_min_zoom(yaml_path)
    by_name = {}
    for layer_datum in layer_data:
        by_name[layer_datum.layer] = layer_datum
    return layer_data, by_name


class CallFuncTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()

    def test_layer_data_count(self):
        self.assertEquals(9, len(self.layer_data))

    def test_layer_names(self):
        exp_layers = set(('landuse', 'pois', 'transit', 'water', 'places',
                          'boundaries', 'buildings', 'roads', 'earth'))
        self.assertEquals(exp_layers, set(self.by_name.keys()))

    def test_layers_called_empty_feature(self):
        import shapely.geometry
        shape = shapely.geometry.Point((0, 0))
        props = {}
        fid = 42

        for layer_datum in self.layer_data:
            fn = layer_datum.fn
            result = fn(shape, props, fid)
            self.assertTrue(isinstance(result, (dict, None.__class__)))


class BuildingsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.buildings = cls.by_name['buildings']

    def test_building_basic(self):
        import shapely.geometry
        shape = shapely.geometry.Point((0, 0))
        props = dict(building='yes')
        fid = 42
        out_props = self.buildings.fn(shape, props, fid)
        self.assertEquals('building', out_props.get('kind'))
        self.assertIsNone(out_props.get('kind_detail'))

    def test_building_kind_detail(self):
        import shapely.geometry
        shape = shapely.geometry.Polygon([(0, 0), (1, 1), (1, 0)])
        props = {
            'building': 'beach_hut',
            'building:part': 'passageway',
        }
        fid = 42
        out_props = self.buildings.fn(shape, props, fid)
        self.assertEquals('building', out_props.get('kind'))
        self.assertEquals('beach_hut', out_props.get('kind_detail'))
        self.assertEquals('passageway', out_props.get('building_part'))


class BoundariesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.boundaries = cls.by_name['boundaries']

    def test_osm(self):
        props = {
            'boundary': 'administrative',
            'boundary:type': 'aboriginal_lands',
            'admin_level': '2',
        }
        out_props = self.boundaries.fn(None, props, None)
        self.assertEquals('aboriginal_lands', out_props.get('kind'))
        self.assertEquals('2', out_props.get('kind_detail'))

    def test_ne(self):
        props = {
            'featurecla': 'Admin-1 region boundary',
        }
        out_props = self.boundaries.fn(None, props, None)
        self.assertEquals('macroregion', out_props.get('kind'))
        self.assertEquals('3', out_props.get('kind_detail'))


class EarthTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.earth = cls.by_name['earth']

    def test_osm(self):
        props = {
            'natural': 'arete',
        }
        out_props = self.earth.fn(None, props, None)
        self.assertEquals('arete', out_props.get('kind'))

    def test_ne(self):
        props = {
            'gid': 42,
        }
        out_props = self.earth.fn(None, props, None)
        self.assertEquals('earth', out_props.get('kind'))


class LanduseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.landuse = cls.by_name['landuse']

    def test_osm(self):
        props = {
            'natural': 'scree',
        }
        out_props = self.landuse.fn(None, props, None)
        self.assertEquals('scree', out_props.get('kind'))


class PlacesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.places = cls.by_name['places']

    def test_osm(self):
        props = {
            'name': 'foo',
            'place': 'isolated_dwelling',
        }
        out_props = self.places.fn(None, props, None)
        self.assertEquals('locality', out_props.get('kind'))
        self.assertEquals('isolated_dwelling', out_props.get('kind_detail'))

    def test_ne(self):
        props = {
            'scalerank': 42,
            'featurecla': 'Scientific station',
        }
        out_props = self.places.fn(None, props, None)
        self.assertEquals('locality', out_props.get('kind'))
        self.assertEquals('scientific_station', out_props.get('kind_detail'))


class PoisTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.pois = cls.by_name['pois']

    def test_disused(self):
        props = dict(disused='yes')
        out_props = self.pois.fn(None, props, None)
        self.assertIsNone(out_props.get('kind'))

        props = dict(disused='no', name='foo', leisure='playground')
        out_props = self.pois.fn(None, props, None)
        self.assertEquals('playground', out_props.get('kind'))

    def test_no_name_ok(self):
        props = dict(historic='landmark')
        out_props = self.pois.fn(None, props, None)
        self.assertEquals('landmark', out_props.get('kind'))

    def test_no_name_none(self):
        props = dict(tourism='aquarium')
        out_props = self.pois.fn(None, props, None)
        self.assertIsNone(out_props.get('kind'))


class RoadsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.roads = cls.by_name['roads']

    def test_osm(self):
        props = {
            'name': 'foo',
            'highway': 'motorway',
        }
        out_props = self.roads.fn(None, props, None)
        self.assertEquals('highway', out_props.get('kind'))
        self.assertEquals('motorway', out_props.get('kind_detail'))

    def test_ne(self):
        props = {
            'featurecla': 'Road',
            'type': 'Road',
            'scalerank': 42,
        }
        out_props = self.roads.fn(None, props, None)
        self.assertEquals('major_road', out_props.get('kind'))
        self.assertEquals('secondary', out_props.get('kind_detail'))


class TransitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.transit = cls.by_name['transit']

    def test_osm(self):
        props = {
            'route': 'subway',
        }
        out_props = self.transit.fn(None, props, None)
        self.assertEquals('subway', out_props.get('kind'))


class WaterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_props()
        cls.water = cls.by_name['water']

    def test_osm(self):
        props = dict(waterway='riverbank')
        out_props = self.water.fn(None, props, None)
        self.assertEquals('riverbank', out_props.get('kind'))

        props = dict(waterway='riverbank', intermittent='yes')
        out_props = self.water.fn(None, props, None)
        self.assertEquals('riverbank', out_props.get('kind'))
        self.assertTrue(out_props.get('intermittent'))


    def test_ne(self):
        props = dict(featurecla='Lake')
        out_props = self.water.fn(None, props, None)
        self.assertEquals('lake', out_props.get('kind'))


class LanduseMinZoomTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data_min_zoom()
        cls.landuse = cls.by_name['landuse']

    def test_small_zoo(self):
        import shapely.geometry
        shape = shapely.geometry.Polygon([(0, 0), (1, 1), (1, 0)])
        props = {
            'zoo': 'enclosure',
        }
        out_min_zoom = self.landuse.fn(shape, props, None)
        self.assertEquals(16, out_min_zoom)

    def test_large_zoo(self):
        import shapely.geometry
        s = 100000
        shape = shapely.geometry.Polygon([(0, 0), (s, s), (s, 0)])
        props = {
            'zoo': 'enclosure',
        }
        out_min_zoom = self.landuse.fn(shape, props, None)
        self.assertEquals(9, out_min_zoom)

    def test_medium_zoo(self):
        import shapely.geometry
        from vectordatasource.util import calculate_way_area, \
            calculate_1px_zoom
        import math

        target_zoom = 11.0
        # want a zoom 11 feature, so make one with a triangle.
        target_area = math.exp((17.256 - target_zoom) * math.log(4))
        # make area with a half-square triangle.
        s = math.sqrt(target_area * 2.0)
        shape = shapely.geometry.Polygon([(0, 0), (s, s), (s, 0)])
        props = {
            'zoo': 'enclosure',
        }

        # test the utility functions we're relying on
        util_way_area = calculate_way_area(shape)
        self.assertAlmostEqual(target_area, util_way_area)
        util_min_zoom = calculate_1px_zoom(shape.area)
        self.assertAlmostEqual(target_zoom, util_min_zoom)

        out_min_zoom = self.landuse.fn(shape, props, None)
        self.assertAlmostEqual(target_zoom, out_min_zoom)


if __name__ == '__main__':
    unittest.main()
