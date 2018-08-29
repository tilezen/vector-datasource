# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class ParkBuilding(FixtureTest):
    def test_park_with_building_tags_should_appear_in_landuse(self):
        # This test make sure park polygons with addresses still end up in
        # the landuse layer
        # Because it's a relation, it's ID will be negative.
        # (Separately a address point is generated for the feature, but we
        # don't test that here.)
        # Way: Olympic Sculpture Park (239782410)
        self.generate_fixtures(dsl.way(508853910, wkt_loads('LINESTRING (-122.355318039444 47.61536890970269, -122.355521507856 47.61585977285878)'), {u'source': u'openstreetmap.org', u'layer': u'2', u'man_made': u'bridge'}),dsl.way(239782410, wkt_loads('LINESTRING (-122.355739439144 47.6159988680818, -122.355618346244 47.61554331016748)'), {u'source': u'openstreetmap.org', u'layer': u'2', u'man_made': u'bridge'}),dsl.way(-7406606, wkt_loads('POLYGON ((-122.357852007198 47.61672909679339, -122.357554036018 47.6169097903414, -122.356940127353 47.61643268293529, -122.356288938604 47.61593879739959, -122.356138111467 47.61584796458379, -122.355618346244 47.61554331016748, -122.355739439144 47.6159988680818, -122.357017112973 47.6168760011799, -122.356663446246 47.6171398951622, -122.356482166221 47.61699099323719, -122.356161557496 47.6171859765585, -122.35620647326 47.61721328627618, -122.355769083549 47.61755129583639, -122.354815162548 47.61697700527541, -122.353628308395 47.61627917683448, -122.353639896662 47.61619639840689, -122.354210865857 47.61577408711059, -122.35425982404 47.6157674865772, -122.354551596844 47.61592868468718, -122.35571213036 47.61674266094208, -122.356054029157 47.61684590579709, -122.355867988061 47.61656868835849, -122.35578327693 47.61650571171499, -122.354844986616 47.61580721087577, -122.354634601176 47.61568186123319, -122.354522671092 47.61561531074531, -122.354509286194 47.61556571574061, -122.35476234161 47.61536539746518, -122.355521507856 47.61585977285878, -122.355318039444 47.61536890970269, -122.35507208072 47.61522508943741, -122.354962845581 47.6151615661711, -122.354996712067 47.6151090034863, -122.355008390166 47.61502888767959, -122.354995274763 47.61496966367098, -122.355237460564 47.61497438706068, -122.356276901179 47.61555348350998, -122.35706571183 47.616087581211, -122.357852007198 47.61672909679339))'), {u'website': u'http://www.seattleartmuseum.org/visit/OSP/', u'addr:housenumber': u'2901', u'name': u'Olympic Sculpture Park', u'addr:postcode': u'98121', u'wheelchair': u'yes', u'way_area': u'74439.2', u'wikipedia': u'en:Olympic Sculpture Park', u'leisure': u'park', u'source': u'openstreetmap.org', u'operator': u'Seattle Art Museum', u'opening_hours': u'Mo-Su sunrise-sunset', u'owner': u'Seattle Art Museum', u'addr:street': u'Western Avenue', u'addr:city': u'Seattle'}))  # noqa

        self.assert_no_matching_feature(
            16, 10493, 22885, 'buildings',
            {'id': -7406606})

        self.assert_has_feature(
            16, 10493, 22885, 'landuse',
            {'id': -7406606, 'kind': 'park'})
