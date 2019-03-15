# -*- encoding: utf-8 -*-
from . import FixtureTest


class Buildings(object):
    def __init__(self, z, x, y, landuse_kind=None):
        from tilequeue.tile import coord_to_mercator_bounds
        from ModestMaps.Core import Coordinate
        import dsl

        bounds = coord_to_mercator_bounds(Coordinate(zoom=z, column=x, row=y))
        self.origin_x = bounds[0]
        self.origin_y = bounds[1]
        self.buildings = []
        self.way_id = 1

        if landuse_kind is not None:
            self.buildings.append(dsl.way(self.way_id, dsl.tile_box(z, x, y), {
                'landuse': landuse_kind,
                'source': 'openstreetmap.org',
            }))
            self.way_id += 1

    # minx, miny, maxx, maxy are in mercator meters from the bottom left
    # corner of the tile, so it's easier to calculate area.
    def add(self, minx, miny, maxx, maxy, height=5, extra_tags={}):
        from dsl import way
        from shapely.geometry import box
        from shapely.ops import transform
        from tilequeue.tile import reproject_mercator_to_lnglat

        shape = box(self.origin_x + minx, self.origin_y + miny,
                    self.origin_x + maxx, self.origin_y + maxy)
        shape_lnglat = transform(reproject_mercator_to_lnglat, shape)

        tags = {
            'source': 'openstreetmap.org',
            'building': 'yes',
        }
        tags.update(extra_tags)

        self.buildings.append(way(self.way_id, shape_lnglat, tags))
        self.way_id += 1


class BuildingScaleRankTest(FixtureTest):

    def _setup_row(self, z, x, y, width, depth, n, height=5, extra_tags={},
                   landuse_kind=None):
        b = Buildings(z, x, y, landuse_kind=landuse_kind)
        for i in xrange(0, n * width, width):
            b.add(i, 0, i + width, depth, height=height, extra_tags=extra_tags)

        self.generate_fixtures(*b.buildings)

    def test_not_merged_z16(self):
        # make a row of buildings, check that they get assigned scale
        # rank and are _not_ merged at z16.
        z, x, y = (16, 0, 0)

        self._setup_row(z, x, y, 10, 40, 10)

        # and there are 10 buildings with scale rank 5
        self.assert_n_matching_features(
            z, x, y, 'buildings', {
                'kind': 'building',
                'scale_rank': 5,
            }, 10)

        # and none with any other scale rank value.
        self.assert_no_matching_feature(
            z, x, y, 'buildings', {
                'scale_rank': (lambda r: r != 5)
            })

    def test_merged_z15(self):
        # make a row of buildings, check that they get assigned scale
        # rank and are merged at z15.
        z, x, y = (15, 0, 0)

        self._setup_row(z, x, y, 10, 40, 10)

        # should be only 1 building feature now
        self.assert_n_matching_features(
            z, x, y, 'buildings', {
                'kind': 'building',
                'scale_rank': 5,
            }, 1)

        # and none with any other scale rank value.
        self.assert_no_matching_feature(
            z, x, y, 'buildings', {
                'scale_rank': (lambda r: r != 5)
            })

    def test_drop_scale_rank_5_at_z14(self):
        # make a row of buildings, check that they get assigned scale
        # rank and are merged at z15.
        z, x, y = (14, 0, 0)

        self._setup_row(z, x, y, 10, 40, 10)

        # scale_rank 5 features should be dropped at this zoom.
        self.assert_no_matching_feature(
            z, x, y, 'buildings', {
                'kind': 'building',
                'scale_rank': 5,
            })

    def test_merged_z14(self):
        # make a row of buildings, check that they get assigned scale
        # rank and are merged at z14.
        z, x, y = (14, 0, 0)

        # z14 area cutoff is 500, so make sure width*depth >= 500, preferably
        # by a margin that means numerical noise won't push it under the
        # threshold.
        self._setup_row(z, x, y, 11, 50, 10, landuse_kind='retail')

        # should be only 1 building feature now
        self.assert_n_matching_features(
            z, x, y, 'buildings', {
                'kind': 'building',
                'scale_rank': 4,
            }, 1)

        # and none with any other scale rank value.
        self.assert_no_matching_feature(
            z, x, y, 'buildings', {
                'scale_rank': (lambda r: r != 4)
            })

    def test_tiny_shed_z17(self):
        # check that a tiny shed, assigned zoom 17 in the buildings.yaml,
        # doesn't get re-assigned a lower zoom. it should stay at z17.
        z, x, y = (16, 0, 0)

        # make one 1x1m building.
        self._setup_row(z, x, y, 1, 1, 1)

        self.assert_n_matching_features(
            z, x, y, 'buildings', {
                'kind': 'building',
                'min_zoom': 17,
            }, 1)

    def test_slightly_larger_outbuilding_z16(self):
        # check that a small building (or large shed), assigned zoom 16 in the
        # buildings.yaml, doesn't get re-assigned a lower zoom. it should stay
        # at z16.
        z, x, y = (16, 0, 0)

        # make one 4x4m building.
        self._setup_row(z, x, y, 4, 4, 1)

        self.assert_n_matching_features(
            z, x, y, 'buildings', {
                'kind': 'building',
                'min_zoom': 16,
            }, 1)
