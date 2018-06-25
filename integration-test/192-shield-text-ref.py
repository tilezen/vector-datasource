from . import FixtureTest


class ShieldTextRef(FixtureTest):

    def test_james_lick_freeway(self):
        # US 101, "James Lick Freeway"
        self.load_fixtures([
            'http://www.openstreetmap.org/way/27183379',
            'http://www.openstreetmap.org/relation/108619',
        ], clip=self.tile_bbox(16, 10484, 25334))
        self.assert_has_feature(
            16, 10484, 25334, 'roads',
            {'kind': 'highway', 'network': 'US:US', 'id': 27183379,
             'shield_text': '101'})

    def test_multiple_shields(self):
        import dsl

        z, x, y = 16, 18022, 25522

        # I-77, I-81, US-11 & US-52 all in one road West Virginia.
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'US',
                'source': 'openstreetmap.org'
            }),
            # http://www.openstreetmap.org/way/51388984
            dsl.way(51388984, dsl.tile_diagonal(z, x, y), {
                'horse': 'no', 'maxspeed': '70 mph', 'bicycle': 'no',
                'source': 'openstreetmap.org', 'hgv': 'designated',
                'surface': 'asphalt', 'oneway': 'yes', 'foot': 'no',
                'lanes': '3', 'sidewalk': 'none',
                'ref': 'I 77;I 81;US 11;US 52', 'highway': 'motorway'
            }),
            dsl.relation(1, {
                'name': 'US 11 (VA)', 'type': 'route', 'route': 'road',
                'wikipedia': 'en:U.S. Route 11', 'is_in:state': 'VA',
                'source': 'openstreetmap.org', 'wikidata': 'Q407534',
                'ref': '11', 'network': 'US:US'
            }, ways=[51388984]),
            dsl.relation(2, {
                'name': 'I 77 (VA) (North)', 'type': 'route', 'route': 'road',
                'wikipedia': 'en:Interstate 77 in Virginia',
                'is_in:state': 'VA', 'source': 'openstreetmap.org',
                'wikidata': 'Q2447354', 'ref': '77', 'network': 'US:I'
            }, ways=[51388984]),
            dsl.relation(3, {
                'direction': 'south', 'name': 'I 81 (VA southbound)',
                'type': 'route', 'route': 'road',
                'wikipedia': 'en:Interstate 81 in Virginia',
                'is_in:state': 'VA', 'source': 'openstreetmap.org',
                'wikidata': 'Q2447647', 'ref': '81', 'network': 'US:I'
            }, ways=[51388984]),
            dsl.relation(4, {
                'name': 'US 52 (VA)', 'type': 'route', 'route': 'road',
                'wikipedia': 'en:U.S. Route 52', 'is_in:state': 'VA',
                'source': 'openstreetmap.org', 'ref': '52', 'network': 'US:US'
            }, ways=[51388984]),
        )

        self.assert_has_feature(
            16, 18022, 25522, 'roads',
            {'kind': 'highway', 'network': 'US:I', 'id': 51388984,
             'shield_text': '77',
             'all_networks': ['US:I', 'US:I', 'US:US', 'US:US'],
             'all_shield_texts': ['77', '81', '11', '52']})

    def test_network_without_ref(self):
        # routes with network but no ref should return a null ref.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/4069015',
            'http://www.openstreetmap.org/relation/6080335',
        ], clip=self.tile_bbox(16, 14852, 26071))
        self.assert_has_feature(
            16, 14852, 26071, 'roads',
            {'kind': 'highway', 'id': 290908536,
             'all_networks': ['US:I', 'US:OK:Turnpike'],
             'all_shield_texts': ['44', type(None)]})
