# -*- encoding: utf-8 -*-
from . import FixtureTest


class LandUseTest(FixtureTest):

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

    def test_airfield_aerodrome(self):
        self._check_remap({'military': 'airfield'}, 'aerodrome')

    def test_artwork_urban_area(self):
        self._check_remap({'tourism': 'artwork'}, 'urban_area')

    def test_attraction_urban_area(self):
        self._check_remap({'tourism': 'attraction'}, 'urban_area')

    def test_college_university(self):
        self._check_remap({'amenity': 'college'}, 'university')

    def test_common_grassland(self):
        self._check_remap({'leisure': 'common'}, 'grassland')

    def test_dam_barren(self):
        self._check_remap({'waterway': 'dam'}, 'barren')

    def test_danger_area_military(self):
        self._check_remap({'military': 'danger_area'}, 'military')

    def test_fort_urban_area(self):
        self._check_remap({'historic': 'fort'}, 'urban_area')

    def test_generator_urban_area(self):
        self._check_remap({'power': 'generator'}, 'urban_area')

    def test_land_barren(self):
        self._check_remap({'natural': 'land'}, 'barren')

    def test_pitch_urban_area(self):
        self._check_remap({'leisure': 'pitch'}, 'urban_area')

    def test_place_of_worship_urban_area(self):
        self._check_remap({'amenity': 'place_of_worship'}, 'urban_area')

    def test_plant_urban_area(self):
        self._check_remap({'power': 'plant'}, 'urban_area')

    def test_prison_urban_area(self):
        self._check_remap({'amenity': 'prison'}, 'urban_area')

    def test_railway_urban_area(self):
        self._check_remap({'landuse': 'railway'}, 'urban_area')

    def test_range_military(self):
        self._check_remap({'military': 'range'}, 'military')

    def test_rock_barren(self):
        self._check_remap({'natural': 'rock'}, 'barren')

    def test_scrub_grassland(self):
        self._check_remap({'natural': 'scrub'}, 'grassland')

    def test_service_area_not_remapped(self):
        self._check_remap({'highway': 'services'}, 'service_area')

    def test_stone_barren(self):
        self._check_remap({'natural': 'stone'}, 'barren')

    def test_wastewater_plant_urban_area(self):
        self._check_remap({'man_made': 'wastewater_plant'}, 'urban_area')

    def test_water_works_urban_area(self):
        self._check_remap({'man_made': 'water_works'}, 'urban_area')

    def test_works_urban_area(self):
        self._check_remap({'man_made': 'works'}, 'urban_area')
