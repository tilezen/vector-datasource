from . import OsmFixtureTest


def count_matching(features, props):
    num_matches = 0

    for f in features:
        f_props = f['properties']
        match = True

        for k, v in props.iteritems():
            got_v = f_props.get(k)
            if got_v != v:
                match = False

        if match:
            num_matches += 1

    return num_matches


class PeakKindTileRank(OsmFixtureTest):

    def test_01(self):
        # the tile 11/420/779 contains all the peaks below. so many, it
        # seems, that they ran out of names!
        #
        # not all of these should appear in the output tile - and they should
        # be ranked according to the elevation descending.
        self.load_fixtures([
            'https://www.openstreetmap.org/node/358914475',
            'https://www.openstreetmap.org/node/358914488',
            'https://www.openstreetmap.org/node/358914492',
            'https://www.openstreetmap.org/node/358914480',
            'https://www.openstreetmap.org/node/358914483',
            'https://www.openstreetmap.org/node/358914525',
            'https://www.openstreetmap.org/node/358914415',
            'https://www.openstreetmap.org/node/358914356',
            'https://www.openstreetmap.org/node/358914437',
            'https://www.openstreetmap.org/node/358914444',
            'https://www.openstreetmap.org/node/358914424',
            'https://www.openstreetmap.org/node/324759328',
            'https://www.openstreetmap.org/node/358914502',
            'https://www.openstreetmap.org/node/358914514',
            'https://www.openstreetmap.org/node/358914547',
            'https://www.openstreetmap.org/node/358914543',
            'https://www.openstreetmap.org/node/358914539',
            'https://www.openstreetmap.org/node/358914432',
            'https://www.openstreetmap.org/node/358931368',
            'https://www.openstreetmap.org/node/358914505',
            'https://www.openstreetmap.org/node/358914428',
            'https://www.openstreetmap.org/node/358914674',
            'https://www.openstreetmap.org/node/358946509',
            'https://www.openstreetmap.org/node/358914509',
            'https://www.openstreetmap.org/node/358914519',
            'https://www.openstreetmap.org/node/358914419',
            'https://www.openstreetmap.org/node/358914530',
            #
            # these are outside of the tile, used to test that the ranking
            # code doesn't consider items which are in the buffer.
            #
            'http://www.openstreetmap.org/node/358914747',
            'http://www.openstreetmap.org/node/358914751',
        ])

        with self.features_in_tile_layer(11, 420, 779, 'pois') as features:
            def assert_peak(rank, elevation, name):
                properties = {'kind': 'peak', 'elevation': elevation,
                              'name': name, 'kind_tile_rank': rank}
                num_matching = count_matching(features, properties)
                self.assertFalse(
                    num_matching != 1,
                    'Did not find peak matching properties %r.'
                    % properties)

            assert_peak(1, 4348, 'Quandary Peak')
            assert_peak(2, 4239, 'Fletcher Mountain')
            assert_peak(3, 4227, 'Pacific Peak')
            assert_peak(4, 4213, 'Crystal Peak')
            assert_peak(5, 4211, 'Atlantic Peak')

            num_matching = count_matching(features, {'kind': 'peak'})
            self.assertFalse(
                num_matching > 5,
                'Found %d peaks, but should only have five.' % num_matching)

    def test_02(self):
        # this tile has 7 peaks in it, and at z16 we should keep all of them
        self.load_fixtures([
            'https://www.openstreetmap.org/node/767614798',
            'https://www.openstreetmap.org/node/767614799',
            'https://www.openstreetmap.org/node/767614800',
            'https://www.openstreetmap.org/node/767614801',
            'https://www.openstreetmap.org/node/774446221',
            'https://www.openstreetmap.org/node/774446223',
            'https://www.openstreetmap.org/node/774446224',
        ])

        with self.features_in_tile_layer(
                16, 12372, 26269, 'pois') as features:

            num = count_matching(features, {'kind': 'peak'})
            self.assertFalse(
                num != 7,
                'Found %d peaks, but expected seven.' % num)

    def test_03(self):
        # check that volcanos are sorted along with other kinds of peak
        self.load_fixtures([
            'https://www.openstreetmap.org/node/1744903493',
            'https://www.openstreetmap.org/node/356546139',
            'https://www.openstreetmap.org/node/348179123',
        ])

        with self.features_in_tile_layer(
                12, 662, 1443, 'pois') as features:
            def assert_peak(rank_spec, elevation, kind, name):
                if isinstance(rank_spec, int):
                    possible_ranks = [rank_spec]
                else:
                    possible_ranks = rank_spec
                matched_one = False
                for rank in possible_ranks:
                    properties = {'kind': kind, 'elevation': elevation,
                                  'name': name, 'kind_tile_rank': rank}
                    num_matching = count_matching(features, properties)
                    if num_matching == 1:
                        matched_one = True
                        break
                self.assertTrue(
                    matched_one,
                    'Did not find %s matching properties %r.' %
                    (kind, properties))

            assert_peak(1, 4392, 'volcano', 'Mount Rainier')
            assert_peak(2, 4302, 'peak', 'Point Success')
            assert_peak((3, 4), 3863, 'peak', 'Gibraltar Rock')
