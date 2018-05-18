from . import FixtureTest


# mini roundabouts are modelled as points, which means they have no intrinsic
# direction. this means we need additional information to tell whether to draw
# the roundabout with clockwise arrows (drives on left) or counter-clockwise
# (drives on right).
#
class MiniRoundaboutDirection(FixtureTest):
    def test_mini_roundabout_drives_on_left(self):
        import dsl

        # randomly chosen tile with the M4 motorway west of London, GB
        z, x, y = (16, 32680, 21796)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'GB',
                'source': 'openstreetmap.org'
            }),
            dsl.point(1, dsl.tile_centre(z, x, y), {
                'highway': 'mini_roundabout'
            }),
        )

        # roundabout should now have a "drives_on_left" attribute
        self.assert_has_feature(
            z, x, y, 'pois',
            {'id': 1, 'kind': 'mini_roundabout', 'drives_on_left': True})

    def test_mini_roundabout_drives_on_right(self):
        import dsl

        # randomly chosen tile in Rouen, France (drives on right).
        z, x, y = (16, 32959, 22386)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'FR',
                'source': 'openstreetmap.org'
            }),
            dsl.point(1, dsl.tile_centre(z, x, y), {
                'highway': 'mini_roundabout'
            }),
        )

        # roundabout should _not_ have a "drives_on_left" attribute - the
        # default for this would be false, and therefore omitted.
        self.assert_has_feature(
            z, x, y, 'pois',
            {'id': 1, 'kind': 'mini_roundabout',
             'drives_on_left': type(None)})
