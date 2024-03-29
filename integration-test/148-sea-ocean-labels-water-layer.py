# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads
from tilequeue.tile import deg2num

from . import FixtureTest


# ocean and sea labels should be in the water layer rather than the places
# layer.
class SeaOceanLabelsWaterLayer(FixtureTest):

    # NOTE: No ocean points in the North America extract :-(
    def test_ocean_point(self):
        z = 16     # visible starting at zoom 9 because of NE - OSM transition, but with different min_zoom
        x, y = deg2num(1.0, 1.0, z)

        # Fake Ocean
        self.generate_fixtures(dsl.way(1, wkt_loads('POINT (1.0 1.0)'), {
                               u'name': u'Atlantic Ocean', u'source': u'openstreetmap.org', u'natural': u'sea', u'place': u'ocean'}))
        # Oceans are not graded by area, they are constant zoom
        self.assert_has_feature(
            z, x, y, 'water',
            {'kind': 'ocean', 'name': 'Atlantic Ocean', 'min_zoom': 1.0,
             'label_placement': True})

        # even though OSM tags as place, Tilezen recasts to water layer
        self.assert_no_matching_feature(
            z, x, y, 'places',
            {'kind': 'ocean', 'name': 'Atlantic Ocean'})

        # ensure the zoom range is correct vis-a-vis the size
        self.assert_no_matching_feature(
            0, x, y, 'water',
            {'kind': 'ocean', 'name': 'Atlantic Ocean'})
        x, y = deg2num(1.0, 1.0, 1)
        self.assert_has_feature(
            1, x, y, 'water',
            {'kind': 'ocean', 'name': 'Atlantic Ocean', 'min_zoom': 1.0,
             'label_placement': True})

    def test_gulf_of_california_point(self):
        z = 16     # visible starting at zoom 9 because of NE - OSM transition, but with different min_zoom
        x, y = deg2num(1, 1, z)

        # Gulf of California: http://www.openstreetmap.org/node/305639734
        self.generate_fixtures(dsl.way(305639734, wkt_loads('POINT (1 1)'), {u'name:ia': u'Golfo de California', u'alt_name:eo': u'Maro de Korteso', u'name:ms': u'Teluk California', u'name:ko': u'\uce7c\ub9ac\ud3ec\ub974\ub2c8\uc544 \ub9cc', u'gns:dsg': u'GULF', u'name:cs': u'Kalifornsk\xfd z\xe1liv', u'alt_name:pl': u'Morze Cort\xe9za', u'wikidata': u'Q132811', u'name:it': u'Golfo di California', u'name:vi': u'V\u1ecbnh Ca Li', u'name:ru': u'\u041a\u0430\u043b\u0438\u0444\u043e\u0440\u043d\u0438\u0439\u0441\u043a\u0438\u0439 \u0437\u0430\u043b\u0438\u0432', u'name:pl': u'Zatoka Kalifornijska', u'name:ta': u'\u0b95\u0bb2\u0bbf\u0baa\u0bcb\u0bb0\u0bcd\u0ba9\u0bbf\u0baf\u0bbe \u0bb5\u0bb3\u0bc8\u0b95\u0bc1\u0b9f\u0bbe', u'wikipedia': u'en:Gulf of California', u'name:de': u'Golf von Kalifornien', u'source': u'openstreetmap.org',
                               u'name:fr': u'Golfe de Californie', u'name:zh': u'\u52a0\u5229\u798f\u5c3c\u4e9a\u6e7e', u'name:sl': u'Kalifornijski zaliv', u'name:lt': u'Kalifornijos \u012flanka', u'gns:uni': u'-2327700', u'name:he': u'\u05de\u05e4\u05e8\u05e5 \u05e7\u05dc\u05d9\u05e4\u05d5\u05e8\u05e0\u05d9\u05d4', u'sqkm': u'160000', u'name:uk': u'\u041a\u0430\u043b\u0456\u0444\u043e\u0440\u043d\u0456\u0439\u0441\u044c\u043a\u0430 \u0437\u0430\u0442\u043e\u043a\u0430', u'name:hu': u'Kaliforniai-\xf6b\xf6l', u'name:el': u'\u039a\u03cc\u03bb\u03c0\u03bf\u03c2 \u03c4\u03b7\u03c2 \u039a\u03b1\u03bb\u03b9\u03c6\u03cc\u03c1\u03bd\u03b9\u03b1\u03c2', u'name:eo': u'Kalifornia Golfo', u'name:en': u'Gulf of California', u'natural': u'sea', u'name': u'Gulf of California', u'place': u'sea', u'alt_name:cs': u'Cort\xe9zovo mo\u0159e', u'name:es': u'Golfo de California'}))

        # Seas are not graded by area, they are constant zoom (that should probably change)
        self.assert_has_feature(
            z, x, y, 'water',
            {'kind': 'sea', 'name': 'Gulf of California', 'min_zoom': 5.0,
             'label_placement': True})

        # even though OSM tags as place, Tilezen recasts to water layer
        self.assert_no_matching_feature(
            z, x, y, 'places',
            {'kind': 'sea', 'name': 'Gulf of California'})

        # ensure the zoom range is correct vis-a-vis the size
        x, y = deg2num(1.0, 1.0, 4)
        self.assert_no_matching_feature(
            4, x, y, 'water',
            {'kind': 'sea', 'name': 'Gulf of California'})
        x, y = deg2num(1.0, 1.0, 5)
        self.assert_has_feature(
            5, x, y, 'water',
            {'kind': 'sea', 'name': 'Gulf of California', 'min_zoom': 5.0,
             'label_placement': True})

    def test_greenland_sea_point(self):
        z = 16     # visible starting at zoom 9 because of NE - OSM transition, but with different min_zoom
        x, y = deg2num(1, 1, z)
        # Greenland Sea: http://www.openstreetmap.org/node/305639396
        self.generate_fixtures(dsl.way(305639396, wkt_loads('POINT (1 1)'), {u'name:pt': u'Mar da Gronel\xe2ndia', u'name:ms': u'Laut Greenland', u'name:ko': u'\uadf8\ub9b0\ub780\ub4dc \ud574', u'gns:dsg': u'SEA', u'name:ar': u'\u0628\u062d\u0631 \u063a\u0631\u064a\u0646\u0644\u0627\u0646\u062f', u'name:cs': u'Gr\xf3nsk\xe9 mo\u0159e', u'wikidata': u'Q132868', u'name:it': u'Mare di Groenlandia', u'name:vi': u'Bi\u1ec3n Greenland', u'name:pl': u'Morze Grenlandzkie', u'name:fi': u'Gr\xf6nlanninmeri', u'name:da': u'Gr\xf8nlandshavet', u'wikipedia': u'en:Greenland Sea',
                               u'name:de': u'Gr\xf6nlandsee', u'source': u'openstreetmap.org', u'name:fr': u'Mer du Groenland', u'name:zh': u'\u683c\u9675\u5170\u6d77', u'name:sk': u'Gr\xf3nske more', u'name:lt': u'Grenlandijos j\u016bra', u'gns:uni': u'-2149780', u'name:uk': u'\u0413\u0440\u0435\u043d\u043b\u0430\u043d\u0434\u0441\u044c\u043a\u0435 \u043c\u043e\u0440\u0435', u'name:sv': u'Gr\xf6nlandshavet', u'name:hu': u'Gr\xf6nlandi-tenger', u'name:hr': u'Grenlandsko more', u'name:eo': u'Gronlanda Maro', u'name:en': u'Greenland Sea', u'name': u'Greenland Sea', u'place': u'sea'}))

        # Seas are not graded by area, they are constant zoom (that should probably change)
        self.assert_has_feature(
            z, x, y, 'water',
            {'kind': 'sea', 'name': 'Greenland Sea', 'min_zoom': 5.0,
             'label_placement': True})

        # even though OSM tags as place, Tilezen recasts to water layer
        self.assert_no_matching_feature(
            z, x, y, 'places',
            {'kind': 'sea', 'name': 'Greenland Sea'})

        # ensure the zoom range is correct vis-a-vis the size
        x, y = deg2num(1.0, 1.0, 4)
        self.assert_no_matching_feature(
            4, x, y, 'water',
            {'kind': 'sea', 'name': 'Greenland Sea'})
        x, y = deg2num(1.0, 1.0, 5)
        self.assert_has_feature(
            5, x, y, 'water',
            {'kind': 'sea', 'name': 'Greenland Sea', 'min_zoom': 5.0,
             'label_placement': True})

    def test_hudson_bay_large_polygon(self):
        z = 16
        lon, lat = (1, 1)

        x, y = deg2num(lat, lon, z)
        # without remapping min_zoom this area would result in min_zoom of 6,
        # but after remapping it'd be 2
        area = 80000000001

        self.generate_fixtures(
            dsl.way(9441240, dsl.box_area(z, x, y, area), {
                'name': u'Hudson Bay',
                'place': u'sea',
                'wikidata': u'Q3040',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water',
            {'kind': 'sea', 'name': 'Hudson Bay', 'min_zoom': 2.0,
             'label_placement': True})

        # ensure the zoom range is correct vis-a-vis the size
        x, y = deg2num(1.0, 1.0, 1)
        self.assert_no_matching_feature(
            1, x, y, 'water',
            {'kind': 'sea', 'name': 'Hudson Bay',
             'label_placement': True})
        # Even though the feature has min_zoom 2, it isn't exported in a tile
        # until zoom 4 because of the queries.yaml water layers start zoom config
        # which is at 4 now so we don't get too much landuse at early zooms
        x, y = deg2num(1.0, 1.0, 4)
        self.assert_has_feature(
            4, x, y, 'water',
            {'kind': 'sea', 'name': 'Hudson Bay', 'min_zoom': 2.0,
             'label_placement': True})

    def test_james_bay_medium_polygon(self):
        z = 16
        lon, lat = (1, 1)

        x, y = deg2num(lat, lon, z)
        # without remapping min_zoom this area would result in min_zoom of 6,
        # but after remapping it'd be 5
        area = 500000001
        self.generate_fixtures(
            dsl.way(13360255, dsl.box_area(z, x, y, area), {
                'name': u'James Bay',
                'place': u'sea',
                'wikidata': u'Q223810',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water',
            {'kind': 'sea', 'name': 'James Bay', 'min_zoom': 5.0,
             'label_placement': True})

        # ensure the zoom range is correct vis-a-vis the size
        x, y = deg2num(1.0, 1.0, 4)
        self.assert_no_matching_feature(
            4, x, y, 'water',
            {'kind': 'sea', 'name': 'James Bay',
             'label_placement': True})

        x, y = deg2num(1.0, 1.0, 5)
        self.assert_has_feature(
            5, x, y, 'water',
            {'kind': 'sea', 'name': 'James Bay', 'min_zoom': 5.0,
             'label_placement': True})
