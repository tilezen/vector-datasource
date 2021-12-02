from . import FixtureTest


class BusinessAndSpurRoutes(FixtureTest):

    def _check_route_relation(
            self, rel_id, way_id, tile, shield_text, network):
        z, x, y = map(int, tile.split('/'))

        self.load_fixtures([
            'https://www.openstreetmap.org/relation/%d' % (rel_id,),
        ], clip=self.tile_bbox(z, x, y))

        # check that First Capitol Dr, part of the above relation, is given
        # a network that includes the "business" extension.
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': way_id, 'shield_text': shield_text, 'network': network})

    def test_first_capitol_dr_i70_business(self):
        import dsl
        z, x, y = 16, 16294, 25097

        self.generate_fixtures(
            dsl.way(12276055, dsl.tile_diagonal(16, 16294, 25097), {
                'source': 'openstreetmap.org',
                'highway': 'primary',
                'name': 'First Capitol Drive',
                'ref': 'I 70 Business;MO 94',
                'tiger:cfcc': 'A25',
                'tiger:county': 'St. Charles, MO',
                'tiger:name_base': 'First Capitol',
                'tiger:name_base_2': 'I-70 (Loop)',
                'tiger:name_type': 'Dr',
                'tiger:reviewed': 'no',
                'tiger:zip_left': '63301',
                'tiger:zip_right': '63301'
            }),
            dsl.relation(1933234, {
                'source': 'openstreetmap.org',
                'is_in:state': 'MO',
                'modifier': 'Business',
                'name': 'I 70 Business (St. Charles, MO)',
                'network': 'US:I',
                'ref': '70',
                'route': 'road',
                'type': 'route'
            }, ways=[12276055]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 12276055, 'shield_text': '70', 'network': 'US:I:Business'})

    def test_business_loop(self):
        self._check_route_relation(
            1935116, 5807439, '16/12285/23316', '15', 'US:I:Business:Loop')

    def test_nj_essex(self):
        self._check_route_relation(
            945855, 221295008, '16/19267/24623', '672', 'US:NJ:Essex:Spur')

    def test_nj_cr(self):
        self._check_route_relation(
            941526, 60523740, '16/19192/24767', '526', 'US:NJ:CR:Spur')
