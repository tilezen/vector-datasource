# -*- encoding: utf-8 -*-
from . import FixtureTest


# To decrease file size let's drop all_networks and all_shield_texts
# from low and mid-zooms when there's often not room to display this
# information.
class DropAllNetworksShieldsAtLowZooms(FixtureTest):

    def _drop_at_zoom(self, z, osm=None, kind=None):
        import dsl

        x = 1 << (z-1)
        y = 1 << (z-1)

        self.generate_fixtures(
            dsl.is_in('US', z, x, y),
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': osm,
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'ref': u'1',
                'network': 'US:I',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[1]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 1,
                'kind': kind,
                'network': u'US:I',
                'shield_text': u'1',
                'all_networks': [u'US:I'],
                'all_shield_texts': [u'1'],
            })

        # feature should still appear at z9, but without the "all_*"
        # attributes. (NOTE: don't test shield text, as it might have
        # been dropped anyway.)
        self.assert_has_feature(
            z-1, x//2, y//2, 'roads', {
                'id': 1,
                'kind': kind,
                'all_networks': type(None),
                'all_shield_texts': type(None),
            })

    # drop from highway: less than zoom 10
    def test_highway(self):
        self._drop_at_zoom(10, osm='motorway', kind='highway')

    # drop from major_road: less than zoom 12
    def test_major_road(self):
        self._drop_at_zoom(12, osm='secondary', kind='major_road')

    # drop from other kinds: less than zoom 14
    def test_other_roads(self):
        self._drop_at_zoom(14, osm='unclassified', kind='minor_road')
        self._drop_at_zoom(14, osm='pedestrian', kind='path')
