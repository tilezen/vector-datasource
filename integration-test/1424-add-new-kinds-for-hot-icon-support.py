# -*- encoding: utf-8 -*-
from . import FixtureTest


class KindsForHotIconSupportTest(FixtureTest):

    def test_health_centre_node(self):
        import dsl

        z, x, y = (16, 17055, 30537)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4581943190
            dsl.point(4581943190, (-86.312320, 12.161792), {
                'amenity': u'doctors',
                'health_facility:type': u'health_centre',
                'name': u'Puesto de Salud Villa Guadalupe',
                'operator': u'MINSA',
                'source': u'openstreetmap.org',
            }),
        )

        # TODO: should this be health_centre or doctors?
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4581943190,
                'kind': u'health_centre',
            })

    def test_health_centre_way(self):
        import dsl

        z, x, y = (16, 16479, 24666)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/237908971
            dsl.way(237908971, dsl.tile_box(z, x, y), {
                'building': u'office',
                'building:levels': u'1',
                'emergency': u'yes',
                'health_facility:type': u'health_centre',
                'medical_system:western': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 237908971,
                'kind': u'health_centre',
            })

    def test_arts_centre_node(self):
        import dsl

        z, x, y = (16, 19298, 24650)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2494292126
            dsl.point(2494292126, (-73.988367, 40.671751), {
                'amenity': u'arts_centre',
                'contact:facebook': u'https://www.facebook.com/' \
                u'Temple-Of-Roses-Inc-114454938634218/',
                'name': u'Temple of Roses',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2494292126,
                'kind': u'arts_centre',
            })

    def test_arts_centre_way(self):
        import dsl

        z, x, y = (16, 19295, 24635)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/249665940
            dsl.way(249665940, dsl.tile_box(z, x, y), {
                'addr:housenumber': u'46',
                'addr:postcode': u'10014',
                'addr:street': u'Barrow Street',
                'alt_name': u'Greenwich House Music',
                'amenity': u'arts_centre',
                'building': u'yes',
                'height': u'16.2',
                'name': u'Greenwich House Music School',
                'nycdoitt:bin': u'1010028',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 249665940,
                'kind': u'arts_centre',
            })

    def test_bucket_toilets_node(self):
        import dsl

        z, x, y = (16, 19396, 24479)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3208479066
            dsl.point(3208479066, (-73.452498, 41.378662), {
                'access': u'public',
                'amenity': u'toilets',
                'source': u'openstreetmap.org',
                'toilets:disposal': u'bucket',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3208479066,
                'kind': u'toilets',
                'kind_detail': u'bucket',
            })

    def test_car_parts_node(self):
        import dsl

        z, x, y = (16, 19305, 24648)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4149649612
            dsl.point(4149649612, (-73.952859, 40.679054), {
                'name': u'Advance Auto Parts',
                'shop': u'car_parts',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4149649612,
                'kind': u'car_parts',
            })

    def test_car_parts_way(self):
        import dsl

        z, x, y = (16, 19323, 24634)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/338893197
            dsl.way(338893197, dsl.tile_box(z, x, y), {
                'addr:city': u'Corona',
                'addr:housenumber': u'105-45',
                'addr:postcode': u'11368',
                'addr:state': u'NY',
                'addr:street': u'Horace Harding Expressway',
                'building': u'yes',
                'height': u'3.9',
                'name': u'Mobil Mart',
                'nycdoitt:bin': u'4048308',
                'operator': u'ExxonMobil',
                'shop': u'car_parts',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 338893197,
                'kind': u'car_parts',
            })

    def test_car_rental_node(self):
        import dsl

        z, x, y = (16, 19294, 24649)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2550085672
            dsl.point(2550085672, (-74.010287, 40.673316), {
                'addr:city': u'Brooklyn',
                'addr:housenumber': u'5',
                'addr:postcode': u'11231',
                'addr:state': u'NY',
                'addr:street': u'Sigourney Street',
                'amenity': u'car_rental',
                'name': u'Best Trails & Travel Corporation',
                'opening_hours': u'Mo-Fr 09:00-18:00',
                'phone': u'+1 212-206-6974',
                'source': u'openstreetmap.org',
                'website': u'http://bttny.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2550085672,
                'kind': u'car_rental',
            })

    def test_car_rental_way(self):
        import dsl

        z, x, y = (16, 19299, 24632)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/265042574
            dsl.way(265042574, dsl.tile_box(z, x, y), {
                'amenity': u'car_rental',
                'height': u'46.4',
                'nycdoitt:bin': u'1015765',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 265042574,
                'kind': u'car_rental',
            })

    def test_craft_node(self):
        import dsl

        z, x, y = (16, 25756, 35156)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4802596181
            dsl.point(4802596181, (-38.516527, -13.009279), {
                'addr:street': u'Rua Morro do Escravo Miguel',
                'craft': u'luthier',
                'name': u'G. Spinola Luthier',
                'source': u'openstreetmap.org',
            }),
        )

        # we are testing that craft=* values that we don't individually
        # whitelist are grouped together under a generic "craft" kind. at
        # the time of writing, we didn't whitelist luthiers.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4802596181,
                'kind': u'craft',
            })

    def test_drinking_water_water_well_powered_node(self):
        import dsl

        z, x, y = (16, 18838, 25133)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4831455841
            dsl.point(4831455841, (-76.519391, 38.625901), {
                'drinking_water': u'yes',
                'man_made': u'water_well',
                'pump': u'powered',
                'pump:status': u'ok',
                'pump:style': u'modern',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4831455841,
                'kind': u'water_well',
                'kind_detail': u'drinkable_powered',
            })

    def test_drinking_water_water_well_manual_node(self):
        import dsl

        z, x, y = (16, 19612, 29311)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4151615348
            dsl.point(4151615348, (-72.263428, 18.651315), {
                'abandoned': u'no',
                'condition': u'fair',
                'disused': u'no',
                'drinking_water': u'yes',
                'man_made': u'water_well',
                'operator:type': u'private',
                'pump': u'manual',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4151615348,
                'kind': u'water_well',
                'kind_detail': u'drinkable_manual',
            })

    def test_drinking_water_water_well_no_node(self):
        import dsl

        z, x, y = (16, 19634, 29121)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2316015603
            dsl.point(2316015603, (-72.142061, 19.634009), {
                'access': u'private',
                'condition': u'good',
                'drinking_water': u'yes',
                'man_made': u'water_well',
                'name': u'Open Door',
                'operator:type': u'private',
                'pump': u'no',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2316015603,
                'kind': u'water_well',
                'kind_detail': u'drinkable_no_pump',
            })

    def test_not_drinking_water_water_well_powered_node(self):
        import dsl

        z, x, y = (16, 19640, 29103)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2321995834
            dsl.point(2321995834, (-72.113625, 19.727593), {
                'access': u'private',
                'condition': u'fair',
                'drinking_water': u'no',
                'man_made': u'water_well',
                'operator:type': u'private',
                'pump': u'powered',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2321995834,
                'kind': u'water_well',
                'kind_detail': u'not_drinkable_powered',
            })

    def test_not_drinking_water_water_well_manual_node(self):
        import dsl

        z, x, y = (16, 18008, 27541)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4859738847
            dsl.point(4859738847, (-81.077826, 27.576623), {
                'drinking_water': u'no',
                'man_made': u'water_well',
                'note': u'non-potable; must be treated',
                'pump': u'manual',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4859738847,
                'kind': u'water_well',
                'kind_detail': u'not_drinkable_manual',
            })

    def test_not_drinking_water_water_well_no_node(self):
        import dsl

        z, x, y = (16, 20096, 23838)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4297637981
            dsl.point(4297637981, (-69.609191, 43.967155), {
                'drinking_water': u'no',
                'man_made': u'water_well',
                'pump': u'no',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4297637981,
                'kind': u'water_well',
                'kind_detail': u'not_drinkable_no_pump',
            })

    def test_funeral_directors_node(self):
        import dsl

        z, x, y = (16, 19310, 24643)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5163881916
            dsl.point(5163881916, (-73.926626, 40.698738), {
                'addr:housenumber': u'176',
                'addr:street': u'Central Avenue',
                'name': u'Ponce Funeral Home',
                'shop': u'funeral_directors',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5163881916,
                'kind': u'funeral_directors',
            })

    def test_funeral_directors_way(self):
        import dsl

        z, x, y = (16, 19300, 24648)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/241845988
            dsl.way(241845988, dsl.tile_box(z, x, y), {
                'addr:housenumber': u'162',
                'addr:postcode': u'11217',
                'addr:street': u'4th Avenue',
                'building': u'yes',
                'height': u'7.8',
                'name': u'Ponce Funeral Homes',
                'nycdoitt:bin': u'3006628',
                'shop': u'funeral_directors',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 241845988,
                'kind': u'funeral_directors',
            })

    def test_bookmaker_node(self):
        import dsl

        z, x, y = (16, 19256, 24654)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4834515322
            dsl.point(4834515322, (-74.220812, 40.653228), {
                'addr:housenumber': u'469',
                'addr:postcode': u'07202',
                'addr:street': u'Edgar Road',
                'name': u'casa',
                'shop': u'bookmaker',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4834515322,
                'kind': u'bookmaker',
            })

    def test_bookmaker_way(self):
        import dsl

        z, x, y = (16, 19275, 24653)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/354356103
            dsl.way(354356103, dsl.tile_box(z, x, y), {
                'amenity': u'gambling',
                'building': u'yes',
                'name': u'Winners',
                'shop': u'bookmaker',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 354356103,
                'kind': u'bookmaker',
            })

    def test_lottery_node(self):
        import dsl

        z, x, y = (16, 19301, 24630)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4555833812
            dsl.point(4555833812, (-73.974215, 40.751658), {
                'name': u'Lotto & Smoke Shop',
                'shop': u'lottery',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4555833812,
                'kind': u'lottery',
            })

    def test_lottery_way(self):
        import dsl

        z, x, y = (16, 18974, 23478)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/457623195
            dsl.way(457623195, dsl.tile_box(z, x, y), {
                'indoor': u'area',
                'level': u'0',
                'name': u'CNIB Lottery',
                'shop': u'lottery',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 457623195,
                'kind': u'lottery',
            })

    def test_photovoltaic_generator_node(self):
        import dsl

        z, x, y = (16, 18769, 24937)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3674184625
            dsl.point(3674184625, (-76.895316, 39.463608), {
                'generator:method': u'photovoltaic',
                'generator:source': u'solar',
                'generator:type': u'solar_photovoltaic_panel',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3674184625,
                'kind': u'generator',
                'kind_detail': u'photovoltaic',
            })

    def test_wind_turbine_generator_node(self):
        import dsl

        z, x, y = (16, 19287, 24641)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3601278314
            dsl.point(3601278314, (-74.053026, 40.708775), {
                'generator:method': u'wind_turbine',
                'generator:source': u'wind',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3601278314,
                'kind': u'generator',
                'kind_detail': u'wind_turbine',
            })

    def test_combustion_generator_node(self):
        import dsl

        z, x, y = (16, 19296, 24652)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3671190948
            dsl.point(3671190948, (-74.000081, 40.663024), {
                'generator:method': u'combustion',
                'generator:source': u'gas',
                'generator:type': u'steam_turbine',
                'operator': u'New York Power Authority',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3671190948,
                'kind': u'generator',
                'kind_detail': u'combustion',
            })

    def test_runoftheriver_generator_node(self):
        import dsl

        z, x, y = (16, 18739, 25837)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4728106977
            dsl.point(4728106977, (-77.058646, 35.542703), {
                'generator:method': u'run-of-the-river',
                'name': u'generater old washington',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4728106977,
                'kind': u'generator',
                'kind_detail': u'run-of-the-river',
            })

    def test_waterstorage_generator_node(self):
        import dsl

        z, x, y = (16, 18307, 24524)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2363460494
            dsl.point(2363460494, (-79.435315, 41.192111), {
                'generator:method': u'water-storage',
                'generator:output:electricity': u'30 MW',
                'generator:source': u'hydro',
                'name': u'Piney Hydro Power Plant',
                'operator': u'Brookfield Power Corp',
                'power': u'generator',
                'source': u'openstreetmap.org',
                'website': u'http://enipedia.tudelft.nl' \
                u'/wiki/Piney_Dam_Powerplant',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2363460494,
                'kind': u'generator',
                'kind_detail': u'water-storage',
            })

    def test_thermal_generator_node(self):
        import dsl

        z, x, y = (16, 18269, 23900)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5265052918
            dsl.point(5265052918, (-79.641370, 43.719978), {
                'generator:method': u'thermal',
                'generator:output:electricity': u'no',
                'generator:output:hot_water': u'yes',
                'generator:source': u'solar',
                'generator:type': u'solar_thermal_collector',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5265052918,
                'kind': u'generator',
                'kind_detail': u'thermal',
            })

    def test_anaerobic_digestion_generator_node(self):
        import dsl

        z, x, y = (16, 22238, 35302)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5691734305
            dsl.point(5691734305, (-57.840700, -13.786471), {
                'generator:method': u'anaerobic_digestion',
                'name': u'Coprodia',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5691734305,
                'kind': u'generator',
                'kind_detail': u'anaerobic_digestion',
            })

    def test_fission_generator_node(self):
        import dsl

        z, x, y = (16, 18800, 24773)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/33180844
            dsl.point(33180844, (-76.725103, 40.154753), {
                'generator:method': u'fission',
                'generator:output:electricity': u'802 MW',
                'generator:source': u'nuclear',
                'name': u'Three Mile Island Unit 1',
                'name:de': u'Three Mile Island Block 1',
                'name:sk': u'Three Mile Island jednotka 1',
                'operator': u'Exelon Nuclear',
                'power': u'generator',
                'short_name': u'TMI-1',
                'source': u'openstreetmap.org',
                'website': u'http://www.exeloncorp.com/' \
                u'PowerPlants/threemileisland/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 33180844,
                'kind': u'generator',
                'kind_detail': u'fission',
            })

    def test_gasification_generator_node(self):
        import dsl

        z, x, y = (16, 19540, 29226)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1695449375
            dsl.point(1695449375, (-72.658127, 19.090002), {
                'generator:method': u'gasification',
                'generator:output:battery_charging': u'yes',
                'generator:output:electricity': u'yes',
                'generator:output:steam': u'yes',
                'generator:source': u'diesel',
                'name': u'Centrale ELECTRICIDeCS',
                'operator': u'CIDeCS',
                'operator_type': u'community',
                'power': u'generator',
                'project': u'OTI_HRI_COSMHA_STM020',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1695449375,
                'kind': u'generator',
                'kind_detail': u'gasification',
            })

    def test_dam_generator_node(self):
        import dsl

        z, x, y = (16, 18335, 24589)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5427396488
            dsl.point(5427396488, (-79.277774, 40.921900), {
                'generator:method': u'dam',
                'generator:output:electricity': u'6 MW',
                'generator:source': u'hydro',
                'name': u'Mahoning Creek Hydroelectric Plant',
                'power': u'generator',
                'source': u'openstreetmap.org',
                'website': u'http://www.hydroworld.com/articles' \
                u'/hr/print/volume-33/issue-8/cover-story/' \
                u'adding-power-to-a-non-powered-dam-mahoning-creek.html',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5427396488,
                'kind': u'generator',
                'kind_detail': u'water-storage',
            })

    def test_waterpumpedstorage_generator_node(self):
        import dsl

        z, x, y = (16, 17962, 26112)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1567492845
            dsl.point(1567492845, (-81.331562, 34.306045), {
                'generator:method': u'water-pumped-storage',
                'generator:output:electricity': u'yes',
                'generator:source': u'hydro',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1567492845,
                'kind': u'generator',
                'kind_detail': u'water-pumped-storage',
            })

    def test_solar_photovoltaic_panel_generator_node(self):
        import dsl

        z, x, y = (16, 18604, 24944)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4029169257
            dsl.point(4029169257, (-77.803940, 39.432044), {
                'generator:method': u'solar_photovoltaic_panel',
                'generator:source': u'solar',
                'generator:type': u'solar_photovoltaic_panel',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4029169257,
                'kind': u'generator',
                'kind_detail': u'photovoltaic',
            })

    def test_wind_generator_node(self):
        import dsl

        z, x, y = (16, 21302, 23427)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3556714052
            dsl.point(3556714052, (-62.984344, 45.569156), {
                'generator:method': u'wind',
                'generator:output:electricity': u'1.5 MW',
                'generator:source': u'wind',
                'generator:type': u'wind_turbine',
                'manufacturer': u'GE',
                'operator': u'RMS Energy',
                'power': u'generator',
                'source': u'openstreetmap.org',
                'start_date': u'2009',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3556714052,
                'kind': u'generator',
                'kind_detail': u'wind_turbine',
            })

    def test_stream_generator_node(self):
        import dsl

        z, x, y = (16, 19067, 31963)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4277423725
            dsl.point(4277423725, (-75.261768, 4.412921), {
                'ele': u'5',
                'generator:method': u'stream',
                'generator:source': u'electricity_network',
                'generator:type': u'horizontal_axis',
                'name': u'PTE',
                'operator': u'Enertolima',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4277423725,
                'kind': u'generator',
                'kind_detail': u'stream',
            })

    def test_barrage_generator_node(self):
        import dsl

        z, x, y = (16, 32398, 22612)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1321199509
            dsl.point(1321199509, (-2.027265, 48.617462), {
                'frequency': u'50',
                'generator:method': u'barrage',
                'generator:output:electricity': u'10 MW',
                'generator:source': u'tidal',
                'generator:type': u'kaplan_turbine',
                'operator': u'EDF',
                'phases': u'3',
                'power': u'generator',
                'source': u'openstreetmap.org',
                'voltage': u'3500',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1321199509,
                'kind': u'generator',
                'kind_detail': u'barrage',
            })

    def test_solar_generator_way(self):
        import dsl

        z, x, y = (16, 19111, 24869)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/542100951
            dsl.way(542100951, dsl.tile_box(z, x, y), {
                'generator:method': u'solar',
                'generator:source': u'solar',
                'generator:type': u'solar_photovoltaic_panel',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 542100951,
                'kind': u'generator',
                'kind_detail': u'photovoltaic',
            })

    def test_photovoltaik_generator_way(self):
        import dsl

        z, x, y = (16, 34069, 22160)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/538293962
            dsl.way(538293962, dsl.tile_box(z, x, y), {
                'generator:method': u'photovoltaik',
                'generator:output:electricity': u'small_installation',
                'generator:place': u'roof',
                'generator:source': u'solar',
                'generator:type': u'solar_photovoltaic_panels',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 538293962,
                'kind': u'generator',
                'kind_detail': u'photovoltaic',
            })

    def test_money_transfer_node(self):
        import dsl

        z, x, y = (16, 19299, 24632)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3854507957
            dsl.point(3854507957, (-73.982208, 40.743233), {
                'amenity': u'money_transfer',
                'shop': u'money_lender',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3854507957,
                'kind': u'money_transfer',
            })

    def test_money_transfer_way(self):
        import dsl

        z, x, y = (16, 18993, 23478)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/366495997
            dsl.way(366495997, dsl.tile_box(z, x, y), {
                'addr:housenumber': u'1717',
                'addr:street': u'Bank Street',
                'amenity': u'money_transfer',
                'building': u'commercial',
                'name': u'Western Union',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 366495997,
                'kind': u'money_transfer',
            })

    def test_charity_node(self):
        import dsl

        z, x, y = (16, 19300, 24649)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4939092647
            dsl.point(4939092647, (-73.981834, 40.674757), {
                'addr:city': u'Brooklyn',
                'addr:housenumber': u'266',
                'addr:postcode': u'11215',
                'addr:state': u'NY',
                'addr:street': u'5th Avenue',
                'branch': u'Park Slope',
                'name': u'Housing Works Thrift Shop',
                'opening_hours': u'Mo-Sa 12:00-18:00; Su 11:00-17:00',
                'operator': u'Housing Works',
                'phone': u'+1 718 636 2271',
                'shop': u'charity',
                'source': u'openstreetmap.org',
                'website': u'https://www.housingworks.org/locations' \
                u'/park-slope-thrift-shop',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4939092647,
                'kind': u'charity',
            })

    def test_charity_way(self):
        import dsl

        z, x, y = (16, 19288, 24628)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/559471750
            dsl.way(559471750, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'name': u'Salvation Army',
                'payment:cash': u'yes',
                'second_hand': u'only',
                'shop': u'charity',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 559471750,
                'kind': u'charity',
            })

    def test_photo_node(self):
        import dsl

        z, x, y = (16, 19313, 24643)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5423484554
            dsl.point(5423484554, (-73.906871, 40.697347), {
                'addr:city': u'Ridgewood',
                'addr:housenumber': u'883',
                'addr:postcode': u'11385',
                'addr:state': u'NY',
                'addr:street': u'Wyckoff Avenue',
                'name': u'Blue Parallax Studios',
                'phone': u'347-825-8664',
                'shop': u'photo',
                'source': u'openstreetmap.org',
                'website': u'http://blueparallaxstudios.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5423484554,
                'kind': u'photo',
            })

    def test_photo_way(self):
        import dsl

        z, x, y = (16, 19259, 24596)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/275087161
            dsl.way(275087161, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'name': u'M&A Video Productions',
                'shop': u'photo',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 275087161,
                'kind': u'photo',
            })

    def test_camera_node(self):
        import dsl

        z, x, y = (16, 19310, 24641)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5691026660
            dsl.point(5691026660, (-73.925771, 40.705740), {
                'addr:housenumber': u'1138',
                'addr:street': u'Flushing Avenue',
                'email': u'brooklyn@csirentals.com',
                'fax': u'+1-718-366-1721',
                'name': u'CSI Rentals - Brooklyn',
                'opening_hours': 'Mo-We 08:00-18:00; Th 08:00-19:00;' \
                ' Fr 08:00-13:00',
                'payment:cash': u'yes',
                'payment:debit_cards': u'yes',
                'phone': u'+1-718-366-7368',
                'shop': u'camera',
                'source': u'openstreetmap.org',
                'website': u'https://csirentals.com/',
                'wheelchair': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5691026660,
                'kind': u'camera',
            })

    def test_camera_way(self):
        import dsl

        z, x, y = (16, 19112, 24830)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/206702693
            dsl.way(206702693, dsl.tile_box(z, x, y), {
                'name': u'Le Camera',
                'shop': u'camera',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 206702693,
                'kind': u'camera',
            })

    def test_copyshop_node(self):
        import dsl

        z, x, y = (16, 19300, 24648)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5534566023
            dsl.point(5534566023, (-73.978641, 40.678851), {
                'fax': u'+1 718 399 7778',
                'name': u'Graphicolor Digital Copy Center',
                'opening_hours': u'Mo-Fr 09:00-18:00; Sa 10:00-18:00',
                'phone': u'+1 718 398 8745',
                'service:computer': u'yes',
                'service:copy': u'yes',
                'service:press': u'yes',
                'service:print': u'yes',
                'shop': u'copyshop',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5534566023,
                'kind': u'copyshop',
            })

    def test_copyshop_way(self):
        import dsl

        z, x, y = (16, 19308, 24648)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/250372504
            dsl.way(250372504, dsl.tile_box(z, x, y), {
                'addr:city': u'Brooklyn',
                'addr:housenumber': u'474',
                'addr:postcode': u'11216',
                'addr:state': u'NY',
                'addr:street': u'Marcus Garvey Boulevard',
                'building': u'yes',
                'height': u'7.1',
                'name': 'Lillian\'s Professional Service Office ' \
                'Print and Ship Center',
                'nycdoitt:bin': u'3053696',
                'shop': u'copyshop',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 250372504,
                'kind': u'copyshop',
            })

    def test_radio_studio_node(self):
        import dsl

        z, x, y = (16, 19315, 24642)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5612341325
            dsl.point(5612341325, (-73.894959, 40.702430), {
                'addr:housenumber': u'70-05',
                'addr:street': u'Fresh Pond Road',
                'amenity': u'studio',
                'name': u'Radio Maria',
                'phone': u'+1-718-417-0550',
                'source': u'openstreetmap.org',
                'studio': u'radio',
                'website': u'https://radiomaria.us/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5612341325,
                'kind': u'studio',
                'kind_detail': u'radio',
            })

    def test_television_studio_node(self):
        import dsl

        z, x, y = (16, 18953, 24511)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4921453835
            dsl.point(4921453835, (-75.884371, 41.245585), {
                'amenity': u'studio',
                'name': u'WYOU',
                'source': u'openstreetmap.org',
                'studio': u'television',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4921453835,
                'kind': u'studio',
                'kind_detail': u'television',
            })

    def test_audio_studio_node(self):
        import dsl

        z, x, y = (16, 19311, 24642)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5627007064
            dsl.point(5627007064, (-73.920193, 40.704739), {
                'addr:housenumber': u'10-80',
                'addr:street': u'Wyckoff Avenue',
                'amenity': u'studio',
                'email': u'info@fontanezrecording.com',
                'name': u'Fontanez Recording Studio NYC',
                'opening_hours': u'Mo, We 17:00-22:00; Fr 17:00-00:00; ' \
                u'Sa 00:00-00:00; Su 06:00-00:00',
                'phone': u'+1-508-425-7201',
                'source': u'openstreetmap.org',
                'studio': u'audio',
                'website': u'https://fontanezrecording.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5627007064,
                'kind': u'studio',
                'kind_detail': u'audio',
            })

    def test_video_studio_node(self):
        import dsl

        z, x, y = (16, 19310, 24641)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5679696984
            dsl.point(5679696984, (-73.924722, 40.708785), {
                'addr:housenumber': u'592',
                'addr:street': u'Johnson Avenue',
                'amenity': u'studio',
                'email': u'the1896@gmail.com',
                'name': u'The 1896',
                'opening_hours': u'Mo-Fr 10:00-18:00',
                'phone': u'+1-718-451-6531',
                'source': u'openstreetmap.org',
                'studio': u'video',
                'website': u'http://the1896.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5679696984,
                'kind': u'studio',
                'kind_detail': u'video',
            })

    def test_cinema_studio_node(self):
        import dsl

        z, x, y = (16, 33204, 22557)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2639428572
            dsl.point(2639428572, (2.395709, 48.816451), {
                'addr:city': u'Ivry-sur-Seine',
                'addr:housenumber': u'29B',
                'addr:postcode': u'94200',
                'addr:street': u'Rue Jean-Jacques Rousseau',
                'amenity': u'studio',
                'email': u'contact@studio-kremlin.com',
                'name': u'Studio Kremlin',
                'phone': u'+33 1 78 13 31 07',
                'source': u'openstreetmap.org',
                'studio': u'cinema',
                'website': u'http://studio-kremlin.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2639428572,
                'kind': u'studio',
                'kind_detail': u'cinema',
            })

    def test_photographer_node(self):
        import dsl

        z, x, y = (16, 15151, 23953)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4923076656
            dsl.point(4923076656, (-96.772852, 43.511553), {
                'craft': u'photographer',
                'name': u'JCPenney Portrait Studio',
                'operator': u'JCPenney',
                'source': u'openstreetmap.org',
                'studio': u'photography',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4923076656,
                'kind': u'photographer',
            })

    def test_photography_studio_node(self):
        import dsl

        z, x, y = (16, 32547, 21370)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2442724914
            dsl.point(2442724914, (-1.213013, 52.928762), {
                'addr:city': u'Nottingham',
                'addr:flats': u'Upper Floor',
                'addr:housenumber': u'2',
                'addr:postcode': u'NG9 2LG',
                'addr:street': u'Derby Street',
                'amenity': u'studio',
                'entrance': u'yes',
                'name': u'The Flour Mill Studio',
                'old_name': u'Phenoptix',
                'source': u'openstreetmap.org',
                'studio': u'photography',
                'website': u'http://www.flourmill.studio/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2442724914,
                'kind': u'studio',
                'kind_detail': u'photography',
            })

    def test_tyres_node(self):
        # i'm surprised there aren't more shop=tires, but there are only 5 -
        # compared with about 13.6k for shop=tyres. i guess there's someone
        # (or a bot) cleaning them up.
        import dsl

        z, x, y = (16, 19298, 24650)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5642678604
            dsl.point(5642678604, (-73.991332, 40.671320), {
                'name': u'AM Tire Shop',
                'phone': u'+1 347 520 4119',
                'shop': u'tyres',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5642678604,
                'kind': u'tyres',
            })

    def test_tyres_way(self):
        import dsl

        z, x, y = (16, 19288, 24629)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/553124856
            dsl.way(553124856, dsl.tile_box(z, x, y), {
                'addr:city': u'Union City',
                'addr:housenumber': u'408',
                'addr:postcode': u'07087',
                'addr:state': u'NJ',
                'addr:street': u'Paterson Plank Road',
                'building': u'yes',
                'name': u'Marco\'s& Son Tires',
                'shop': u'tyres',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 553124856,
                'kind': u'tyres',
            })

    def test_ruins_node(self):
        import dsl

        z, x, y = (16, 20692, 35974)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2251296242
            dsl.point(2251296242, (-66.332562, -17.344941), {
                # real feature has the tag 'disused': u'yes', but we want to
                # test the "ruins" processing, so ignore it here. it's tested
                # below.
                'man_made': u'watermill',
                'name': u'Molino 1',
                'ruins': u'yes',
                'source': u'openstreetmap.org',
                'tourism': u'attraction',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2251296242,
                'kind': u'ruins',
                'kind_detail': 'watermill',
            })

    def test_ruins_disused_node(self):
        import dsl

        z, x, y = (16, 20692, 35974)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2251296242
            dsl.point(2251296242, (-66.332562, -17.344941), {
                'disused': u'yes',
                'man_made': u'watermill',
                'name': u'Molino 1',
                'ruins': u'yes',
                'source': u'openstreetmap.org',
                'tourism': u'attraction',
            }),
        )

        # because disused=yes, don't show this at all.
        self.assert_no_matching_feature(
            z, x, y, 'pois', {
                'id': 2251296242,
            })

    def test_disused_watermill_node(self):
        import dsl

        z, x, y = (16, 31350, 24995)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5168606282
            dsl.point(5168606282, (-7.785627, 39.218363), {
                'man_made': u'watermill',
                'source': u'openstreetmap.org',
                'watermill:disused': u'yes',
            }),
        )

        # shouldn't output disused watermills
        self.assert_no_matching_feature(
            z, x, y, 'pois', {
                'id': 5168606282,
            })

    def test_abandoned_watermill_node(self):
        import dsl

        z, x, y = (16, 35192, 21852)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/292797056
            dsl.point(292797056, (13.319711, 51.301431), {
                'abandoned:man_made': u'watermill',
                'addr:city': u'Riesa',
                'addr:country': u'DE',
                'addr:housenumber': u'54',
                'addr:street': u'Großenhainer Straße',
                'description': u'Röhrborn-Mühle (Brückenmühle), ' \
                u'Großenhainer Straße 54 in Riesa',
                'heritage': u'yes',
                'heritage:operator': u'lfd',
                'image': u'https://commons.wikimedia.org/wiki/' \
                u'File%3ARiesa_Roehrborn-Muehle.jpg',
                'lfd:criteria': u'Baudenkmal',
                'man_made': u'watermill',
                'name': u'Röhrborn-Mühle',
                'old_name': u'Brückenmühle',
                'ref:lfd': u'09271356',
                'source': u'openstreetmap.org',
            }),
        )

        # don't output abandoned watermills
        self.assert_no_matching_feature(
            z, x, y, 'pois', {
                'id': 292797056,
            })

    def test_well_drinkable_pump_unknown(self):
        import dsl

        z, x, y = (16, 18406, 23509)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2944866554
            dsl.point(2944866554, (-78.892701, 45.252528), {
                'drinking_water': u'yes',
                'man_made': u'water_well',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2944866554,
                'kind': u'water_well',
                'kind_detail': u'drinkable',
            })

    def test_well_not_drinkable_pump_unknown(self):
        import dsl

        z, x, y = (16, 19787, 24199)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3149670266
            dsl.point(3149670266, (-71.304862, 42.523910), {
                'drinking_water': u'no',
                'man_made': u'water_well',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3149670266,
                'kind': u'water_well',
                'kind_detail': u'not_drinkable',
            })

    def test_shop_fallback_node(self):
        import dsl

        z, x, y = (16, 19297, 24646)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2549967219
            dsl.point(2549967219, (-73.994662, 40.685270), {
                'addr:housenumber': u'254',
                'addr:postcode': u'11231',
                'addr:street': u'Court Street',
                'name': u'American Beer Distributing Co.',
                'shop': u'beverages',
                'source': u'openstreetmap.org',
            }),
        )

        # currently we don't break out shop=beverages as a separate kind, so
        # this triggers the fallback to the generic shop kind.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2549967219,
                'kind': u'shop',
            })

    def test_shop_fallback_way(self):
        import dsl

        z, x, y = (16, 19303, 24648)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/265733688
            dsl.way(265733688, dsl.tile_box(z, x, y), {
                'addr:housenumber': u'648',
                'addr:postcode': u'11238',
                'addr:street': u'Washington Avenue',
                'building': u'yes',
                'height': u'11.5',
                'name': u'Prospect Heights Beer Works',
                'nycdoitt:bin': u'3027946',
                'shop': u'beverages',
                'source': u'openstreetmap.org',
            }),
        )

        # currently we don't break out shop=beverages as a separate kind, so
        # this triggers the fallback to the generic shop kind.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 265733688,
                'kind': u'shop',
            })

    def test_shop_yes_node(self):
        import dsl

        z, x, y = (16, 19298, 24646)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3781172742
            dsl.point(3781172742, (-73.991079, 40.686835), {
                'addr:city': u'Brooklyn',
                'addr:housenumber': u'64',
                'addr:postcode': u'11201',
                'addr:state': u'NY',
                'addr:street': u'Bergen Street',
                'name': u'Homage Skate Shop',
                'shop': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        # when we have the shop=yes tag, we fall back to the generic shop kind.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3781172742,
                'kind': u'shop',
            })

    def test_shop_yes_way(self):
        import dsl

        z, x, y = (16, 19288, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/515962755
            dsl.way(515962755, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'name': u'Audio Tour Pavilion',
                'shop': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        # when we have the shop=yes tag, we fall back to the generic shop kind.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 515962755,
                'kind': u'shop',
            })

    def test_office_fallback_node(self):
        import dsl

        z, x, y = (16, 19312, 24637)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5344121866
            dsl.point(5344121866, (-73.912454, 40.725519), {
                'addr:housenumber': u'55-60',
                'addr:street': u'58th Street',
                'name': u'Petro Home Services',
                'office': u'energy_supplier',
                'phone': u'+1-718-354-3804',
                'source': u'openstreetmap.org',
                'website': u'www.petro.com',
            }),
        )

        # we don't currently break out office=energy_supplier separately, so it
        # gets the generic fallback.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5344121866,
                'kind': u'office',
            })

    def test_office_fallback_way(self):
        import dsl

        z, x, y = (16, 18572, 24941)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/239373623
            dsl.way(239373623, dsl.tile_box(z, x, y), {
                'addr:city': u'Martinsburg',
                'addr:housenumber': u'901',
                'addr:postcode': u'25401',
                'addr:state': u'WV',
                'addr:street': u'Wilson Street',
                'building': u'yes',
                'name': u'FIRSTENERGY',
                'office': u'energy_supplier',
                'source': u'openstreetmap.org',
            }),
        )

        # we don't currently break out office=energy_supplier separately, so it
        # gets the generic fallback.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 239373623,
                'kind': u'office',
            })

    def test_office_yes_node(self):
        import dsl

        z, x, y = (16, 19300, 24649)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5633395353
            dsl.point(5633395353, (-73.980805, 40.675520), {
                'name': u'Fil Doux Textiles',
                'office': u'yes',
                'phone': u'+1 212 202 1459',
                'source': u'openstreetmap.org',
                'website': u'https://fildoux.com',
            }),
        )

        # generic office=yes => generic kind:office
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5633395353,
                'kind': u'office',
            })

    def test_office_yes_way(self):
        import dsl

        z, x, y = (16, 19299, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/250369751
            dsl.way(250369751, dsl.tile_box(z, x, y), {
                'addr:city': u'Brooklyn',
                'addr:housenumber': u'2',
                'addr:postcode': u'11201',
                'addr:state': u'NY',
                'addr:street': u'MetroTech',
                'alt_name': u'2 MetroTech Center',
                'building': u'school',
                'height': u'57.5',
                'layer': u'1',
                'name': u'2 MetroTech Center',
                'nycdoitt:bin': u'3255603',
                'office': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        # generic office=yes => generic kind:office
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 250369751,
                'kind': u'office',
            })

    def test_industrial_factory_node(self):
        import dsl

        z, x, y = (16, 18807, 24829)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2632929388
            dsl.point(2632929388, (-76.685326, 39.921063), {
                'addr:city': u'York',
                'addr:housenumber': u'2315',
                'addr:postcode': u'17402',
                'addr:state': u'PA',
                'addr:street': u'South Queen Street',
                'building': u'factory',
                'description': u'Custom Electronic Assembly',
                'industrial': u'factory',
                'name': u'Keystone Electronics Inc.',
                'phone': u'+1-717-747-5900',
                'source': u'openstreetmap.org',
                'website': u'http://keyelectron.com/',
            }),
        )

        # we don't currently break out a separate kind for industrial=factory,
        # so it gets the generic fallback.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2632929388,
                'kind': u'industrial',
            })

    def test_industrial_factory_way(self):
        import dsl

        z, x, y = (16, 19286, 24611)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/475766379
            dsl.way(475766379, dsl.tile_box(z, x, y), {
                'building': u'industrial',
                'industrial': u'factory',
                'name': u'Coca-Cola Bottling Co',
                'source': u'openstreetmap.org',
            }),
        )

        # we don't currently break out a separate kind for industrial=factory,
        # so it gets the generic fallback.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 475766379,
                'kind': u'industrial',
            })

    def test_industrial_yes_way(self):
        # couldn't find an industrial=yes, so this is a wholly synthetic test.
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'industrial': u'yes',
                'name': u'Something industrial',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1,
                'kind': u'industrial',
            })
