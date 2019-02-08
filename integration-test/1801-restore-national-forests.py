# -*- encoding: utf-8 -*-
from . import FixtureTest


class ForestTest(FixtureTest):

    def test_tahoe_national_forest(self):
        import dsl

        z, x, y = (7, 21, 48)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/972004
            dsl.way(972004, dsl.box_area(z, x, y, 8124122989), {
                'attribution': 'USDA-Forest Service, Pacific Southwest Region',
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'name': 'Tahoe National Forest',
                'name:de': 'Nationalforst Tahoe',
                'operator': 'United States Forest Service',
                'ownership': 'national',
                'protect_class': '6',
                'protected': 'perpetuity',
                'protection_title': 'National Forest',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'website': 'http://www.r5.fs.fed.us/tahoe/',
                'wikidata': 'Q3079156',
                'wikipedia': 'en:Tahoe National Forest',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 972004,
                'kind': 'forest',
                'min_zoom': 7,
            })
