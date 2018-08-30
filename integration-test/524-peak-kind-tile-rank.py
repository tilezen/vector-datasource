# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


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


class PeakKindTileRank(FixtureTest):

    def test_01(self):
        # the tile 11/420/779 contains all the peaks below. so many, it
        # seems, that they ran out of names!
        #
        # not all of these should appear in the output tile - and they should
        # be ranked according to the elevation descending.
        self.generate_fixtures(dsl.way(324759328, wkt_loads('POINT (-106.102478872583 39.4727091543367)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Peak 8', u'ele:ft': u'12987', u'gnis:county_id': u'117', u'ele': u'3955', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179628'}),dsl.way(358914356, wkt_loads('POINT (-106.14224369695 39.42304321384119)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Mayflower Hill', u'gnis:county_id': u'117', u'ele': u'3763', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179584'}),dsl.way(358914415, wkt_loads('POINT (-106.160577503415 39.41609878975068)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Gold Hill', u'gnis:county_id': u'117', u'ele': u'3638', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179615'}),dsl.way(358914419, wkt_loads('POINT (-106.128909823525 39.40332118260089)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Fletcher Mountain', u'wikipedia': u'en:Fletcher Mountain', u'gnis:county_id': u'117', u'ele': u'4239', u'source': u'openstreetmap.org', u'wikidata': u'Q14684500', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179617'}),dsl.way(358914424, wkt_loads('POINT (-106.161410601009 39.38582140713158)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Little Bartlett Mountain', u'gnis:county_id': u'117', u'ele': u'3943', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179618'}),dsl.way(358914428, wkt_loads('POINT (-106.136132188577 39.3805437679749)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Wheeler Mountain', u'gnis:county_id': u'117', u'ele': u'4154', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179620'}),dsl.way(358914432, wkt_loads('POINT (-106.15918834866 39.3769325583209)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Bartlett Mountain', u'gnis:county_id': u'065', u'ele': u'4128', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179621'}),dsl.way(358914437, wkt_loads('POINT (-106.111373182043 39.4936342680104)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Peak 6', u'gnis:county_id': u'117', u'ele': u'3835', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179626'}),dsl.way(358914444, wkt_loads('POINT (-106.10557608402 39.47832019795361)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Peak 7', u'gnis:county_id': u'117', u'ele': u'3857', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179627'}),dsl.way(358914475, wkt_loads('POINT (-106.056130115836 39.49054248224699)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Shock Hill', u'gnis:county_id': u'117', u'ele': u'2991', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179631'}),dsl.way(358914480, wkt_loads('POINT (-106.029462548648 39.49582011272368)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Gibson Hill', u'gnis:county_id': u'117', u'ele': u'3187', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179635'}),dsl.way(358914483, wkt_loads('POINT (-106.013628663787 39.49082020023229)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Prospect Hill', u'gnis:county_id': u'117', u'ele': u'3259', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179636'}),dsl.way(358914488, wkt_loads('POINT (-106.03390714318 39.47220925579419)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Barney Ford Hill', u'gnis:county_id': u'117', u'ele': u'3019', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179641'}),dsl.way(358914492, wkt_loads('POINT (-106.034184902265 39.46943156018197)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Little Mountain', u'gnis:county_id': u'117', u'ele': u'3062', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179643'}),dsl.way(358914502, wkt_loads('POINT (-106.105205888291 39.45165316685299)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Peak 9', u'gnis:county_id': u'117', u'ele': u'3992', u'source': u'openstreetmap.org', u'alt_name': u'Tenmile Range Peak 9', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179647'}),dsl.way(358914505, wkt_loads('POINT (-106.102733275471 39.44330958556778)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Peak 10', u'wikipedia': u'en:Peak 10 (Tenmile Range)', u'gnis:county_id': u'117', u'ele': u'4150', u'source': u'openstreetmap.org', u'wikidata': u'Q14685050', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179648'}),dsl.way(358914509, wkt_loads('POINT (-106.114394216343 39.4346179598258)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Crystal Peak', u'wikipedia': u'en:Crystal Peak (Tenmile Range)', u'gnis:county_id': u'117', u'ele': u'4213', u'source': u'openstreetmap.org', u'wikidata': u'Q5191323', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179650'}),dsl.way(358914514, wkt_loads('POINT (-106.08724200806 39.42859865741799)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Mount Helen', u'gnis:county_id': u'117', u'ele': u'4016', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179653'}),dsl.way(358914519, wkt_loads('POINT (-106.12335419265 39.42304321384119)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Pacific Peak', u'wikipedia': u'en:Pacific Peak', u'gnis:county_id': u'117', u'ele': u'4227', u'source': u'openstreetmap.org', u'wikidata': u'Q14685041', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179656'}),dsl.way(358914525, wkt_loads('POINT (-106.01501763888 39.4324875721444)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Mount Argentine 11,412 ft', u'gnis:county_id': u'117', u'ele': u'3479', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179665'}),dsl.way(358914530, wkt_loads('POINT (-106.106431190338 39.39728897267168)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Quandary Peak', u'wikipedia': u'en:Quandary Peak', u'gnis:county_id': u'117', u'ele': u'4348', u'source': u'openstreetmap.org', u'wikidata': u'Q2122147', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179667'}),dsl.way(358914539, wkt_loads('POINT (-106.098353269809 39.37748820529328)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'North Star Mountain', u'gnis:county_id': u'117', u'ele': u'4086', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179669'}),dsl.way(358914543, wkt_loads('POINT (-106.022240093764 39.39471030408239)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Red Mountain', u'gnis:county_id': u'117', u'ele': u'4030', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179676'}),dsl.way(358914547, wkt_loads('POINT (-106.004739564556 39.39109927202649)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Red Peak', u'gnis:county_id': u'117', u'ele': u'4020', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179677'}),dsl.way(358914674, wkt_loads('POINT (-106.149187943591 39.36832161758159)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Clinton Peak', u'gnis:county_id': u'065', u'ele': u'4210', u'source': u'openstreetmap.org', u'wikidata': u'Q14684391', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179905'}),dsl.way(358914747, wkt_loads('POINT (-106.111409024822 39.35137746412247)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Mount Lincoln', u'wikipedia': u'en:Mount Lincoln (Colorado)', u'gnis:county_id': u'093', u'ele': u'4348', u'source': u'openstreetmap.org', u'wikidata': u'Q502645', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179956'}),dsl.way(358914751, wkt_loads('POINT (-106.118631479707 39.3469330032385)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Mount Cameron', u'gnis:county_id': u'093', u'ele': u'4335', u'source': u'openstreetmap.org', u'gnis:created': u'10/13/1978', u'gnis:feature_id': u'179957'}),dsl.way(358931368, wkt_loads('POINT (-106.105298145271 39.43109857008699)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Father Dyer Peak', u'gnis:county_id': u'117', u'ele': u'4144', u'source': u'openstreetmap.org', u'gnis:created': u'02/01/1990', u'gnis:feature_id': u'196484'}),dsl.way(358946509, wkt_loads('POINT (-106.126131963171 39.4135987554159)'), {u'gnis:state_id': u'08', u'natural': u'peak', u'name': u'Atlantic Peak', u'gnis:county_id': u'117', u'ele': u'4211', u'source': u'openstreetmap.org', u'gnis:created': u'09/26/2001', u'gnis:feature_id': u'1934911'}))  # noqa

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
        self.generate_fixtures(dsl.way(767614798, wkt_loads('POINT (-112.036483199163 33.58948611769299)'), {u'source': u'openstreetmap.org', u'natural': u'peak'}),dsl.way(767614799, wkt_loads('POINT (-112.036826535265 33.5900222852225)'), {u'source': u'openstreetmap.org', u'natural': u'peak'}),dsl.way(767614800, wkt_loads('POINT (-112.037234190741 33.58966930552238)'), {u'source': u'openstreetmap.org', u'natural': u'peak'}),dsl.way(767614801, wkt_loads('POINT (-112.037561446999 33.5894100886431)'), {u'source': u'openstreetmap.org', u'natural': u'peak'}),dsl.way(774446221, wkt_loads('POINT (-112.03813987221 33.58874819905389)'), {u'source': u'openstreetmap.org', u'natural': u'peak'}),dsl.way(774446223, wkt_loads('POINT (-112.036165824373 33.58910567244519)'), {u'source': u'openstreetmap.org', u'natural': u'peak'}),dsl.way(774446224, wkt_loads('POINT (-112.035720529487 33.5886498692911)'), {u'source': u'openstreetmap.org', u'natural': u'peak'}))  # noqa

        with self.features_in_tile_layer(
                16, 12372, 26269, 'pois') as features:

            num = count_matching(features, {'kind': 'peak'})
            self.assertFalse(
                num != 7,
                'Found %d peaks, but expected seven.' % num)

    def test_03(self):
        # check that volcanos are sorted along with other kinds of peak
        self.generate_fixtures(dsl.way(348179123, wkt_loads('POINT (-121.745391605932 46.84582071887297)'), {u'is_in:state_code': u'WA', u'gnis:state_id': u'53', u'natural': u'peak', u'name': u'Gibraltar Rock', u'is_in:country': u'USA', u'gnis:ST_num': u'53', u'gnis:Cell': u'Mount Rainier East', u'gnis:county_id': u'053', u'ele': u'3863', u'source': u'openstreetmap.org', u'gnis:Class': u'Summit', u'gnis:ST_alph': u'WA', u'gnis:created': u'09/10/1979', u'gnis:County': u'Pierce', u'gnis:id': u'1533567', u'gnis:feature_id': u'1533567', u'is_in:county': u'Pierce', u'gnis:County_num': u'53'}),dsl.way(356546139, wkt_loads('POINT (-121.767518369021 46.8457629638095)'), {u'gnis:state_id': u'53', u'natural': u'peak', u'name': u'Point Success', u'gnis:county_id': u'053', u'ele': u'4302', u'source': u'openstreetmap.org', u'gnis:created': u'09/10/1979', u'gnis:feature_id': u'1524537'}),dsl.way(1744903493, wkt_loads('POINT (-121.760467941514 46.85289407719969)'), {u'name:it': u'Monte Rainier', u'name:pt': u'Monte Rainier', u'old_name_2': u'Mount Seattle Seahawks (was renamed temporarily by the Washington State Legislature for Super Bowl XLVIII in 2014)', u'natural': u'volcano', u'name': u'Mount Rainier', u'name:lt': u'Reinyro kalnas', u'start_date': u'about 500,000 BC', u'wikipedia': u'en:Mount Rainier', u'ele': u'4392', u'source': u'openstreetmap.org', u'name:fr': u'Mont Rainier', u'condition': u'active', u'type': u'strato', u'old_name_1': u'Talol;Tacoma;Tahoma', u'name:es': u'Monte Rainier', u'name:ja': u'\u30ec\u30fc\u30cb\u30a2\u5c71'}))  # noqa

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
