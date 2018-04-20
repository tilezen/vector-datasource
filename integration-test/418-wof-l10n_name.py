from . import FixtureTest


class WofL10nName(FixtureTest):
    def test_hollywood(self):
        # Hollywood (wof neighbourhood)
        self.load_fixtures([
            'https://data.whosonfirst.org/858/260/37/85826037.geojson'
        ])

        self.assert_has_feature(
            16, 11227, 26157, 'places',
            {'id': 85826037, 'kind': 'neighbourhood',
             'source': "whosonfirst.org",
             'name': 'Hollywood',
             'name:ko': '\xed\x97\x90\xeb\xa6\xac\xec\x9a\xb0\xeb\x93\x9c'})

    def test_san_francisco_wof(self):
        # San Francisco (wof neighbourhood)
        self.load_fixtures([
            'https://data.whosonfirst.org/858/826/41/85882641.geojson'
        ])

        self.assert_has_feature(
            16, 14893, 29234, 'places',
            {'id': 85882641, 'kind': 'neighbourhood',
             'source': "whosonfirst.org",
             'name': 'San Francisco',
             'name:es': 'San Francisco'})

    def test_san_francisco_osm(self):
        # San Francisco (osm city)
        #
        # note: presence of Chinese name tested, but not its value, as that
        # can and does change.
        self.load_fixtures(['http://www.openstreetmap.org/node/26819236'])

        self.assert_has_feature(
            16, 10482, 25330, 'places',
            {'id': 26819236, 'kind': 'locality', 'kind_detail': 'city',
             'source': "openstreetmap.org",
             'name': 'San Francisco',
             'name:zh': None})

    def test_londonderry(self):
        # Node: Londonderry/Derry (267762522)
        self.load_fixtures(['http://www.openstreetmap.org/node/267762522'])

        self.assert_has_feature(
            16, 31436, 20731, 'places',
            {'id': 267762522, 'name:en_GB': 'Londonderry'})

    def test_jerusalem(self):
        # Node: Jerusalem (29090735)
        #
        # note: presence of Chinese name tested, but not its value, as that
        # can and does change.
        self.load_fixtures(['http://www.openstreetmap.org/node/29090735'])

        self.assert_has_feature(
            16, 39180, 26661, 'places',
            {'id': 29090735,
             'name:zh-min-nan': None,
             'name:zh': None,
             'name:zh-yue': None,
             })
