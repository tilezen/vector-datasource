# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class CampGroundsZoom(FixtureTest):
    def test_large(self):
        # update landuse to include campground features and fix label zoom
        # large campground in landuse zoom 16
        self.generate_fixtures(dsl.way(237314510, wkt_loads('POLYGON ((-121.782736997744 36.2494015554296, -121.78273268583 36.2500247223074, -121.781764840943 36.24992779200338, -121.780515194552 36.24980260829389, -121.779159996114 36.2492724588565, -121.778565221564 36.24881315731069, -121.77808830598 36.2481851993462, -121.777545004896 36.24808297820778, -121.777387979385 36.24670040787668, -121.774731930584 36.24606258003467, -121.773446082086 36.24603338356518, -121.772757972579 36.24589710908079, -121.771997369028 36.24587276656409, -121.771906818847 36.2447091709354, -121.772510486718 36.24280069459819, -121.773772080703 36.24091166140629, -121.775933157782 36.2409846935689, -121.778106362117 36.24265470604907, -121.779349899965 36.24555138667509, -121.779567112601 36.24627948845148, -121.781411623374 36.24846527443778, -121.782736997744 36.2494015554296))'), {u'source': u'openstreetmap.org', u'way_area': u'634751', u'tourism': u'camp_site', u'name': u'Pfeiffer Big Sur'}))  # noqa

        self.assert_has_feature(
            16, 10599, 25679, 'landuse',
            {'kind': 'camp_site', 'sort_rank': 106})

        self.assert_has_feature(
            16, 10599, 25679, 'pois',
            {'kind': 'camp_site'})

        # large campground in landuse zoom 13
        self.assert_has_feature(
            13, 1324, 3209, 'landuse',
            {'kind': 'camp_site', 'sort_rank': 106})

        # large campground in point zoom 13
        self.assert_has_feature(
            13, 1324, 3209, 'pois',
            {'kind': 'camp_site'})

    def test_small(self):
        # small campground in landuse zoom 16
        self.generate_fixtures(dsl.way(417405356, wkt_loads('POLYGON ((-122.476928279516 37.7965135543643, -122.476625187939 37.7970964741721, -122.476314101356 37.79714729842829, -122.4760216099 37.79714211662731, -122.475865572535 37.7971003072876, -122.475608744195 37.79708710433336, -122.475371139802 37.7970130683686, -122.475147279634 37.79698410701219, -122.475147279634 37.7963016662754, -122.475329727468 37.7958671695696, -122.475884886313 37.7958692991137, -122.476244571753 37.79590912157668, -122.476509934088 37.79596037255811, -122.476855875304 37.79629946575938, -122.476928279516 37.7965135543643))'), {u'source': u'openstreetmap.org', u'way_area': u'29753.2', u'tourism': u'camp_site', u'name': u'Rob Hill Campground', u'area': u'yes'}))  # noqa

        self.assert_has_feature(
            16, 10471, 25326, 'landuse',
            {'kind': 'camp_site', 'sort_rank': 106, 'min_zoom': 14})

        # small campground in point zoom 16
        self.assert_has_feature(
            16, 10471, 25326, 'pois',
            {'kind': 'camp_site'})

        # small campground in landuse zoom 14
        self.assert_has_feature(
            14, 2617, 6331, 'landuse',
            {'kind': 'camp_site', 'sort_rank': 106})

        # small campground in point zoom 13
        self.assert_no_matching_feature(
            13, 1308, 3165, 'pois',
            {'kind': 'camp_site'})
