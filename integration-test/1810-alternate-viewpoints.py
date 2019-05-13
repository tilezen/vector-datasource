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
            # country boundary.
            dsl.way(3, dsl.fit_in_tile(
                z, x, y,
                'LINESTRING(0.5 0.9, 0.9 0.9, 0.9 0.1, 0.1 0.1, 0.1 0.5)'), {
                    'admin_level': '2',
                    'boundary': 'administrative',
                    'name': 'XX',
                    'source': 'openstreetmap.org',
                    'mz_boundary_from_polygon': True,  # need this for hack
                }),
            dsl.way(4, dsl.fit_in_tile(
                z, x, y,
                'LINESTRING(0.1 0.5, 0.1 0.1, 0.9 0.1, 0.9 0.9, 0.5 0.9)'), {
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
            })

        # should get a section recognised only by XX
        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'unrecognized_country',
                'kind:xx': 'country',
            })

        # should get a section recognised _except_ by XX
        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'kind:xx': 'unrecognized_country',
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
