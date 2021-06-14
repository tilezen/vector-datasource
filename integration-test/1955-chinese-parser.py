# -*- encoding: utf-8 -*-
import dsl
from . import FixtureTest


class ChineseNameTest(FixtureTest):
    def test_osm_data(self):
        z, x, y = (12, 4646, 3566)

        self.generate_fixtures(
            # https://www.openstreetmap.org/edit?node=26819236#map=19/37.77831/-122.41241
            dsl.point(1, dsl.tile_centre(z, x, y), {
                'name': 'San Francisco',
                'name:zh': '旧金山/三藩市/舊金山',
                'name:zh-Hans': '旧金山',
                'name:zh-Hant': '舊金山',
            })
        )

        self.assert_has_feature(
            z, x, y, "places",
            {"name": "San Francisco"})
