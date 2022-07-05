from . import FixtureTest


class RemoveSea(FixtureTest):
    def test_drop_sea_polygon_but_keep_label(self):
        # Drop sea polygon but keep the label
        import dsl

        z, x, y = (12, 2338, 1579)

        self.generate_fixtures(
            # http://www.openstreetmap.org/relation/4594226
            dsl.way(-4594226, dsl.box_area(z, x, y, 333248147246), {
                'name': '\u0391\u03B9\u03B3\u03B1\u03AF\u03BF\u03BD \u03A0\u03AD\u03BB\u03B1\u03B3\u03BF\u03C2 / Ege Denizi',
                'name:el': '\u0391\u03B9\u03B3\u03B1\u03AF\u03BF \u03A0\u03AD\u03BB\u03B1\u03B3\u03BF\u03C2',
                'name:en': 'Aegean Sea',
                'name:tr': 'Ege Denizi',
                'place': 'sea',
                'wikidata': 'Q34575'
            }),
        )

        self.assert_no_matching_feature(
            12, 2315, 1580, 'water',
            {'id': -4594226, 'kind': 'sea', 'label_placement': None})

        self.assert_has_feature(
            9, 292, 197, 'water',
            {'id': -4594226, 'kind': 'sea', 'label_placement': True})

        self.assert_has_feature(
            12, 2338, 1579, 'water',
            {'id': -4594226, 'kind': 'sea', 'label_placement': True})
