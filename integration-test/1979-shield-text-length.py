# -*- encoding: utf-8 -*-
import dsl
from . import FixtureTest

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
                'bus_shield_text': '23',
                'bus_shield_text_length': '2'
            })

        # make sure text length is encoded as a string
        self.assert_no_matching_feature(z, x, y, 'roads', {'id': 417097119, 'shield_text_length': 2})

    # empty strings and route refs over 6 chars in length don't report length
    def test_lengths_over_6_or_empty_are_not_reported(self):

        rel123456 = rel35.copy()
        rel123456['ref'] = '123456'

        relCycleTooLong = rel50Cycle.copy()
        relCycleTooLong['ref'] = '1234567'

        relBusEmpty = rel23Bus.copy()
        relBusEmpty['ref'] = ''

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/417097119
            dsl.way(417097119, dsl.tile_diagonal(z, x, y), way35),
            dsl.relation(1976278, rel123456, ways=[417097119]),
            dsl.relation(32312, relCycleTooLong, ways=[417097119]),
            dsl.relation(3002741, relBusEmpty, ways=[417097119])
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 417097119,
                'shield_text': '123456',
                'shield_text_length': '6',
                'bicycle_shield_text': '1234567',
                'bus_shield_text': '',
            })

        self.assert_no_matching_feature(z, x, y, 'roads', {
            'id': 417097119, 'bicycle_shield_text_length': '7', 'bus_shield_text_length': '0'})

    def test_walking_shield_works(self):

        # modify the data to include a trail to make sure we're adding walking shield text length too
        self.generate_fixtures(
            # https://www.openstreetmap.org/way/417097119
            dsl.way(417097119, dsl.tile_diagonal(z, x, y), way35),
            dsl.relation(1976278, {
                "name": "Pacific Crest Trail",
                "network": "nwn",
                "ref": "PCT",
                "route": "hiking",
                "type": "route",
                "wikidata": "Q2003736",
                "wikipedia": "en:Pacific Crest Trail",
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
