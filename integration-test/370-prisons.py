# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class Prisons(FixtureTest):
    def test_rikers_island(self):
        self.generate_fixtures(dsl.way(113738569, wkt_loads('LINESTRING (-73.88619559241629 40.78670926170489, -73.88598960872169 40.7867636061766, -73.88581210162148 40.78669477437268, -73.88544783477379 40.78668321171088, -73.88529018044149 40.78672259276838, -73.88495340204139 40.78655996721398, -73.883889617082 40.78629157636468, -73.88361302580599 40.78626858693091, -73.88341225233998 40.78631579007937, -73.8833307751437 40.78649045504029, -73.88328738651551 40.78648215710478, -73.88328738651551 40.78631789857658, -73.8829500691263 40.7861866955101, -73.88169287688619 40.78589680995149, -73.88157798236141 40.78593775585329, -73.88141251268598 40.7858288614642, -73.88110654650029 40.78573180179259, -73.8807860276069 40.78578771144548, -73.8794390936699 40.78556169196288, -73.87916142441559 40.7854651760361, -73.87862306406581 40.78537117659838, -73.87804203374 40.78545470143099, -73.87782455160971 40.78556720132448, -73.8766314990809 40.78586048914709, -73.876209740055 40.78582926956337, -73.8760088767575 40.78590007474199, -73.87512152091979 40.78593816395188, -73.8743435798838 40.78582457642207, -73.8736586144796 40.7858032192241, -73.87312357789638 40.78588232244199, -73.8729069042499 40.7859578206963, -73.87267298294989 40.78618309065278, -73.8723882170048 40.7863659178819, -73.87206850659518 40.78650956749447, -73.87172292470538 40.78674721441948, -73.8715374225992 40.78687011849157, -73.8714113889649 40.78732058343628, -73.87127897729199 40.787511977401, -73.8711282399873 40.78760957858857, -73.870890006774 40.7879340760004, -73.8709898994336 40.7884577846806, -73.87103867795351 40.78882471836661, -73.8710150522615 40.78898216936368, -73.8710622138139 40.78919987960899, -73.8710590697104 40.78938970386069, -73.8712609211548 40.7899572690156, -73.8713451831284 40.79014348645999, -73.871699388845 40.79054836137328, -73.8720644641764 40.7908744086858, -73.8728886684496 40.79141836140191, -73.87358504245789 40.79172175694869, -73.8738783423981 40.79182479278079, -73.8741893391495 40.7918462160525, -73.87428527922179 40.79181336703301, -73.87487690966789 40.79212498999629, -73.87526866496339 40.79240519097548, -73.87530989763491 40.79251611487138, -73.8755793023886 40.79288717469921, -73.87592048253349 40.79315438273728, -73.87630505130659 40.79332576528559, -73.8769245295266 40.79370158118189, -73.87768118049038 40.79410786256829, -73.8780131079879 40.79429651665539, -73.87850394745909 40.79447836943888, -73.8791124662326 40.79465369300449, -73.87945247856759 40.79470408654268, -73.87967651839951 40.79481038209889, -73.87984216773791 40.7947959645414, -73.8799593978824 40.7948418014822, -73.8804840140084 40.79485628703697, -73.88151429180769 40.79501800818069, -73.88172665354088 40.7950254209571, -73.88205364030431 40.79509771248509, -73.8826248789935 40.79517381232468, -73.8830125918701 40.79532118325839, -73.88324552502328 40.79548997596088, -73.883586166179 40.79585428654799, -73.88368004012619 40.79587781671319, -73.8837236084175 40.79585727882378, -73.88357673386849 40.79560347895109, -73.88365183302629 40.79557491620369, -73.8838148772504 40.79563476194608)'), {u'source': u'openstreetmap.org', u'area': u'yes'}), dsl.way(-3955540, wkt_loads(
            'POLYGON ((-73.892691849225 40.79306338658551, -73.89258018863518 40.79354427739299, -73.89255449681798 40.7938367138842, -73.89243430223299 40.7939277089761, -73.8924429260597 40.7939666776881, -73.8923999865892 40.7945450169311, -73.89222831853839 40.79494775678188, -73.89221125054799 40.79525317640758, -73.89212528177529 40.79569508367947, -73.8919107640854 40.79654631474289, -73.89165330692499 40.79691667199458, -73.8910352660095 40.7974690077811, -73.89073486937851 40.79770709151379, -73.890674772086 40.79775476256129, -73.8906644414602 40.79775945485938, -73.89063093430009 40.79777448381198, -73.8902113312309 40.7979627874593, -73.8901255421213 40.79784582028729, -73.8895247488593 40.79780025743779, -73.8890439705192 40.79783276347388, -73.8886577847786 40.79806016927321, -73.8883882003618 40.7982225626507, -73.88825453104748 40.79830321516039, -73.88823719356249 40.79831361973499, -73.8878939472925 40.79837856328498, -73.88742179277918 40.79834605751611, -73.8869154124535 40.79815768695209, -73.88628883754281 40.79775476256129, -73.88537902382311 40.79710511408508, -73.8844692101033 40.79632536430771, -73.88407440053589 40.79598098210779, -73.8838148772504 40.79563476194608, -73.88365183302629 40.79557491620369, -73.88357673386849 40.79560347895109, -73.8837236084175 40.79585727882378, -73.88368004012619 40.79587781671319, -73.883586166179 40.79585428654799, -73.88324552502328 40.79548997596088, -73.8830125918701 40.79532118325839, -73.8826248789935 40.79517381232468, -73.88205364030431 40.79509771248509, -73.88172665354088 40.7950254209571, -73.88151429180769 40.79501800818069, -73.8804840140084 40.79485628703697, -73.8799593978824 40.7948418014822, -73.87984216773791 40.7947959645414, -73.87967651839951 40.79481038209889, -73.87945247856759 40.79470408654268, -73.8791124662326 40.79465369300449, -73.87850394745909 40.79447836943888, -73.8780131079879 40.79429651665539, -73.87768118049038 40.79410786256829, -73.8769245295266 40.79370158118189, -73.87630505130659 40.79332576528559, -73.87592048253349 40.79315438273728, -73.8755793023886 40.79288717469921, -73.87530989763491 40.79251611487138, -73.87526866496339 40.79240519097548, -73.87487690966789 40.79212498999629, -73.87428527922179 40.79181336703301, -73.8741893391495 40.7918462160525, -73.8738783423981 40.79182479278079, -73.87358504245789 40.79172175694869, -73.8728886684496 40.79141836140191, -73.8720644641764 40.7908744086858, -73.871699388845 40.79054836137328, -73.8713451831284 40.79014348645999, -73.8712609211548 40.7899572690156, -73.8710590697104 40.78938970386069, -73.8710622138139 40.78919987960899, -73.8710150522615 40.78898216936368, -73.87103867795351 40.78882471836661, -73.8709898994336 40.7884577846806, -73.870890006774 40.7879340760004, -73.8711282399873 40.78760957858857, -73.87127897729199 40.787511977401, -73.8714113889649 40.78732058343628, -73.8715374225992 40.78687011849157, -73.87172292470538 40.78674721441948, -73.87206850659518 40.78650956749447, -73.8723882170048 40.7863659178819, -73.87267298294989 40.78618309065278, -73.8729069042499 40.7859578206963, -73.87312357789638 40.78588232244199, -73.8736586144796 40.7858032192241, -73.8743435798838 40.78582457642207, -73.87512152091979 40.78593816395188, -73.8760088767575 40.78590007474199, -73.876209740055 40.78582926956337, -73.8766314990809 40.78586048914709, -73.87782455160971 40.78556720132448, -73.87804203374 40.78545470143099, -73.87862306406581 40.78537117659838, -73.87916142441559 40.7854651760361, -73.8794390936699 40.78556169196288, -73.8807860276069 40.78578771144548, -73.88110654650029 40.78573180179259, -73.88141251268598 40.7858288614642, -73.88157798236141 40.78593775585329, -73.88169287688619 40.78589680995149, -73.8829500691263 40.7861866955101, -73.88328738651551 40.78631789857658, -73.88328738651551 40.78648215710478, -73.8833307751437 40.78649045504029, -73.88341225233998 40.78631579007937, -73.88361302580599 40.78626858693091, -73.883889617082 40.78629157636468, -73.88495340204139 40.78655996721398, -73.88529018044149 40.78672259276838, -73.88544783477379 40.78668321171088, -73.88581210162148 40.78669477437268, -73.88598960872169 40.7867636061766, -73.88619559241629 40.78670926170489, -73.8869056208169 40.78672558545581, -73.8878939472925 40.7868835175382, -73.8886406269566 40.78713048120878, -73.88915563110901 40.78744239820899, -73.88965338760802 40.7882676857086, -73.88986799512941 40.7890150877971, -73.8902113312309 40.78992475912329, -73.8906146747935 40.7901717794957, -73.89094094290471 40.7901717794957, -73.89145576739399 40.79018476980371, -73.89205674031911 40.79024972130569, -73.89221125054799 40.79060059434208, -73.89230557365281 40.79109449311719, -73.8923914525939 40.7915039189505, -73.8924943995255 40.7920172619265, -73.89257156480841 40.79233568492049, -73.8926832253982 40.7926866149435, -73.892691849225 40.79306338658551))'), {u'amenity': u'prison', u'gnis:state_id': u'36', u'name': u'Rikers Island', u'way_area': u'2.91925e+06', u'wikipedia': u'en:Rikers Island', u'gnis:county_id': u'005', u'ele': u'8', u'source': u'openstreetmap.org', u'wikidata': u'Q120119', u'gnis:created': u'01/23/1980', u'place': u'island', u'gnis:feature_id': u'962524', u'gnis:edited': u'10/27/2005'}))

        self.assert_has_feature(
            13, 2414, 3077, 'pois',
            {'kind': 'prison', 'name': 'Rikers Island'})

    def test_sf_county_jail(self):
        self.generate_fixtures(dsl.way(103383866, wkt_loads('POLYGON ((-122.405405674236 37.7750759902303, -122.405402530132 37.77510730333, -122.405390941865 37.77513542120428, -122.405370370445 37.7751609828988, -122.405343510818 37.7751800831593, -122.405308207027 37.77519329002789, -122.405271106606 37.77519925441941, -122.405233916353 37.77521459142397, -122.405207236389 37.77523738391099, -122.405195109133 37.77526841292399, -122.405189988736 37.77530178507459, -122.40517902929 37.77532777273878, -122.405156481576 37.7753534763759, -122.405124681215 37.7753754877707, -122.405084706185 37.77539231583258, -122.405040239578 37.77539998431529, -122.405001701852 37.7754085048506, -122.404973404921 37.77543001919798, -122.40495984036 37.77546040909061, -122.404953731816 37.775489378883, -122.40494510799 37.7755201947773, -122.404926692526 37.7755525017494, -122.404902617677 37.77558026443279, -122.404866146076 37.77560497392239, -122.404823835426 37.77562357703839, -122.404775416232 37.77563138750548, -122.404730500468 37.7756304644503, -122.404686932177 37.7756232930214, -122.404642914728 37.77560589697787, -122.404608060095 37.77558267857869, -122.404580571647 37.7755517917062, -122.40456547995 37.77552090482079, -122.404540506786 37.77548952089179, -122.404512928506 37.77546616044729, -122.404495770684 37.77547972228678, -122.404411329048 37.7754131201402, -122.404476007748 37.7753617839031, -122.404456244812 37.77534658893809, -122.405062877123 37.77486759091759, -122.405081023092 37.77488172090658, -122.405129891443 37.77484302319169, -122.405137976281 37.77484941364138, -122.405149474717 37.7748406800266, -122.405161781636 37.77483620671129, -122.405176514007 37.77483499962618, -122.405191066714 37.7748381238465, -122.405202834645 37.7748440882667, -122.405212626281 37.7748518988162, -122.405216309374 37.77484849057651, -122.405254038616 37.77487809965338, -122.405214872069 37.77490905781239, -122.405243887653 37.77493256044269, -122.405271825258 37.77494796850748, -122.40530775787 37.7749591872807, -122.405339109073 37.77497061906689, -122.405367944994 37.77499028741538, -122.405387528267 37.77501549413599, -122.405400194512 37.77504538716529, -122.405405674236 37.7750759902303))'), {
                               u'building': u'yes', u'addr:housenumber': u'425', u'amenity': u'prison', u'name': u'SF County Jail', u'way_area': u'6040.46', u'height': u'18.63', u'source': u'openstreetmap.org', u'addr:street': u'7th Street'}))

        self.assert_has_feature(
            14, 2621, 6332, 'pois',
            {'kind': 'prison', 'name': 'SF County Jail'})

    def test_rikers_island_landuse(self):
        # Rikers Island also should have a landuse polygon
        self.generate_fixtures(dsl.way(113738569, wkt_loads('LINESTRING (-73.88619559241629 40.78670926170489, -73.88598960872169 40.7867636061766, -73.88581210162148 40.78669477437268, -73.88544783477379 40.78668321171088, -73.88529018044149 40.78672259276838, -73.88495340204139 40.78655996721398, -73.883889617082 40.78629157636468, -73.88361302580599 40.78626858693091, -73.88341225233998 40.78631579007937, -73.8833307751437 40.78649045504029, -73.88328738651551 40.78648215710478, -73.88328738651551 40.78631789857658, -73.8829500691263 40.7861866955101, -73.88169287688619 40.78589680995149, -73.88157798236141 40.78593775585329, -73.88141251268598 40.7858288614642, -73.88110654650029 40.78573180179259, -73.8807860276069 40.78578771144548, -73.8794390936699 40.78556169196288, -73.87916142441559 40.7854651760361, -73.87862306406581 40.78537117659838, -73.87804203374 40.78545470143099, -73.87782455160971 40.78556720132448, -73.8766314990809 40.78586048914709, -73.876209740055 40.78582926956337, -73.8760088767575 40.78590007474199, -73.87512152091979 40.78593816395188, -73.8743435798838 40.78582457642207, -73.8736586144796 40.7858032192241, -73.87312357789638 40.78588232244199, -73.8729069042499 40.7859578206963, -73.87267298294989 40.78618309065278, -73.8723882170048 40.7863659178819, -73.87206850659518 40.78650956749447, -73.87172292470538 40.78674721441948, -73.8715374225992 40.78687011849157, -73.8714113889649 40.78732058343628, -73.87127897729199 40.787511977401, -73.8711282399873 40.78760957858857, -73.870890006774 40.7879340760004, -73.8709898994336 40.7884577846806, -73.87103867795351 40.78882471836661, -73.8710150522615 40.78898216936368, -73.8710622138139 40.78919987960899, -73.8710590697104 40.78938970386069, -73.8712609211548 40.7899572690156, -73.8713451831284 40.79014348645999, -73.871699388845 40.79054836137328, -73.8720644641764 40.7908744086858, -73.8728886684496 40.79141836140191, -73.87358504245789 40.79172175694869, -73.8738783423981 40.79182479278079, -73.8741893391495 40.7918462160525, -73.87428527922179 40.79181336703301, -73.87487690966789 40.79212498999629, -73.87526866496339 40.79240519097548, -73.87530989763491 40.79251611487138, -73.8755793023886 40.79288717469921, -73.87592048253349 40.79315438273728, -73.87630505130659 40.79332576528559, -73.8769245295266 40.79370158118189, -73.87768118049038 40.79410786256829, -73.8780131079879 40.79429651665539, -73.87850394745909 40.79447836943888, -73.8791124662326 40.79465369300449, -73.87945247856759 40.79470408654268, -73.87967651839951 40.79481038209889, -73.87984216773791 40.7947959645414, -73.8799593978824 40.7948418014822, -73.8804840140084 40.79485628703697, -73.88151429180769 40.79501800818069, -73.88172665354088 40.7950254209571, -73.88205364030431 40.79509771248509, -73.8826248789935 40.79517381232468, -73.8830125918701 40.79532118325839, -73.88324552502328 40.79548997596088, -73.883586166179 40.79585428654799, -73.88368004012619 40.79587781671319, -73.8837236084175 40.79585727882378, -73.88357673386849 40.79560347895109, -73.88365183302629 40.79557491620369, -73.8838148772504 40.79563476194608)'), {u'source': u'openstreetmap.org', u'area': u'yes'}), dsl.way(-3955540, wkt_loads(
            'POLYGON ((-73.892691849225 40.79306338658551, -73.89258018863518 40.79354427739299, -73.89255449681798 40.7938367138842, -73.89243430223299 40.7939277089761, -73.8924429260597 40.7939666776881, -73.8923999865892 40.7945450169311, -73.89222831853839 40.79494775678188, -73.89221125054799 40.79525317640758, -73.89212528177529 40.79569508367947, -73.8919107640854 40.79654631474289, -73.89165330692499 40.79691667199458, -73.8910352660095 40.7974690077811, -73.89073486937851 40.79770709151379, -73.890674772086 40.79775476256129, -73.8906644414602 40.79775945485938, -73.89063093430009 40.79777448381198, -73.8902113312309 40.7979627874593, -73.8901255421213 40.79784582028729, -73.8895247488593 40.79780025743779, -73.8890439705192 40.79783276347388, -73.8886577847786 40.79806016927321, -73.8883882003618 40.7982225626507, -73.88825453104748 40.79830321516039, -73.88823719356249 40.79831361973499, -73.8878939472925 40.79837856328498, -73.88742179277918 40.79834605751611, -73.8869154124535 40.79815768695209, -73.88628883754281 40.79775476256129, -73.88537902382311 40.79710511408508, -73.8844692101033 40.79632536430771, -73.88407440053589 40.79598098210779, -73.8838148772504 40.79563476194608, -73.88365183302629 40.79557491620369, -73.88357673386849 40.79560347895109, -73.8837236084175 40.79585727882378, -73.88368004012619 40.79587781671319, -73.883586166179 40.79585428654799, -73.88324552502328 40.79548997596088, -73.8830125918701 40.79532118325839, -73.8826248789935 40.79517381232468, -73.88205364030431 40.79509771248509, -73.88172665354088 40.7950254209571, -73.88151429180769 40.79501800818069, -73.8804840140084 40.79485628703697, -73.8799593978824 40.7948418014822, -73.87984216773791 40.7947959645414, -73.87967651839951 40.79481038209889, -73.87945247856759 40.79470408654268, -73.8791124662326 40.79465369300449, -73.87850394745909 40.79447836943888, -73.8780131079879 40.79429651665539, -73.87768118049038 40.79410786256829, -73.8769245295266 40.79370158118189, -73.87630505130659 40.79332576528559, -73.87592048253349 40.79315438273728, -73.8755793023886 40.79288717469921, -73.87530989763491 40.79251611487138, -73.87526866496339 40.79240519097548, -73.87487690966789 40.79212498999629, -73.87428527922179 40.79181336703301, -73.8741893391495 40.7918462160525, -73.8738783423981 40.79182479278079, -73.87358504245789 40.79172175694869, -73.8728886684496 40.79141836140191, -73.8720644641764 40.7908744086858, -73.871699388845 40.79054836137328, -73.8713451831284 40.79014348645999, -73.8712609211548 40.7899572690156, -73.8710590697104 40.78938970386069, -73.8710622138139 40.78919987960899, -73.8710150522615 40.78898216936368, -73.87103867795351 40.78882471836661, -73.8709898994336 40.7884577846806, -73.870890006774 40.7879340760004, -73.8711282399873 40.78760957858857, -73.87127897729199 40.787511977401, -73.8714113889649 40.78732058343628, -73.8715374225992 40.78687011849157, -73.87172292470538 40.78674721441948, -73.87206850659518 40.78650956749447, -73.8723882170048 40.7863659178819, -73.87267298294989 40.78618309065278, -73.8729069042499 40.7859578206963, -73.87312357789638 40.78588232244199, -73.8736586144796 40.7858032192241, -73.8743435798838 40.78582457642207, -73.87512152091979 40.78593816395188, -73.8760088767575 40.78590007474199, -73.876209740055 40.78582926956337, -73.8766314990809 40.78586048914709, -73.87782455160971 40.78556720132448, -73.87804203374 40.78545470143099, -73.87862306406581 40.78537117659838, -73.87916142441559 40.7854651760361, -73.8794390936699 40.78556169196288, -73.8807860276069 40.78578771144548, -73.88110654650029 40.78573180179259, -73.88141251268598 40.7858288614642, -73.88157798236141 40.78593775585329, -73.88169287688619 40.78589680995149, -73.8829500691263 40.7861866955101, -73.88328738651551 40.78631789857658, -73.88328738651551 40.78648215710478, -73.8833307751437 40.78649045504029, -73.88341225233998 40.78631579007937, -73.88361302580599 40.78626858693091, -73.883889617082 40.78629157636468, -73.88495340204139 40.78655996721398, -73.88529018044149 40.78672259276838, -73.88544783477379 40.78668321171088, -73.88581210162148 40.78669477437268, -73.88598960872169 40.7867636061766, -73.88619559241629 40.78670926170489, -73.8869056208169 40.78672558545581, -73.8878939472925 40.7868835175382, -73.8886406269566 40.78713048120878, -73.88915563110901 40.78744239820899, -73.88965338760802 40.7882676857086, -73.88986799512941 40.7890150877971, -73.8902113312309 40.78992475912329, -73.8906146747935 40.7901717794957, -73.89094094290471 40.7901717794957, -73.89145576739399 40.79018476980371, -73.89205674031911 40.79024972130569, -73.89221125054799 40.79060059434208, -73.89230557365281 40.79109449311719, -73.8923914525939 40.7915039189505, -73.8924943995255 40.7920172619265, -73.89257156480841 40.79233568492049, -73.8926832253982 40.7926866149435, -73.892691849225 40.79306338658551))'), {u'amenity': u'prison', u'gnis:state_id': u'36', u'name': u'Rikers Island', u'way_area': u'2.91925e+06', u'wikipedia': u'en:Rikers Island', u'gnis:county_id': u'005', u'ele': u'8', u'source': u'openstreetmap.org', u'wikidata': u'Q120119', u'gnis:created': u'01/23/1980', u'place': u'island', u'gnis:feature_id': u'962524', u'gnis:edited': u'10/27/2005'}))

        self.assert_has_feature(
            13, 2414, 3077, 'landuse',
            {'kind': 'prison'})
