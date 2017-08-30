# -*- coding: utf-8 -*-
from . import OsmFixtureTest


class FixCityNames(OsmFixtureTest):

    def setUp(self):
        # need to call this to make sure the environment exists.
        super(FixCityNames, self).setUp()

        # data is in the fixture
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'ne_10m_populated_places/1140-fix-city-names.shp'
        ])

    def test_quebec(self):
        self.assert_has_feature(
            7, 38, 45, 'places',
            {'name': 'Québec', 'source': 'naturalearthdata.com'})

    def test_saudarkrokur(self):
        # this one has an interesting character outside of the extended latin
        # charset, so hopefully will test an extra path from just acute
        # characters and umlauts.
        self.assert_has_feature(
            7, 57, 32, 'places',
            {'name': 'Sauðárkrókur', 'source': 'naturalearthdata.com'})

    def test_utqiagvik(self):
        # ditto interesting character
        self.assert_has_feature(
            7, 8, 27, 'places',
            {'name': 'Utqiaġvik', 'source': 'naturalearthdata.com'})
