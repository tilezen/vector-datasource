from . import FixtureTest


class FractionalPois(FixtureTest):
    def test_apple_store(self):
        # Apple Store, SF
        self.load_fixtures(['https://www.openstreetmap.org/way/332223480'])

        self.assert_has_feature(
            15, 5242, 12663, 'pois',
            {'id': 332223480, 'min_zoom': 15.31})

    def test_state_boundary(self):
        import dsl

        z, x, y, = 9, 150, 192

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/224951
            dsl.way(-224951, dsl.tile_diagonal(z, x, y), {
                'ISO3166-2': 'US-NJ',
                'admin_level': '4',
                'boundary': 'administrative',
                'is_in:country_code': 'US',
                'name': 'New Jersey',
                'ref': 'NJ',
                'ref:fips': '34',
                'type': 'boundary',
                'wikidata': 'Q1408',
                'wikipedia': 'en:New Jersey',
                'source': 'openstreetmap.org',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # https://www.openstreetmap.org/relation/61320
            dsl.way(-61320, dsl.tile_diagonal(z, x, y), {
                'ISO3166-2': 'US-NY',
                'admin_level': '4',
                'alt_name': 'New York State',
                'boundary': 'administrative',
                'is_in:country_code': 'US',
                'name': 'New York',
                'ref': 'NY',
                'ref:fips': '36',
                'type': 'boundary',
                'wikidata': 'Q1384',
                'wikipedia': 'en:New York (state)',
                'source': 'openstreetmap.org',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        # NOTE: might not have an ID if it has been merged
        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'min_zoom': 8,
             'source': 'openstreetmap.org',
             'name': 'New Jersey - New York'})

    def test_major_road_route(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/568499',
        ], clip=self.tile_bbox(9, 150, 192))

        self.assert_has_feature(
            9, 150, 192, 'roads',
            {'min_zoom': 8, 'sort_rank': 380,
             'source': 'openstreetmap.org',
             'kind': 'major_road',
             'kind_detail': 'primary',
             'network': 'US:NJ:Hudson'})

    def test_train_route(self):
        import dsl

        z, x, y = 9, 150, 192

        self.generate_fixtures(
            dsl.way(1359387, dsl.tile_diagonal(z, x, y), {
                "website": "http://www.amtrak.com",
                "passenger": "national",
                "via": "New York Penn Station",
                "from": "Washington, DC",
                "name": "Vermonter",
                "service": "long_distance",
                "to": "Saint Albans, Vermont",
                "route": "train",
                "wikipedia": "en:Vermonter (train)",
                "route_name": "Vermonter",
                "route_pref_color": "0",
                "public_transport:version": "1",
                "wikidata": "Q1412872",
                "source": "openstreetmap.org",
                "operator": "Amtrak",
                "ref": "54-57",
                "colour": "#005480",
                "network": "Amtrak"
            }),
        )

        self.assert_has_feature(
            z, x, y, 'transit',
            {'min_zoom': 5, 'ref': '54-57',
             'source': 'openstreetmap.org',
             'name': 'Vermonter'})


class FractionalPoisNe(FixtureTest):

    def setUp(self):
        super(FractionalPoisNe, self).setUp()

        fixtures = []
        for table in ('ne_10m_admin_1_states_provinces_lines',
                      'ne_10m_lakes',
                      'ne_10m_roads',
                      'water_polygons'):
            fixtures.append(
                'file://integration-test/fixtures/' +
                table +
                '/976-fractional-pois2.shp')

        self.load_fixtures(fixtures)

    def test_boundaries(self):
        # Test that source and min_zoom are set properly for boundaries, roads,
        # transit, and water
        self.assert_has_feature(
            5, 9, 12, 'boundaries',
            {'min_zoom': 2,
             'source': 'naturalearthdata.com',
             'kind': 'region'})

    def test_roads(self):
        self.assert_has_feature(
            7, 37, 48, 'roads',
            {'min_zoom': 5, 'id': int, 'shield_text': '95',
             'source': 'naturalearthdata.com'})

    def test_water_osm(self):
        self.assert_has_feature(
            9, 150, 192, 'water',
            {'min_zoom': 0,
             'source': 'osmdata.openstreetmap.de',
             'kind': 'ocean',
             'name': type(None)})


# move stuff into this class when it gets ported from fixture-based tests
# above to generative tests. eventually the class above should be empty.
class FractionalPoisNeGenerative(FixtureTest):

    def test_water_ne(self):
        import dsl

        z, x, y = (7, 36, 50)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                u'scalerank': 7,
                u'source': u'naturalearthdata.com',
                u'year': 1953,
                u'featurecla': u'Reservoir',
                u'name_abb': u'John H. Kerr Res.',
                u'name': u'John H. Kerr Reservoir',
                u'min_zoom': 7,
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water',
            {'min_zoom': 7, 'id': int,
             'source': 'naturalearthdata.com',
             'name': 'John H. Kerr Reservoir'})
