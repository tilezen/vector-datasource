# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class ClipBuildings(FixtureTest):

    def test_high_line(self):
        from ModestMaps.Core import Coordinate
        from shapely.geometry import box
        from shapely.geometry import shape
        from tilequeue.tile import coord_to_mercator_bounds

        # this is mid way along the High Line in NYC, which is a huge long
        # "building". we should be clipping it to the bounds of the tile.
        #
        # NOTE: we _don't_ clip the fixture, that has to happen in the
        # query.
        #
        # NOTE: https://github.com/tilezen/vector-datasource/issues/1142
        # we want to clip all buildings to the bounding box of the tile, so
        # that there are no overlaps.
        self.generate_fixtures(dsl.way(-7141751, wkt_loads('POLYGON ((-74.00832281293381 40.7394398124915, -74.00830439747038 40.73966530823048, -74.0082918210565 40.73982512183188, -74.00828544301798 40.73989665667138, -74.00824780360749 40.74035717312061, -74.0081553669648 40.74069231492279, -74.00811530210309 40.74088125683539, -74.0080881729816 40.74100921431009, -74.0080344537276 40.7412720027987, -74.00796914620641 40.74157065885181, -74.00796609193439 40.7415827057976, -74.00790518615818 40.7418352147232, -74.00789764030981 40.7418808840249, -74.0078936877226 40.74190436524828, -74.00789207075501 40.74191437028878, -74.007885602885 40.74195357369829, -74.007860450057 40.74210528250789, -74.00779999343838 40.7424276881022, -74.00749717135611 40.74284265453919, -74.007488817024 40.74285388452819, -74.00746671846798 40.74288471594268, -74.00752034789051 40.74290778844879, -74.0074379723789 40.74302110904868, -74.0073881158806 40.74299286399228, -74.00735317141609 40.74304166327489, -74.00734670354599 40.74303737547328, -74.0071343418129 40.74333268865769, -74.00714152833518 40.7433354110594, -74.00720117647001 40.74335909594929, -74.0071084703327 40.7434796981892, -74.0072566923546 40.7437145724654, -74.00722453266739 40.74375826674808, -74.00704909169241 40.7435598046351, -74.007006511548 40.74347636325429, -74.0069896232206 40.74356552165899, -74.0069869282748 40.7438065890523, -74.00709068369009 40.74385001103649, -74.00699887586801 40.7439780989187, -74.00706741732419 40.74432778710959, -74.00708035306428 40.74433329989039, -74.00711341106678 40.744347388106, -74.007046127252 40.74443368686849, -74.007101373642 40.74445587407167, -74.00708762941809 40.74447459026498, -74.0070408271918 40.74453808916498, -74.0070927498152 40.7445568053351, -74.00703382033259 40.74463806748181, -74.00705088832299 40.7446452817044, -74.00700031317248 40.74471701553578, -74.0070119014397 40.74472218799129, -74.0069620449414 40.7447906549294, -74.00697138742039 40.74479501067649, -74.0068542471073 40.74495338272707, -74.0068584691891 40.7449572620549, -74.00670602508541 40.74516769823619, -74.0065572640744 40.74538031160611, -74.0064573714148 40.7455893852941, -74.00637858916438 40.74570011513548, -74.00529737688839 40.74719049227489, -74.00533169253218 40.74720430766089, -74.0051680194875 40.74743569793549, -74.00471814319322 40.7480852878009, -74.0046617289933 40.74806351013981, -74.0045451276695 40.74821847165479, -74.0042063729758 40.7486820609962, -74.00387318783689 40.74914911786458, -74.0037918903037 40.74930155885421, -74.0029797234554 40.75042022003169, -74.0024423512524 40.75115756792688, -74.00222927086701 40.75145250479549, -74.00216468199808 40.75154546339898, -74.00211725095109 40.75161909523129, -74.00202679060199 40.75180405912329, -74.0020020869317 40.75189048431209, -74.0019877138871 40.75201991773139, -74.00199759535521 40.75216098762209, -74.0020531112398 40.75232410568999, -74.00212012556001 40.7524433987087, -74.0023955490261 40.75275990185269, -74.00240471184199 40.75277038161278, -74.00259560383988 40.75289178338889, -74.00570575101661 40.7542046641078, -74.00567574728599 40.75424855564479, -74.00574958880239 40.7543362705831, -74.00584202544509 40.75444487635099, -74.00588595306249 40.754521090819, -74.0059412892841 40.7546320099334, -74.00597362863429 40.7547336062359, -74.00598063549349 40.7548837888313, -74.00595278771969 40.75507779402898, -74.00586277652819 40.75525798495069, -74.0051998198485 40.75615648254439, -74.0049826970444 40.75629046679348, -74.0047818337468 40.75638049262529, -74.004583126406 40.75643601870109, -74.0043705850098 40.7564614000904, -74.00415813344509 40.75645445933609, -74.00391792393809 40.75641975555381, -74.0036937942747 40.75633660249569, -74.0035551842264 40.75626270370049, -74.00342133524899 40.75614716011579, -74.00323655179511 40.75604100682211, -74.0032781437928 40.7559694213001, -74.00344442195181 40.75607326111, -74.00358303200019 40.75617961849289, -74.0037192165972 40.75625807651728, -74.00387399632069 40.75632966172837, -74.00404952712719 40.75637130632149, -74.0042944078737 40.7564013149091, -74.0045462056478 40.75638049262529, -74.0047724912679 40.75632278900709, -74.00491568272419 40.75625120378858, -74.0051167256847 40.75611490586368, -74.00575650583011 40.75523716230868, -74.0058257659385 40.7551008623049, -74.00586511214789 40.7549114844519, -74.0058535238808 40.75474517445868, -74.00580267923569 40.75459036425079, -74.00572883771929 40.75445637657539, -74.0056178957818 40.7543247703379, -74.00550937929539 40.7542461739342, -74.0054216138922 40.75418846846359, -74.00530842616639 40.7541330766085, -74.00510280179779 40.75403842039558, -74.0024419020948 40.75292267820008, -74.002192889098 40.75281686000951, -74.00141404974669 40.75248606649619, -74.00118758446349 40.75237527990329, -74.00101214348858 40.75224128776399, -74.0011183243551 40.75214901064349, -74.00120168801348 40.75223618394428, -74.00128118891618 40.75228171000207, -74.00163764042088 40.75243958786818, -74.00213333079469 40.75264966012008, -74.0020663164745 40.75254806063321, -74.00206191472959 40.752541187521, -74.00196157291228 40.7523855555718, -74.0019134232131 40.75228232245999, -74.0018975230326 40.75222339036788, -74.0018773109387 40.7521055940779, -74.00187533464511 40.7519693557054, -74.00189949932619 40.75184686342378, -74.0018782990855 40.7518331170536, -74.00193462345381 40.75175057072168, -74.0019308505296 40.7517460793273, -74.0020133158727 40.75158295984141, -74.00235772995261 40.75111578396379, -74.00276080402058 40.75055911563168, -74.00280293500738 40.75050031811769, -74.00320879385281 40.74992418139269, -74.0032147227337 40.7498771565471, -74.003217148185 40.74985850992759, -74.00400919277099 40.7487908801634, -74.00460522496201 40.74797197582978, -74.00628336774419 40.74566179868388, -74.0063335835686 40.74558707133109, -74.0063781400067 40.7455128202991, -74.0064454238215 40.74536928621749, -74.00646042568668 40.74533940876668, -74.00645476630049 40.745336754505, -74.0066254462044 40.74511311556489, -74.00678471750429 40.74488757023619, -74.0068654760483 40.7447548561216, -74.0069019476489 40.7446670604849, -74.00692377671029 40.74458089814269, -74.0069330293577 40.74452508993101, -74.00693788026018 40.74449548433628, -74.0069397667223 40.74444797923952, -74.00694201251051 40.74438060089219, -74.0069160511988 40.74437638123579, -74.0069313225587 40.74427116197648, -74.00690634939379 40.74400049045201, -74.00676773934539 40.74393699103869, -74.0068508335092 40.7438227872252, -74.006828016301 40.7437319957343, -74.0067652240626 40.74370980828958, -74.00683502316021 40.74362167097459, -74.00684301816629 40.74344927541001, -74.0068445453022 40.7434198054563, -74.0069314123902 40.74324441472271, -74.0069853113072 40.7432670106833, -74.0070602308019 40.74316417177648, -74.0071325451823 40.7430648718473, -74.0071720710548 40.74301035551058, -74.00724510408739 40.74291010250508, -74.00734311028489 40.74277568292929, -74.0075530465668 40.74249166538279, -74.00761943206631 40.74235336548188, -74.0076729716572 40.7421333918186, -74.0077141144973 40.7417787916529, -74.00771788742139 40.7417611636875, -74.00776837274039 40.74152716731758, -74.00777636774639 40.74149027776248, -74.00778535089928 40.7414489641588, -74.00784490920259 40.74118386225317, -74.0079128218381 40.7408822097112, -74.0079423764109 40.74075071273261, -74.0079467781558 40.74073077036279, -74.0079894481318 40.74054148770819, -74.00804208940748 40.74043360792479, -74.00809320354709 40.74026106797047, -74.00813228026199 40.7398473105725, -74.0081335379034 40.73983077111318, -74.00813488537628 40.7397962628454, -74.00815689410079 40.73947901735949, -74.00815994837281 40.73943511607349, -74.00818644867358 40.739436205098, -74.00832281293381 40.7394398124915))'), {
                               u'website': u'http://www.thehighline.org/', u'building': u'yes', u'layer': u'1', u'way_area': u'48210.6', u'name': u'The High Line', u'building:colour': u'#3D4647', u'building:part': u'yes', u'wheelchair': u'yes', u'name:he': u'\u05e8\u05db\u05d1\u05ea \u05de\u05e2\u05d2\u05dc\u05d9\u05ea \u05e0\u05d7\u05de\u05d3\u05d4', u'wikipedia': u'en:High Line (New York City)', u'leisure': u'park', u'height': u'7.5', u'min_height': u'5;5.5', u'roof:shape': u'flat', u'wikidata': u'Q843869', u'source': u'openstreetmap.org', u'old_railway_operator': u'NYC', u'building:material': u'metal', u'roof:material': u'concrete;grass'}), dsl.way(-7141751, wkt_loads('POLYGON ((-74.0076264389255 40.74321957276918, -74.0075904164826 40.74326918860679, -74.00753804470159 40.74324237291861, -74.00753391245129 40.74323760870891, -74.00745557935851 40.7431462719373, -74.0073948532453 40.74307290296429, -74.00735317141609 40.74304166327489, -74.0073881158806 40.74299286399228, -74.0074379723789 40.74302110904868, -74.00751720378699 40.74311666572878, -74.00757927737311 40.74318949017198, -74.0076264389255 40.74321957276918))'), {u'website': u'http://www.thehighline.org/', u'building': u'yes', u'layer': u'1', u'way_area': u'355.099', u'name': u'The High Line', u'building:colour': u'#3D4647', u'building:part': u'yes', u'wheelchair': u'yes', u'name:he': u'\u05e8\u05db\u05d1\u05ea \u05de\u05e2\u05d2\u05dc\u05d9\u05ea \u05e0\u05d7\u05de\u05d3\u05d4', u'wikipedia': u'en:High Line (New York City)', u'leisure': u'park', u'height': u'7.5', u'min_height': u'5;5.5', u'roof:shape': u'flat', u'wikidata': u'Q843869', u'source': u'openstreetmap.org', u'old_railway_operator': u'NYC', u'building:material': u'metal', u'roof:material': u'concrete;grass'}))
        coord = Coordinate(zoom=16, column=19295, row=24631)
        with self.features_in_tile_layer(
                coord.zoom, coord.column, coord.row, 'buildings') as buildings:
            # tile bounds as a box
            tile_bounds = coord_to_mercator_bounds(coord)
            bbox = box(*tile_bounds)

            # need to check that we at least saw the high line
            saw_the_high_line = False

            for building in buildings:
                building_bounds = shape(building['geometry']).bounds
                building_box = box(*building_bounds)

                if building['properties']['id'] == -7141751:
                    saw_the_high_line = True

                self.assertTrue(
                    building_box.within(bbox),
                    'feature %r extends outside of the bounds of the '
                    'tile (%r not within %r).' %
                    (building['properties']['id'], building_bounds,
                     tile_bounds))

        self.assertTrue(
            saw_the_high_line,
            "Expected to see the High Line in this tile, but didn't.")
