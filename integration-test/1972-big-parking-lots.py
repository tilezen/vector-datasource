# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads
from tilequeue.tile import deg2num

from . import FixtureTest


def _tile_centre(z, x, y):
    from tilequeue.tile import num2deg
    lat, lon = num2deg(x + 0.5, y + 0.5, z)
    return (lon, lat)


class BigParkingLotsTest(FixtureTest):

    def test_osm_big_parking_capacity(self):
        lon, lat = (8.9140471, 48.8352716)
        self.generate_fixtures(
            dsl.point(8712714905, (lon, lat), {
                u'amenity': u'parking',
                u'capacity': u'6472217472217',
                u'parking': u'surface',
                u'source': u'openstreetmap.org',
            })
        )

        x, y = deg2num(lat, lon, 16)
        self.assert_has_feature(
            16, x, y, 'pois', {
                'id': 8712714905,
                'kind': 'parking',
                'min_zoom': 18,
                'source': u'openstreetmap.org',
            })
