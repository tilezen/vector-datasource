# -*- encoding: utf-8 -*-
from . import FixtureTest


# test that features get assigned the correct collision rank.
#
# note that the collision rank system has been designed to make changing ranks
# and re-arranging / re-ordering very easy. in turn, this might make these
# tests very fragile because they check the exact number which is assigned as
# the rank.
#
# if updating these after every change becomes onerous, consider only testing
# important salient values (e.g: the first ones after an important reserved
# block) and switching the other tests to relative, as in CollisionOrderTest
#
class CollisionRankTest(FixtureTest):

    def _check_rank(self, tags, zoom=16, source='openstreetmap.org',
                    layer='pois', kind=None, rank=None, geom_type='point'):
        import dsl

        z, x, y = (zoom, 0, 0)

        all_tags = tags.copy()
        all_tags['source'] = source
        if 'name' not in all_tags:
            all_tags['name'] = 'Some name'

        assert geom_type in ('point', 'line', 'polygon')
        if geom_type == 'point':
            shape = dsl.tile_centre_shape(z, x, y)
        elif geom_type == 'line':
            shape = dsl.tile_diagonal(z, x, y)
        elif geom_type == 'polygon':
            shape = dsl.tile_box(z, x, y)

        self.generate_fixtures(dsl.way(1, shape, all_tags))

        self.assert_has_feature(
            z, x, y, layer, {
                'kind': kind,
                'collision_rank': rank,
            })

    def test_continent(self):
        self._check_rank(
            {'place': 'continent'},
            zoom=1, layer='earth',
            kind='continent', rank=300)

    def test_transit_subway(self):
        self._check_rank(
            {'route': 'subway'},
            geom_type='line',
            layer='transit',
            kind='subway', rank=765)

    def test_pois_swimming_area(self):
        self._check_rank(
            {'leisure': 'swimming_area'},
            layer='pois',
            kind='swimming_area', rank=3099)

    def test_pois_battlefield(self):
        self._check_rank(
            {'historic': 'battlefield'},
            layer='pois',
            kind='battlefield', rank=546)

    def test_pois_picnic_site(self):
        self._check_rank(
            {'tourism': 'picnic_site'},
            layer='pois', kind='picnic_site',
            rank=3097)

    def test_water_ocean(self):
        self._check_rank(
            {'place': 'ocean'},
            layer='water', kind='ocean',
            rank=301)

    def test_pois_water_park(self):
        self._check_rank(
            {'leisure': 'water_park'},
            layer='pois', kind='water_park',
            rank=1155)

    def test_pois_fast_food(self):
        self._check_rank(
            {'amenity': 'fast_food'},
            layer='pois', kind='fast_food',
            rank=1156)

    def test_pois_chemist(self):
        self._check_rank(
            {'shop': 'chemist'},
            layer='pois', kind='chemist',
            rank=1257)

    def test_pois_cafe(self):
        self._check_rank(
            {'amenity': 'cafe'},
            layer='pois', kind='cafe',
            rank=1894)

    def test_pois_doityourself(self):
        self._check_rank(
            {'shop': 'doityourself'},
            layer='pois', kind='doityourself',
            rank=1071)

    def test_pois_shelter(self):
        self._check_rank(
            {'amenity': 'shelter'},
            layer='pois', kind='shelter',
            rank=3123)

    def test_transit_station(self):
        self._check_rank(
            {'railway': 'station'},
            geom_type='polygon',
            layer='transit', kind='station',
            rank=3747)

    def test_pois_aviary(self):
        self._check_rank(
            {'zoo': 'aviary'},
            layer='pois', kind='aviary',
            rank=3309)

    def test_pois_travel_agent(self):
        self._check_rank(
            {'office': 'travel_agent'},
            layer='pois', kind='travel_agent',
            rank=3745)

    def test_pois_aerodrome(self):
        self._check_rank(
            {'aeroway': 'aerodrome'},
            layer='pois', kind='aerodrome',
            rank=493)

    def test_pois_caravan_site(self):
        self._check_rank(
            {'tourism': 'caravan_site'},
            layer='pois', kind='caravan_site',
            rank=1354)

    def test_water_riverbank(self):
        self._check_rank(
            {'waterway': 'riverbank'},
            geom_type='line',
            layer='water', kind='riverbank',
            rank=2372)

    def test_pois_wood(self):
        self._check_rank(
            {'landuse': 'wood'},
            geom_type='polygon',
            layer='pois', kind='wood',
            rank=500)

    def test_landuse_industrial(self):
        self._check_rank(
            {'landuse': 'industrial'},
            geom_type='polygon',
            layer='landuse', kind='industrial',
            rank=2849)

    def test_pois_tobacco(self):
        self._check_rank(
            {'shop': 'tobacco'},
            layer='pois', kind='tobacco',
            rank=3743)

    def test_pois_healthcare_centre(self):
        self._check_rank(
            {'healthcare': 'centre'},
            layer='pois', kind='healthcare_centre',
            rank=3445)

    def test_pois_generator(self):
        self._check_rank(
            {'power': 'generator'},
            layer='pois', kind='generator',
            rank=2703)

    def test_pois_post_box(self):
        self._check_rank(
            {'amenity': 'post_box'},
            layer='pois', kind='post_box',
            rank=4318)

    def test_landuse_grass(self):
        self._check_rank(
            {'landuse': 'grass'},
            geom_type='polygon',
            layer='landuse', kind='grass',
            rank=2901)

    def test_non_maritime_boundary(self):
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import LineString
        from ModestMaps.Core import Coordinate
        import dsl

        z, x, y = (8, 44, 88)

        left_props = {
            'source': 'openstreetmap.org',
            'boundary': 'administrative',
            'admin_level': '2',
            'name': 'Country 1',
            'mz_boundary_from_polygon': True,  # need this for hack
        }
        right_props = {
            'source': 'openstreetmap.org',
            'boundary': 'administrative',
            'admin_level': '2',
            'name': 'Country 2',
            'mz_boundary_from_polygon': True,  # need this for hack
        }

        minx, miny, maxx, maxy = coord_to_bounds(
            Coordinate(zoom=z, column=x, row=y))

        # move the coordinate points slightly out of the tile, so that we
        # don't get borders along the sides of the tile.
        w = maxx - minx
        h = maxy - miny
        minx -= 0.5 * w
        miny -= 0.5 * h
        maxx += 0.5 * w
        maxy += 0.5 * h

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'source': 'tilezen.org',
                'maritime_boundary': True,
                'min_zoom': 0,
                'kind': 'maritime',
            }),
            dsl.way(
                1,
                LineString([
                    [minx, miny],
                    [minx, maxy],
                    [maxx, maxy],
                    [minx, miny],
                ]),
                left_props,
            ),
            dsl.way(
                2,
                LineString([
                    [minx, miny],
                    [maxx, maxy],
                    [maxx, miny],
                    [minx, miny],
                ]),
                right_props,
            ),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'maritime_boundary': type(None),
                'collision_rank': 807,
            })

    def test_maritime_boundary(self):
        import dsl

        z, x, y = (8, 44, 88)

        self.generate_fixtures(
            dsl.way(2, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'name': 'Country 1',
                'boundary': 'administrative',
                'admin_level': '2',
                'mz_boundary_from_polygon': True,  # need this for hack
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'kind': 'country',
                'maritime_boundary': True,
                'collision_rank': 2375,
            })


# helper class to make it easier to write CollisionOrderTest.
#
# creates items, identified by their unique ID, and makes a tile based on them.
# the tile is then checked to make sure the collision_rank assigned each
# feature is the same as the order of IDs passed in from the test.
class ItemList(object):

    def __init__(self, test_instance, zoom=16, x=0, y=0):
        self.test_instance = test_instance
        self.items = []
        self.id_counter = 1
        self.z = zoom
        self.x = x
        self.y = y

    def append(self, tags={}, source='openstreetmap.org', layer='pois',
               geom_type='point'):
        import dsl

        all_tags = tags.copy()
        all_tags['source'] = source
        if 'name' not in all_tags:
            all_tags['name'] = 'Some name'

        assert geom_type in ('point', 'line', 'polygon')
        if geom_type == 'point':
            shape = dsl.tile_centre_shape(self.z, self.x, self.y)
        elif geom_type == 'line':
            shape = dsl.tile_diagonal(self.z, self.x, self.y)
        elif geom_type == 'polygon':
            shape = dsl.tile_box(self.z, self.x, self.y)

        item_fid = self.id_counter
        self.id_counter += 1

        self.items.append(dsl.way(item_fid, shape, all_tags))
        return item_fid

    def assert_order(self, order):
        self.test_instance.generate_fixtures(*self.items)

        items = {}

        with self.test_instance.tile(self.z, self.x, self.y) as layers:
            for layer_name, features in layers.iteritems():
                for feature in features:
                    fid = feature['properties']['id']
                    rank = feature['properties']['collision_rank']
                    assert fid not in items
                    items[fid] = rank

        self.test_instance.assertTrue(items, msg="Expected some items, but "
                                      "received an empty tile.")
        # note that we only get inside this "if" statement if we're in
        # "download only" mode, as it short-circuits the assertions.
        # otherwise a genuinely empty tile would have triggered the assertion
        # already.
        #
        # i'm really looking forward to the day when we remove all
        # non-generative fixtures, and we can remove this hack too!
        if not items:
            return

        rank = 0
        for item_fid in order:
            self.test_instance.assertTrue(
                item_fid in items, msg="Item %d missing from items seen in "
                "tile (%r), perhaps it wasn't correctly matched?"
                % (item_fid, items.keys()))
            item_rank = items[item_fid]
            self.test_instance.assertTrue(
                item_rank > rank, msg="Item ranks lower than previous items "
                "in the list. (%d <= %d)" % (item_rank, rank))
            rank = item_rank


# a more robust way to do the tests: rather than check the exact value of the
# collision_rank, we can check that one kind has a rank value more or less than
# another. this is closer to a long term meaning of collision priority; that
# some features should be displayed in preference to others.
#
class CollisionOrderTest(FixtureTest):

    # example of a more robust test: it doesn't matter exactly what the
    # collision_rank of fuel or police is, what matters is that fuel's rank
    # is less than police's.
    def test_fuel_before_police(self):
        items = ItemList(self)

        # set up all the test items
        police = items.append(tags={'amenity': 'police'})
        fuel = items.append(tags={'amenity': 'fuel'})

        items.assert_order([fuel, police])


# we should only apply a collision_rank where there's a label, so the feature
# should either be a PONI (POI with no name) or a named feature. we also extend
# this to include shield text and ref.
class WhereTest(FixtureTest):

    def test_toilets(self):
        # toilets are PONIs - we want to see an icon on the map even if it's
        # not a famous enough set of facilities that it got a name.
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'amenity': 'toilets',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'kind': 'toilets',
                'collision_rank': int,
            })

    def test_road_no_name_no_shield(self):
        # we'll only need a collision rank on a road if it has some form of
        # label, which means a name, ref, shield_text or one of the shield
        # text variants. if it has none of them, we still want the feature,
        # but no the collision_rank.
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'unclassified',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'kind': 'minor_road',
                'collision_rank': type(None),
            })

    def test_road_ref(self):
        # if the road has no name and no shield text, but does have a ref, then
        # we want to keep it.
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'unclassified',
                'ref': '1',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'kind': 'minor_road',
                'name': type(None),
                'shield_text': type(None),
                'ref': '1',
                'collision_rank': int,
            })

    def test_road_shield_text(self):
        # if the road has no name, but does have a shield, then we want to give
        # it a collision_rank.
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.is_in('US', z, x, y),
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'motorway',
                'source': 'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': 'US-I',
                'ref': '101',
                'type': 'route',
                'route': 'road',
            }, ways=[1]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'kind': 'highway',
                'name': type(None),
                'shield_text': '101',
                'collision_rank': int,
            })
