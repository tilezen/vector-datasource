-- These fill in the gaps caused by several missing ways along Aurora Ave in Seattle in Daylight 1.15

-- way 8591493
update planet_osm_line
set way = st_geometryfromtext('LineString (-13619633.12467937543988228 6049279.65133139304816723, -13619631.32130362465977669 6049506.8966157054528594, -13619632.42336658574640751 6049588.83264238853007555, -13619633.04675573110580444 6049635.17195791471749544, -13619634.13768674246966839 6049716.00193730648607016, -13619633.15807522274553776 6049923.34396426193416119, -13619633.12467937543988228 6049951.40641953889280558, -13619633.04675573110580444 6050016.2908675679937005, -13619632.99109598807990551 6050065.73955697193741798, -13619632.9465681929141283 6050103.6030330928042531, -13619634.2044784389436245 6050257.30632273852825165, -13619634.37145767547190189 6050285.96485182363539934, -13619634.26013818383216858 6050405.78960587084293365, -13619634.31579792685806751 6050437.4236185634508729, -13619634.66088834963738918 6050570.60507556796073914, -13619634.82786758616566658 6050586.07528126612305641)')
where osm_id = 8591493;

-- way 338894965
update planet_osm_line
set way = st_geometryfromtext('LineString (-13619651.60371484979987144 6050599.95882281567901373, -13619651.38107586838304996 6050519.93042933195829391, -13619651.28088832460343838 6050482.2634601229801774, -13619650.80221451632678509 6050364.81761655956506729, -13619649.47751257382333279 6050252.19936301372945309, -13619649.95618638582527637 6050159.92753368522971869, -13619650.3012768067419529 6050103.95010195393115282, -13619651.93767332099378109 6049925.82297607138752937, -13619648.65374834276735783 6049712.59751071780920029, -13619647.87451190687716007 6049633.3044985169544816, -13619646.64999750815331936 6049508.02038007136434317)')
where osm_id = 338894965;

-- way 52840110
update planet_osm_line
set way = st_geometryfromtext('LineString (-13619417.71033274382352829 6053710.50138364918529987, -13619413.46906014531850815 6053762.45136499404907227, -13619409.45042652636766434 6053787.40135585237294436, -13619403.69520885124802589 6053812.0207349956035614, -13619396.23680296912789345 6053836.16069143451750278, -13619387.10860472172498703 6053859.73854971956461668, -13619376.35514191351830959 6053882.60549627617001534, -13619364.0432062316685915 6053904.67885359935462475, -13619341.66798858158290386 6053941.73245906084775925, -13619328.57681646570563316 6053968.61750403046607971, -13619322.91065438091754913 6053985.71418752893805504, -13619318.96994440816342831 6054003.29040714539587498, -13619316.82147823646664619 6054021.16428527142852545)')
where osm_id = 52840110;

-- way 398813067
update planet_osm_line
set way = st_geometryfromtext('LineString (-13619549.90222806110978127 6053201.8644335912540555, -13619536.44370162300765514 6053232.6159133343026042, -13619521.92764002270996571 6053262.87150845024734735, -13619489.88989057391881943 6053317.57984575442969799)')
where osm_id = 398813067;

-- way 48003053
update planet_osm_line
set way = st_geometryfromtext('LineString (-13619639.90403636731207371 6052813.9422768410295248, -13619641.28439805097877979 6052734.17439109832048416, -13619641.21760635823011398 6052699.4735244931653142, -13619641.58496067859232426 6052651.15044444613158703, -13619642.03023864142596722 6052532.74929661210626364, -13619642.63136388920247555 6052414.68040402606129646, -13619642.35306516289710999 6052367.9128730520606041, -13619641.64062042348086834 6052354.5885539697483182, -13619640.13780729658901691 6052340.5699377441778779, -13619636.65350723452866077 6052311.09454891830682755)')
where osm_id = 48003053;
