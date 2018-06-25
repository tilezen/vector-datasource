from . import FixtureTest


class AddCountryCodesToRoads(FixtureTest):
    def test_add_country_code_to_road(self):
        import dsl

        # randomly chosen tile with the M4 motorway west of London, GB
        z, x, y = (16, 32680, 21796)

        # although we model these both as "ways", this is really just a way to
        # get geometry into the pipeline. in real usage, the admin_area comes
        # from a static shapefile.
        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            dsl.way(2, dsl.tile_diagonal(z, x, y),
                    {'highway': 'motorway', 'ref': 'M4',
                     'source': 'openstreetmap.org'}),
        )

        # should have deleted this layer before output.
        with self.layers_in_tile(z, x, y) as layers:
            self.assertNotIn('admin_areas', layers)

        # the country_code will have been used internally to generate a
        # "country_code" property, but (as per #1534) it should be stripped out
        # before the tile is output.
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 2, 'country_code': type(None), 'network': 'GB:M-road'})

    # the backfill national network in the UK should still be more important
    # than the EU "e-road" desigation, as that isn't signed.
    def test_backfill_more_important_than_eroad(self):
        import dsl

        # randomly chosen tile with the M4 motorway west of London, GB
        z, x, y = (16, 32680, 21796)

        # although we model these both as "ways", this is really just a way to
        # get geometry into the pipeline. in real usage, the admin_area comes
        # from a static shapefile.
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y),
                    {'kind': 'admin_area', 'iso_code': 'GB',
                     'source': 'openstreetmap.org'}),
            dsl.way(2, dsl.tile_diagonal(z, x, y),
                    {'highway': 'motorway', 'ref': 'M4',
                     'source': 'openstreetmap.org'}),
            dsl.relation(
                1, {
                    'network': 'e-road',
                    'route': 'road',
                    'ref': 'E 30',
                    'type': 'route',
                },
                ways=[2],
            ),
        )

        # the main network should be GB, not e-road
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 2, 'network': 'GB:M-road', 'shield_text': 'M4'})
