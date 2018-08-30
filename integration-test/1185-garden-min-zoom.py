# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class GardenMinZoom(FixtureTest):
    def test_very_small_garden(self):
        # this garden previously had a min_zoom of 12, but based on its size
        # should be z16 instead.
        self.generate_fixtures(dsl.way(273274870, wkt_loads('POLYGON ((-3.21498191780828 55.95510687265239, -3.214945985196921 55.95512180922219, -3.21470002647213 55.95521167997651, -3.21469032466706 55.95521600503268, -3.21460184061157 55.95515389516738, -3.21486163339174 55.95505728521119, -3.21493475625587 55.9550301780537, -3.21495829211631 55.9550474783568, -3.2149060999983 55.95507176917629, -3.214947242838309 55.9550993792197, -3.21496107689369 55.95509289161558, -3.21498191780828 55.95510687265239))'), {u'access': u'private', u'source': u'openstreetmap.org', u'way_area': u'624.137', u'leisure': u'garden'}))  # noqa

        self.assert_has_feature(
            16, 32182, 20422, 'landuse',
            {'kind': 'garden', 'id': 273274870, 'min_zoom': 16, 'tier': 6})

        # shouldn't be a POI now as it has no name.
        self.assert_no_matching_feature(
            16, 32182, 20422, 'pois',
            {'kind': 'garden'})

    def test_small_named_garden(self):
        # instead, here's a small, named garden
        self.generate_fixtures(dsl.way(162235630, wkt_loads('POLYGON ((-73.96195698819621 40.68120769466639, -73.96188341617439 40.68141737870257, -73.9618302359096 40.681406683334, -73.96190371809979 40.68119699926421, -73.96195698819621 40.68120769466639))'), {u'source': u'openstreetmap.org', u'way_area': u'195.222', u'name': u"Brooklyn's Finest Garden", u'leisure': u'garden'}))  # noqa

        self.assert_has_feature(
            16, 19303, 24647, 'pois',
            {'kind': 'garden', 'id': 162235630, 'min_zoom': 16, 'tier': 6})
