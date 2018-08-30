# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class WinterSportsPistes(FixtureTest):
    def test_piste_easy(self):
        self.generate_fixtures(dsl.way(313466665, wkt_loads('LINESTRING (-119.93007239669 38.9275517567953, -119.930262120878 38.92763282176809, -119.930440975451 38.9277428184021, -119.930456516306 38.92783548379489, -119.930401269916 38.92798328694239, -119.9302510716 38.928088111683, -119.930030175872 38.92810006169358, -119.929705884054 38.9279892968984, -119.929199863055 38.92776581005308, -119.928681445304 38.92749361358528, -119.928150361308 38.9271922744548, -119.927675691512 38.92685697027189, -119.927363347288 38.92658966223798, -119.927063489646 38.9262348573128, -119.926757433629 38.9256469129224, -119.926710541571 38.92552866653467, -119.926704343196 38.92537806284178, -119.926696438021 38.9252491933492)'), {u'name': u"Patsy's", u'piste:type': u'downhill', u'source': u'openstreetmap.org', u'piste:oneway': u'yes', u'piste:grooming': u'classic', u'piste:difficulty': u'easy'}))  # noqa

        self.assert_has_feature(
            15, 5467, 12531, 'roads',
            {'kind': 'piste',
             'kind_detail': 'downhill',
             'piste_difficulty': 'easy',
             'id': 313466665})

    def test_piste_expert(self):
        self.generate_fixtures(dsl.way(313466720, wkt_loads('LINESTRING (-119.930747390795 38.92849049748221, -119.930782694585 38.92838742040661, -119.93089758911 38.9283186556843, -119.931012393804 38.92831516154018, -119.931202297655 38.92835988657251, -119.931361389291 38.92845269092479, -119.931493890796 38.92861076552828, -119.931727991759 38.9288891073537, -119.932015093324 38.92909176579129, -119.932540787428 38.92951790567929, -119.933061989956 38.92986500723499, -119.933577892424 38.93031378389799, -119.933983930932 38.93075116720339)'), {u'name': u'The Face', u'piste:type': u'downhill', u'source': u'openstreetmap.org', u'piste:oneway': u'yes', u'piste:grooming': u'mogul', u'piste:difficulty': u'expert'}))  # noqa

        self.assert_has_feature(
            15, 5467, 12531, 'roads',
            {'kind': 'piste',
             'kind_detail': 'downhill',
             'piste_difficulty': 'expert',
             'id': 313466720})

    def test_piste_intermediate(self):
        # Way: 49'er (313466490)
        self.generate_fixtures(dsl.way(313466490, wkt_loads('LINESTRING (-119.904198760551 38.93351027461519, -119.904416512176 38.93363759179209, -119.904749966809 38.93377028930887, -119.904922712838 38.9339660858234, -119.905075067111 38.93411345693338, -119.905378787508 38.9342667672842, -119.905649719398 38.93437360916958, -119.90606069864 38.93451538929079, -119.906553334742 38.93471146325469, -119.90692936952 38.9349014574302, -119.907340528426 38.93506741367678, -119.907677935646 38.93519409917329, -119.907896585587 38.93527746132089, -119.908209109474 38.93541728311039, -119.908515524817 38.93549875834877, -119.908814663807 38.9356004974517)'), {u'name': u"49'er", u'piste:type': u'downhill', u'source': u'openstreetmap.org', u'piste:oneway': u'yes', u'piste:grooming': u'classic', u'piste:difficulty': u'intermediate'}))  # noqa

        self.assert_has_feature(
            16, 10939, 25061, 'roads',
            {'kind': 'piste',
             'kind_detail': 'downhill',
             'piste_difficulty': 'intermediate',
             'id': 313466490})
