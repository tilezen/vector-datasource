# -*- encoding: utf-8 -*-
from . import FixtureTest


class LanduseSortRankTest(FixtureTest):

    def _check(self, tags, expected_kind, expected_sort_rank):
        import dsl

        z, x, y = (16, 0, 0)

        full_tags = {
            'source': 'openstreetmap.org'
        }
        full_tags.update(tags)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), full_tags),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 1,
                'kind': expected_kind,
                'sort_rank': expected_sort_rank,
            })

    def test_airfield(self):
        self._check({'military': 'airfield'}, 'airfield', 69)

    def test_danger_area(self):
        self._check({'military': 'danger_area'}, 'danger_area', 50)

    def test_naval_base(self):
        self._check({'military': 'naval_base'}, 'naval_base', 49)

    def test_port_terminal(self):
        self._check({'landuse': 'port_terminal'}, 'port_terminal', 64)

    def test_ferry_terminal(self):
        self._check({'landuse': 'ferry_terminal'}, 'ferry_terminal', 64)

    def test_container_terminal(self):
        self._check({'landuse': 'container_terminal'},
                    'container_terminal', 64)

    def test_shipyard(self):
        self._check({'landuse': 'shipyard'}, 'shipyard', 63)

    def test_wharf(self):
        self._check({'landuse': 'wharf'}, 'wharf', 65)

    def test_quay(self):
        self._check({'man_made': 'quay'}, 'quay', 65)
