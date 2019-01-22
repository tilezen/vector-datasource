# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


# update landuse to include barriers features and delete from boundaries
class MoveBarriersToLanduse(FixtureTest):

    def test_city_wall(self):
        # city_wall in landuse
        self.generate_fixtures(dsl.way(2173322159, wkt_loads('POINT (-1.57745475431703 54.77092927329858)'), {u'source': u'openstreetmap.org', u'barrier': u'gate'}),dsl.way(81522922, wkt_loads('LINESTRING (-1.57738576370321 54.77094310897829, -1.57745475431703 54.77092927329858, -1.57777320708525 54.77089486544558, -1.57799536045501 54.77087890516648, -1.57818158121341 54.77094259078807, -1.57824149884286 54.7709935806684, -1.57826431605108 54.77104457048438, -1.5782444632833 54.771161370085, -1.57803344902306 54.7717867137644)'), {u'source': u'openstreetmap.org', u'barrier': u'city_wall'}))  # noqa

        self.assert_has_feature(
            12, 2030, 1300, 'landuse',
            {'kind': 'city_wall'})

        # city_wall not in boundaries
        self.assert_no_matching_feature(
            12, 2030, 1300, 'boundaries',
            {'kind': 'city_wall'})

    def test_citywalls(self):
        # citywalls in landuse
        self.generate_fixtures(dsl.way(392978585, wkt_loads('LINESTRING (24.4720476224511 35.37148697890318, 24.4712704898988 35.3713100065569)'), {u'source': u'openstreetmap.org', u'historic': u'citywalls'}))  # noqa

        self.assert_has_feature(
            12, 2326, 1617, 'landuse',
            {'kind': 'city_wall'})

        # citywalls not in boundaries
        self.assert_no_matching_feature(
            12, 2326, 1617, 'boundaries',
            {'kind': 'city_wall'})

    def test_dam(self):
        # dam in landuse
        self.generate_fixtures(dsl.way(109629543, wkt_loads('LINESTRING (-114.911712215386 36.12550132309848, -114.911372921704 36.12508207375689, -114.910614114783 36.12413356646388, -114.910065872965 36.12300306315098, -114.909903996551 36.12218449022499, -114.909913698356 36.12134696976019, -114.910197476154 36.12046227373689, -114.910567222725 36.1194246008354, -114.910692986865 36.11847290485559, -114.910504789813 36.11758636227938, -114.909941905456 36.11669131929139)'), {u'source': u'openstreetmap.org', u'waterway': u'dam'}))  # noqa

        self.assert_has_feature(
            13, 1481, 3213, 'landuse',
            {'kind': 'dam'})

        # dam not in boundaries
        self.assert_no_matching_feature(
            12, 740, 1606, 'boundaries',
            {'kind': 'dam'})

    def test_fence(self):
        # fence in landuse
        self.generate_fixtures(dsl.way(3522432756, wkt_loads('POINT (-73.99964652459359 40.73439355833799)'), {u'source': u'openstreetmap.org', u'barrier': u'gate'}),dsl.way(345599214, wkt_loads('LINESTRING (-73.9992052721261 40.73439648531308, -73.99922701135588 40.73437109550148, -73.9993464872887 40.73422018588509, -73.9995127654478 40.73416532195229, -73.99964652459359 40.73439355833799, -73.9997997771811 40.73465507965219, -73.99953360636241 40.73468911410468, -73.99935097886518 40.7347122575225, -73.99925423030911 40.7347215829562)'), {u'source': u'openstreetmap.org', u'barrier': u'fence'}))  # noqa

        self.assert_has_feature(
            16, 19296, 24635, 'landuse',
            {'kind': 'fence'})

        # fence not in boundaries
        self.assert_no_matching_feature(
            16, 19296, 24635, 'boundaries',
            {'kind': 'fence'})

    def test_retaining_wall(self):
        # retaining_wall in landuse
        self.generate_fixtures(dsl.way(288896098, wkt_loads('LINESTRING (-73.99848590124648 40.75414757104189, -73.99858175148739 40.75397751643467, -73.9986491251337 40.75378119434839, -73.99868658488099 40.75361998524168)'), {u'source': u'openstreetmap.org', u'barrier': u'retaining_wall'}))  # noqa

        self.assert_has_feature(
            15, 9648, 12315, 'landuse',
            {'kind': 'retaining_wall'})

        # retaining_wall not in boundaries
        self.assert_no_matching_feature(
            15, 9648, 12315, 'boundaries',
            {'kind': 'retaining_wall'})

    def test_snow_fence(self):
        # snow_fence in landuse
        self.generate_fixtures(dsl.way(356771680, wkt_loads('LINESTRING (-105.418546531019 41.17472586849339, -105.417813236252 41.17203419617208, -105.417465408574 41.17044640452401)'), {u'source': u'openstreetmap.org', u'man_made': u'snow_fence'}))  # noqa

        self.assert_has_feature(
            15, 6788, 12264, 'landuse',
            {'kind': 'snow_fence'})

        # snow_fence not in boundaries
        self.assert_no_matching_feature(
            15, 6788, 12264, 'boundaries',
            {'kind': 'snow_fence'})
