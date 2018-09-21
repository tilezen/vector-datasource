# Roads layer network values

Any road with `shield_text` will include a `network` property with a value like `AA:bcdef` where `AA` is a 2-character country code, followed by a `:` separator, and `bcdef` category value which either indicates the "region" (state or province) or "level" of the road network. There are exceptions to this for trans-national networks like `e-road`. In some cases, like the United States and Canada an additional _modifier_ to appended to indicate `Truck` and other alternate routes, or further network disambiguation.

## OpenStreetMap ETL logic

Some countries without network tags but with ref values with `;` and `/` and other separators, including: **Switzerland**, **Greece**, **India**, **Italy**, **Japan**, **Russia**, **Turkey**, **Vietnam**, and **South Africa**.

When we don't see network we backfill based on common road operators values. Network values always replace plural `??:roads` with singular `??:road`.

When a network value can't be determined from the upstream data source we calculate where the road is located and provide the relevant 2-char country code as the network value. See table below for mapping of country codes to country names.

#### Network value include:

_If not specified the network is from the raw OpenStreetMap network value._

* `AM:AM` - **Armenia**
* `AR:national` - **Argentina** when ref starts with `RN`
* `AR:provincial` - **Argentina** when ref starts with `RP`
* `AsianHighway` - **Asian Highway** across multiple countries when network is `AH` or ref starts with `AH` 
* `AT:A-road` - **Austria**
* `AU:A-road` - **Australia** when ref starts with `A`
* `AU:B-road` - **Australia** when ref starts with `B`
* `AU:C-road` - **Australia** when ref starts with `C`
* `AU:M-road` - **Australia** when ref starts with `M`
* `AU:Metro-road` - **Australia** when ref starts with `MR`
* `AU:N-route` - **Australia** when ref starts with `N`
* `AU:R-route` - **Australia** when ref starts with `R`
* `AU:S-route` - **Australia** when ref starts with `S`
* `AU:T-drive` - **Australia** when ref starts with `T`
* `BE:A-road` - **Belgium**
* `BE:N-road` - **Belgium**
* `BE:R-road` - **Belgium**
* `BR:AC` - **Acre** region in Brazil when ref starts with `AC`
* `BR:AL` - **Alagoas** region in Brazil when ref starts with `AL`
* `BR:AM` - **Amazonas** region in Brazil when ref starts with `AM`
* `BR:AP` - **Amapá** region in Brazil when ref starts with `AP`
* `BR:BA` - **Bahia** region in Brazil when ref starts with `BA`
* `BR:BR` - **Federal routes in Brazil** and when ref starts with `BR`
* `BR:CE` - **Ceará** region in Brazil when ref starts with `CE`
* `BR:DF` - **Distrito Federal** region in Brazil when ref starts with `DF`
* `BR:ES` - **Espírito Santo** region in Brazil when ref starts with `ES`
* `BR:GO` - **Goiás** region in Brazil when ref starts with `GO`
* `BR:MA` - **Maranhão** region in Brazil when ref starts with `MA`
* `BR:MG:local` - **Minas Gerais** region in Brazil local roads when ref starts with `MG` or `LMG`
* `BR:MG` - **Minas Gerais** region in Brazil state roads when ref starts with `AMG`, `CMG`, or `MGC`
* `BR:MS` - **Mato Grosso do Sul** region in Brazil when ref starts with `MS`
* `BR:MT` - **Mato Grosso** region in Brazil when ref starts with `MT`
* `BR:PA` - **Pará** region in Brazil when ref starts with `PA`
* `BR:PB` - **Paraíba** region in Brazil when ref starts with `PB`
* `BR:PE` - **Pernambuco** region in Brazil when ref starts with `PE`
* `BR:PI` - **Piauí** region in Brazil when ref starts with `PI`
* `BR:PR` - **connecting roads in Paraná** region in Brazil when ref starts with `PR` or `PRC`
* `BR:PR` - **Paraná** region in Brazil when ref starts with `PR`
* `BR:RJ` - **Rio de Janeiro** region in Brazil when ref starts with `RJ`
* `BR:RN` - **Rio Grande do Norte** region in Brazil when ref starts with `RN`
* `BR:RO` - **Rondônia** region in Brazil when ref starts with `RO`
* `BR:RR` - **Roraima** region in Brazil when ref starts with `RR`
* `BR:RS` - **Rio Grande do Sul** region in Brazil state roads when ref starts with `RS`, `ERS`, `VRS`, or `RSC`
* `BR:SC` - **Santa Catarina** region in Brazil when ref starts with `SC`
* `BR:SE` - **Sergipe** region in Brazil when ref starts with `SE`
* `BR:SP:PLN` - **municipal roads in Paulínia** region in Brazil, with ref starts with `PLN`
* `BR:SP:SCA` - **municipal roads in São Carlos** region in Brazil when ref starts with `SCA`
* `BR:SP` - **São Paulo** region in Brazil and access roads ref prefix of `SPA`
* `BR:TO` - **Tocantins** region in Brazil when ref starts with `TO`
* `BR:Trans-Amazonian` - **Trans-Amazonian** route in Brazil when network is `BR` and ref is `BR-230`
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
* `CA:NB2` - **New Brunswich** region in Canada when network starts with `CA:NB` ref is >= 100
* `CA:NB3` - **New Brunswich** region in Canada network starts with `CA:NB` and ref >= 200
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
* `CA:transcanada` - **Canada Transcanada** highway when `nat_name` is `trans-canada highway`
* `CA:yellowhead` - **Canada Transcanda variant**
* `CA:YT` - **Yukon Territory** region in Canada
* `CD:RRIG` - **Democratic Republic of the Congo** if network `CD:rrig`
* `CH:motorway` - **Switzerland** when ref starts with `A`
* `CH:national` - **Switzerland** normalized `ch:national` and when `CH:Nationalstrasse`
* `CH:regional` - **Switzerland** normalized `ch:regional`
* `CL:national` - **Chile**
* `CL:regional` - **Chile**
* `CN:expressway:regional` - **China** when ref starts with `S` and normalized from `CN-expressways-regional`
* `CN:expressway` - **China** when ref starts with `G` and normalized from `CN-expressways`
* `CN:JX` - **Jinxia** region in China, when ref starts with `X` or network is `JX-roads`
* `CN:road` - **China** normalization of `CN-roads`
* `CZ:national` - **Czechia** normalization of `cz:national`
* `CZ:regional` - **Czechia** normalization of `cz:regional`
* `DE:BAB` - **Germany** federal autobahn when network is `BAB` or ref starts with `A`
* `DE:BS` - **Germany** federal roads when ref starts with `B`
* `DE:Hamburg:Ring` - **Hamburg** region ring road in Germany  when prefix `Ring`
* `DE:KS` - **Germany** county routes when network `Kreisstra\xc3\x9fen Hildesheim` or ref starts with `K`
* `DE:LS` - **Germany** county routes when network `Landesstra\xc3\x9fen NRW` or ref starts with `L`
* `DE:STS` - **Germany** when ref starts with `S` or `St`
* `DE` - **Germany** when operator in `autobahnplus A8 GmbH`, `Bundesrepublik Deutschland`, `Via Solutions Südwest`, `The Danish Road Directorate`
* `DK:national` - **Denmark**, normalization of `dk:national`
* `e-road` - **European E-Road** when ref starts with `E` or network is `e-road` already
* `ES:A-road` - **Spain** when ref starts with `A` or `AP` and ref digits are 1 or 2 in length.
* `ES:autonoma` - **Spain** when ref starts with `ARA`, `A`, `CA`, `CL`, `CM`, `C`, `EX`, `AG`, `M`, `R`, `Ma`, `Me`, `ML`, `RC`, `RM`, `V`, `CV`, `Cv`
* `ES:city` - **Spain** when ref starts with `AI`, `IA`, `CT`, `CS`, `CU`, `CHE`, `EL`, `FE`, `GJ`, `H`,  `VM`, `J`, `LN`, `LL`, `LO`, `ME`, `E`, `MU`, `O`, `PA`, `PR`, `PI`, `CHMS`, `PT`, `SL`, `S`, `SC`, `SI`, `VG`, `EI`, 
* `ES:N-road` - **Spain** when ref starts with `N`
* `ES:province` - **Spain** when ref starts with `AC`, `DP`, `AB`, `F`, `AL`, `AE`, `AS`, `AV`, `BA`, `B`,  , `BP`, `BV`, `BI`, `BU`, `CC`, `CO`, `CR`, `GIP`, `GIV`, `GI`, `GR`, `GU`, `HU`, `JA`, `JV`, `LR`, `LE`, `L`,  , `LP`, `LV`, `LU`, `MP`, `MA`, `NA`, `OU`, `P`, `PP`, `EP`, `PO`, `DSA`, `SA`, `NI`, `SG`, `SE`, `SO`, `TP`, `TV`, `TE`, `TO`, `VA`, `ZA`, `CP`, `Z`, `PM`, `PMV`
* `ES` - **Spain** when operator in `Administración central`, `Departamento de Infraestructuras Viarias y Movilidad`
* `FR:A-road` - **France**
* `FR:D-road` - **France** when ref starts with `^FR:[0-9]+:([A-Z]+)-road$` to strip department numbers or `N`
* `FR:N-road` - **France** when ref starts with `RN` or `RNIL`
* `FR` - **France** when operator in `APRR`, `ASF`, `Autoroutes du Sud de la France`, `DIRIF`, `DIRNO`
* `GA:L-road` - **Gabon** when ref starts `L`
* `GA:national` - **Gabon** when ref starts with `N` or `RN`
* `GB:A-road-green` - **United Kingdom** when highway is `trunk` and ref starts with `A`
* `GB:A-road-white` - **United Kingdom** when highway is `primary` and ref starts with `A`
* `GB:B-road` - **United Kingdom** when highway is `secondary` and ref starts with `B`
* `GB:M-road` - **United Kingdom** when highway is `motorway` and ref starts or ends with `M`
* `GB` - **United Kingdom** when operator in `Highways England`, `Midland Expressway Ltd`, `Transport for Scotland`, `Transport Scotland`, `Welsh Government`
* `GR:motorway` - **Greece** when ref starts with Greek `Α` or Latin `A`
* `GR:national` - **Greece** when ref starts with Greek `ΕΟ` or Latin `EO`
* `GR:provincial` - **Greece** generically for any provincial network when the network starts with `GR:provincial:`. Note that `ΕΠ` provincial refs are ignored.
* `GR` - **Greece** when operator in `Αττική Οδός`, `Αυτοκινητόδρομος Αιγαίου`,`Εγνατία Οδός`, `Κεντρική Οδός`, `Μορέας`, `Νέα Οδός`, `Ολυμπία Οδός`
* `HU:national` - **Hungary** national routes
* `ID:national` - Indonesia
* `IN:MDR` - **India** network starts with `IN:MDR` or ref is `MDR`
* `IN:NH` - **India** national highway, when network starts with `IN:NH` or ref starts with `NH` or `ORR`
* `IN:SH` - **India** state highway, when network starts with `IN:SH` or ref starts with `SH`
* `IR:national` - **Iran** national road network normalized from `ir:national`
* `IR:freeway` - **Iran** freeway network normalized from `ir:freeways`
* `IT:A-road` - **Italy** A-roads
* `IT:B-road` - **Italy** B-roads
* `IT` - **Italy** when operator in `Autostrade per l' Italia S.P.A.`, `Autocamionale della Cisa S.P.A.`, `Autostrada dei Fiori S.P.A.`, `Autostrade Centropadane`, `S.A.L.T.`, `SATAP`
* `JP:expressway` - **Japan** expressways when ref starts with `C` or `E`.
* `JP:national` - **Japan** national routes when name starts with `国道` and ends with `号`.
* `JP:prefectural` - **Japan** regional routes when network starts with `JP:prefectural:` to remove prefecture detail
* `JP` - **Japan** when operator in `東日本高速道路`
* `KR:expressway` - **South Korea** expressways (gosokdoro) when ncat is `고속도로`
* `KR:local` - **South Korea** local highways (jibangdo) when ncat is `지방도`
* `KR:metropolitan` - **South Korea** for metropolitan city roads (gwangyeoksido) when ncat is `광역시도로` and special city (Seoul) roads - (teukbyeolsido) when ncat is `특별시도`
* `KR:national` - **South Korea** for national roads (gukdo) when ncat is `국도`
* `KZ:national` - **Kazakhstan** national routes
* `KZ:regional` - **Kazakhstan** regional routes
* `LA:national` - **Laos** national routes when network == `LO:network` to correct for bad country code
* `MX:AGU` - **Aguascalientes** region in Mexico when ref starts with `AGS`
* `MX:BCN` - **Baja California Norte** region in Mexico when ref starts with `BCN`
* `MX:BCS` - **Baja California Sur** region in Mexico when ref starts with `BC` or `BCS`
* `MX:CAM` - **Campeche** region in Mexico when ref starts with `CAM`
* `MX:CHH` - **Chihuahua** region in Mexico when ref starts with `CHIH`
* `MX:CHP` - **Chiapas** region in Mexico when ref starts with `CHIS`
* `MX:CMX:EXT` - road in **Mexico City** when ref starts with `EXT`
* `MX:CMX:INT` - interior ring road in **Mexico City** when prefix is `INT`
* `MX:COA` - **Coahuila** region in Mexico when ref starts with `COAH`
* `MX:COL` - **Colima** region in Mexico when ref starts with `COL`
* `MX:DUR` - **Durango** region in Mexico when ref starts with `DGO`
* `MX:GRO` - **Guerrero** region in Mexico when ref starts with `GRO`
* `MX:GUA` - **Guanajuato** region in Mexico when ref starts with `GTO`
* `MX:HID` - **Hidalgo** region in Mexico when ref starts with `HGO`
* `MX:JAL` - **Jalisco** region in Mexico when ref starts with `JAL`
* `MX:MEX` - **Mexican** region in Mexico national roads when ref starts with `MEX`
* `MX:MIC` - **Michoacán** region in Mexico when ref starts with `MICH`
* `MX:MOR` - **Morelos** region in Mexico when ref starts with `MOR`
* `MX:NAY` - **Nayarit** region in Mexico when ref starts with `NAY`
* `MX:NLE` - **Nuevo León** region in Mexico when ref starts with `NL`
* `MX:OAX` - **Oaxaca** region in Mexico when ref starts with `OAX`
* `MX:PUE` - **Puebla** region in Mexico when ref starts with `PUE`
* `MX:QUE` - **Querétaro** region in Mexico when ref starts with `QRO`
* `MX:ROO` - **Quintana Roo** region in Mexico when ref starts with `ROO` or ref.upper().startswith(`Q. ROO`)
* `MX:SIN` - **Sinaloa** region in Mexico when ref starts with `SIN`
* `MX:SLP` - **San Luis Potosí** region in Mexico when ref starts with `SLP`
* `MX:SON` - **Sonora** region in Mexico when ref starts with `SON`
* `MX:TAB` - **Tabasco** region in Mexico when ref starts with `TAB`
* `MX:TAM` - **Tamaulipas** region in Mexico when ref starts with `TAM`
* `MX:VER` - **Veracruz** region in Mexico when ref starts with `VER`
* `MX:YUC` - **Yucatán** region in Mexico when ref starts with `YUC`
* `MX:ZAC` - **Zacatecas** region in Mexico when ref starts with `ZAC`
* `MY:expressway` - **Malaysia** when ref starts with `E`
* `MY:federal` - **Malaysia** when ref starts with starts with `FT` or is missing
* `MY:JHR` - **Johor** region in Malaysia when ref starts with `J`
* `MY:KDH` - **Kedah** region in Malaysia when ref starts with `K`
* `MY:KTN` - **Kelantan** region in Malaysia when ref starts with `D`
* `MY:MLK` - **Malacca** region in Malaysia when ref starts with `M`
* `MY:NSN` - **Negiri Sembilan** region in Malaysia when ref starts with `N`
* `MY:PHG` - **Pahang** region in Malaysia when ref starts with `C`
* `MY:PLS` - **Perlis** region in Malaysia when ref starts with `R`
* `MY:PNG` - **Penang** region in Malaysia when ref starts with `P`
* `MY:PRK` - **Perak** region in Malaysia when ref starts with `A`
* `MY:SBH` - **Sabah** region in Malaysia when ref starts with `SA`
* `MY:SGR:municipal` - **Selangor** municipal in Malaysia when ref starts with `MBSA`
* `MY:SGR` - **Selangor** region in Malaysia when ref starts with `B`
* `MY:SWK` - **Sarawak** region in Malaysia when ref starts with `Q`
* `MY:TRG` - **Terengganu** region in Malaysia when ref starts with `T`
* `NL:A-road` - **Netherlands**
* `NL:N-road` - **Netherlands**
* `NO:fylkesvei` - **Norway** when network starts with `no:fylkesvei` or `NO:Fylkesvei` or when ref starts with `Fv`
* `NO:oslo:ring` - **Norway** when ref starts with `Ring`
* `NO:riksvei` - **Norway** when network starts with `no:riksvei` or `NO:Riksvei` or when ref starts with `Rv`
* `NZ:SH` - **New Zealand**
* `NZ:SR` - **New Zealand**
* `PE:AM` - **Amazonas** region in Peru, when ref starts with `AM`
* `PE:AN` - **Ancash** region in Peru, when ref starts with `AN`
* `PE:AP` - **Apurímac** region in Peru, when ref starts with `AP`
* `PE:AR` - **Arequipa** region in Peru, when ref starts with `AR`
* `PE:AY` - **Ayacucho** region in Peru, when ref starts with `AY`
* `PE:CA` - **Cajamarca** region in Peru, when ref starts with `CA`
* `PE:CU` - **Cusco** region in Peru, when ref starts with `CU`
* `PE:HU` - **Huánuco** region in Peru, when ref starts with `HU`
* `PE:HV` - **Huancavelica** region in Peru, when ref starts with `HV`
* `PE:IC` - **Ica** region in Peru, when ref starts with `IC`
* `PE:JU` - **Junín** region in Peru, when ref starts with `JU`
* `PE:LA` - **Lambayeque** region in Peru, when ref starts with `LA`
* `PE:LI` - **La Libertad** region in Peru, when ref starts with `LI`
* `PE:LM` - **Lima (including Callao)** region in Peru, when ref starts with `LM`
* `PE:LO` - **Loreto** region in Peru, when ref starts with `LO`
* `PE:MD` - **Madre de Dios** region in Peru, when ref starts with `MD`
* `PE:MO` - **Moquegua** region in Peru, when ref starts with `MO`
* `PE:PA` - **Pasco** region in Peru, when ref starts with `PA`
* `PE:PE` - **Peru federal routes** when ref starts with `PE`
* `PE:PI` - **Piura** region in Peru, when ref starts with `PI`
* `PE:PU` - **Puno** region in Peru, when ref starts with `PU`
* `PE:SM` - **San Martín** region in Peru, when ref starts with `SM`
* `PE:TA` - **Tacna** region in Peru, when ref starts with `TA`
* `PE:TU` - **Tumbes** region in Peru, when ref starts with `TU`
* `PE:UC` - **Ucayali** region in Peru, when ref starts with `UC`
* `PH:NHN` - **Philippines** national highway network normalized from `PH:nhn`
* `PK` - **Pakistan** when operator is `Hyderabad Metropolitan Development Authority`
* `PL:expressway` - **Poland** when network is `PL:expressways` or when ref starts with `S`
* `PL:motorway` - **Poland** when network is `PL:motorways` or ref starts with `A`
* `PL:national` - **Poland** normalized from `pl:national`
* `PL:regional` - **Poland** normalized from `pl:regional`
* `PT:express` - **Portugal** when ref starts `VE`
* `PT:motorway` - **Portugal** when ref starts `A`
* `PT:municipal` - **Portugal** when ref starts `EM`
* `PT:national` - **Portugal** when ref starts `EN`
* `PT:primary` - **Portugal** when ref starts `IP`
* `PT:rapid` - **Portugal** when ref starts `VR`
* `PT:regional` - **Portugal** when ref starts `ER`
* `PT:secondary` - **Portugal** when ref starts `IC`
* `PT` - **Portugal** when operator in `Euroscut`
* `RO:county` - **Romania** when ref starts with `DJ`
* `RO:local` - **Romania** when ref starts with `DC`
* `RO:motorway` - **Romania** when ref starts with `A`
* `RO:national` - **Romania** when ref starts with `DN`
* `RU:national` - **Russia** and ref starts cyrillic `М` or latin `M`
* `RU:regional` - **Russia** when ref starts with cyrillic `А` or latin `A` or cyrillic `Р` or latin `P`
* `SG:expressway` - **Singapore** for prefixes including `AYE` (Ayer Rajah Expressway), `BKE` (Bukit Timah Expressway), `CTE` (Central Expressway), `ECP` (East Coast Parkway), `KJE` (Kranji Expressway), `KPE` (Kallang-Paya Lebar Expressway), `MCE` (Marina Coastal Expressway), `PIE` (Pan Island Expressway), `SLE` (Seletar Expressway), `TPE` (Tampines Expressway)
* `TR:highway` - **Turkey** State Highway System roads when ref starts with `D`
* `TR:motorway` - **Turkey** Otoyol roads when ref starts with `O`
* `TR:provincial` - **Turkey** when ref is `D010`, `D100`, `D200`, `D300`, `D400`,`D550`, `D650`, `D750`, `D850`, or `D950`
* `UA:international` - **Ukraine** when ref starts with cyrillic `M` or latin `M`
* `UA:national` - **Ukraine** when ref starts with cyrillic `Н` or latin `H`
* `UA:regional` - **Ukraine** when ref starts with cyrillic `Р` or latin `P`, see also `UA:regional-yellow`
* `UA:territorial` - **Ukraine** when ref starts with cyrillic `Т` or latin `T`
* `US:AK` - **Alaska** region in United States
* `US:AL` - **Alabama** region in United States
* `US:AR` - **Arkansas** region in United States
* `US:AZ` - **Arizona** region in United States
* `US:BIA` - **Bureau of Indian Affairs** routes in United States, not widely populated OSM value
* `US:BLM` - **Bureau of Land Management** routes in United States, not widely populated OSM value
* `US:CA` - **California** region in United States
* `US:CO` - **Colorado** region in United States
* `US:CT` - **Connecticut** region in United States
* `US:DC` - **District of Columbia** region in United States
* `US:DE` - **Deleware** region in United States
* `US:FL` - **Florida** region in United States
* `US:FSH` - **U.S. Forest Service Highway** in United States
* `US:FSR` - **U.S. Forest Service Road** in United States
* `US:GA` - **Georgia** region in United States
* `US:HI` - **Hawaii** region in United States
* `US:I:Alternate` - **Interstate alternate** route in United States based on network + modifier
* `US:I:Business` - **Interstate business** alternate in United States based on network + modifier
* `US:I:Bypass` - **Interstate bypass** alternate in United States based on network + modifier
* `US:I:Connector` - **Interstate connector** alternate in United States based on network + modifier
* `US:I:Historic` - **Interstate historic** alternate in United States based on network + modifier
* `US:I:Scenic` - **Interstate scenic** alternate in United States based on network + modifier
* `US:I:Spur` - **Interstate spur** alternate in United States based on network + modifier
* `US:I:Toll` - **Interstate toll** alternate in United States based on network + modifier
* `US:I:Truck` - **Interstate truck** alternate in United States based on network + modifier
* `US:I` - **Interstate** route in United States
* `US:IA` - **Iowa** region in United States
* `US:ID` - **Idaho** region in United States
* `US:IL` - **Illinois** region in United States
* `US:IN` - **Indiana** region in United States
* `US:KS` - **Kansas** region in United States
* `US:KY` - **Kentucky** region in United States
* `US:LA` - **Louisiana** region in United States
* `US:MA` - **Massachuesets** region in United States
* `US:MD` - **Maryland** region in United States
* `US:ME` - **Maine** region in United States
* `US:MI` - **Michigan** region in United States
* `US:MN` - **Minnesotta** region in United States
* `US:MO` - **Missouri** region in United States
* `US:MS` - **Mississippi** region in United States
* `US:MT` - **Montana** region in United States
* `US:NC` - **North Carolina** region in United States
* `US:ND` - **North Dakota** region in United States
* `US:NE` - **Nebraska** region in United States
* `US:NH` - **New Hampshire** region in United States
* `US:NJ` - **New Jersey** region in United States
* `US:NM` - **New Mexico** region in United States
* `US:NV` - **Nevada** region in United States
* `US:NY` - **New York** region in United States
* `US:OH` - **Ohio** region in United States
* `US:OK` - **Oklahoma** region in United States
* `US:OR` - **Oregon** region in United States
* `US:PA` - **Pennsylvania** region in United States
* `US:RI` - **Rhode Island** region in United States
* `US:SC` - **South Carolina** region in United States
* `US:SD` - **South Dakota** region in United States
* `US:TN` - **Tennessee** region in United States
* `US:TX` - **Texas** region in United States
* `US:US:Alternate` - **U.S. Federal alternate** route in United States based on network + modifier
* `US:US:Business` - **U.S. Federal business** alternate in United States based on network + modifier
* `US:US:Bypass` - **U.S. Federal bypass** alternate in United States based on network + modifier
* `US:US:Connector` - **U.S. Federal connector** alternate in United States based on network + modifier
* `US:US:Historic` - **U.S. Federal historic** alternate in United States based on network + modifier
* `US:US:Scenic` - **U.S. Federal scenic** alternate in United States based on network + modifier
* `US:US:Spur` - **U.S. Federal spur** alternate in United States based on network + modifier
* `US:US:Toll` - **U.S. Federal toll** alternate in United States based on network + modifier
* `US:US:Truck` - **U.S. Federal truck** alternate in United States based on network + modifier
* `US:US` - **U.S. Federal** route in United States
* `US:UT` - **Utah** region in United States
* `US:VA` - **Virginia** region in United States
* `US:VT` - **Vermont** region in United States
* `US:WA` - **Washington** region in United States
* `US:WI` - **Wisconsin** region in United States
* `US:WV` - **West Virginia** region in United States
* `US:WY` - **Wyoming** region in United States
* `VN:expressway` - **Vietnam** normalized from `VN:expressways` or when ref starts with `CT`
* `VN:national` - **Vietnam** when name starts with `Quốc lộ` or ref starts with `QL`
* `VN:provincial` - **Vietnam** when name starts with `Tỉnh lộ` or when ref starts with `ĐT` or `DT` or`TL` or network is `VN:TL`
* `VN:road` - **Vietnam** for all other Vietnamese roads that have a ref
* `ZA:kruger` - **South Africa** when ref starts with `H`
* `ZA:metropolitan` - **South Africa** when ref starts with `M`
* `ZA:national` - **South Africa** when ref starts with `N`
* `ZA:provincial` - **South Africa** when ref starts with `R` and ref is 2 chars
* `ZA:regional` - **South Africa** when ref starts with `R` and ref is 3 chars
* `ZA:S-road` - **South Africa** when ref starts with `S`