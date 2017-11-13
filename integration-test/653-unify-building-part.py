from . import FixtureTest


def _tile_centre(z, x, y):
    from tilequeue.tile import num2deg
    lat, lon = num2deg(x + 0.5, y + 0.5, z)
    return (lon, lat)


class UnifyBuildingPart(FixtureTest):
    def test_one_madison(self):
        # Way: One Madison
        self.load_fixtures([
            'http://www.openstreetmap.org/way/264768910',  # the building
            'http://www.openstreetmap.org/way/160967738',  # a part
            'http://www.openstreetmap.org/way/160967739',  # a part
        ])

        self.assert_has_feature(
            16, 19298, 24633, 'buildings',
            {'id': 264768910, 'kind': 'building', 'root_id': type(None)})

        self.assert_has_feature(
            16, 19298, 24633, 'buildings',
            {'id': 160967738, 'kind': 'building_part', 'root_id': 264768910})

        self.assert_has_feature(
            16, 19298, 24633, 'buildings',
            {'id': 160967739, 'kind': 'building_part', 'root_id': 264768910})

    def test_ferry_building(self):
        # Relation: Ferry Building
        # note: the relation includes the ways with the IDs tested below.
        self.load_fixtures(['http://www.openstreetmap.org/relation/6062613'])

        self.assert_has_feature(
            16, 10486, 25326, 'buildings',
            {'id': 24460886, 'kind': 'building', 'root_id': type(None)})

        self.assert_has_feature(
            16, 10486, 25326, 'buildings',
            {'id': 404449724, 'kind': 'building_part', 'root_id': 24460886})

    def test_waterloo_station(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/1242762',  # tube and rail
            'http://www.openstreetmap.org/relation/238793',   # tube station
            'http://www.openstreetmap.org/relation/238792',   # building
        ])

        self.assert_has_feature(
            16, 32747, 21793, 'pois',
            {'id': 3638795617, 'root_id': 1242762,
             'root_relation_id': type(None)})

        self.assert_has_feature(
            16, 32747, 21793, 'pois',
            {'id': 3638795618, 'root_id': 1242762,
             'root_relation_id': type(None)})

    def test_generic_station_hierarchy(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.point(1, _tile_centre(z, x, y), {
                'railway': 'station',
                'name': 'Foo Station',
            }),
            dsl.relation(2, {
                'type': 'site',
                'site': 'public_transport',
            }, nodes=[1]),
        )

        # NOTE: the check for 'root_relation_id' = None is because this
        # property was renamed to 'root_id' and therefore the old key should
        # not be used any more.
        self.assert_has_feature(
            z, x, y, 'pois',
            {'id': 1, 'kind': 'station', 'root_id': 2,
             'root_relation_id': type(None)})
