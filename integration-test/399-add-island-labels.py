# -*- encoding: utf-8 -*-
import dsl
from . import FixtureTest


class AddIslandLabels(FixtureTest):
    def test_ne_land_110m(self):
        # Natural Earth 110m
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(1, 0, 0), {
                u'source': u'naturalearthdata.com',
                u'featurecla': u'Country',
                u'scalerank': 1,
                u'min_zoom': 0,
            }))

        self.assert_has_feature(
            1, 0, 0, 'earth',
            {'kind': 'earth', 'source': 'naturalearthdata.com'})

    def test_ne_land_50m(self):
        # Natural Earth 50m
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(2, 0, 1), {
                u'source': u'naturalearthdata.com',
                u'featurecla': u'Land',
                u'scalerank': 0,
                u'min_zoom': 0,
            }))

        self.assert_has_feature(
            2, 0, 1, 'earth',
            {'kind': 'earth', 'source': 'naturalearthdata.com'})

    def test_ne_land_10m(self):
        # Natural Earth 10m
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(7, 20, 49), {
                u'source': u'naturalearthdata.com',
                u'featurecla': u'Land',
                u'scalerank': 0,
                u'min_zoom': 0,
            }),
            dsl.way(2, dsl.tile_box(0, 0, 0), {
                u'source': u'naturalearthdata.com',
                u'featurecla': u'Land',
                u'scalerank': 0,
                u'min_zoom': 0,
            }),
        )

        self.assert_has_feature(
            7, 20, 49, 'earth',
            {'kind': 'earth', 'source': 'naturalearthdata.com'})

    def test_openstreetmapdata_land(self):
        # OSM derived data from osmdata.openstreetmap.de
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(8, 40, 98), {
                u'source': u'osmdata.openstreetmap.de',
                u'fid': 35442,
            }),
        )

        self.assert_has_feature(
            8, 40, 98, 'earth',
            {'kind': 'earth', 'source': 'osmdata.openstreetmap.de'})

    def test_osm_continent_label(self):
        # NODE continent labels (from places)
        self.generate_fixtures(
            dsl.way(36966063, dsl.tile_box(1, 0, 0), {
                u'name': u'North America',
                u'place': u'continent',
                u'population': u'528720588',
                u'source': u'openstreetmap.org',
                u'sqkm': u'24709000',
                u'wikidata': u'Q49',
                u'wikipedia': u'en:North America',
            }))

        self.assert_has_feature(
            1, 0, 0, 'earth',
            {'kind': 'continent', 'label_placement': True,
             'name': 'North America'})

    def test_osm_archipelago_label(self):
        # NODE archipelago labels (from place nodes)
        self.generate_fixtures(
            dsl.way(3860848374, dsl.tile_box(15, 10817, 11412), {
                u'name:en': u'Bird Rocks',
                u'name': u'Rochers aux Oiseaux',
                u'wikipedia': u'fr:Rochers aux Oiseaux',
                u'source': u'openstreetmap.org',
                u'name:fr': u'Rochers aux Oiseaux',
                u'place': u'archipelago',
                u'wikidata': u'Q3437623'}))

        self.assert_has_feature(
            15, 10817, 11412, 'earth',
            {'kind': 'archipelago', 'label_placement': True, 'min_zoom': 15,
             'name': 'Rochers aux Oiseaux'})

    # LARGE archipelago labels (from place polygons)
    # There aren't any today
    # Really these should be lines, but will initially be points

    def test_osm_medium_archipelago_label(self):
        # MEDIUM archipelago labels (from place polygons)
        # Really these should be lines, but will initially be points
        self.generate_fixtures(
            dsl.way(-6722301, dsl.tile_box(15, 9367, 12534), {
                u'gnis:state_id': u'11',
                u'name': u'Three Sisters Islands',
                u'way_area': u'152.404',
                u'gnis:county_id': u'001',
                u'ele': u'2',
                u'source': u'openstreetmap.org',
                u'place': u'archipelago',
                u'gnis:created': u'12/18/1979',
                u'gnis:feature_id': u'528687',
                u'name:hu': u'Three Sisters Islands',
            }),
        )

        self.assert_has_feature(
            15, 9367, 12534, 'earth',
            {'kind': 'archipelago', 'label_placement': True, 'min_zoom': 15,
             'name': 'Three Sisters Islands'})

    def test_osm_small_archipelago_label(self):
        # SMALL archipelago labels (from place polygons)
        # Really these should be lines, but will initially be points
        # In Europe, with a name, is exported
        self.generate_fixtures(
            dsl.way(395338481, dsl.tile_box(15, 18647, 9497), {
                u'source': u'openstreetmap.org',
                u'way_area': u'131979',
                u'place': u'archipelago',
                u'name': u'Louekrinpaadet',
            }))

        self.assert_has_feature(
            15, 18647, 9497, 'earth',
            {'kind': 'archipelago', 'label_placement': True,
             'name': 'Louekrinpaadet'})

    def test_island_label_yerba_buena(self):
        # NODE island labels (from place nodes)
        # Yerba Buena Island, near SF
        self.generate_fixtures(
            dsl.way(358796350, dsl.tile_box(15, 5245, 12661), {
                u'gnis:state_id': u'06',
                u'name': u'Yerba Buena Island',
                u'gnis:county_id': u'075',
                u'ele': u'98',
                u'source': u'openstreetmap.org',
                u'place': u'island',
                u'gnis:created': u'01/19/1981',
                u'gnis:feature_id': u'255246',
            }))

        self.assert_has_feature(
            15, 5245, 12661, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Yerba Buena Island'})

    def test_island_label_bird_island(self):
        # NODE island labels (from place nodes)
        # Bird Island, north of SF
        self.generate_fixtures(
            dsl.way(358761955, dsl.tile_box(15, 5230, 12659), {
                u'gnis:state_id': u'06',
                u'name': u'Bird Island',
                u'gnis:county_id': u'041',
                u'ele': u'13',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q2904412',
                u'place': u'island',
                u'gnis:created': u'01/19/1981',
                u'gnis:feature_id': u'219312',
            }))

        self.assert_has_feature(
            15, 5230, 12659, 'earth',
            {'kind': 'island', 'label_placement': True, 'name': 'Bird Island'})

    def test_island_label_kent_island(self):
        # NODE island labels (from place nodes)
        # http://www.openstreetmap.org/node/358768646
        # Kent Island, north of SF
        self.generate_fixtures(
            dsl.way(358768646, dsl.tile_box(15, 5217, 12649), {
                u'gnis:state_id': u'06',
                u'name': u'Kent Island',
                u'gnis:county_id': u'041',
                u'ele': u'2',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q6391792',
                u'place': u'island',
                u'gnis:created': u'01/19/1981',
                u'gnis:feature_id': u'226520',
            }))

        self.assert_has_feature(
            15, 5217, 12649, 'earth',
            {'kind': 'island', 'label_placement': True, 'name': 'Kent Island'})

    def test_large_island_label_polygon_manitoulin(self):
        # LARGE island labels (from place polygons)
        # Manitoulin Island, Canada
        self.generate_fixtures(
            dsl.way(1291715736, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'leisure': u'slipway',
            }),
            dsl.way(1292498026, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'leisure': u'slipway',
            }),
            dsl.way(1388979110, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'leisure': u'slipway',
            }),
            dsl.way(1388981959, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'leisure': u'slipway',
            }),
            dsl.way(1390370546, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'leisure': u'slipway',
            }),
            dsl.way(3692917366, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'leisure': u'slipway',
            }),
            dsl.way(3769817229, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'leisure': u'slipway',
            }),
            dsl.way(-4227580, dsl.tile_box(7, 34, 45), {
                u'name': u'Manitoulin Island',
                u'way_area': u'5.73809e+09',
                u'wikipedia': u'en:Manitoulin Island',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q654405',
                u'place': u'island',
            }))

        self.assert_has_feature(
            7, 34, 45, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Manitoulin Island'})

    def test_large_island_label_polygon_trinidad(self):
        # LARGE island labels (from place polygons)
        # Trinidad, the island of the nation
        self.generate_fixtures(
            dsl.way(108502504, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'045 (21-FEB-16 20:50:18)',
            }),
            dsl.way(109207429, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'amenity': u'ferry_terminal',
                u'name': u'Chaguaramas',
            }),
            dsl.way(4153664406, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'001 (21-FEB-16 20:26:44)',
            }),
            dsl.way(4153664426, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'021 (21-FEB-16 20:35:41)',
            }),
            dsl.way(4153664437, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'028 (21-FEB-16 20:20:45)',
            }),
            dsl.way(4153664439, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'029 (21-FEB-16 20:21:45)',
            }),
            dsl.way(4153664441, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'030 (21-FEB-16 20:22:16)',
            }),
            dsl.way(4153664442, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'030 (21-FEB-16 20:42:49)',
            }),
            dsl.way(4153664443, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'031 (21-FEB-16 20:22:57)',
            }),
            dsl.way(4153664446, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'033 (21-FEB-16 20:25:35);032 (21-FEB-16 20:24:43)',
            }),
            dsl.way(4153664447, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'034 (21-FEB-16 20:25:52)',
            }),
            dsl.way(4153664449, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'035 (21-FEB-16 20:26:17)',
            }),
            dsl.way(4153664450, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'035 (21-FEB-16 20:44:08)',
            }),
            dsl.way(4153664451, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'036 (21-FEB-16 20:26:39)',
            }),
            dsl.way(4153664452, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'036 (21-FEB-16 20:46:18)',
            }),
            dsl.way(4153664453, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'037 (21-FEB-16 20:26:55)',
            }),
            dsl.way(4153664455, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'038 (21-FEB-16 20:27:31)',
            }),
            dsl.way(4153664457, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'039 (21-FEB-16 20:27:40)',
            }),
            dsl.way(4153664458, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'039 (21-FEB-16 20:47:25)',
            }),
            dsl.way(4153664459, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'040 (21-FEB-16 20:27:56)',
            }),
            dsl.way(4153664461, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'041 (21-FEB-16 20:28:19)',
            }),
            dsl.way(4153664462, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'041 (21-FEB-16 20:47:52)',
            }),
            dsl.way(4153664463, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'042 (21-FEB-16 20:28:35)',
            }),
            dsl.way(4153664464, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'042 (21-FEB-16 20:48:37)',
            }),
            dsl.way(4153664466, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'043 (21-FEB-16 20:49:10)',
            }),
            dsl.way(4153664468, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'044 (21-FEB-16 20:49:59)',
            }),
            dsl.way(4153664469, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'045 (21-FEB-16 20:29:49);020 (21-FEB-16 20:35:30)',
            }),
            dsl.way(4153664472, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'131 (21-FEB-16 20:26:03)',
            }),
            dsl.way(4153664473, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'132 (21-FEB-16 20:26:58)',
            }),
            dsl.way(4153664474, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'133 (21-FEB-16 20:28:42)',
            }),
            dsl.way(4153664475, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'134 (21-FEB-16 20:30:53)',
            }),
            dsl.way(4153664476, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'135 (21-FEB-16 20:33:09)',
            }),
            dsl.way(4153664477, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'136 (21-FEB-16 20:35:55)',
            }),
            dsl.way(4153664479, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'138 (21-FEB-16 20:41:16)',
            }),
            dsl.way(4153664480, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'139 (21-FEB-16 20:43:14)',
            }),
            dsl.way(4153664481, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'140 (21-FEB-16 20:43:55)',
            }),
            dsl.way(4153664482, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'141 (21-FEB-16 20:45:02)',
            }),
            dsl.way(4153664483, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'amenity': u'shelter',
                u'name': u'142 (21-FEB-16 20:47:29)',
            }),
            dsl.way(4160979594, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'029 (21-FEB-16 20:42:03)',
            }),
            dsl.way(4160979598, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'019 (21-FEB-16 20:35:08)',
            }),
            dsl.way(503798550, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798549, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798548, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798547, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798546, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798537, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798534, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798533, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798532, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798531, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(503798530, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(414317527, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(503798529, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(503798528, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(503798527, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(503798526, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(503798525, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(503798524, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(503798523, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(503798518, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(414192850, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'name': u'Paria Bay K\xfcstenlinie',
                u'area': u'yes',
            }),
            dsl.way(103455735, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(95446422, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(95446414, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(95446409, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(15803357, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12198328, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12196838, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(12196628, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(12196093, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12195974, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12195229, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12195077, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(12194398, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12193282, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12188831, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12192990, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12190794, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12186656, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12183090, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12182984, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12181634, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(12181592, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(12181239, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(12181064, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12176487, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12174244, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12172532, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12171115, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12169853, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12169025, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(12169005, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12168352, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'area': u'yes',
            }),
            dsl.way(12167998, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(12167711, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'is_in:country': u'Trinidad and Tobago',
                u'converted_by': u'mikes',
                u'area': u'yes',
            }),
            dsl.way(-5176042, dsl.tile_box(7, 42, 60), {
                u'name': u'Trinidad',
                u'way_area': u'5.02427e+09',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q128323',
                u'place': u'island',
                u'population': u'1259822',
            }))

        self.assert_has_feature(
            7, 42, 60, 'earth',
            {'kind': 'island', 'label_placement': True, 'name': 'Trinidad'})

    def test_medium_island_label_polygon_cockburn(self):
        # MEDIUM island labels (from place polygons)
        # Cockburn Island, Canada
        self.generate_fixtures(
            dsl.way(124916662, dsl.tile_box(9, 137, 182), {
                u'source': u'openstreetmap.org',
                u'way_area': u'3.52545e+08',
                u'place': u'island',
                u'name': u'Cockburn Island',
            }))

        self.assert_has_feature(
            9, 137, 182, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Cockburn Island'})

    def test_medium_island_label_polygon_san_miguel(self):
        # MEDIUM island labels (from place polygons)
        # San Miguel Island, California
        self.generate_fixtures(
            dsl.way(-7117158, dsl.tile_box(10, 169, 408), {
                u'attribution': u'CASIL cnty24k09_1_poly.shp',
                u'name': u'San Miguel Island',
                u'way_area': u'5.58819e+07',
                u'wikipedia': u'en:San Miguel Island',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q1348353',
                u'nist:fips_code': u'083',
                u'place': u'island',
                u'is_in': u'Santa Barbara County',
            }))

        self.assert_has_feature(
            10, 169, 408, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'San Miguel Island'})

    def test_medium_island_label_polygon_west_anacapa(self):
        # MEDIUM island labels (from place polygons)
        # West Anacapa Island, California
        self.generate_fixtures(
            dsl.way(40500922, dsl.tile_box(12, 689, 1636), {
                u'attribution': u'CASIL cnty24k09_1_poly.shp',
                u'name': u'West Anacapa Island',
                u'area': u'yes',
                u'way_area': u'2.6511e+06',
                u'source': u'openstreetmap.org',
                u'place': u'island',
            }))

        self.assert_has_feature(
            12, 689, 1636, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'West Anacapa Island'})

    def test_medium_island_label_polygon_angel(self):
        # MEDIUM island labels (from place polygons)
        # Angel Island, near SF
        # 12, 654, 1581
        self.generate_fixtures(
            dsl.way(157429145, dsl.tile_box(12, 654, 1581), {
                u'gnis:state_id': u'06',
                u'name': u'Angel Island',
                u'area': u'yes',
                u'way_area': u'4.90495e+06',
                u'gnis:county_id': u'041',
                u'ele': u'130',
                u'source': u'openstreetmap.org',
                u'place': u'island',
                u'gnis:created': u'01/19/1981',
                u'wikidata': u'Q531734',
                u'gnis:feature_id': u'218281',
            }))

        self.assert_has_feature(
            12, 654, 1581, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Angel Island'})

    def test_small_island_label_polygon_great_gull(self):
        # SMALL island labels (from place polygons)
        # Great Gull Island, NY state
        self.generate_fixtures(
            dsl.way(22693068, dsl.tile_box(15, 9819, 12261), {
                u'gnis:state_id': u'36',
                u'name': u'Great Gull Island',
                u'area': u'yes',
                u'way_area': u'124363',
                u'wikipedia': u'en:Great Gull Island',
                u'gnis:county_id': u'103',
                u'ele': u'7',
                u'source': u'openstreetmap.org',
                u'place': u'island',
                u'gnis:created': u'01/23/1980',
                u'wikidata': u'Q12059029',
                u'gnis:feature_id': u'951624',
            }))

        self.assert_has_feature(
            15, 9819, 12261, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Great Gull Island'})

    def test_small_island_label_polygon_goose(self):
        # SMALL island labels (from place polygons)
        # Goose Island, NY state
        self.generate_fixtures(
            dsl.way(308262375, dsl.tile_box(16, 19659, 24507), {
                u'name': u'Goose Island',
                u'area': u'yes',
                u'way_area': u'2683.01',
                u'source': u'openstreetmap.org',
                u'place': u'island',
                u'gnis:feature_id': u'951362',
            }))

        self.assert_has_feature(
            16, 19659, 24507, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Goose Island'})

    def test_small_island_label_polygon_rincon(self):
        # SMALL island labels (from place polygons)
        # Rincon Island, California
        self.generate_fixtures(
            dsl.way(37248735, dsl.tile_box(16, 11023, 26103), {
                u'gnis:state_id': u'06',
                u'name': u'Rincon Island',
                u'area': u'yes',
                u'way_area': u'20618.1',
                u'gnis:county_id': u'111',
                u'ele': u'1',
                u'source': u'openstreetmap.org',
                u'place': u'island',
                u'gnis:created': u'12/02/1996',
                u'gnis:feature_id': u'1702937',
                u'description': u'Petroleum installation',
            }))

        self.assert_has_feature(
            16, 11023, 26103, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Rincon Island'})

    def test_islet_node(self):
        # NODE islet labels (from place nodes)
        # Pyramid Rock, SF
        self.generate_fixtures(
            dsl.way(358795646, dsl.tile_centre_shape(16, 10466, 25327), {
                u'gnis:state_id': u'06',
                u'name': u'Pyramid Rock',
                u'gnis:county_id': u'075',
                u'created_by': u'Potlatch 0.10f',
                u'ele': u'4',
                u'source': u'openstreetmap.org',
                u'place': u'islet',
                u'gnis:created': u'01/19/1981',
                u'gnis:feature_id': u'253806',
            }))

        self.assert_has_feature(
            16, 10466, 25327, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Pyramid Rock', 'min_zoom': 17})

    def test_large_islet_polygon_sugarloaf(self):
        # LARGE islet labels (from place polygons)
        # Sugarloaf Island, west of SF
        # 15, 5188, 12673
        self.generate_fixtures(
            dsl.way(40500803, dsl.tile_box(15, 5188, 12673), {
                u'attribution': u'CASIL cnty24k09_1_poly.shp',
                u'name': u'Sugarloaf Island',
                u'area': u'yes',
                u'way_area': u'15116',
                u'source': u'openstreetmap.org',
                u'place': u'islet',
                u'nist:fips_code': u'075',
                u'is_in': u'San Francisco County',
            }))

        self.assert_has_feature(
            15, 5188, 12673, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Sugarloaf Island'})

    def test_large_islet_polygon_alcatraz(self):
        # LARGE islet labels (from place polygons)
        # Alcatraz Island, near SF
        self.generate_fixtures(
            dsl.way(24433344, dsl.tile_box(15, 5240, 12659), {
                u'gnis:state_id': u'06',
                u'name': u'Alcatraz Island',
                u'area': u'yes',
                u'way_area': u'129954',
                u'wikipedia': u'en:Alcatraz Island',
                u'gnis:county_id': u'075',
                u'ele': u'37',
                u'source': u'openstreetmap.org',
                u'place': u'islet',
                u'alt_name': u'Alcatraz',
                u'boundary': u'national_park',
                u'gnis:created': u'01/19/1981',
                u'wikidata': u'Q131354',
                u'gnis:feature_id': u'218080',
            }))

        self.assert_has_feature(
            15, 5240, 12659, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Alcatraz Island'})

    def test_medium_islet_polygon_bird(self):
        # MEDIUM islet labels (from place polygons)
        # Bird Island, west of SF
        self.generate_fixtures(
            dsl.way(157449982, dsl.tile_box(16, 10493, 25303), {
                u'gnis:state_id': u'06',
                u'name': u'Bird Island',
                u'area': u'yes',
                u'way_area': u'1014.28',
                u'gnis:county_id': u'013',
                u'ele': u'0',
                u'source': u'openstreetmap.org',
                u'place': u'islet',
                u'gnis:created': u'01/19/1981',
                u'gnis:feature_id': u'219313',
            }))

        self.assert_has_feature(
            16, 10493, 25303, 'earth',
            {'kind': 'islet', 'label_placement': True, 'name': 'Bird Island'})

    def test_small_islet_polygon_sail_rock(self):
        from shapely.wkt import loads as wkt_loads
        # SMALL islet labels (from place polygons)
        # Sail Rock, near SF
        self.generate_fixtures(
            dsl.way(306344403, wkt_loads("""POLYGON ((
            -122.500536 37.492763,
            -122.500504 37.492799,
            -122.500449 37.492802,
            -122.500431 37.492755,
            -122.500433 37.492726,
            -122.500455 37.492708,
            -122.500527 37.492728,
            -122.500536 37.492763
            ))"""), {
                u'source': u'openstreetmap.org',
                u'way_area': u'115.753',
                u'place': u'islet',
                u'name': u'Sail Rock',
                u'area': u'yes',
            }))

        self.assert_has_feature(
            16, 10467, 25395, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Sail Rock', 'min_zoom': 17})

    def test_small_islet_polygon_little_mile_rock(self):
        from shapely.wkt import loads as wkt_loads
        # SMALL islet labels (from place polygons)
        # Little Mile Rock, SF
        self.generate_fixtures(
            dsl.way(32289183, wkt_loads("""POLYGON ((
            -122.509878 37.792498,
            -122.509865 37.792546,
            -122.509816 37.792555,
            -122.509808 37.792504,
            -122.509849 37.792485,
            -122.509878 37.792498
            ))"""), {
                u'gnis:state_id': u'06',
                u'name': u'Little Mile Rock',
                u'area': u'yes',
                u'way_area': u'54.2306',
                u'gnis:county_id': u'075',
                u'ele': u'0',
                u'source': u'openstreetmap.org',
                u'place': u'islet',
                u'gnis:created': u'01/19/1981',
                u'gnis:feature_id': u'227302',
            }))

        self.assert_has_feature(
            16, 10465, 25326, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Little Mile Rock', 'min_zoom': 17})

    def test_island_should_only_get_one_label_placement(self):
        # island polygon split across multiple tiles shouldn't get a label
        # placement in each tile, only one.
        # Treasure Island, San Francisco
        self.generate_fixtures(
            dsl.way(26767313, dsl.tile_box(14, 2622, 6329), {
                u'name': u'Treasure Island',
                u'way_area': u'2.61873e+06',
                u'wikipedia': u'en:Treasure Island, San Francisco',
                u'name:de': u'Schatzinsel',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q778565',
                u'place': u'island',
            }))

        self.assert_has_feature(
            14, 2622, 6329, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Treasure Island'})

        # neighbouring tiles should not have a placement
        for (x, y) in ((2623, 6329), (2622, 6340), (2623, 6340)):
            self.assert_no_matching_feature(
                14, x, y, 'earth',
                {'kind': 'island', 'label_placement': True,
                 'name': 'Treasure Island'})

    def test_island_multi_polygon(self):
        # multi-polygonal islands
        # Islas Marietas
        # main island should get label
        self.generate_fixtures(
            dsl.way(2942608223, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'natural': u'cave_entrance',
            }),
            dsl.way(317525639, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(22648275, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'area': u'yes',
            }),
            dsl.way(359188602, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'way_area': u'118.33',
                u'area': u'yes',
            }),
            dsl.way(359188596, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'way_area': u'116.613',
                u'area': u'yes',
            }),
            dsl.way(359188594, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'way_area': u'186.304',
                u'area': u'yes',
            }),
            dsl.way(359188588, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'way_area': u'681.532',
                u'area': u'yes',
            }),
            dsl.way(359188586, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'way_area': u'1694.22',
                u'area': u'yes',
            }),
            dsl.way(359188583, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'way_area': u'793.111',
                u'area': u'yes',
            }),
            dsl.way(22648278, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'way_area': u'2747.76',
                u'area': u'yes',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'1694.22',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'793.111',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'681.532',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'186.304',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(22648236, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'area': u'yes',
                u'way_area': u'521377',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'name:it': u'Isole Marieta',
            }),
            dsl.way(22648230, dsl.tile_box(0, 0, 0), {
                u'source': u'openstreetmap.org',
                u'way_area': u'4719.11',
                u'area': u'yes',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'118.33',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'116.613',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'521377',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'385951',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(-5344925, dsl.tile_box(0, 0, 0), {
                u'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'4719.11',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }),
            dsl.way(-5344925, dsl.tile_box(15, 6773, 14457), {
                'name:pt': u'Ilhas Marietas',
                u'name:en': u'Marieta Islands',
                u'name': u'Islas Marietas',
                u'way_area': u'2747.76',
                u'leisure': u'nature_reserve',
                u'source': u'openstreetmap.org',
                u'name:fr': u'\xceles Marieta',
                u'place': u'island',
                u'name:it': u'Isole Marieta',
                u'name:es': u'Islas Marietas',
            }))

        self.assert_has_feature(
            15, 6773, 14457, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Islas Marietas'})
