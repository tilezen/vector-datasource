from . import FixtureTest


class NormalizeBoundariesKind(FixtureTest):
    def test_aboriginal_lands_protected_area(self):
        # Relation: Hoopa Valley Tribe
        #
        # Note: this is tagged as a "protected_area" rather than a political
        # boundary, but it seems that some "protect_class" values indicate
        # political "protection"
        import dsl

        z, x, y = 16, 10237, 24570

        self.generate_fixtures(
            dsl.way(-6214773, dsl.tile_diagonal(z, x, y), {
                "name": "Hoopa Valley Tribe",
                "url": "http://hoopa-nsn.gov",
                "source": "openstreetmap.org",
                "boundary": "protected_area",
                "population": "2633",
                "protect_class": "24",
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'id': -6214773, 'kind': 'aboriginal_lands',
             'kind_detail': type(None)})

    def test_aboriginal_lands_puyallup(self):
        # use relation instead of way, as osm2pgsql treats the relation as
        # superseding the way and removes its tags when both are present.
        import dsl

        z, x, y = 16, 10483, 22987

        self.generate_fixtures(
            dsl.way(-3854097, dsl.tile_diagonal(z, x, y), {
                'boundary': 'aboriginal_lands',
                'name': 'Puyallup Tribe Reservation',
                'type': 'boundary',
                'source': 'openstreetmap.org',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'id': -3854097, 'kind': 'aboriginal_lands',
             'kind_detail': type(None)})

    def test_aboriginal_lands_sumas(self):
        # Way: Upper Sumas 6 (55602811)
        import dsl

        z, x, y = 16, 10523, 22492

        self.generate_fixtures(
            dsl.way(-6791772, dsl.tile_diagonal(z, x, y), {
                "attribution": "GeoBase",
                "name": "Upper Sumas 6",
                "source": "openstreetmap.org",
                "name:fr": "Upper Sumas No 6",
                "boundary": "protected_area",
                "protect_class": "24",
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'id': -6791772, 'kind': 'aboriginal_lands',
             'kind_detail': type(None)})

    def test_country(self):
        import dsl

        z, x, y = 16, 10417, 25370

        # Relation: United States of America
        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/148838
            dsl.way(-148838, dsl.tile_diagonal(z, x, y), {
                u'ISO3166-1': u'US',
                u'ISO3166-1:alpha2': u'US',
                u'ISO3166-1:alpha3': u'USA',
                u'ISO3166-1:numeric': u'840',
                u'admin_level': u'2',
                u'border_type': u'national',
                u'boundary': u'administrative',
                u'name': u'United States of America',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q30',
                u'wikipedia': u'en:United States',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'id': -148838, 'kind': 'country', 'kind_detail': '2'})

    def test_state_border(self):
        import dsl

        z, x, y = 16, 12553, 24147

        # Relation: Wyoming (161991) & Idaho (162116)
        self.generate_fixtures(
            # http://www.openstreetmap.org/relation/161991
            dsl.way(-161991, dsl.tile_diagonal(z, x, y), {
                u'ISO3166-2': u'US-WY',
                u'wikidata': u'Q1214',
                u'ref:fips': u'56',
                u'wikipedia': u'en:Wyoming',
                u'source': u'openstreetmap.org',
                u'boundary': u'administrative',
                u'ref': u'WY',
                u'admin_level': u'4',
                u'is_in:country_code': u'US',
                u'name': u'Wyoming',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # http://www.openstreetmap.org/relation/162116
            dsl.way(-162116, dsl.tile_diagonal(z, x, y), {
                u'ISO3166-2': u'US-ID',
                u'wikidata': u'Q1221',
                u'ref:fips': u'16',
                u'wikipedia': u'en:Idaho',
                u'source': u'openstreetmap.org',
                u'boundary': u'administrative',
                u'ref': u'ID',
                u'admin_level': u'4',
                u'is_in:country_code': u'US',
                u'name': u'Idaho',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'id': set([-161991, -162116]), 'kind': 'region',
             'kind_detail': '4'})

    def test_county_border(self):
        import dsl

        z, x, y = 16, 10484, 25346

        # SF City/County -- San Mateo County
        self.generate_fixtures(
            # http://www.openstreetmap.org/relation/396487
            dsl.way(-396487, dsl.tile_diagonal(z, x, y), {
                u'admin_level': u'6',
                u'attribution': u'CASIL cnty24k09_1_poly.shp',
                u'name': u'San Francisco City and County',
                u'county:ansi': u'075',
                u'county:abbrev': u'SFO',
                u'source': u'openstreetmap.org',
                u'county:name': u'San Francisco',
                u'alt_name': u'San Francisco',
                u'nist:fips_code': u'6075',
                u'nist:state_fips': u'6',
                u'boundary': u'administrative',
                u'population': u'870887',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # http://www.openstreetmap.org/relation/396498
            dsl.way(-396498, dsl.tile_diagonal(z, x, y), {
                u'admin_level': u'6',
                u'attribution': u'CASIL cnty24k09_1_poly.shp',
                u'name': u'San Mateo County',
                u'county:ansi': u'081',
                u'county:abbrev': u'SMT',
                u'way_area': u'3.05109e+09',
                u'wikipedia': u'en:San Mateo County, California',
                u'source': u'openstreetmap.org',
                u'county:name': u'San Mateo',
                u'wikidata': u'Q108101',
                u'alt_name': u'San Mateo',
                u'nist:fips_code': u'6081',
                u'nist:state_fips': u'6',
                u'boundary': u'administrative',
                u'population': u'765135',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'id': set([-396487, -396498]), 'kind': 'county',
             'kind_detail': '6'})

    def test_locality(self):
        import dsl

        z, x, y = 16, 10487, 25355

        # Relation: Brisbane (2834528)
        self.generate_fixtures(
            # http://www.openstreetmap.org/relation/2834528
            dsl.way(-2834528, dsl.tile_diagonal(z, x, y), {
                u'tiger:PCICBSA': u'N',
                u'tiger:STATEFP': u'06',
                u'wikidata': u'Q917671',
                u'tiger:FUNCSTAT': u'A',
                u'tiger:CPI': u'N',
                u'is_in': u'USA, California',
                u'tiger:LSAD': u'25',
                u'is_in:country': u'USA',
                u'wikipedia': u'en:Brisbane, California',
                u'source': u'openstreetmap.org',
                u'border_type': u'city',
                u'tiger:CLASSFP': u'C1',
                u'boundary': u'administrative',
                u'admin_level': u'8',
                u'tiger:NAMELSAD': u'Brisbane city',
                u'is_in:country_code': u'US',
                u'tiger:reviewed': u'no',
                u'is_in:state': u'California',
                u'tiger:PCINECTA': u'N',
                u'tiger:PLCIDFP': u'0608310',
                u'is_in:state_code': u'CA',
                u'tiger:PLACEFP': u'08310',
                u'name': u'Brisbane',
                u'tiger:NAME': u'Brisbane',
                u'tiger:MTFCC': u'G4110',
                u'is_in:iso_3166_2': u'US:CA',
                u'tiger:PLACENS': u'02409912',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries',
            {'id': -2834528, 'kind': 'locality', 'kind_detail': '8'})


class NormalizeBoundariesKindNaturalEarth(FixtureTest):

    def setUp(self):
        super(NormalizeBoundariesKindNaturalEarth, self).setUp()
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_admin_0_boundary_lines_land/'
            '841-normalize-boundaries-kind-admin0.shp',
            'file://integration-test/fixtures/'
            'ne_10m_admin_1_states_provinces_lines/'
            '841-normalize-boundaries-kind-admin1.shp',
        ])

    def test_admin1(self):
        # ne data
        # Admin-1 boundary
        self.assert_has_feature(
            7, 75, 70, 'boundaries',
            {'kind': 'region', 'kind_detail': '4'})

    def test_admin1_statistical(self):
        # Admin-1 statistical boundary
        self.assert_has_feature(
            7, 101, 56, 'boundaries',
            {'kind': 'region', 'kind_detail': '4'})

    def test_admin1_statistical_meta(self):
        # Admin-1 statistical meta bounds
        self.assert_has_feature(
            7, 26, 52, 'boundaries',
            {'kind': 'region', 'kind_detail': '4'})

    def test_admin1_region(self):
        # Admin-1 region boundary
        self.assert_has_feature(
            7, 99, 57, 'boundaries',
            {'kind': 'macroregion', 'kind_detail': '3'})

    def test_disputed(self):
        # Disputed (please verify)
        self.assert_has_feature(
            7, 39, 71, 'boundaries',
            {'kind': 'disputed', 'kind_detail': '2'})

    def test_indefinite(self):
        # Indefinite (please verify)
        self.assert_has_feature(
            7, 20, 44, 'boundaries',
            {'kind': 'indefinite', 'kind_detail': '2'})

    def test_indeterminant(self):
        # Indeterminant frontier
        self.assert_has_feature(
            7, 91, 50, 'boundaries',
            {'kind': 'indeterminate', 'kind_detail': '2'})

    def test_international(self):
        # International boundary (verify)
        self.assert_has_feature(
            7, 67, 37, 'boundaries',
            {'kind': 'country', 'kind_detail': '2'})

    def test_lease_limit(self):
        # Lease limit
        self.assert_has_feature(
            7, 86, 45, 'boundaries',
            {'kind': 'lease_limit', 'kind_detail': '2'})

    def test_line_of_control(self):
        # Line of control (please verify)
        self.assert_has_feature(
            7, 90, 50, 'boundaries',
            {'kind': 'line_of_control', 'kind_detail': '2'})

    def test_overlay(self):
        # Overlay limit
        self.assert_has_feature(
            7, 109, 49, 'boundaries',
            {'kind': 'overlay_limit', 'kind_detail': '2'})
