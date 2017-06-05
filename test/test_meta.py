# -*- coding: utf-8 -*-

import unittest


class CallFuncTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from vectordatasource.meta.python import parse_layers
        from vectordatasource.meta import find_yaml_path
        yaml_path = find_yaml_path()
        cls.layer_data = layer_data = parse_layers(yaml_path)
        cls.by_name = {}
        for layer_datum in layer_data:
            cls.by_name[layer_datum.layer] = layer_datum

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

    def test_building_basic(self):
        import shapely.geometry
        buildings_layer_data = self.by_name['buildings']
        shape = shapely.geometry.Point((0, 0))
        props = dict(
            building='yes',
        )
        fid = 42
        new_props = buildings_layer_data.fn(shape, props, fid)
        self.assertEquals('building', new_props.get('kind'))
        self.assertIsNone(new_props.get('kind_detail'))
