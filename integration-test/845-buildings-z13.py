# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class BuildingsZ13(FixtureTest):
    def test_buildings_exist_at_zoom_13(self):
        # Earlier work in 845 dropped buildings from zoom 13
        self.generate_fixtures(dsl.way(60500069, wkt_loads('POLYGON ((-122.390304275657 37.61656749592758, -122.38865110604 37.61697721529517, -122.388628288832 37.616918013192, -122.388243360733 37.61701137033331, -122.388205092502 37.61691972094558, -122.388382869096 37.61685311852468, -122.388579061154 37.61679398747918, -122.388837775956 37.6167310139313, -122.388856640577 37.61660620518289, -122.388870025475 37.61647506326769, -122.38886912716 37.61633602269909, -122.388863198279 37.61620872278979, -122.388850981191 37.61610348139231, -122.388843615005 37.61603965337279, -122.388825558868 37.61596401318499, -122.388805346774 37.61587826857059, -122.38879510598 37.6158481689854, -122.388779744789 37.61580291284848, -122.388750459711 37.6157168834181, -122.388717222045 37.61564195447828, -122.388684523369 37.61556851977449, -122.388621281973 37.61545132296039, -122.388605471624 37.61542200593848, -122.388564418615 37.6153626602813, -122.388506297616 37.6152791208705, -122.388410267712 37.6151573694829, -122.388306961455 37.61504266255769, -122.388212279024 37.61495065495198, -122.388114182995 37.6148646956939, -122.387633763981 37.61497968752667, -122.387571780226 37.61481666378049, -122.387783333476 37.61476528738829, -122.387773362176 37.61473440460918, -122.389432640337 37.6143154222277, -122.390249388594 37.61642546694318, -122.390304275657 37.61656749592758))'), {u'building': u'yes', u'layer': u'2', u'name': u'International Terminal Main Hall', u'way_area': u'50934.8', u'source': u'openstreetmap.org', u'aeroway': u'terminal', u'woe:id': u'12521721', u'ref': u'INTL'}), dsl.way(23654700, wkt_loads(
            'POLYGON ((-122.390360420363 37.62100747264069, -122.390251903876 37.62117247507878, -122.390117605741 37.62120776662641, -122.387781716508 37.62023069686398, -122.387501262476 37.62029779433149, -122.387482577518 37.62029146169928, -122.387177689311 37.6207477656035, -122.387105644425 37.6207185218227, -122.386971436122 37.62092180499501, -122.386909362536 37.62093639127049, -122.386797162957 37.62088999978909, -122.386780184798 37.62083499880809, -122.387210028661 37.6201823838037, -122.387194038649 37.62017398771638, -122.38685321783 37.619292677888, -122.387054081128 37.61898785297091, -122.386910440514 37.61861948561809, -122.386849175412 37.61862610301178, -122.386800666386 37.61848002213009, -122.386625944064 37.6185022224579, -122.386457240453 37.61851609765939, -122.386286919875 37.6185210073455, -122.38610384322 37.61851538611069, -122.385931097191 37.61849816662929, -122.385765897011 37.6184689931186, -122.385603571439 37.61843377142578, -122.385426782991 37.6183829667728, -122.385273979561 37.6183274658518, -122.385072667106 37.61825019142338, -122.384886715842 37.61852549010209, -122.384940884254 37.61857871392129, -122.384286820895 37.61957167270749, -122.384235257598 37.61952008613909, -122.384202289427 37.6195692534761, -122.383889585877 37.61943889948098, -122.383914199715 37.6193981993876, -122.383847814216 37.61939307629729, -122.384295624385 37.6187057963089, -122.384387522039 37.6187072905574, -122.384773078959 37.61812189861791, -122.384737775168 37.61810510597689, -122.384905131305 37.61784460609038, -122.38495714376 37.61776370222508, -122.385019127515 37.61766721517829, -122.385580844062 37.61790231319129, -122.385772814038 37.6179645741931, -122.385949871981 37.61800129037081, -122.386129265543 37.61802505625921, -122.386295633534 37.61802918326898, -122.386463438829 37.61802370430757, -122.386623159286 37.6180010769047, -122.386778477999 37.6179694127602, -122.386935593342 37.61792188094031, -122.387079233956 37.6178639603882, -122.387214430406 37.61779906654648, -122.38733866741 37.617724495483, -122.387459580647 37.617637685563, -122.38755848516 37.61754760237487, -122.387655413379 37.61744969192978, -122.387732488831 37.6173527775396, -122.387815582994 37.6172341604157, -122.387831303512 37.61723956827911, -122.38807627409 37.61686649593879, -122.388205092502 37.61691972094558, -122.388243360733 37.61701137033331, -122.388113284679 37.61720769034191, -122.388191258446 37.61724269914719, -122.388256835462 37.6172819061434, -122.38830669196 37.61733278270469, -122.388250457423 37.61741610634039, -122.388289713801 37.61743311260478, -122.388280011996 37.61744606297911, -122.388352236545 37.6174761619175, -122.388230694487 37.6176490704763, -122.388112027038 37.61779380103491, -122.387964164342 37.6179336927427, -122.387814415184 37.61805650691409, -122.38764193865 37.61816878991299, -122.387474313018 37.61825801848708, -122.387298243222 37.61833308710078, -122.387107171561 37.61840289017029, -122.387179935099 37.61854747695178, -122.38712118528 37.61856775607931, -122.387524259348 37.61959686117071, -122.387582290515 37.61958319963239, -122.38789643137 37.6197137668357, -122.387976561093 37.61992516425759, -122.39032089449 37.620911060956, -122.390360420363 37.62100747264069))'), {u'building': u'yes', u'name': u'Domestic Terminal 3', u'way_area': u'73814', u'addr:state': u'CA', u'ele': u'8', u'source': u'openstreetmap.org', u'aeroway': u'terminal', u'gnis:import_uuid': u'57871b70-0100-4405-bb30-88b2e001a944', u'woe:id': u'12521721', u'gnis:feature_id': u'2124419', u'gnis:county_name': u'San Mateo'}))

        self.assert_has_feature(
            13, 1310, 3170, 'buildings',
            {'kind': 'building'})
