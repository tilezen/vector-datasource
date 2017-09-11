# -*- encoding: utf-8 -*-
from . import OsmFixtureTest


class RoadsAccess(OsmFixtureTest):

    def test_restricted_access(self):
        # Add surface properties to roads layer (at max zooms)
        # restricted access road in military base, Kraków, Poland
        self.load_fixtures(['https://www.openstreetmap.org/way/43322699'])

        self.assert_has_feature(
            16, 36393, 22203, 'roads',
            {'id': 43322699, 'kind': 'minor_road', 'kind_detail': 'service',
             'access': 'private'})

        self.assert_has_feature(
            14, 9098, 5550, 'roads',
            {'id': 43322699, 'kind': 'minor_road', 'kind_detail': 'service',
             'access': 'private'})

    def test_no_access(self):
        # motorway bridge in Honk-Kong
        # ID may get dropped due to a merge with the other carriageway
        self.load_fixtures(['http://www.openstreetmap.org/way/276506948'])

        self.assert_has_feature(
            12, 3344, 1785, 'roads',
            {'kind': 'highway', 'kind_detail': 'motorway',
             'alt_name:en': 'Shenzhen Bay Bridge', 'access': 'no'})

    def test_access_yes(self):
        # cycleway in Gdańsk, Poland
        self.load_fixtures(['http://www.openstreetmap.org/way/151351130'])

        self.assert_has_feature(
            16, 36155, 20940, 'roads',
            {'id': 151351130, 'kind': 'path', 'access': 'yes'})
