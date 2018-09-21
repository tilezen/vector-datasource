# Roads layer network values

Any road with `shield_text` will include a `network` property with a value like `AA:bcdef` where `AA` is a 2-character country code, followed by a `:` separator, and `bcdef` category value which either indicates the "region" (state or province) or "level" of the road network. There are exceptions to this for trans-national networks like `e-road`. In some cases, like the United States and Canada an additional _modifier_ to appended to indicate `Truck` and other alternate routes, or further network disambiguation.

## OpenStreetMap ETL logic

Some countries without network tags but with ref values with `;` and `/` and other separators, including: Switzerland, **Greece**, **India**, **Italy**, **Japan**, **Russia**, **Turkey**, Vietnam, and South Africa.

When we don't see network we backfill based on common road operators values. Network values always replace plural `??:roads` with singular `??:road`.

When a network value can't be determined from the upstream data source we calculate where the road is located and provide the relevant 2-char country code as the network value. See table below for mapping of country codes to country names.

#### Network value include:

* `AM:AM` - **Armenia**
* `AR:national` - **Argentina** ref starts with `RN`
* `AR:provincial` - **Argentina** ref starts with `RP`
* `AsianHighway` - **Asian Highway** across multiple countries if network == `AH` or net == `AH` or ref prefixed with `AH` 
* `AT:A-road` - **Austria** from OSM
* `AU:A-road` - **Australia** when ref prefixed `A`
* `AU:B-road` - **Australia** when ref prefixed `B`
* `AU:C-road` - **Australia** when ref prefixed `C`
* `AU:M-road` - **Australia** when ref prefixed `M`
* `AU:Metro-road` - **Australia** when ref prefixed `MR`
* `AU:N-route` - **Australia** when ref prefixed `N`
* `AU:R-route` - **Australia** when ref prefixed `R`
* `AU:S-route` - **Australia** when ref prefixed `S`
* `AU:T-drive` - **Australia** when ref prefixed `T`
* `BE:A-road` - **Belgium** OSM network value
* `BE:N-road` - **Belgium** OSM network value
* `BE:R-road` - **Belgium** OSM network value
* `BR:AC` - **Acre** region in Brazil
* `BR:AL` - **Alagoas** region in Brazil
* `BR:AM` - **Amazonas** region in Brazil
* `BR:AP` - **Amapá** region in Brazil
* `BR:BA` - **Bahia** region in Brazil
* `BR:BR` - **Federal routes in Brazil** and when ref prefixed with `BR`
* `BR:CE` - **Ceará** region in Brazil
* `BR:DF` - **Distrito Federal** region in Brazil
* `BR:ES` - **Espírito Santo** region in Brazil
* `BR:GO` - **Goiás** region in Brazil
* `BR:MA` - **Maranhão** region in Brazil
* `BR:MG:local` - **Minas Gerais** region in Brazil local roads, ref prefix including `LMG`
* `BR:MG` - **Minas Gerais** region in Brazil state roads, ref prefix including `AMG`, `CMG`, `MGC`
* `BR:MS` - **Mato Grosso do Sul** region in Brazil
* `BR:MT` - **Mato Grosso** region in Brazil
* `BR:PA` - **Pará** region in Brazil
* `BR:PB` - **Paraíba** region in Brazil
* `BR:PE` - **Pernambuco** region in Brazil
* `BR:PI` - **Piauí** region in Brazil
* `BR:PR` - **connecting roads in Paraná** region in Brazil with ref prefix in `PRC`
* `BR:PR` - **Paraná** region in Brazil
* `BR:RJ` - **Rio de Janeiro** region in Brazil
* `BR:RN` - **Rio Grande do Norte** region in Brazil
* `BR:RO` - **Rondônia** region in Brazil
* `BR:RR` - **Roraima** region in Brazil
* `BR:RS` - **Rio Grande do Sul** region in Brazil state roads with prefix in (ERS, VRS, RSC)
* `BR:SC` - **Santa Catarina** region in Brazil
* `BR:SE` - **Sergipe** region in Brazil
* `BR:SP:PLN` - **municipal roads in Paulínia** region in Brazil, with ref prefix in `PLN`
* `BR:SP:SCA` - **municipal roads in São Carlos** region in Brazil with ref in `SCA`
* `BR:SP` - **São Paulo** region in Brazil and access roads ref prefix of `SPA`
* `BR:TO` - **Tocantins** region in Brazil
* `BR:Trans-Amazonian` - **Trans-Amazonian** route in Brazil when network is BR and ref == `BR-230`
* `BR` - **Brazil** fallback when operator in `Autopista Litoral Sul`, `Cart`, `DNIT`, `Ecovias`, `NovaDutra`, `Triângulo do Sol`, `Viapar`, `ViaRondon`
* `CA:AB:primary` - **Alberta** region in Canada
* `CA:AB:trunk` - **Alberta** region in Canada
* `CA:AB` - **Alberta** region in Canada
* `CA:BC:primary` - **British Columbia** region in Canada
* `CA:BC:trunk` - **British Columbia** region in Canada
* `CA:BC` - **British Columbia** region in Canada
* `CA:MB:PTH` - **Manitoba** region in Canada
* `CA:MB` - **Manitoba** region in Canada
* `CA:NB` - **New Brunswich** region in Canada
* `CA:NB2` - **New Brunswich** region in Canada network.startswith(`CA:NB`) and \ and refnum >= 100
* `CA:NB3` - **New Brunswich** region in Canada network.startswith(`CA:NB`) and \ and refnum >= 200
* `CA:NS:R` - **Nova Scotia** region in Canada
* `CA:NS:T` - **Nova Scotia** region in Canada
* `CA:NS:H` - **Nova Scotia** region in Canada
* `CA:NT` - **Northwest Territories** region in Canada
* `CA:ON:primary` - **Ontario** region in Canada
* `CA:ON:secondary` - **Ontario** region in Canada
* `CA:PEI` - **Prince Edward Island** region in Canada
* `CA:QC:A` - **Quebec** region in Canada
* `CA:QC:R` - **Quebec** region in Canada
* `CA:qc` - **Quebec** region in Canada, should be normalized to `CA:QC`
* `CA:SK:primary` - **Sashsqatuan** region in Canada
* `CA:SK:secondary` - **Sashsqatuan** region in Canada
* `CA:SK:teriary` - **Sashsqatuan** region in Canada
* `CA:transcanada` - **Canada Transcanada** highway and when ref)) when nat_name and nat_name.lower() == `trans-canada highway`
* `CA:yellowhead` - **Canada Transcanda variant**, normalized when name contains that value
* `CA:YT` - **Yukon Territory** region in Canada
* `CD:RRIG` - **Democratic Republic of the Congo** if network == `CD:rrig`
* `CH:motorway` - **Switzerland** when prefix is `A`
* `CH:national` - **Switzerland** normalized `ch:national` and when `CH:Nationalstrasse`
* `CH:regional` - **Switzerland** normalized `ch:regional`
* `CL:national` - **Chile** pass-thru from OSM
* `CL:regional` - **Chile** pass-thru from OSM
* `CN:expressway:regional` - **China** (when expressway starts with S; normalized from `CN-expressways-regional`)
* `CN:expressway` - **China** (when expressway starts with G; normalized from `CN-expressways`)
* `CN:JX` - **Jinxia** region in China, when ref starts with `X` or network == `JX-roads`:)
* `CN:road` - **China**, normalization of `CN-roads`
* `CZ:national` - **Czechia**, normalization of `cz:national`
* `CZ:regional` - **Czechia**, normalization of `cz:regional`
* `DE:BAB` - **Germany** federal autobahn - when network == `BAB` or when prefix `A`
* `DE:BS` - **Germany** federal roads, when prefix `B`
* `DE:Hamburg:Ring` - **Hamburg** region ring road in Germany  when prefix `Ring`
* `DE:KS` - **Germany** county routes when network == `Kreisstra\xc3\x9fen Hildesheim` or when prefix `K`
* `DE:LS` - **Germany** county routes when network = `Landesstra\xc3\x9fen NRW` or prefix `L`
* `DE:STS` - **Germany** when prefix `S` or `St`
* `DE` - **Germany** when operator in `autobahnplus A8 GmbH`, `Bundesrepublik Deutschland`, `Via Solutions Südwest`, `The Danish Road Directorate`
* `DK:national` - **Denmark**, normalization of `dk:national`
* `e-road` - **European E-Road** which is a rough mix of US:I and US:US. and prefix == `E` and num
* `ES:A-road` - **Spain** when prefix in (`A`, `AP`) and num_digits > 0 and num_digits < 3
* `ES:autonoma` - **Spain**when prefix in `ARA`, `A`, `CA`, `CL`, `CM`, `C`, `EX`, `AG`, `M`, `R`, `Ma`, `Me`, `ML`, `RC`, `RM`, `V`, `CV`, `Cv`
* `ES:city` - **Spain** when prefix in `AI`, `IA`, `CT`, `CS`, `CU`, `CHE`, `EL`, `FE`, `GJ`, `H`,  `VM`, `J`, `LN`, `LL`, `LO`, `ME`, `E`, `MU`, `O`, `PA`, `PR`, `PI`, `CHMS`, `PT`, `SL`, `S`, `SC`, `SI`, `VG`, `EI`, 
* `ES:N-road` - **Spain** when prefix == `N`
* `ES:province` - **Spain** when prefix in `AC`, `DP`, `AB`, `F`,  , `AL`, `AE`, `AS`, `AV`, `BA`, `B`,  , `BP`, `BV`, `BI`, `BU`, `CC`, `CO`, `CR`, `GIP`,, `GIV`,, `GI`, `GR`, `GU`, `HU`, `JA`, `JV`, `LR`, `LE`, `L`,  , `LP`, `LV`, `LU`,, `MP`,, `MA`,, `NA`,, `OU`,, `P`, `PP`,, `EP`,, `PO`,, `DSA`, `SA`,, `NI`,, `SG`,, `SE`,, `SO`,, `TP`,, `TV`,, `TE`,, `TO`,, `VA`,, `ZA`,, `CP`,, `Z`, `PM`,, `PMV`
* `ES` - **Spain** when operator in `Administración central`, `Departamento de Infraestructuras Viarias y Movilidad`
* `FR:A-road` - **France**
* `FR:D-road` - **France** when ref in `^FR:[0-9]+:([A-Z]+)-road$` or N
* `FR:N-road` - **France** when ref starts RN or RNIL
* `FR` - **France** when operator in `APRR`, `ASF`, `Autoroutes du Sud de la **France**`, `DIRIF`, `DIRNO`
* `GA:L-road` - **Gabon** when ref starts `L`
* `GA:national` - **Gabon** when prefix in (`N`, `RN`)
* `GB:A-road-green` - **United Kingdom** highway == `trunk` and ref starts with `A`
* `GB:A-road-white` - **United Kingdom** highway == `primary` and ref starts with `A`
* `GB:B-road` - **United Kingdom** highway == `secondary` and ref starts with `B`
* `GB:M-road` - **United Kingdom** highway == `motorway`: and ref starts or ends with `M`
* `GB` - **United Kingdom** when operator in `Highways England`, `Midland Expressway Ltd`, `Transport for Scotland`, `Transport Scotland`, `Welsh Government`
* `GR:motorway` - **Greece** when ref starts with Greek `Α` or Latin `A`
* `GR:national` - **Greece** when ref starts with Greek `ΕΟ` or Latin `EO`
* `GR:provincial` - **Greece** generically for any provincial network when the network starts with `GR:provincial:`. Note that `ΕΠ` provincial refs are ignored.
* `GR` - **Greece** when operator in `Αττική Οδός`, `Αυτοκινητόδρομος Αιγαίου`,`Εγνατία Οδός`, `Κεντρική Οδός`, `Μορέας`, `Νέα Οδός`, `Ολυμπία Οδός`
* `HU:national` - **Hungary** national routes, pass-thru OpenStreetMap network
* `ID:national` - Indonesia, pass-thru OpenStreetMap network
* `IN:MDR` - **India** network.startswith(`IN:MDR`) or ref == `MDR`
* `IN:NH` - **India** national highway, when network starts with `IN:NH`  or ref starts with `NH` or `ORR`.
* `IN:SH` - **India** state highway, when network starts with `IN:SH` or ref starts with `SH`.
* `IR:national` - **Iran** national road network (from `ir:national`)
* `IR:freeway` - **Iran** freeway network (upstream `ir:freeways` values are normalized)
* `IT:A-road` - **Italy** A-roads passthru from OpenStreetMap network value
* `IT:B-road` - **Italy** B-roads passthru from OpenStreetMap network value
* `IT` - **Italy** when operator in "Autostrade per l` Italia S.P.A.", `Autocamionale della Cisa S.P.A.`, `Autostrada dei Fiori S.P.A.`, `Autostrade Centropadane`, `S.A.L.T.`, `SATAP`
* `JP:expressway` - **Japan** expressways when ref starts with `C` or `E`.
* `JP:national` - **Japan** national routes when name starts with `国道` ends with `号`.
* `JP:prefectural` - **Japan** regional routes when network starts with `JP:prefectural:`
* `JP` - **Japan** when operator in `東日本高速道路`
* `KR:expressway` - **South Korea** expressways - gosokdoro (ncat=`고속도로`)
* `KR:local` - **South Korea** local highways - jibangdo (ncat=`지방도`)
* `KR:metropolitan` - **South Korea** for metropolitan city roads - gwangyeoksido (ncat=`광역시도로`) and special city (Seoul) roads - teukbyeolsido (ncat=`특별시도`)
* `KR:national` - **South Korea** for national roads - gukdo (ncat=`국도`)
* `KZ:national` - **Kazakhstan** national routes
* `KZ:regional` - **Kazakhstan** regional routes
* `LA:national` - **Laos** national routes when network == `LO:network` to correct for bad country code
* `MX:AGU` - **Aguascalientes** region in Mexico when prefix starts with `AGS`
* `MX:BCN` - **Baja California Norte** region in Mexico
* `MX:BCS` - **Baja California Sur** region in Mexico when prefix starts with `BC` or `BCS`
* `MX:CAM` - **Campeche** region in Mexico when prefix starts with `CAM`
* `MX:CHH` - **Chihuahua** region in Mexico when prefix starts with `CHIH`
* `MX:CHP` - **Chiapas** region in Mexico when prefix starts with `CHIS`
* `MX:CMX:EXT` - road in **Mexico City** when prefix is `EXT`
* `MX:CMX:INT` - interior ring road in **Mexico City** when prefix is `INT`
* `MX:COA` - **Coahuila** region in Mexico when prefix starts with `COAH`
* `MX:COL` - **Colima** region in Mexico when prefix starts with `COL`
* `MX:DUR` - **Durango** region in Mexico when prefix starts with `DGO`
* `MX:GRO` - **Guerrero** region in Mexico when prefix starts with `GRO`
* `MX:GUA` - **Guanajuato** region in Mexico when prefix starts with `GTO`
* `MX:HID` - **Hidalgo** region in Mexico when prefix starts with `HGO`
* `MX:JAL` - **Jalisco** region in Mexico when prefix starts with `JAL`
* `MX:MEX` - **Mexican** region in Mexico national roads when prefix starts with `MEX`
* `MX:MIC` - **Michoacán** region in Mexico when prefix starts with `MICH`
* `MX:MOR` - **Morelos** region in Mexico when prefix starts with `MOR`
* `MX:NAY` - **Nayarit** region in Mexico when prefix starts with `NAY`
* `MX:NLE` - **Nuevo León** region in Mexico when prefix starts with `NL`
* `MX:OAX` - **Oaxaca** region in Mexico when prefix starts with `OAX`
* `MX:PUE` - **Puebla** region in Mexico when prefix starts with `PUE`
* `MX:QUE` - **Querétaro** region in Mexico when prefix starts with `QRO`
* `MX:ROO` - **Quintana Roo** region in Mexico when prefix starts with `ROO` or ref.upper().startswith(`Q. ROO`)
* `MX:SIN` - **Sinaloa** region in Mexico when prefix starts with `SIN`
* `MX:SLP` - **San Luis Potosí** region in Mexico when prefix starts with `SLP`
* `MX:SON` - **Sonora** region in Mexico when prefix starts with `SON`
* `MX:TAB` - **Tabasco** region in Mexico when prefix starts with `TAB`
* `MX:TAM` - **Tamaulipas** region in Mexico when prefix starts with `TAM`
* `MX:VER` - **Veracruz** region in Mexico when prefix starts with `VER`
* `MX:YUC` - **Yucatán** region in Mexico when prefix starts with `YUC`
* `MX:ZAC` - **Zacatecas** region in Mexico when prefix starts with `ZAC`
* `MY:expressway` - **Malaysia** when prefix is E
* `MY:federal` - **Malaysia** when prefix is FT or none
* `MY:JHR` - **Johor** region in Malaysia when prefix starts with `J`
* `MY:KDH` - **Kedah** region in Malaysia when prefix starts with `K`
* `MY:KTN` - **Kelantan** region in Malaysia when prefix starts with `D`
* `MY:MLK` - **Malacca** region in Malaysia when prefix starts with `M`
* `MY:NSN` - **Negiri Sembilan** region in Malaysia when prefix starts with `N`
* `MY:PHG` - **Pahang** region in Malaysia when prefix starts with `C`
* `MY:PLS` - **Perlis** region in Malaysia when prefix starts with `R`
* `MY:PNG` - **Penang** region in Malaysia when prefix starts with `P`
* `MY:PRK` - **Perak** region in Malaysia when prefix starts with `A`
* `MY:SBH` - **Sabah** region in Malaysia when prefix starts with `SA`
* `MY:SGR:municipal` - **Selangor** municipal in Malaysia when prefix == `MBSA` (but strip ref prefix to BSA#)
* `MY:SGR` - **Selangor** region in Malaysia when prefix starts with `B`
* `MY:SWK` - **Sarawak** region in Malaysia when prefix starts with `Q`
* `MY:TRG` - **Terengganu** region in Malaysia when prefix starts with `T`
* `NL:A-road` - **Netherlands** pass-thru from OpenStreetMap
* `NL:N-road` - **Netherlands** pass-thru from OpenStreetMap
* `NO:fylkesvei` - **Norway** when network.lower().startswith(`no:fylkesvei`) or `NO:Fylkesvei` or when prefix == `Fv`
* `NO:oslo:ring` - **Norway** when prefix == `Ring`
* `NO:riksvei` - **Norway** when network.lower().startswith(`no:riksvei`) or `NO:Riksvei` or prefix == `Rv`
* `NZ:SH` - **New Zealand** state highway
* `NZ:SR` - **New Zealand** state route
* `PE:AM` - **Amazonas** region in Peru, when ref prefix is AM
* `PE:AN` - **Ancash** region in Peru, when ref prefix is AN
* `PE:AP` - **Apurímac** region in Peru, when ref prefix is AP
* `PE:AR` - **Arequipa** region in Peru, when ref prefix is AR
* `PE:AY` - **Ayacucho** region in Peru, when ref prefix is AY
* `PE:CA` - **Cajamarca** region in Peru, when ref prefix is CA
* `PE:CU` - **Cusco** region in Peru, when ref prefix is CU
* `PE:HU` - **Huánuco** region in Peru, when ref prefix is HU
* `PE:HV` - **Huancavelica** region in Peru, when ref prefix is HV
* `PE:IC` - **Ica** region in Peru, when ref prefix is IC
* `PE:JU` - **Junín** region in Peru, when ref prefix is JU
* `PE:LA` - **Lambayeque** region in Peru, when ref prefix is LA
* `PE:LI` - **La Libertad** region in Peru, when ref prefix is LI
* `PE:LM` - **Lima (including Callao)** region in Peru, when ref prefix is LM
* `PE:LO` - **Loreto** region in Peru, when ref prefix is LO
* `PE:MD` - **Madre de Dios** region in Peru, when ref prefix is MD
* `PE:MO` - **Moquegua** region in Peru, when ref prefix is MO
* `PE:PA` - **Pasco** region in Peru, when ref prefix is PA
* `PE:PE` - **Peru federal routes** when prefix == `PE`
* `PE:PI` - **Piura** region in Peru, when ref prefix is PI
* `PE:PU` - **Puno** region in Peru, when ref prefix is PU
* `PE:SM` - **San Martín** region in Peru, when ref prefix is SM
* `PE:TA` - **Tacna** region in Peru, when ref prefix is TA
* `PE:TU` - **Tumbes** region in Peru, when ref prefix is TU
* `PE:UC` - **Ucayali** region in Peru, when ref prefix is UC
* `PH:NHN` - **Philippines** national highway network (normalized from `PH:nhn`)
* `PK` - **Pakistan** when operator is `Hyderabad Metropolitan Development Authority`
* `PL:expressway` - **Poland** when network == `PL:expressways` or when ref starts with `S`
* `PL:motorway` - **Poland** when network == `PL:motorways` or ref starts with `A`
* `PL:national` - **Poland** normalized from `pl:national`
* `PL:regional` - **Poland** normalized from `pl:regional`
* `PT:express` - **Portugal** when prefix starts `VE`
* `PT:motorway` - **Portugal** when prefix starts `A`
* `PT:municipal` - **Portugal** when prefix starts `EM`
* `PT:national` - **Portugal** when prefix starts `EN`
* `PT:primary` - **Portugal** when prefix starts `IP`
* `PT:rapid` - **Portugal** when prefix starts `VR`
* `PT:regional` - **Portugal** when prefix starts `ER`
* `PT:secondary` - **Portugal** when prefix starts `IC`
* `PT` - **Portugal** when operator in `Euroscut`
* `RO:county` - **Romania** when ref prefixed with `DJ`
* `RO:local` - **Romania** when ref prefixed with `DC`
* `RO:motorway` - **Romania** when ref prefixed with `A`
* `RO:national` - **Romania** when ref prefixed with `DN`
* `RU:national` - **Russia** and ref if prefix in (u`М`, `M`):  # cyrillic M & latin M!
* `RU:regional` - **Russia** when ref prefixed with cyrillic `А` or latin `A` prefixed with cyrillic `Р` or latin `P`
* `SG:expressway` - **Singapore** for prefixes including `AYE` (Ayer Rajah Expressway), `BKE` (Bukit Timah Expressway), `CTE` (Central Expressway), `ECP` (East Coast Parkway), `KJE` (Kranji Expressway), `KPE` (Kallang-Paya Lebar Expressway), `MCE` (Marina Coastal Expressway), `PIE` (Pan Island Expressway), `SLE` (Seletar Expressway), `TPE` (Tampines Expressway), 
* `TR:highway` - **Turkey** State Highway System roads prefixed with `D`
* `TR:motorway` - **Turkey** Otoyol roads prefixed with `O`
* `TR:provincial` - **Turkey** when ref in (`D010`, `D100`, `D200`, `D300`, `D400`,`D550`, `D650`, `D750`, `D850`, `D950`)
* `UA:international` - **Ukraine** when ref prefixed with cyrillic `M` or latin `M`
* `UA:national` - **Ukraine** when ref prefixed with cyrillic `Н` or latin `H`
* `UA:regional` - **Ukraine** when ref prefixed with cyrillic `Р` or latin `P`, see also `UA:regional-yellow`
* `UA:territorial` - ****Ukraine**** when ref prefixed with cyrillic `Т` or latin `T`
* `US:AK` - **Alaska** region in United States, pass-thru OSM network value
* `US:AL` - **Alabama** region in United States, pass-thru OSM network value
* `US:AR` - **Arkansas** region in United States, pass-thru OSM network value
* `US:AZ` - **Arizona** region in United States, pass-thru OSM network value
* `US:BIA` - **Bureau of **India**n Affairs** routes in United States, not widely populated OSM value
* `US:BLM` - **Bureau of Land Management** routes in United States, not widely populated OSM value
* `US:CA` - **California** region in United States, pass-thru OSM network value
* `US:CO` - **Colorado** region in United States, pass-thru OSM network value
* `US:CT` - **Connecticut** region in United States, pass-thru OSM network value
* `US:DC` - **District of Columbia** region in United States, pass-thru OSM network value
* `US:DE` - **Deleware** region in United States, pass-thru OSM network value
* `US:FL` - **Florida** region in United States, pass-thru OSM network value
* `US:FSH` - **U.S. Forest Service Highway** in United States, pass-thru OSM network value
* `US:FSR` - **U.S. Forest Service Road** in United States, pass-thru OSM network value
* `US:GA` - **Georgia** region in United States, pass-thru OSM network value
* `US:HI` - **Hawaii** region in United States, pass-thru OSM network value
* `US:I:Alternate` - **Interstate alternate** route in United States, based on OSM network value + modifier tag
* `US:I:Business` - **Interstate business** alternate in United States, based on OSM network value + modifier tag
* `US:I:Bypass` - **Interstate bypass** alternate in United States, based on OSM network value + modifier tag
* `US:I:Connector` - **Interstate connector** alternate in United States, based on OSM network value + modifier tag
* `US:I:Historic` - **Interstate historic** alternate in United States, based on OSM network value + modifier tag
* `US:I:Scenic` - **Interstate scenic** alternate in United States, based on OSM network value + modifier tag
* `US:I:Spur` - **Interstate spur** alternate in United States, based on OSM network value + modifier tag
* `US:I:Toll` - **Interstate toll** alternate in United States, based on OSM network value + modifier tag
* `US:I:Truck` - **Interstate truck** alternate in United States, based on OSM network value + modifier tag
* `US:I` - **Interstate** route in United States, pass-thru OSM network value
* `US:IA` - **Iowa** region in United States, pass-thru OSM network value
* `US:ID` - **Idaho** region in United States, pass-thru OSM network value
* `US:IL` - **Illinois** region in United States, pass-thru OSM network value
* `US:IN` - ****India**na** region in United States, pass-thru OSM network value
* `US:KS` - **Kansas** region in United States, pass-thru OSM network value
* `US:KY` - **Kentucky** region in United States, pass-thru OSM network value
* `US:LA` - **Louisiana** region in United States, pass-thru OSM network value
* `US:MA` - **Massachuesets** region in United States, pass-thru OSM network value
* `US:MD` - **Maryland** region in United States, pass-thru OSM network value
* `US:ME` - **Maine** region in United States, pass-thru OSM network value
* `US:MI` - **Michigan** region in United States, pass-thru OSM network value
* `US:MN` - **Minnesotta** region in United States, pass-thru OSM network value
* `US:MO` - **Missouri** region in United States, pass-thru OSM network value
* `US:MS` - **Mississippi** region in United States, pass-thru OSM network value
* `US:MT` - **Montana** region in United States, pass-thru OSM network value
* `US:NC` - **North Carolina** region in United States, pass-thru OSM network value
* `US:ND` - **North Dakota** region in United States, pass-thru OSM network value
* `US:NE` - **Nebraska** region in United States, pass-thru OSM network value
* `US:NH` - **New Hampshire** region in United States, pass-thru OSM network value
* `US:NJ` - **New Jersey** region in United States, pass-thru OSM network value
* `US:NM` - **New Mexico** region in United States, pass-thru OSM network value
* `US:NV` - **Nevada** region in United States, pass-thru OSM network value
* `US:NY` - **New York** region in United States, pass-thru OSM network value
* `US:OH` - **Ohio** region in United States, pass-thru OSM network value
* `US:OK` - **Oklahoma** region in United States, pass-thru OSM network value
* `US:OR` - **Oregon** region in United States, pass-thru OSM network value
* `US:PA` - **Pennsylvania** region in United States, pass-thru OSM network value
* `US:RI` - **Rhode Island** region in United States, pass-thru OSM network value
* `US:SC` - **South Carolina** region in United States, pass-thru OSM network value
* `US:SD` - **South Dakota** region in United States, pass-thru OSM network value
* `US:TN` - **Tennessee** region in United States, pass-thru OSM network value
* `US:TX` - **Texas** region in United States, pass-thru OSM network value
* `US:US:Alternate` - **U.S. Federal alternate** route in United States, based on OSM network value + modifier tag
* `US:US:Business` - **U.S. Federal business** alternate in United States, based on OSM network value + modifier tag
* `US:US:Bypass` - **U.S. Federal bypass** alternate in United States, based on OSM network value + modifier tag
* `US:US:Connector` - **U.S. Federal connector** alternate in United States, based on OSM network value + modifier tag
* `US:US:Historic` - **U.S. Federal historic** alternate in United States, based on OSM network value + modifier tag
* `US:US:Scenic` - **U.S. Federal scenic** alternate in United States, based on OSM network value + modifier tag
* `US:US:Spur` - **U.S. Federal spur** alternate in United States, based on OSM network value + modifier tag
* `US:US:Toll` - **U.S. Federal toll** alternate in United States, based on OSM network value + modifier tag
* `US:US:Truck` - **U.S. Federal truck** alternate in United States, based on OSM network value + modifier tag
* `US:US` - **U.S. Federal** route in United States, pass-thru OSM network value
* `US:UT` - **Utah** region in United States, pass-thru OSM network value
* `US:VA` - **Virginia** region in United States, pass-thru OSM network value
* `US:VT` - **Vermont** region in United States, pass-thru OSM network value
* `US:WA` - **Washington** region in United States, pass-thru OSM network value
* `US:WI` - **Wisconsin** region in United States, pass-thru OSM network value
* `US:WV` - **West Virginia** region in United States, pass-thru OSM network value
* `US:WY` - **Wyoming** region in United States, pass-thru OSM network value
* `VN:expressway` - **Vietnam** (normalized `VN:expressway`) or ref prefixed with `CT`
* `VN:national` - **Vietnam** when name.startswith(u`Quốc lộ`) or ref prefixed with `QL`
* `VN:provincial` - **Vietnam** when name.startswith(u`Tỉnh lộ`) or when ref prefixed with `ĐT` or `DT` or (normalized `VN:TL`) or ref prefixed with `TL`
* `VN:road` - **Vietnam** for all other Vietnamese roads that have a ref
* `ZA:kruger` - **South Africa** when ref prefixed with `H`
* `ZA:metropolitan` - **South Africa** when ref prefixed with `M`
* `ZA:national` - **South Africa** when ref prefixed with `N`
* `ZA:provincial` - **South Africa** when ref prefixed with `R` and 2 chars
* `ZA:regional` - **South Africa** when ref prefixed with `R` and 3 chars
* `ZA:S-road` - **South Africa** when ref prefixed with `S`