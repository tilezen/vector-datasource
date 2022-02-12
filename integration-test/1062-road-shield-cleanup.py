from . import FixtureTest


class RoadShieldCleanup(FixtureTest):
    def _check_network_relation(
            self, way_id, rel_id, tile, expected_shield_text):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/%d' % (way_id,),
            'https://www.openstreetmap.org/relation/%d' % (rel_id,),
        ], clip=self.tile_bbox(*tile))

        z, x, y = tile
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': way_id, 'shield_text': expected_shield_text})

    def test_A151(self):
        tile = (16, 32949, 22362)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/%d' % (208288552,),
            'https://www.openstreetmap.org/relation/%d' % (1159812,),
        ], clip=self.tile_bbox(*tile))

        z, x, y = tile
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': type(None), 'shield_text': 'A151'})

    def test_E402(self):
        tile = (16, 32975, 22371)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/%d' % (121496753,),
            'https://www.openstreetmap.org/relation/%d' % (88503,),
        ], clip=self.tile_bbox(*tile))

        z, x, y = tile
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': type(None), 'shield_text': 'E402'})

    def test_A52(self):
        self._check_network_relation(
            way_id=358261897, rel_id=5715176, tile=(16, 32416, 21339),
            expected_shield_text='A52')

    def test_M1(self):
        import dsl
        from shapely.wkt import loads as wkt_loads
        z, x, y = 16, 32531, 21377
        self.generate_fixtures(
            dsl.way(3109799, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'lanes': '3',
                'maxspeed:type': 'UK:motorway',
                'highways_england:area': '7',
                'wikipedia': 'en:M1 motorway',
                'operator': 'Highways England',
                'ref': 'M1',
                'proposed:active_traffic_management': 'yes',
                'oneway': 'yes',
                'carriageway_ref': 'A',
                'highway': 'motorway',
                'int_ref': 'E 13',
                'lit': 'yes',
                'maxspeed': '70 mph'
            }),
            dsl.relation(2332838, {
                'wikipedia': 'en:European route E13',
                'wikidata': 'Q1247738',
                'type': 'route',
                'route': 'road',
                'ref': 'E 13',
                'network': 'e-road',
                'e-road:class': 'A-intermediate',
                'description:fr': 'E 13 Doncaster - Londres'
            }, ways=[35568189]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 3109799, 'shield_text': 'M1'})
