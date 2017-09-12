from . import FixtureTest


class ImproveRoadLineMerging(FixtureTest):

    def _assert_is_linestring(self, z, x, y, layer, name,
                              max_coords, max_count):
        with self.features_in_tile_layer(z, x, y, layer) as features:
            self._assert_features_are_linestrings(
                features, name, max_coords, max_count)

    def _assert_features_are_linestrings(self, features, name,
                                         max_coords, max_count):
        count = 0
        total_coords = 0
        for feature in features:
            props = feature['properties']
            if props.get('name') == name:
                # should have been merged to become a single linestring.
                geom_type = feature['geometry']['type']
                self.assertTrue(
                    geom_type in ('LineString', 'MultiLineString'),
                    'Expected linestring, got %r' % geom_type)
                count += 1
                coords = feature['geometry']['coordinates']
                if geom_type == 'LineString':
                    self.assertFalse(
                        len(coords) > max_coords,
                        'Single feature exceeded max coords: %d > %d' %
                        (len(coords), max_coords))
                    total_coords += len(coords)
                else:
                    for line in coords:
                        self.assertFalse(
                            len(line) > max_coords,
                            'Single part of multi-feature exceeded max '
                            'coords: %d > %d' % (len(line), max_coords))
                        total_coords += len(line)
        self.assertFalse(
            count > max_count,
            'Expected at most %d features, found %d' % (max_count, count))
        self.assertFalse(
            total_coords > max_coords,
            'Expected at most %d coordinates, found %d in total' %
            (max_coords, total_coords))

    def test_pitkin_ave_nyc(self):
        # Pitkin Ave, NYC
        #
        # all of these are teriary roads, so we'd expect them to be merged
        #
        # note that there are 2 Pitkin Ave.s due to cycle path differences
        self.load_fixtures([
            'http://www.openstreetmap.org/way/183794629',
            'http://www.openstreetmap.org/way/221583055',
            'http://www.openstreetmap.org/way/279918415',
            'http://www.openstreetmap.org/way/279918410',
            'http://www.openstreetmap.org/way/473433733',
            'http://www.openstreetmap.org/way/219606150',
        ], clip=self.tile_bbox(11, 603, 770))
        self._assert_is_linestring(
            12, 1207, 1540, 'roads', 'Pitkin Ave.', 19, 9)
        self._assert_is_linestring(
            11, 603, 770, 'roads', 'Pitkin Ave.', 23, 10)

    def test_linden_blvd(self):
        # Linden Blvd, NYC
        #
        # many segments, one road?
        self.load_fixtures([
            'http://www.openstreetmap.org/way/183794593',
            'http://www.openstreetmap.org/way/221698693',
            'http://www.openstreetmap.org/way/420314185',
            'http://www.openstreetmap.org/way/420314186',
            'http://www.openstreetmap.org/way/420314187',
            'http://www.openstreetmap.org/way/420314188',
            'http://www.openstreetmap.org/way/420314189',
            'http://www.openstreetmap.org/way/420314190',
            'http://www.openstreetmap.org/way/420314194',
            'http://www.openstreetmap.org/way/420314195',
            'http://www.openstreetmap.org/way/420314197',
            'http://www.openstreetmap.org/way/420314198',
            'http://www.openstreetmap.org/way/420314200',
            'http://www.openstreetmap.org/way/420314201',
            'http://www.openstreetmap.org/way/420314202',
            'http://www.openstreetmap.org/way/420314203',
            'http://www.openstreetmap.org/way/420314205',
            'http://www.openstreetmap.org/way/420314206',
            'http://www.openstreetmap.org/way/420314208',
            'http://www.openstreetmap.org/way/420314209',
            'http://www.openstreetmap.org/way/420314213',
            'http://www.openstreetmap.org/way/420314215',
            'http://www.openstreetmap.org/way/420314217',
            'http://www.openstreetmap.org/way/420908360',
            'http://www.openstreetmap.org/way/420908361',
            'http://www.openstreetmap.org/way/420908362',
            'http://www.openstreetmap.org/way/420908363',
            'http://www.openstreetmap.org/way/420910104',
            'http://www.openstreetmap.org/way/420910105',
            'http://www.openstreetmap.org/way/420910106',
            'http://www.openstreetmap.org/way/420910107',
            'http://www.openstreetmap.org/way/421092462',
            'http://www.openstreetmap.org/way/421092463',
            'http://www.openstreetmap.org/way/421092464',
            'http://www.openstreetmap.org/way/421092465',
            'http://www.openstreetmap.org/way/421092466',
            'http://www.openstreetmap.org/way/421092467',
            'http://www.openstreetmap.org/way/421092468',
            'http://www.openstreetmap.org/way/421092472',
            'http://www.openstreetmap.org/way/421092475',
            'http://www.openstreetmap.org/way/421092476',
            'http://www.openstreetmap.org/way/421092482',
            'http://www.openstreetmap.org/way/421092484',
            'http://www.openstreetmap.org/way/421092485',
            'http://www.openstreetmap.org/way/421092487',
        ], clip=self.tile_bbox(13, 2413, 3081))

        self._assert_is_linestring(
            13, 2413, 3081, 'roads', 'Linden Blvd.', 23, 8)

    def test_merge_only_same_properties(self):
        # check that we don't merge across linestrings with different
        # properties. in this case, the central section of this road is a
        # bridge. we currently drop the `is_bridge` property on major roads
        # at zoom < 13, so a z13 tile should still have it.
        self.load_fixtures([
            'http://www.openstreetmap.org/way/421314247',
            'http://www.openstreetmap.org/way/421314246',  # bridge
            'http://www.openstreetmap.org/way/9678799',
            # relation for ND 200
            'http://www.openstreetmap.org/relation/1109565',
        ], clip=self.tile_bbox(13, 1865, 2866))

        with self.features_in_tile_layer(13, 1865, 2866, 'roads') as features:
            # looking for features in US:ND 200 - there should be 3 in this
            # tile, and one should be the bridge.
            count_nd_200 = 0
            count_bridge = 0
            for feature in features:
                props = feature['properties']
                if props.get('network') == 'US:ND' and \
                   props.get('shield_text') == '200':
                    # note that we can merge into multilinestrings, so count
                    # each of those individually
                    if feature['geometry']['type'] == 'MultiLineString':
                        count_nd_200 += len(feature['geometry']['coordinates'])
                    else:
                        count_nd_200 += 1
                    if props.get('is_bridge') is True:
                        count_bridge += 1

            self.assertTrue(
                count_nd_200 == 3,
                'Expecting 3 US:ND 200 roads, got %d' % count_nd_200)
            self.assertTrue(
                count_bridge == 1,
                'Expecting one bridge, but got %d' % count_bridge)
