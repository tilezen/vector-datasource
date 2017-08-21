from . import OsmFixtureTest


class FixBadUnicodeShieldText(OsmFixtureTest):

    def test_cyrillic(self):
        # route relation with a cyrillic capital letter Ka at the end.
        self.load_fixtures(['http://www.openstreetmap.org/relation/3948946'])

        self.assert_has_feature(
            16, 63085, 15623, 'roads',
            {'id': 425415345, 'shield_text': u'77\u041a'})

        self.assert_has_feature(
            16, 63085, 15623, 'roads',
            {'id': -3948946, 'osm_relation': type(True),
             'shield_text': u'77\u041a'})
