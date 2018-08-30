# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class BuildingHeight(FixtureTest):
    def test_from_building_levels(self):
        # check that we synthesize a height value from building:levels
        # Way: R5 Tower A (431358377)
        self.generate_fixtures(dsl.way(431358377, wkt_loads('POLYGON ((127.055528903431 37.25885030044089, 127.056004112216 37.2594416554027, 127.05683658099 37.2590179623059, 127.056361372205 37.25842660401769, 127.055528903431 37.25885030044089))'), {u'building': u'office', u'building:levels': u'25', u'way_area': u'10799.6', u'name': u'R5 Tower A', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 55897, 25449, 'buildings',
            {'id': 431358377, 'height': 77.0, 'kind': 'building',
             'building:levels': type(None), 'building_levels': type(None)})

    def test_min_height_from_min_levels(self):
        self.generate_fixtures(dsl.way(336433763, wkt_loads('POLYGON ((-75.1567581775674 39.9518723960957, -75.156733114571 39.95199318243088, -75.15669017510038 39.95220658946529, -75.15667077149018 39.95231009060419, -75.1564673929099 39.95228529992648, -75.15649012028659 39.95217801127889, -75.1565289275069 39.95200075739349, -75.15656144652019 39.9518483627573, -75.1567581775674 39.9518723960957))'), {u'building:part': u'yes', u'source': u'openstreetmap.org', u'way_area': u'1444.36', u'building:min_levels': u'1'}))  # noqa

        self.assert_has_feature(
            16, 19086, 24821, 'buildings',
            {'id': 336433763, 'min_height': 3.0, 'kind': 'building_part',
             'building_part': type(None), 'building:min_levels': type(None),
             'building_min_levels': type(None)})
