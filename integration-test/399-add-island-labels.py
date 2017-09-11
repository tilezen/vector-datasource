from . import OsmFixtureTest


class AddIslandLabels(OsmFixtureTest):
    def test_ne_land_110m(self):
        # Natural Earth 110m
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_110m_land/399-ne_110m_land.shp',
        ])

        self.assert_has_feature(
            1, 0, 0, 'earth',
            {'kind': 'earth', 'source': 'naturalearthdata.com'})

    def test_ne_land_50m(self):
        # Natural Earth 50m
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_50m_land/399-ne_50m_land.shp',
        ])

        self.assert_has_feature(
            2, 0, 1, 'earth',
            {'kind': 'earth', 'source': 'naturalearthdata.com'})

    def test_ne_land_10m(self):
        # Natural Earth 10m
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_land/399-ne_10m_land.shp',
        ])

        self.assert_has_feature(
            7, 20, 49, 'earth',
            {'kind': 'earth', 'source': 'naturalearthdata.com'})

    def test_openstreetmapdata_land(self):
        # OSM derived data from openstreetmapdata.com
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'land_polygons/399-earth-fixture.shp',
        ])

        self.assert_has_feature(
            8, 40, 98, 'earth',
            {'kind': 'earth', 'source': 'openstreetmapdata.com'})

    def test_osm_continent_label(self):
        # NODE continent labels (from places)
        self.load_fixtures(['http://www.openstreetmap.org/node/36966063'])

        self.assert_has_feature(
            1, 0, 0, 'earth',
            {'kind': 'continent', 'label_placement': True,
             'name': 'North America'})

    def test_osm_archipelago_label(self):
        # NODE archipelago labels (from place nodes)
        self.load_fixtures(['http://www.openstreetmap.org/node/3860848374'])

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
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/6722301'
        ], simplify=100)

        self.assert_has_feature(
            15, 9367, 12534, 'earth',
            {'kind': 'archipelago', 'label_placement': True, 'min_zoom': 15,
             'name': 'Three Sisters Islands'})

    def test_osm_small_archipelago_label(self):
        # SMALL archipelago labels (from place polygons)
        # Really these should be lines, but will initially be points
        # In Europe, with a name, is exported
        self.load_fixtures(['http://www.openstreetmap.org/way/395338481'])

        self.assert_has_feature(
            15, 18647, 9497, 'earth',
            {'kind': 'archipelago', 'label_placement': True,
             'name': 'Louekrinpaadet'})

    def test_island_label_yerba_buena(self):
        # NODE island labels (from place nodes)
        # Yerba Buena Island, near SF
        self.load_fixtures(['http://www.openstreetmap.org/node/358796350'])

        self.assert_has_feature(
            15, 5245, 12661, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Yerba Buena Island'})

    def test_island_label_bird_island(self):
        # NODE island labels (from place nodes)
        # Bird Island, north of SF
        self.load_fixtures(['http://www.openstreetmap.org/node/358761955'])

        self.assert_has_feature(
            15, 5230, 12659, 'earth',
            {'kind': 'island', 'label_placement': True, 'name': 'Bird Island'})

    def test_island_label_kent_island(self):
        # NODE island labels (from place nodes)
        # http://www.openstreetmap.org/node/358768646
        # Kent Island, north of SF
        self.load_fixtures(['http://www.openstreetmap.org/node/358768646'])

        self.assert_has_feature(
            15, 5217, 12649, 'earth',
            {'kind': 'island', 'label_placement': True, 'name': 'Kent Island'})

    def test_large_island_label_polygon_manitoulin(self):
        # LARGE island labels (from place polygons)
        # Manitoulin Island, Canada
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/4227580',
        ], simplify=100)

        self.assert_has_feature(
            7, 34, 45, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Manitoulin Island'})

    def test_large_island_label_polygon_trinidad(self):
        # LARGE island labels (from place polygons)
        # Trinidad, the island of the nation
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/5176042',
        ], simplify=100)

        self.assert_has_feature(
            7, 42, 60, 'earth',
            {'kind': 'island', 'label_placement': True, 'name': 'Trinidad'})

    def test_medium_island_label_polygon_cockburn(self):
        # MEDIUM island labels (from place polygons)
        # Cockburn Island, Canada
        self.load_fixtures([
            'http://www.openstreetmap.org/way/124916662',
        ], simplify=100)

        self.assert_has_feature(
            9, 137, 182, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Cockburn Island'})

    def test_medium_island_label_polygon_san_miguel(self):
        # MEDIUM island labels (from place polygons)
        # San Miguel Island, California
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/7117158',
        ], simplify=100)

        self.assert_has_feature(
            10, 169, 408, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'San Miguel Island'})

    def test_medium_island_label_polygon_west_anacapa(self):
        # MEDIUM island labels (from place polygons)
        # West Anacapa Island, California
        self.load_fixtures([
            'http://www.openstreetmap.org/way/40500922',
        ], simplify=100)

        self.assert_has_feature(
            12, 689, 1636, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'West Anacapa Island'})

    def test_medium_island_label_polygon_angel(self):
        # MEDIUM island labels (from place polygons)
        # Angel Island, near SF
        # 12, 654, 1581
        self.load_fixtures([
            'http://www.openstreetmap.org/way/157429145',
        ], simplify=100)

        self.assert_has_feature(
            12, 654, 1581, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Angel Island'})

    def test_small_island_label_polygon_great_gull(self):
        # SMALL island labels (from place polygons)
        # Great Gull Island, NY state
        self.load_fixtures(['http://www.openstreetmap.org/way/22693068'])

        self.assert_has_feature(
            15, 9819, 12261, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Great Gull Island'})

    def test_small_island_label_polygon_goose(self):
        # SMALL island labels (from place polygons)
        # Goose Island, NY state
        self.load_fixtures(['http://www.openstreetmap.org/way/308262375'])

        self.assert_has_feature(
            16, 19659, 24507, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Goose Island'})

    def test_small_island_label_polygon_rincon(self):
        # SMALL island labels (from place polygons)
        # Rincon Island, California
        self.load_fixtures(['http://www.openstreetmap.org/way/37248735'])

        self.assert_has_feature(
            16, 11023, 26103, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Rincon Island'})

    def test_islet_node(self):
        # NODE islet labels (from place nodes)
        # Pyramid Rock, SF
        self.load_fixtures(['http://www.openstreetmap.org/node/358795646'])

        self.assert_has_feature(
            16, 10466, 25327, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Pyramid Rock', 'min_zoom': 17})

    def test_large_islet_polygon_sugarloaf(self):
        # LARGE islet labels (from place polygons)
        # Sugarloaf Island, west of SF
        # 15, 5188, 12673
        self.load_fixtures(['http://www.openstreetmap.org/way/40500803'])

        self.assert_has_feature(
            15, 5188, 12673, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Sugarloaf Island'})

    def test_large_islet_polygon_alcatraz(self):
        # LARGE islet labels (from place polygons)
        # Alcatraz Island, near SF
        self.load_fixtures(['http://www.openstreetmap.org/way/24433344'])

        self.assert_has_feature(
            15, 5240, 12659, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Alcatraz Island'})

    def test_medium_islet_polygon_bird(self):
        # MEDIUM islet labels (from place polygons)
        # Bird Island, west of SF
        self.load_fixtures(['http://www.openstreetmap.org/way/157449982'])

        self.assert_has_feature(
            16, 10493, 25303, 'earth',
            {'kind': 'islet', 'label_placement': True, 'name': 'Bird Island'})

    def test_small_islet_polygon_sail_rock(self):
        # SMALL islet labels (from place polygons)
        # Sail Rock, near SF
        self.load_fixtures(['http://www.openstreetmap.org/way/306344403'])

        self.assert_has_feature(
            16, 10467, 25395, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Sail Rock', 'min_zoom': 17})

    def test_small_islet_polygon_little_mile_rock(self):
        # SMALL islet labels (from place polygons)
        # Little Mile Rock, SF
        self.load_fixtures(['http://www.openstreetmap.org/way/32289183'])

        self.assert_has_feature(
            16, 10465, 25326, 'earth',
            {'kind': 'islet', 'label_placement': True,
             'name': 'Little Mile Rock', 'min_zoom': 17})

    def test_island_should_only_get_one_label_placement(self):
        # island polygon split across multiple tiles shouldn't get a label
        # placement in each tile, only one.
        # Treasure Island, San Francisco
        self.load_fixtures(['http://www.openstreetmap.org/way/26767313'])

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
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/5344925',
        ], simplify=100)

        self.assert_has_feature(
            15, 6773, 14457, 'earth',
            {'kind': 'island', 'label_placement': True,
             'name': 'Islas Marietas'})
