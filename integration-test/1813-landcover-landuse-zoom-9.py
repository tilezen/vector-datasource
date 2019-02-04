# -*- encoding: utf-8 -*-
from . import FixtureTest


class LandcoverTest(FixtureTest):

    def _starts_at(self, zoom, props):
        import dsl

        all_props = {'source': 'openstreetmap.org'}
        all_props.update(props)

        # biggest polygon possible - covering the whole world - should be
        # visible at this zoom, and have a min zoom of this zoom.
        world = dsl.tile_box(0, 0, 0)
        self.generate_fixtures(dsl.way(1, world, all_props))

        self.assert_has_feature(
            zoom, 0, 0, 'landuse', {
                'min_zoom': zoom,
            })

    def test_landuse_farmland(self):
        # farmland (and farm), modify the min to be 9 instead of 10.
        self._starts_at(9, {'landuse': 'farmland'})
        self._starts_at(9, {'landuse': 'farm'})

    def test_landuse_orchard(self):
        # starts at 10 now, should be 9?
        self._starts_at(9, {'landuse': 'orchard'})

    def test_landuse_forest(self):
        # do we need a custom `tier2_min_zoom` to show all at zoom 9?
        self._starts_at(9, {'landuse': 'forest'})

    def test_landuse_residential(self):
        # okay to start at 10, because of NE overlap
        self._starts_at(10, {'landuse': 'residential'})

    def test_landuse_commercial(self):
        # okay to start at 10, because of NE overlap
        self._starts_at(10, {'landuse': 'commercial'})

    def test_landuse_retail(self):
        # okay to start at 10, because of NE overlap
        self._starts_at(10, {'landuse': 'retail'})

    def test_landuse_industrial(self):
        # okay to start at 10, because of NE overlap
        self._starts_at(10, {'landuse': 'industrial'})

    def test_landuse_meadow(self):
        # starts at 9, but throttled
        self._starts_at(9, {'landuse': 'meadow'})

    def test_landuse_vineyard(self):
        # starts at 9, but throttled
        self._starts_at(9, {'landuse': 'vineyard'})

    def test_natural_wood(self):
        # do we need a custom `tier2_min_zoom` to show all at zoom 9?
        self._starts_at(9, {'natural': 'wood'})

    def test_natural_sand(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'sand'})

    def test_natural_scree(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'scree'})

    def test_natural_shingle(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'shingle'})

    def test_natural_bare_rock(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'bare_rock'})

    def test_natural_heath(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'heath'})

    def test_natural_grassland(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'grassland'})

    def test_natural_scrub(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'scrub'})

    def test_natural_wetland(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'wetland'})

    def test_natural_mud(self):
        # starts at 9, but throttled
        self._starts_at(9, {'natural': 'mud'})
