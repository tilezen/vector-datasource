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
def parse_layers(yaml_path):
    from vectordatasource.meta.python import parse_layers
    return parse_layers(yaml_path)


@memoize
def find_yaml_path():
    from vectordatasource.meta import find_yaml_path
    return find_yaml_path()


@memoize
def make_layer_data():
    yaml_path = find_yaml_path()
    layer_data = parse_layers(yaml_path)
    by_name = {}
    for layer_datum in layer_data:
        by_name[layer_datum.layer] = layer_datum
    return layer_data, by_name


class CallFuncTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.layer_data, cls.by_name = make_layer_data()

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
        cls.layer_data, cls.by_name = make_layer_data()
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
        cls.layer_data, cls.by_name = make_layer_data()
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
        cls.layer_data, cls.by_name = make_layer_data()
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
        cls.layer_data, cls.by_name = make_layer_data()
        cls.landuse = cls.by_name['landuse']

    def test_osm(self):
        props = {
            'natural': 'scree',
        }
        out_props = self.landuse.fn(None, props, None)
        self.assertEquals('scree', out_props.get('kind'))


if __name__ == '__main__':
    unittest.main()
