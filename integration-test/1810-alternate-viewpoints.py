# -*- encoding: utf-8 -*-
from . import FixtureTest


class CountryBoundaryTest(FixtureTest):

    def test_boundary(self):
        import dsl

        z, x, y = (8, 0, 0)

        # +---------------------+
        # |                     |
        # |  aaaaaaa*cccccccc   |
        # |  a      b       c   |
        # |  a      b       c   |
        # |  a      b       c   |
        # |  *bbbbbbb       c   |
        # |  c              c   |
        # |  c              c   |
        # |  cccccccccccccccc   |
        # |                     |
        # +---------------------+
        #
        #  a = claimed boundary. ways in a boundary=claim relation. we should
        #      get a linestring geometry for the whole relation from osm2pgsql.
        #
        #  b = "on the ground" boundary. ways in a boundary=administrative
        #      relation, but ways have disputed=yes, disputed_by=XX on them.
        #      we pick up each way as an individual geometry.
        #
        #  c = accepted boundary. ways in a boundary=administrative relation,
        #      ways have no extra tagging on them. the ways in b/c relation
        #      give us a country polygon, from which we extract the boundary.
        #
        self.generate_fixtures(
            # "a" relation gives us a linestring.
            dsl.way(1, dsl.fit_in_tile(
                z, x, y, 'LINESTRING(0.1 0.5, 0.1 0.9, 0.5 0.9)'), {
                    'admin_level': '2',
                    'boundary': 'claim',
                    'claimed_by': 'XX',
                    'source': 'openstreetmap.org',
                    'type': 'boundary',
                    'name': 'XX Claim',
                }),
            # "b" ways give us linestring(s)
            dsl.way(2, dsl.fit_in_tile(
                z, x, y, 'LINESTRING(0.1 0.5, 0.5 0.5, 0.5 0.9)'), {
                    'admin_level': '2',
                    'boundary': 'administrative',
                    'disputed': 'yes',
                    'disputed_by': 'XX',
                    'source': 'openstreetmap.org',
                }),
            # "b & c" ways + country relation give us a polygon => oriented
            # boundary curve. we get an oriented boundary curve for each
            # country boundary. (note: b & c together should be a closed ring).
            dsl.way(3, dsl.fit_in_tile(
                z, x, y,
                'LINESTRING(0.5 0.9, 0.9 0.9, 0.9 0.1, 0.1 0.1, 0.1 0.5, '
                '0.5 0.5, 0.5 0.9)'), {
                    'admin_level': '2',
                    'boundary': 'administrative',
                    'name': 'XX',
                    'source': 'openstreetmap.org',
                    'mz_boundary_from_polygon': True,  # need this for hack
                }),
            dsl.way(4, dsl.fit_in_tile(
                z, x, y,
                'LINESTRING(0.5 0.9, 0.9 0.9, 0.9 0.1, 0.1 0.1, 0.1 0.5, '
                '0.5 0.5, 0.5 0.9)'), {
                    'admin_level': '2',
                    'boundary': 'administrative',
                    'name': 'YY',
                    'source': 'openstreetmap.org',
                    'mz_boundary_from_polygon': True,  # need this for hack
                }),
            # this is just here to turn off maritime boundaries for everything
            # in this tile.
            dsl.way(5, dsl.tile_box(z, x, y), {
                'source': 'tilezen.org',
                'maritime_boundary': True,
                'min_zoom': 0,
                'kind': 'maritime',
            }),
        )

        # should get a non-disputed section of border
        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'name:left': 'XX',
                'name:right': 'YY',
                'name': 'XX - YY',
            })

        # should get a section recognised only by XX
        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'unrecognized_country',
                'kind:xx': 'country',
                'name': 'XX Claim',

                # we should have dropped the claimed_by/disputed_by tags
                'claimed_by': type(None),
                'disputed_by': type(None),
            })

        # should get a section recognised _except_ by XX
        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'kind:xx': 'unrecognized_country',
                'name': 'XX - YY',
            })

    def test_claim(self):
        # test that a claim by countries BB & CC (and recognised by DD) is
        # only kind:country for those countries. everyone else's view is
        # kind: unrecognized_country.
        #
        # TODO: recognized_by not working yet.
        import dsl

        z, x, y = (8, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'admin_level': '2',
                'boundary': 'claim',
                'name': 'Extent of CC claim',
                'claimed_by': 'CC',
                'disputed_by': 'AA;DD',
            }),
            dsl.way(2, dsl.tile_diagonal(z, x, y), {
                'admin_level': '2',
                'boundary': 'claim',
                'name': 'Extent of BB claim',
                'claimed_by': 'BB',
                'disputed_by': 'AA',
                'recognized_by': 'DD',
            }),
            dsl.way(3, dsl.tile_diagonal(z, x, y), {
                'admin_level': '3',
                'boundary': 'administrative',
                'name': 'Region Name',
                'type': 'boundary',
            }),
            dsl.way(4, dsl.tile_diagonal(z, x, y), {
                'dispute': 'yes',
                'disputed_by': 'AA',
                'name': 'BB claim',  # note: also CC claim?!
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                # generally unrecognised
                'kind': 'unrecognized_country',
                # but BB & CC both claim this as a border
                'kind:bb': 'country',
                'kind:cc': 'country',
                # AA disputes that this border exists. NOTE: the kind:aa is
                # added to the output even though it duplicates the kind. this
                # is to help with multi-level fallback. see
                # https://github.com/tilezen/vector-datasource/pull/1895#discussion_r283912502
                'kind:aa': 'unrecognized_country',
                # DD recognizes BB's claim, so should see this as a country.
                'kind:dd': 'country',
            })

        # because AA disputes the whole boundary (way 4), all the boundaries
        # should be unrecognized (either by default or kind:aa).
        with self.features_in_tile_layer(z, x, y, 'boundaries') as features:
            for feature in features:
                # calculate fallback: prefer kind:aa if it exists, else fall
                # back to kind.
                props = feature['properties']
                kind = props.get('kind')
                kind_aa = props.get('kind:aa', kind)
                self.assertTrue(kind_aa is not None)
                self.assertTrue(kind_aa.startswith('unrecognized_'))

    def test_whole_claim(self):
        # test that something where XA claims the whole boundary of XB works
        # as expected - we get a boundary where XB is a country except in
        # XA's viewpoint and a second boundary feature where the whole thing
        # is just a boundary of XA in XA's viewpoint.
        import dsl

        z, x, y = 8, 0, 0

        #
        #  +----------------+
        #  |                |
        #  |  aaaaaaaaaaa   |
        #  |  a         a   |
        #  |  a         a   |
        #  |  a         a   |
        #  |  a         a   |
        #  |  aaaaaaaaaaa   |
        #  |                |
        #  +----------------+
        #
        # this is mapped in OSM using 3 different elements:
        #
        #  1. a country boundary relation for XB
        #  2. the ways making up the country boundary relation are tagged
        #     disputed=yes, disputed_by=XA
        #  3. a claim relation with claimed_by=XA containing the same ways
        #     as the country boundary relation.
        #
        linestring = 'LINESTRING(0.1 0.1, 0.1 0.9, 0.9 0.9, 0.9 0.1, 0.1 0.1)'

        self.generate_fixtures(
            # country boundary relation gives us a linestring boundary
            # extracted from the country polygon.
            dsl.way(1, dsl.fit_in_tile(z, x, y, linestring), {
                'admin_level': '2',
                'boundary': 'administrative',
                'name': 'XB',
                'source': 'openstreetmap.org',
                'type': 'boundary',
                'mz_boundary_from_polygon': True,
            }),
            # ways making up the country boundary tagged disputed
            dsl.way(2, dsl.fit_in_tile(z, x, y, linestring), {
                'disputed': 'yes',
                'disputed_by': 'XA',
                'source': 'openstreetmap.org',
            }),
            # claim relation
            dsl.way(3, dsl.fit_in_tile(z, x, y, linestring), {
                'admin_level': '2',
                'boundary': 'claim',
                'claimed_by': 'XA',
                'name': "Extent of XA's claim",
                'source': 'openstreetmap.org',
            }),
        )

        saw_xa = False
        saw_xb = False

        with self.features_in_tile_layer(z, x, y, 'boundaries') as features:
            for feature in features:
                props = feature['properties']
                kind = props.get('kind')

                if kind == 'country':
                    # generally accepted viewpoint, XA should dispute
                    self.assertEqual(
                        props.get('kind:xa'), 'unrecognized_country')
                    self.assertEqual(props.get('name'), 'XB')
                    saw_xb = True

                elif kind == 'unrecognized_country':
                    # XA's viewpoint, which should claim it as part of XA
                    self.assertEqual(props.get('kind:xa'), 'country')
                    self.assertEqual(props.get('name'), "Extent of XA's claim")
                    saw_xa = True

        self.assertTrue(saw_xa, "Expected to see XA's viewpoint boundary")
        self.assertTrue(saw_xb, "Expected to see XB's country boundary")


class PlaceTest(FixtureTest):

    def test_disputed_capital(self):
        import dsl

        z, x, y = 16, 0, 0

        # a country capital which CN doesn't think is a country capital. this
        # is just a test case, and any resemblance to real disputes, living or
        # dead, is purely coincidental.
        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'name': 'Foo',
                'featurecla': 'Admin-0 capital',
                'fclass_cn': 'Admin-1 capital',
                'scalerank': 4,
                'min_zoom': 4,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'kind': 'locality',
                'country_capital': type(True),
                'country_capital:cn': type(False),
                'region_capital:cn': type(True),
            })

    # NOTE: this isn't a test, just a factoring-out of common code used by all
    # the subsequent tests, which are testing variations of what happens when
    # the default (featurecla) is different from an override (fclass_iso).
    def _check(self, default, dispute, expected):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'name': 'Foo',
                'featurecla': default,
                'fclass_iso': dispute,
                'scalerank': 4,
                'min_zoom': 4,
                'source': 'naturalearthdata.com',
            }),
        )

        expected['kind'] = 'locality'
        self.assert_has_feature(z, x, y, 'places', expected)

    def test_country_country(self):
        # explicit override still comes out in the output
        self._check(
            'Admin-0 capital',
            'Admin-0 capital',
            {'country_capital:iso': type(True)}
        )

    def test_country_region(self):
        # region override disables country_capital and adds region_capital.
        self._check(
            'Admin-0 capital',
            'Admin-1 capital',
            {
                'country_capital:iso': type(False),
                'region_capital:iso': type(True),
            }
        )

    def test_country_none(self):
        # override to none should just disable country_capital
        self._check(
            'Admin-0 capital',
            'Populated place',
            {'country_capital:iso': type(False)}
        )

    def test_region_country(self):
        # override sets country_capital and disables region_capital
        self._check(
            'Admin-1 capital',
            'Admin-0 capital',
            {
                'country_capital:iso': type(True),
                'region_capital:iso': type(False),
            }
        )

    def test_region_region(self):
        # explicit override still comes out in the output
        self._check(
            'Admin-1 capital',
            'Admin-1 capital',
            {'region_capital:iso': type(True)}
        )

    def test_region_none(self):
        # disables region_capital
        self._check(
            'Admin-1 capital',
            'Populated place',
            {'region_capital:iso': type(False)}
        )

    def test_none_country(self):
        # sets country_capital
        self._check(
            'Populated place',
            'Admin-0 capital',
            {'country_capital:iso': type(True)}
        )

    def test_none_region(self):
        # sets region_capital
        self._check(
            'Populated place',
            'Admin-1 capital',
            {'region_capital:iso': type(True)}
        )

    def test_none_none(self):
        # does nothing?
        self._check(
            'Populated place',
            'Populated place',
            {}
        )


class RegionBoundary(FixtureTest):

    def test_dispute(self):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            # way, tagged disputed
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'admin_level': '4',
                'boundary': 'administrative',
                'disputed': 'yes',
                'disputed_by': 'XB',
                'name': 'XA internal region border',
                'source': 'openstreetmap.org',
            }),
            # way used in relations for region borders
            #
            # NOTE: we won't use this one, since we don't pay attention to
            # admin_level=3, but i included it for completeness, so that the
            # test more closely resembles the data it's based on.
            dsl.way(2, dsl.tile_diagonal(z, x, y), {
                'admin_level': '3',  # 3?!? as always... data = mess
                'border_type': 'province',
                'boundary': 'administrative',
                'is_in:country_code': 'XA',
                'name': 'XA region 1',
                'type': 'boundary',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
            # this one we do pay attention to, admin_level=4
            dsl.way(3, dsl.tile_diagonal(z, x, y), {
                'admin_level': '4',
                'boundary': 'administrative',
                'name': 'XA region 2',
                'place': 'District',
                'type': 'boundary',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'region',
                'kind:xb': 'unrecognized_region',
                'name': 'XA region 2',
            })

    def test_claim(self):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            # XA's claim relation
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'admin_level': '4',
                'boundary': 'claim',
                'name': 'XA region claim',
                'claimed_by': 'XA',
                'disputed_by': 'XB',
                'source': 'openstreetmap.org',
            }),
            # XA's claim _way_, disputed by XB
            dsl.way(2, dsl.tile_diagonal(z, x, y), {
                'disputed': 'yes',
                'disputed_by': 'XB',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'unrecognized_region',
                'kind:xa': 'region',
            })


class CountyBoundary(FixtureTest):

    def test_dispute(self):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            # way, tagged disputed
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'admin_level': '4',
                'boundary': 'administrative',
                'disputed': 'yes',
                'disputed_by': 'XB',
                'name': 'XA internal county border',
                'source': 'openstreetmap.org',
            }),
            # line from relation / county polygon
            dsl.way(3, dsl.tile_diagonal(z, x, y), {
                'admin_level': '6',
                'boundary': 'administrative',
                'name': 'XA county 2',
                'place': 'District',
                'type': 'boundary',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'county',
                'kind:xb': 'unrecognized_county',
                'name': 'XA county 2',
            })

    def test_claim(self):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            # XA's claim relation
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'admin_level': '6',
                'boundary': 'claim',
                'name': 'XA county claim',
                'claimed_by': 'XA',
                'disputed_by': 'XB',
                'source': 'openstreetmap.org',
            }),
            # XA's claim _way_, disputed by XB
            dsl.way(2, dsl.tile_diagonal(z, x, y), {
                'disputed': 'yes',
                'disputed_by': 'XB',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'unrecognized_county',
                'kind:xa': 'county',
            })


class NaturalEarth(FixtureTest):

    def test_country_claim(self):
        # test that a boundary tagged as generally unrecognized, but a country
        # boundary in some viewpoint, gets output with the appropriate kind:XX
        # viewpoint property.
        import dsl

        z, x, y = 8, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'featurecla': 'Unrecognized',
                'fclass_gb': 'International boundary (verify)',
                'min_zoom': 0,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'unrecognized_country',
                'kind:gb': 'country',
            })

    def test_country_dispute(self):
        # check that a boundary which is disputed and shouldn't be shown in
        # some viewpoint is output with a kind:XX property reflecting that.
        import dsl

        z, x, y = 8, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'featurecla': 'International boundary (verify)',
                'fclass_gb': 'Unrecognized',
                'min_zoom': 0,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'kind:gb': 'unrecognized_country',
            })

    def test_region_claim(self):
        # test that a boundary tagged as generally unrecognized, but a region
        # boundary in some viewpoint, gets output with the appropriate kind:XX
        # viewpoint property.
        import dsl

        z, x, y = 8, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'featurecla': 'Unrecognized Admin-1 boundary',
                'fclass_gb': 'Admin-1 boundary',
                'scalerank': 0,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'unrecognized_region',
                'kind:gb': 'region',
            })

    def test_region_dispute(self):
        # check that a boundary which is disputed and shouldn't be shown in
        # some viewpoint is output with a kind:XX property reflecting that.
        import dsl

        z, x, y = 8, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'featurecla': 'Admin-1 boundary',
                'fclass_gb': 'Unrecognized Admin-1 boundary',
                'scalerank': 0,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'region',
                'kind:gb': 'unrecognized_region',
            })

    def test_country_view_region(self):
        # check that viewpoint can have kind:XX = region on a kind = country,
        # not just unrecognized.
        import dsl

        z, x, y = 8, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'featurecla': 'International boundary (verify)',
                'fclass_gb': 'Admin-1 boundary',
                'min_zoom': 0,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'kind:gb': 'region',
            })

    def test_region_view_country(self):
        # check that viewpoint can have kind:XX = country on a kind = region,
        # not just unrecognized.
        import dsl

        z, x, y = 8, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'featurecla': 'Admin-1 boundary',
                'fclass_gb': 'International boundary (verify)',
                'min_zoom': 0,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'region',
                'kind:gb': 'country',
            })

    def test_unrecognized_macroregion(self):
        import dsl

        z, x, y = 8, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'featurecla': 'Admin-1 region boundary',
                'fclass_gb': 'Unrecognized Admin-1 region boundary',
                'scalerank': 0,
                'source': 'naturalearthdata.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'macroregion',
                'kind:gb': 'unrecognized_macroregion',
            })
