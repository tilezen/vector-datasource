from . import FixtureTest


class LanduseTier(FixtureTest):
    def test_large_national_park(self):
        # area 1.75564e+10
        import dsl

        z, x, y = (6, 12, 23)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/1453306
            dsl.way(-1453306, dsl.box_area(z, x, y, 17556377754), {
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'gnis:feature_id': '1609331',
                'heritage': '1',
                'heritage:operator': 'whc',
                'leisure': 'nature_reserve',
                'name': 'Yellowstone National Park',
                'name:sk': u'Yellowstonsk\xfd n\xe1rodn\xfd park',
                'operator': 'United States National Park Service',
                'ownership': 'national',
                'protect_id': '2',
                'protected': 'perpetuity',
                'protection_title': 'National Park',
                'ref:whc': '28',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'website': 'http://www.nps.gov/yell/',
                'whc:criteria': '(vii)(viii)(ix)(x)',
                'whc:inscription_date': '1978',
                'wikidata': 'Q351',
                'wikipedia': 'en:Yellowstone National Park',
            }),
        )

        # zoom 3
        self.assert_has_feature(
            z-3, x//8, y//8, 'landuse',
            {'kind': 'national_park', 'id': -1453306, 'tier': 1,
             'min_zoom': 3})

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'national_park', 'id': -1453306, 'tier': 1,
             'min_zoom': 5})

    def test_national_park(self):
        import dsl

        z, x, y = (8, 56, 118)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/921675
            dsl.way(-921675, dsl.box_area(z, x, y, 39749331), {
                'boundary': 'national_park',
                'is_in:country': 'Mexico',
                'iucn_level': '2',
                'name': 'Parque Nacional El Veladero',
                'protect_id': '5404',
                'protection_title': 'National Park',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wikidata': 'Q9055960',
                'wikipedia': 'es:Parque Nacional El Veladero',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse',
            {'kind': 'national_park', 'tier': 1, 'min_zoom': 8})

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'national_park', 'id': -921675, 'tier': 1,
             'min_zoom': 8})

    def test_national_forest(self):
        # this is USFS, so demoted to tier 2 :-(
        # area 86685400
        self.load_fixtures(['http://www.openstreetmap.org/way/34416231'])

        self.assert_has_feature(
            8, 71, 98, 'landuse',
            {'kind': 'forest', 'id': 34416231,
             'tier': 2, 'min_zoom': 8})

        # this one is clipped by the polygon min_zoom, and so appears at the
        # same level.
        #
        # note that the feature _is_ present in the zoom 8 tile, but gets
        # merged with a nearby feature of the same name, so instead we test
        # this at z9.
        self.assert_has_feature(
            9, 142, 196, 'pois',
            {'kind': 'forest', 'id': 34416231,
             'tier': 2, 'min_zoom': 8})
