# -*- encoding: utf-8 -*-
from . import FixtureTest


class PoiMinZoomTest(FixtureTest):

    def _check(self, props, landuse_zoom, poi_zoom=None, kind=None):
        import dsl

        if kind is None:
            assert len(props) == 1
            kind = props.values()[0]

        if poi_zoom is None:
            poi_zoom = landuse_zoom

        x, y = 0, 0
        tags = {
            'source': 'openstreetmap.org',
            'name': 'Insert Name Here',
        }
        tags.update(props)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(landuse_zoom, x, y), tags),
        )

        self.assert_has_feature(
            landuse_zoom, x, y, 'landuse', {
                'min_zoom': landuse_zoom,
            })
        zdiff = landuse_zoom - poi_zoom
        pcoord = (1 << (zdiff - 1)) - 1 if zdiff > 0 else 0
        self.assert_has_feature(
            poi_zoom, pcoord, pcoord, 'pois', {
                'min_zoom': poi_zoom,
            })

    def test_quay(self):
        self._check({'landuse': 'quay'}, 16)
        self._check({'man_made': 'quay'}, 16)

    def test_range(self):
        self._check({'military': 'range'}, 11)

    def test_wharf(self):
        self._check({'landuse': 'wharf'}, 16)

    def test_boatyard(self):
        self._check({'waterway': 'boatyard'}, 15)

    def test_shipyard(self):
        self._check({'landuse': 'shipyard'}, 15)

    def test_danger_area(self):
        self._check({'military': 'danger_area'}, 11)

    def test_port_terminal(self):
        self._check({'landuse': 'port_terminal'}, 13)

    def test_sports_centre(self):
        self._check({'leisure': 'sports_centre'}, 12)

    def test_ferry_terminal(self):
        self._check({'landuse': 'ferry_terminal'}, 13)

    def test_container_terminal(self):
        self._check({'landuse': 'container_terminal'}, 13)
