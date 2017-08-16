import unittest
from . import OsmFixtureTest


class ShieldTextRef(OsmFixtureTest):

    def test_james_lick_freeway(self):
        # US 101, "James Lick Freeway"
        self.load_fixtures([
            'http://www.openstreetmap.org/way/27183379',
            'http://www.openstreetmap.org/relation/108619',
        ], clip=self.tile_bbox(16, 10484, 25334))
        self.assert_has_feature(
            16, 10484, 25334, 'roads',
            { 'kind': 'highway', 'network': 'US:US', 'id': 27183379,
              'shield_text': '101' })

    def test_multiple_shields(self):
        # I-77, I-81, US-11 & US-52 all in one road West Virginia.
        self.load_fixtures([
            'http://www.openstreetmap.org/way/51388984',
            'http://www.openstreetmap.org/relation/2309416',
            'http://www.openstreetmap.org/relation/2301037',
            'http://www.openstreetmap.org/relation/2297359',
            'http://www.openstreetmap.org/relation/1027748',
        ], clip=self.tile_bbox(16, 18022, 25522))
        self.assert_has_feature(
            16, 18022, 25522, 'roads',
            { 'kind': 'highway', 'network': 'US:I', 'id': 51388984,
              'shield_text': '77',
              'all_networks': ['US:I', 'US:I', 'US:US', 'US:US'],
              'all_shield_texts': ['77', '81', '11', '52'] })

    def test_network_without_ref(self):
        # routes with network but no ref should return a null ref.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/4069015',
            'http://www.openstreetmap.org/relation/6080335',
        ], clip=self.tile_bbox(16, 14852, 26071))
        self.assert_has_feature(
            16, 14852, 26071, 'roads',
            { 'kind': 'highway', 'id': 290908536,
              'all_networks': ['US:I', 'US:OK:Turnpike'],
              'all_shield_texts': ['44', None] })
