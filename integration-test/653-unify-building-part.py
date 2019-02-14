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
        import dsl
        from shapely.wkt import loads as wkt_loads

        # Relation: Ferry Building
        # note: the relation includes the ways with the IDs tested below.
        self.generate_fixtures(
            dsl.way(558731934, wkt_loads(
                'POLYGON (('
                '-122.3943195 37.79614009995349, '
                '-122.3941179 37.79592239995348, '
                '-122.393776 37.79555339995338, '
                '-122.3938404 37.79551619995339, '
                '-122.3937117 37.79537719995337, '
                '-122.3935595 37.79521299995339, '
                '-122.3934953 37.79525009995339, '
                '-122.3931776 37.7949072999533, '
                '-122.3929673 37.79468029995329, '
                '-122.3928191 37.79476609995328, '
                '-122.3925072 37.79494659995339, '
                '-122.3927175 37.79517349995338, '
                '-122.3930756 37.79556009995338, '
                '-122.3931871 37.79568039995348, '
                '-122.393513 37.79603209995351, '
                '-122.3936579 37.7961884999535, '
                '-122.3938596 37.79640619995361, '
                '-122.3941735 37.79622449995349, '
                '-122.3943195 37.79614009995349))'
            ), {
                u'shop': u'mall',
                u'amenity': u'ferry_terminal',
                u'gnis:county_name': u'San Francisco',
                u'name:ko': u'\ud398\ub9ac \ube4c\ub529',
                u'height': u'83.1',
                u'historic': u'landmark',
                u'wikidata': u'Q1408117',
                u'name': u'Ferry Building',
                u'addr:housenumber': u'1',
                u'addr:city': u'San Francisco',
                u'gnis:reviewed': u'no',
                u'addr:housename': u'Ferry Building',
                u'building': u'terminal',
                u'addr:state': u'CA',
                u'ele': u'1',
                u'source': u'openstreetmap.org',
                u'addr:postcode': u'94111',
                u'gnis:feature_id': u'223477',
                u'type': u'building',
            }),
            dsl.way(406710839, wkt_loads(
                'POLYGON (('
                '-122.3936092 37.79544279995339, '
                '-122.3936089 37.7954418999534, '
                '-122.3936082 37.79544109995338, '
                '-122.3936073 37.79544059995339, '
                '-122.3936063 37.7954402999534, '
                '-122.3936051 37.7954402999534, '
                '-122.3936041 37.79544059995339, '
                '-122.3936032 37.79544119995339, '
                '-122.3936026 37.7954418999534, '
                '-122.3936023 37.79544279995339, '
                '-122.3936024 37.7954436999534, '
                '-122.3936029 37.79544449995338, '
                '-122.3936036 37.79544509995339, '
                '-122.3936046 37.79544559995339, '
                '-122.3936057 37.79544569995338, '
                '-122.3936068 37.79544559995339, '
                '-122.3936078 37.79544509995339, '
                '-122.3936086 37.79544449995338, '
                '-122.3936091 37.7954435999534, '
                '-122.3936092 37.79544279995339))'
            ), {
                u'building:part': u'yes',
                u'source': u'openstreetmap.org',
                u'height': u'83.1 m',
            }),
            dsl.way(406710838, wkt_loads(
                'POLYGON (('
                '-122.3936199 37.79544339995338, '
                '-122.3936194 37.79543979995341, '
                '-122.3936176 37.79543649995337, '
                '-122.3936145 37.79543389995337, '
                '-122.3936105 37.79543209995339, '
                '-122.3936056 37.79543139995339, '
                '-122.3936008 37.7954319999534, '
                '-122.3935965 37.79543389995337, '
                '-122.3935932 37.79543679995339, '
                '-122.3935914 37.79544049995339, '
                '-122.3935912 37.79544429995338, '
                '-122.3935927 37.79544809995338, '
                '-122.3935956 37.79545119995338, '
                '-122.3935997 37.79545329995339, '
                '-122.3936045 37.7954541999534, '
                '-122.3936091 37.79545389995341, '
                '-122.3936133 37.79545249995339, '
                '-122.3936167 37.79545009995339, '
                '-122.393619 37.79544689995338, '
                '-122.3936199 37.79544339995338))'
            ), {
                u'source': u'openstreetmap.org',
                u'roof:shape': u'dome',
                u'building:part': u'yes',
                u'height': u'70 m',
            }),
            dsl.way(406710837, wkt_loads(
                'POLYGON (('
                '-122.3936287 37.79544329995338, '
                '-122.3936278 37.7954376999534, '
                '-122.3936248 37.79543259995341, '
                '-122.39362 37.7954283999534, '
                '-122.3936138 37.79542569995341, '
                '-122.3936068 37.79542449995338, '
                '-122.3935997 37.79542509995339, '
                '-122.3935925 37.79542779995338, '
                '-122.3935869 37.7954321999534, '
                '-122.3935835 37.7954378999534, '
                '-122.3935828 37.79544419995339, '
                '-122.3935848 37.79545029995339, '
                '-122.3935894 37.7954554999534, '
                '-122.3935959 37.79545909995339, '
                '-122.3936035 37.79546079995339, '
                '-122.3936115 37.7954601999534, '
                '-122.3936187 37.79545759995338, '
                '-122.3936239 37.79545379995338, '
                '-122.3936273 37.79544879995338, '
                '-122.3936287 37.79544329995338))'
            ), {
                u'building:part': u'yes',
                u'source': u'openstreetmap.org',
                u'height': u'68.2 m',
            }),
            dsl.way(406710836, wkt_loads(
                'POLYGON (('
                '-122.3936436 37.79544799995338, '
                '-122.393612 37.79541359995338, '
                '-122.3935665 37.79543819995339, '
                '-122.3935976 37.7954731999534, '
                '-122.3936436 37.79544799995338))'
            ), {
                u'building:part': u'yes',
                u'source': u'openstreetmap.org',
                u'height': u'64.5 m',
            }),
            dsl.way(406710835, wkt_loads(
                'POLYGON (('
                '-122.393655 37.79545069995338, '
                '-122.3936127 37.7954034999534, '
                '-122.3935557 37.7954352999534, '
                '-122.3935959 37.79548299995339, '
                '-122.393655 37.79545069995338))'
            ), {
                u'building:part': u'yes',
                u'source': u'openstreetmap.org',
                u'height': u'60.5 m',
            }),
            dsl.way(406710834, wkt_loads(
                'POLYGON (('
                '-122.393671 37.79545169995338, '
                '-122.3936161 37.79539129995338, '
                '-122.393541 37.7954341999534, '
                '-122.3935926 37.79549459995339, '
                '-122.393671 37.79545169995338))'
            ), {
                u'building:part': u'yes',
                u'source': u'openstreetmap.org',
                u'height': u'54.2 m',
            }),
            dsl.way(406710833, wkt_loads(
                'POLYGON (('
                '-122.3936878 37.7954564999534, '
                '-122.3936147 37.79537329995339, '
                '-122.3935202 37.79542729995338, '
                '-122.3935933 37.79550739995337, '
                '-122.3936878 37.7954564999534))'
            ), {
                u'building:part': u'yes',
                u'source': u'openstreetmap.org',
                u'height': u'50.5 m',
            }),
            dsl.way(404449724, wkt_loads(
                'POLYGON (('
                '-122.3936972 37.79545779995338, '
                '-122.3936167 37.79536829995339, '
                '-122.3935128 37.7954270999534, '
                '-122.3935926 37.79551349995339, '
                '-122.3936972 37.79545779995338))'
            ), {
                u'building:part': u'yes',
                u'source': u'openstreetmap.org',
                u'height': u'43.5 m',
            }),
            dsl.way(24460886, wkt_loads(
                'POLYGON (('
                '-122.3943195 37.79614009995349, '
                '-122.3941179 37.79592239995348, '
                '-122.393776 37.79555339995338, '
                '-122.3938404 37.79551619995339, '
                '-122.3937117 37.79537719995337, '
                '-122.3935595 37.79521299995339, '
                '-122.3934953 37.79525009995339, '
                '-122.3931776 37.7949072999533, '
                '-122.3929673 37.79468029995329, '
                '-122.3928191 37.79476609995328, '
                '-122.3925072 37.79494659995339, '
                '-122.3927175 37.79517349995338, '
                '-122.3930756 37.79556009995338, '
                '-122.3931871 37.79568039995348, '
                '-122.393513 37.79603209995351, '
                '-122.3936579 37.7961884999535, '
                '-122.3938596 37.79640619995361, '
                '-122.3941735 37.79622449995349, '
                '-122.3943195 37.79614009995349))'
            ), {
                u'building:part': u'yes',
                u'source': u'openstreetmap.org',
                u'height': u'16.1',
            }),
            dsl.relation(6062613, {
                'source': 'openstreetmap.org',
                'type': 'building',
            }, ways=[
                558731934,
                24460886,
                404449724,
                406710833,
                406710834,
                406710836,
                406710838,
                406710837,
                406710839,
                406710835,
            ]),
        )

        self.assert_has_feature(
            16, 10486, 25326, 'buildings',
            {'id': 558731934, 'kind': 'building', 'root_id': type(None)})

        self.assert_has_feature(
            16, 10486, 25326, 'buildings',
            {'id': 404449724, 'kind': 'building_part', 'root_id': 558731934})

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
