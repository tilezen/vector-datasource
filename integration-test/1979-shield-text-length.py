# -*- encoding: utf-8 -*-
import unittest

import dsl

from . import FixtureTest
from . import SKIP_UNIT_TEST_MESSAGE

z, x, y = (16, 10470, 25340)

way35 = {
    'cycleway:right': 'lane',
    'hgv': 'designated',
    'hgv:state_network': 'yes',
    'highway': 'primary',
    'lanes': '2',
    'lcn_ref': '50',
    'maxspeed': '35 mph',
    'name': 'Sloat Boulevard',
    'name:etymology:wikidata': 'Q634931',
    'oneway': 'yes',
    'ref': 'CA 35',
    'sidewalk': 'right',
    'source': 'openstreetmap.org',
    'source:hgv:state_network': 'Caltrans http://www.dot.ca.gov/hq/traffops/trucks/truckmap/',
    'tiger:cfcc': 'A45',
    'tiger:county': 'San Francisco, CA',
    'tiger:name_base': 'Sloat',
    'tiger:name_type': 'Blvd',
}

rel35 = {
    'network': 'US:CA',
    'ref': '35',
    'route': 'road',
    'source': 'openstreetmap.org',
    'type': 'route',
}

rel50Cycle = {
    'cycle_network': 'US:CA:SF',
    'network': 'lcn',
    'ref': '50',
    'source': 'openstreetmap.org',
    'route': 'bicycle',
    'type': 'route',
}

rel23Bus = {
    'network': 'Muni',
    'ref': '23',
    'route': 'bus',
    'source': 'openstreetmap.org',
    'type': 'route',
}


class ShieldTextLengthTest(FixtureTest):
    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_create_shield_text_length(self):
        self.generate_fixtures(
            # https://www.openstreetmap.org/way/417097119
            dsl.way(417097119, dsl.tile_diagonal(z, x, y), way35),
            dsl.relation(1976278, rel35, ways=[417097119]),
            dsl.relation(32312, rel50Cycle, ways=[417097119]),
            dsl.relation(3002741, rel23Bus, ways=[417097119])
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 417097119,
                'shield_text': '35',
                'shield_text_length': '2',
                'bicycle_shield_text': '50',
                'bicycle_shield_text_length': '2',
                'is_bus_related': True,
                'bus_shield_text': type(None),
                'bus_shield_text_length': type(None),
            })

        # make sure text length is encoded as a string
        self.assert_no_matching_feature(z, x, y, 'roads', {'id': 417097119, 'shield_text_length': 2})

    def test_missing_ref_does_not_report_length_or_text(self):
        rel_bus_missing = rel23Bus.copy()
        del rel_bus_missing['ref']

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/417097119
            dsl.way(417097119, dsl.tile_diagonal(z, x, y), way35),
            dsl.relation(3002741, rel_bus_missing, ways=[417097119])
        )

        self.assert_no_matching_feature(
            z, x, y, 'roads', {
                'id': 417097119,
                'bus_shield_text': 'None',
                'bus_shield_text_length': '4'
            })

    # empty strings and route refs over 6 chars in length don't report length
    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_lengths_over_6_or_empty_are_not_reported(self):

        rel123456 = rel35.copy()
        rel123456['ref'] = '123456'

        rel_cycle_too_long = rel50Cycle.copy()
        rel_cycle_too_long['ref'] = '1234567'

        rel_bus_empty = rel23Bus.copy()
        rel_bus_empty['ref'] = ''

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/417097119
            dsl.way(417097119, dsl.tile_diagonal(z, x, y), way35),
            dsl.relation(1976278, rel123456, ways=[417097119]),
            dsl.relation(32312, rel_cycle_too_long, ways=[417097119]),
            dsl.relation(3002741, rel_bus_empty, ways=[417097119])
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 417097119,
                'shield_text': '123456',
                'shield_text_length': '6',
                'bicycle_shield_text': '1234567',
                'bus_shield_text': type(None),
                'is_bus_related': True,
            })

        self.assert_no_matching_feature(z, x, y, 'roads', {
            'id': 417097119, 'bicycle_shield_text_length': '7', 'bus_shield_text_length': '0'})

    def test_walking_shield_works(self):

        # modify the data to include a trail to make sure we're adding walking shield text length too
        self.generate_fixtures(
            # https://www.openstreetmap.org/way/417097119
            dsl.way(417097119, dsl.tile_diagonal(z, x, y), way35),
            dsl.relation(1976278, {
                'name': 'Pacific Crest Trail',
                'network': 'nwn',
                'ref': 'PCT',
                'route': 'hiking',
                'type': 'route',
                'wikidata': 'Q2003736',
                'wikipedia': 'en:Pacific Crest Trail',
            }, ways=[417097119]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 417097119,
                'walking_shield_text': 'PCT',
                'walking_shield_text_length': '3',
            })

    def test_hgv_shield_text_length(self):
        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y),
                    {'highway': 'unclassified',
                     'source': 'openstreetmap.org',
                     'maxweight': 1.5}))

        self.assert_has_feature(
            z, x, y, 'roads', {
                'kind': 'minor_road',
                'kind_detail': 'unclassified',
                'hgv_restriction': 'weight',
                'hgv_restriction_shield_text': '1.5t',
                'hgv_restriction_shield_text_length': '4'})
