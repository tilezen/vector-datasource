# -*- coding: utf-8 -*-
from . import FixtureTest


class MinZoomFromNETest(FixtureTest):

    def setUp(self):
        import dsl

        super(MinZoomFromNETest, self).setUp()

        self.lon, self.lat = (-3.2765753, 54.7023545)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/838090640
            dsl.point(838090640, (self.lon, self.lat), {
                'name': u'United Kingdom',
                'place': u'country',
                'population': u'61792000',
                'source': u'openstreetmap.org',
                'wikidata': u'Q145',
                'wikipedia': u'de:United Kingdom',  # LOL, de:
                # NOTE: these aren't in the data from OSM, but are joined at
                # database query time from the Natural Earth data.
                '__ne_min_zoom': 1.7,
                '__ne_max_zoom': 6.7,
            }),
        )

    def test_uk_should_show_up_zooms_2_to_6(self):
        from tilequeue.tile import deg2num
        # should show up in zooms within the range 2-6

        for zoom in xrange(2, 6):
            x, y = deg2num(self.lat, self.lon, zoom)
            self.assert_has_feature(
                zoom, x, y, 'places', {
                    'id': 838090640,
                    'min_zoom': 2.0,
                    'max_zoom': 6.7,
                })

    def test_uk_should_not_show_up_zoom_0_to_1(self):
        from tilequeue.tile import deg2num
        # shouldn't be in the zoom 0 or zoom 1 tiles because min_zoom >= 1.5

        for zoom in xrange(0, 1):
            x, y = deg2num(self.lat, self.lon, zoom)
            self.assert_no_matching_feature(
                zoom, x, y, 'places', {'id': 838090640})

    def test_uk_should_not_show_up_zoom_7(self):
        # shouldn't be in the zoom 7 tile because max_zoom < 7
        from tilequeue.tile import deg2num

        zoom = 7
        x, y = deg2num(self.lat, self.lon, zoom)
        self.assert_no_matching_feature(
            zoom, x, y, 'places', {'id': 838090640})


class MinZoomFromAdminAreaBasedDefault(FixtureTest):

    def test_united_kingdom(self):
        # in the absence of data joined from NE, we should fall back to a
        # default based on the country that the label point is in.
        import dsl
        from tilequeue.tile import deg2num

        lon, lat = (-3.2765753, 54.7023545)
        z = 6
        x, y = deg2num(lat, lon, z)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/node/838090640
            dsl.point(838090640, (lon, lat), {
                'name': u'United Kingdom',
                'place': u'country',
                'population': u'61792000',
                'source': u'openstreetmap.org',
                'wikidata': u'Q145',
                'wikipedia': u'de:United Kingdom',  # LOL, de:
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 838090640,
                'min_zoom': 6,
                'max_zoom': 6.7,
            })

    def test_ne_min_zoom_should_override_default(self):
        import dsl
        from tilequeue.tile import deg2num

        lon, lat = (-3.2765753, 54.7023545)
        z = 5
        x, y = deg2num(lat, lon, z)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/node/838090640
            dsl.point(838090640, (lon, lat), {
                'name': u'United Kingdom',
                'place': u'country',
                'population': u'61792000',
                'source': u'openstreetmap.org',
                'wikidata': u'Q145',
                'wikipedia': u'de:United Kingdom',  # LOL, de:
                # NE joins should override defaults from location
                '__ne_min_zoom': 0,
                '__ne_max_zoom': 16,
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 838090640,
                'min_zoom': 0,
                'max_zoom': 16,
            })

    def test_wales(self):
        # wales is a country within the UK, but mapped as place=state.
        # should get a fallback from the states_provinces spreadsheet.
        import dsl

        z, x, y = (10, 501, 336)

        self.generate_fixtures(
            dsl.is_in('GB', z, x, y),
            # https://www.openstreetmap.org/node/2642288017
            dsl.point(2642288017, (-3.73893, 52.2928116), {
                'is_in': u'United Kingdom, Europe',
                'name': u'Wales',
                'note': u'geographical centre of Wales',
                'place': u'state',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 2642288017,
                'min_zoom': 10,
                'max_zoom': 11,
            })
