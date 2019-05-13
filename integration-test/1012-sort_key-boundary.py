from . import FixtureTest


# Adds tests for OSM features (but not NE features)
class SortKeyBoundary(FixtureTest):

    def test_usa_country_boundary(self):
        import dsl

        z, x, y = 8, 39, 95

        # country boundary of USA
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
                u'gnis:feature_id': u'1890467',
                u'name': u'United States of America',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q30',
                u'wikipedia': u'en:United States',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, "boundaries",
            {"kind": "country", "sort_rank": 262})

    def test_nevada_california_boundary(self):
        import dsl

        z, x, y = 8, 42, 96
        # region boundary between Nevada - California
        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/165473
            dsl.way(-165473, dsl.tile_diagonal(z, x, y), {
                u'ISO3166-2': u'US-NV',
                u'admin_level': u'4',
                u'boundary': u'administrative',
                u'is_in:country_code': u'US',
                u'name': u'Nevada',
                u'ref': u'NV',
                u'ref:fips': u'32',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q1227',
                u'wikipedia': u'en:Nevada',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # https://www.openstreetmap.org/relation/165475
            dsl.way(-165475, dsl.tile_diagonal(z, x, y), {
                u'ISO3166-2': u'US-CA',
                u'admin_level': u'4',
                u'alt_name:vi': u'California',
                u'boundary': u'administrative',
                u'is_in:country_code': u'US',
                u'name': u'California',
                u'place': u'state',
                u'ref': u'CA',
                u'ref:fips': u'06',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q99',
                u'wikipedia': u'en:California',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, "boundaries",
            {"kind": "region", "sort_rank": 256})

    def test_mendocino_humboldt_county_boundary(self):
        import dsl

        z, x, y = 10, 159, 387

        # county boundary between Mendocino County - Humboldt County
        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/396458
            dsl.way(-396458, dsl.tile_diagonal(z, x, y), {
                u'admin_level': u'6',
                u'alt_name': u'Humboldt',
                u'attribution': u'CASIL cnty24k09_1_poly.shp',
                u'boundary': u'administrative',
                u'county:abbrev': u'HUM',
                u'county:ansi': u'023',
                u'county:name': u'Humboldt',
                u'name': u'Humboldt County',
                u'nist:fips_code': u'6023',
                u'nist:state_fips': u'6',
                u'population': u'135727',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q109651',
                u'wikipedia': u'en:Humboldt County, California',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # https://www.openstreetmap.org/relation/396489
            dsl.way(-396489, dsl.tile_diagonal(z, x, y), {
                u'admin_level': u'6',
                u'alt_name': u'Mendocino',
                u'attribution': u'CASIL cnty24k09_1_poly.shp',
                u'boundary': u'administrative',
                u'county:abbrev': u'MEN',
                u'county:ansi': u'045',
                u'county:name': u'Mendocino',
                u'name': u'Mendocino County',
                u'nist:fips_code': u'6045',
                u'nist:state_fips': u'6',
                u'source': u'openstreetmap.org',
                u'wikidata': u'Q108087',
                u'wikipedia': u'en:Mendocino County, California',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, "boundaries",
            {"kind": "county", "sort_rank": 254})

    def test_san_francisco_daly_city_locality_boundary(self):
        import dsl

        z, x, y, = 11, 326, 792

        # locality boundary between San Francisco - Daly City
        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/111968
            dsl.way(-111968, dsl.tile_diagonal(z, x, y), {
                u'admin_level': u'8',
                u'alt_name:vi': u'X\u0103ng Ph\u0103ng',
                u'border_type': u'city',
                u'boundary': u'administrative',
                u'is_in': u'USA, California',
                u'is_in:country': u'USA',
                u'is_in:country_code': u'US',
                u'is_in:iso_3166_2': u'US:CA',
                u'is_in:state': u'California',
                u'is_in:state_code': u'CA',
                u'name': u'San Francisco',
                u'old_name:vi': u'C\u1ef1u Kim S\u01a1n',
                u'place_name': u'San Francisco',
                u'source': u'openstreetmap.org',
                u'tiger:CLASSFP': u'C1',
                u'tiger:CPI': u'Y',
                u'tiger:FUNCSTAT': u'A',
                u'tiger:LSAD': u'25',
                u'tiger:MTFCC': u'G4110',
                u'tiger:NAME': u'San Francisco',
                u'tiger:NAMELSAD': u'San Francisco city',
                u'tiger:PCICBSA': u'Y',
                u'tiger:PCINECTA': u'N',
                u'tiger:PLACEFP': u'67000',
                u'tiger:PLACENS': u'02411786',
                u'tiger:PLCIDFP': u'0667000',
                u'tiger:STATEFP': u'06',
                u'tiger:reviewed': u'no',
                u'wikidata': u'Q62',
                u'wikipedia': u'en:San Francisco',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # https://www.openstreetmap.org/relation/112271
            dsl.way(-112271, dsl.tile_diagonal(z, x, y), {
                u'admin_level': u'8',
                u'border_type': u'city',
                u'boundary': u'administrative',
                u'is_in': u'USA, California',
                u'is_in:country': u'USA',
                u'is_in:country_code': u'US',
                u'is_in:iso_3166_2': u'US:CA',
                u'is_in:state': u'California',
                u'is_in:state_code': u'CA',
                u'name': u'Daly City',
                u'place': u'city',
                u'source': u'openstreetmap.org',
                u'tiger:CLASSFP': u'C1',
                u'tiger:CPI': u'Y',
                u'tiger:FUNCSTAT': u'A',
                u'tiger:LSAD': u'25',
                u'tiger:MTFCC': u'G4110',
                u'tiger:NAME': u'Daly City',
                u'tiger:NAMELSAD': u'Daly City city',
                u'tiger:PCICBSA': u'N',
                u'tiger:PCINECTA': u'N',
                u'tiger:PLACEFP': u'17918',
                u'tiger:PLACENS': u'02410291',
                u'tiger:PLCIDFP': u'0617918',
                u'tiger:STATEFP': u'06',
                u'tiger:reviewed': u'no',
                u'way_area': u'3.17446e+07',
                u'wikidata': u'Q370925',
                u'wikipedia': u'en:Daly City, California',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, "boundaries",
            {"kind": "locality", "sort_rank": 252})
