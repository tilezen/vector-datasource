# -*- encoding: utf-8 -*-
from . import FixtureTest


class LanduseTest(FixtureTest):

    def _check_remap(self, tags, remapped_kind):
        import dsl

        z, x, y = (12, 0, 0)

        all_tags = tags.copy()
        all_tags['source'] = 'openstreetmap.org'

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), all_tags),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'kind': remapped_kind,
            })

    def test_grassland_landuse_meadow(self):
        self._check_remap({'landuse': 'meadow'}, 'grassland')

    def test_grassland_landuse_grass(self):
        self._check_remap({'landuse': 'grass'}, 'grassland')

    def test_urban_area_landuse_village_green(self):
        self._check_remap({'landuse': 'village_green'}, 'urban_area')

    def test_grassland_natural_grassland(self):
        self._check_remap({'natural': 'grassland'}, 'grassland')

    def test_grassland_natural_heath(self):
        self._check_remap({'natural': 'heath'}, 'grassland')

    def test_farmland_landuse_farmland(self):
        self._check_remap({'landuse': 'farmland'}, 'farmland')

    def test_farmland_landuse_orchard(self):
        self._check_remap({'landuse': 'orchard'}, 'farmland')

    def test_farmland_landuse_vineyard(self):
        self._check_remap({'landuse': 'vineyard'}, 'farmland')

    def test_farmland_landuse_farm(self):
        self._check_remap({'landuse': 'farm'}, 'farmland')

    def test_farmland_landuse_plant_nursery(self):
        self._check_remap({'landuse': 'plant_nursery'}, 'farmland')

    # there used to be a test here for allotments, but they now have a
    # min_zoom of 13, which means they don't appear at any zooms where we
    # remap.

    def test_grassland_natural_scrub(self):
        self._check_remap({'natural': 'scrub'}, 'grassland')

    def test_forest_landuse_forest(self):
        self._check_remap({'landuse': 'forest'}, 'forest')

    def test_forest_natural_wood(self):
        self._check_remap({'natural': 'wood'}, 'forest')

    def test_barren_landuse_quarry(self):
        self._check_remap({'landuse': 'quarry'}, 'barren')

    def test_barren_natural_scree(self):
        self._check_remap({'natural': 'scree'}, 'barren')

    def test_barren_natural_shingle(self):
        self._check_remap({'natural': 'shingle'}, 'barren')

    def test_wetland_natural_wetland(self):
        self._check_remap({'natural': 'wetland'}, 'wetland')

    def test_wetland_natural_mud(self):
        self._check_remap({'natural': 'mud'}, 'wetland')

    def test_urban_area_landuse_residential(self):
        self._check_remap({'landuse': 'residential'}, 'urban_area')

    def test_urban_area_landuse_commercial(self):
        self._check_remap({'landuse': 'commercial'}, 'urban_area')

    def test_urban_area_landuse_retail(self):
        self._check_remap({'landuse': 'retail'}, 'urban_area')

    def test_urban_area_landuse_industrial(self):
        self._check_remap({'landuse': 'industrial'}, 'urban_area')

    def test_landuse_cemetery(self):
        # i.e: checking that it's _not_ remapped.
        self._check_remap({'landuse': 'cemetery'}, 'cemetery')

    def test_landuse_recreation_ground_not_remapped(self):
        self._check_remap(
            {'landuse': 'recreation_ground'}, 'recreation_ground')

    def test_school_not_remapped(self):
        self._check_remap({'amenity': 'school'}, 'school')

    def test_glacier_natural_glacier(self):
        self._check_remap({'natural': 'glacier'}, 'glacier')

    def test_desert_natural_bare_rock(self):
        self._check_remap({'natural': 'bare_rock'}, 'desert')

    def test_desert_natural_sand(self):
        self._check_remap({'natural': 'sand'}, 'desert')

    def test_desert_natural_desert(self):
        self._check_remap({'natural': 'desert'}, 'desert')
