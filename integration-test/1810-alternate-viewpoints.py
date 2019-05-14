# -*- encoding: utf-8 -*-
from . import FixtureTest


class BoundaryTest(FixtureTest):

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
                'kind': 'unrecognized_country',
                'kind:bb': 'country',
                'kind:cc': 'country',
                # 'kind:dd': 'country',
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
