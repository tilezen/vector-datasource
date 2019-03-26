from . import FixtureTest


class OsmNeTransition(FixtureTest):

    def _assert_osm_ne_transition(self, z, x, y, layer):
        # checks that the OSM->NE transition happens for the given layer
        # between the z/x/y coordinate given and the parent tile
        # (z-1)/(x/2)/(y/2)
        osm = {'source': set([
            'openstreetmap.org',
            'osmdata.openstreetmap.de',
        ])}
        ne = {'source': 'naturalearthdata.com'}

        # assert OSM feature exists at upper zoom level
        self.assert_has_feature(z, x, y, layer, osm)
        self.assert_no_matching_feature(z, x, y, layer, ne)

        # assert NE feature exists at lower zoom level
        self.assert_has_feature(z-1, x/2, y/2, layer, ne)
        self.assert_no_matching_feature(z-1, x/2, y/2, layer, osm)

    def test_roads(self):
        # TODO!
        # since the choice of which table to pull data from is controlled in
        # the query for postgres data and there is not yet any equivalent in
        # the fixture data source, then this test currently cannot pass.
        # this means we need some way of tracking which table or template the
        # data came from in order to use the queries.yaml 'sources' lookup to
        # exclude data which comes from the wrong table or template.

        # self.load_fixtures([
        #     'file://integration-test/fixtures/'
        #     'ne_10m_roads/976-fractional-pois.shp',
        #     'http://www.openstreetmap.org/relation/1675644',
        # ], clip=self.tile_bbox(8, 75, 96))

        # self._assert_osm_ne_transition(8, 75, 96, 'roads')
        pass

    # TODO: there are more tests to add here.
