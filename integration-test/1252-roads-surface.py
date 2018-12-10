# -*- encoding: utf-8 -*-
from . import FixtureTest


class RoadsSurface(FixtureTest):
    def test_cobblestones(self):
        # Add surface properties to roads layer (at max zooms)
        # Prince St with cobblestones in Alexandria, VA
        self.load_fixtures(['https://www.openstreetmap.org/way/190536019'])

        self.assert_has_feature(
            15, 9371, 12546, 'roads',
            {'id': 190536019, 'kind': 'minor_road', 'surface': 'cobblestone'})

        # and that surface property is simplified at some zooms
        self.assert_has_feature(
            13, 2342, 3136, 'roads',
            {'id': 190536019, 'kind': 'minor_road', 'surface': 'unpaved'})

    def test_asphalt(self):
        # motorway in Kraków, Poland
        self.load_fixtures(['http://www.openstreetmap.org/way/431783017'])

        self.assert_has_feature(
            12, 2273, 1388, 'roads',
            {'id': 431783017, 'kind_detail': 'motorway', 'surface': 'asphalt'})

        # But strip that surface property off at earlier zooms
        self.assert_no_matching_feature(
            7, 71, 43, 'roads',
            {'kind_detail': 'motorway', 'surface': 'asphalt'})

    def test_concrete_lanes(self):
        # track with cycling route in Schartau, Germany
        # http://www.openstreetmap.org/way/58691615
        #
        # the track is part of this NCN relation, which needs to be present
        # for the min zoom to be assigned correctly.
        #
        # first, test at high zoom, where we do not expect the road to be
        # merged, so should still retain its original ID.
        self.load_fixtures(
            ['http://www.openstreetmap.org/way/58691615',
             'http://www.openstreetmap.org/relation/2599024'],
            clip=self.tile_bbox(15, 17456, 10780))

        self.assert_has_feature(
            15, 17456, 10780, 'roads',
            {'id': 58691615, 'kind_detail': 'track',
             'surface': 'concrete_lanes'})

        # check at a bunch of lower zooms, where we're expecting the road to be
        # merged, so be stricter with the set of properties we expect to see.
        # we'd expect the surface tag to have been stripped off by now.
        for z in (13, 11, 10, 9, 8):
            delta_z = 15 - z
            coord_scale = 2 ** delta_z

            props = {
                'kind': 'path',
                'kind_detail': 'track',
                'is_bicycle_related': True,
                'surface': 'concrete_lanes' if z >= 12 else 'unpaved',
                'min_zoom': 8,
            }

            if z >= 13:
                props.update({
                    'bicycle_network': 'ncn',
                    'bicycle_shield_text': 'D10',
                })

            self.assert_has_feature(
                z, 17456 / coord_scale, 10780 / coord_scale, 'roads', props)
