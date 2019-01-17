# -*- encoding: utf-8 -*-
from . import FixtureTest


class HgvTest(FixtureTest):

    def test_low_emission_zone_way(self):
        import dsl

        z, x, y = (13, 4212, 2702)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/373249337
            dsl.way(373249337, dsl.box_area(z, x, y, 8608219), {
                'boundary': 'low_emission_zone',
                'name': 'Milieuzone Utrecht',
                'source': 'openstreetmap.org',
                'website': 'http://www.utrecht.nl/verkeersbeleid/milieuzone/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 373249337,
                'min_zoom': lambda z: 12 <= z < 13,
                'kind': 'low_emission_zone',
            })
