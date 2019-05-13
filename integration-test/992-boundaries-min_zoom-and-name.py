from . import FixtureTest


class BoundariesMinZoomAndNameNe(FixtureTest):
    # global:
    #   # NOTE: Natural Earth 1:50 million used zooms 0,1,2,3,4
    #   #       and only has USA, Canada, Brazil, and Australia
    #   #       all with scalerank of 2 (a documented NE omission).
    #   #       Then 1:10 million NE is selected at zooms 5, 6, 7
    #   #       and includes most all countries, with various scalerank
    #   #       but is inconsistent with 1:50 in scalerank=2 so countries
    #   #       like Russia will "pop" in at 5, but with min_zoom of 2
    #   #       (and India, China, Indonesia, and South Africa).
    #   - &ne_region_boundaries_min_zoom |
    #       CASE WHEN scalerank =   0 THEN  6.7
    #            WHEN scalerank <=  2 THEN  2
    #            WHEN scalerank <=  3 THEN  3
    #            WHEN scalerank <=  4 THEN  5
    #            WHEN scalerank <=  5 THEN  5.5
    #            WHEN scalerank <=  6 THEN  6
    #            WHEN scalerank <=  7 THEN  6.7
    #            WHEN scalerank <=  8 THEN  6.8
    #            WHEN scalerank <=  9 THEN  7
    #       END

    def test_england_wales_boundary(self):
        # England-Wales boundary in United Kingdom (scalerank=4, 1:10m NE
        # only)
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_admin_0_boundary_lines_map_units/'
            '992-ne_10m_admin_0_boundary_lines_map_units_eng_wales.shp',
        ])

        self.assert_has_feature(
            5, 15, 10, 'boundaries',
            {'kind': 'map_unit', 'min_zoom': 5, 'sort_rank': 258})

    def test_usa_region(self):
        # region min_zoom (via scalerank)
        # USA region (scalerank=2, 1:50m NE and 1:10m NE)
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_admin_1_states_provinces_lines/'
            '992-ne_10m_admin_1_states_provinces_lines-nv-ca-'
            'europe-mexico.shp',
        ])

        self.assert_has_feature(
            2, 0, 1, 'boundaries',
            {'kind': 'region', 'min_zoom': 2})

        # USA region NO name, Natural Earth
        self.assert_has_feature(
            2, 0, 1, 'boundaries',
            {'kind': 'region', 'name': type(None)})

    def test_10m_regions(self):
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_admin_1_states_provinces_lines/'
            '992-ne_10m_admin_1_states_provinces_lines-nv-ca'
            '-europe-mexico.shp',
        ])

        # Germany region (scalerank=3, 1:10m NE only)
        self.assert_has_feature(
            5, 17, 10, 'boundaries',
            {'kind': 'region', 'min_zoom': 3})

        # Germany region NO name, Natural Earth
        self.assert_has_feature(
            5, 17, 10, 'boundaries',
            {'kind': 'region', 'name': type(None)})

        # Mexico region (scalerank=4, 1:10m NE only)
        self.assert_has_feature(
            5, 7, 14, 'boundaries',
            {'kind': 'region', 'min_zoom': 5})

        # Mexico region NO name, Natural Earth
        self.assert_has_feature(
            5, 7, 14, 'boundaries',
            {'kind': 'region', 'name': type(None)})

        # Poland region (scalerank=5, 1:10m NE only)
        self.assert_has_feature(
            5, 17, 10, 'boundaries',
            {'kind': 'region', 'min_zoom': 5.5})

        # Poland region NO name, Natural Earth
        self.assert_has_feature(
            5, 17, 10, 'boundaries',
            {'kind': 'region', 'name': type(None)})

        # Austria region (scalerank=6, 1:10m NE only)
        self.assert_has_feature(
            6, 34, 22, 'boundaries',
            {'kind': 'region', 'min_zoom': 6})

        # Austria region NO name, Natural Earth
        self.assert_has_feature(
            6, 34, 22, 'boundaries',
            {'kind': 'region', 'name': type(None)})

        # Austria region HAS name, Natural Earth
        self.assert_has_feature(
            7, 68, 44, 'boundaries',
            {'kind': 'region', 'name': 'Tirol - Salzburg'})

        # Sweden region (scalerank=7, 1:10m NE only)
        self.assert_has_feature(
            6, 35, 18, 'boundaries',
            {'kind': 'region', 'min_zoom': 6.7})

        # United Kingdom region (scalerank=8, 1:10m NE only)
        self.assert_has_feature(
            6, 31, 18, 'boundaries',
            {'kind': 'region', 'min_zoom': 6.8})

        # Switzerland region (scalerank=9, 1:10m NE only)
        self.assert_has_feature(
            7, 66, 44, 'boundaries',
            {'kind': 'region', 'min_zoom': 7})


class BoundariesMinZoomAndNameOsm(FixtureTest):
    def test_region_boundary_zug_luzern_z8(self):
        import dsl

        z, x, y = 8, 133, 89

        # Switzerland region HAS NO name, OpenStreetMap
        self.generate_fixtures(
            # http://www.openstreetmap.org/relation/1686447
            dsl.way(-1686447, dsl.tile_diagonal(z+2, x*4, y*4), {
                u'name': u'Zug',
                u'admin_level': u'4',
                u'wikipedia': u'de:Kanton Zug',
                u'swisstopo:KANTONSNUM': u'9',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q11933',
                u'boundary': u'administrative',
                u'ISO3166-2': u'CH-ZG',
                u'ref': u'ZG',
                u'alt_name': u'Kanton Zug',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # http://www.openstreetmap.org/relation/1685677
            dsl.way(-1685677, dsl.tile_diagonal(z+2, x*4, y*4), {
                u'name': u'Luzern',
                u'admin_level': u'4',
                u'wikipedia': u'de:Kanton Luzern',
                u'swisstopo:KANTONSNUM': u'3',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q12121',
                u'alt_name': u'Kanton Luzern',
                u'boundary': u'administrative',
                u'ISO3166-2': u'CH-LU',
                u'ref': u'LU',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        # test that the regional boundary is present at zoom 8, although it
        # should have had its name stripped off, since it's very short.
        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'kind': 'region', 'name': type(None)})

    def test_region_boundary_zug_luzern_z12(self):
        import dsl

        z, x, y = 12, 2144, 1438

        # Switzerland region HAS name, OpenStreetMap
        # do this at z12, as the boundary between Zug and Luzern is quite
        # short, and we want enough space to label.
        self.generate_fixtures(
            # http://www.openstreetmap.org/relation/1686447
            dsl.way(-1686447, dsl.tile_diagonal(z, x, y), {
                u'name': u'Zug',
                u'admin_level': u'4',
                u'way_area': u'5.16033e+08',
                u'wikipedia': u'de:Kanton Zug',
                u'swisstopo:KANTONSNUM': u'9',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q11933',
                u'boundary': u'administrative',
                u'ISO3166-2': u'CH-ZG',
                u'ref': u'ZG',
                u'alt_name': u'Kanton Zug',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # http://www.openstreetmap.org/relation/1685677
            dsl.way(-1685677, dsl.tile_diagonal(z, x, y), {
                u'name': u'Luzern',
                u'admin_level': u'4',
                u'way_area': u'3.21768e+09',
                u'wikipedia': u'de:Kanton Luzern',
                u'swisstopo:KANTONSNUM': u'3',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q12121',
                u'alt_name': u'Kanton Luzern',
                u'boundary': u'administrative',
                u'ISO3166-2': u'CH-LU',
                u'ref': u'LU',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        # name should be present at zoom 12
        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'kind': 'region', 'name': 'Zug - Luzern'})

    def test_region_boundary_salzburg_tirol(self):
        import dsl

        z, x, y = 8, 136, 89

        # Austria region HAS name, OpenStreetMap
        self.generate_fixtures(
            # http://www.openstreetmap.org/relation/52343
            dsl.way(-52343, dsl.tile_diagonal(z, x, y), {
                u'ISO3166-2': u'AT-7',
                u'wikidata': u'Q153809',
                u'source': u'openstreetmap.org',
                u'ref:at:gkz': u'7',
                u'wikipedia': u'de:Tirol (Bundesland)',
                u'boundary': u'administrative',
                u'website': u'http://www.tirol.gv.at',
                u'admin_level': u'4',
                u'population': u'707573',
                u'name': u'Tirol',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # http://www.openstreetmap.org/relation/86539
            dsl.way(-86539, dsl.tile_diagonal(z, x, y), {
                u'ISO3166-2': u'AT-5',
                u'wikidata': u'Q43325',
                u'ref:at:gkz': u'5',
                u'way_area': u'1.56144e+10',
                u'wikipedia': u'de:Land Salzburg',
                u'source': u'openstreetmap.org',
                u'boundary': u'administrative',
                u'website': u'http://www.salzburg.gv.at',
                u'admin_level': u'4',
                u'description': u'Land Salzburg',
                u'name': u'Salzburg',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'kind': 'region', 'name': 'Salzburg - Tirol'})
