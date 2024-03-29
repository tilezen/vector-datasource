-- Recasts a few rows in the ne_10m_admin_0_countries_iso and ne_10m_admin_0_countries_tlc
-- tables to either show or hide certain labels.
-- The TLC table yields around 10 country and dependency features over ISO (including Kosovo and Taiwan),
-- which Tilezen sometimes has opinions about.


-- sets featurcla to equal fclass_tlc values. We can then further modify the values while keeping the fclass intact.
-- featurecla column has a shorter varchar length and needs altering first.
alter table ne_10m_admin_0_countries_tlc alter column featurecla type varchar;
update ne_10m_admin_0_countries_tlc set featurecla = fclass_tlc;

-- Akrotiri Sovereign Base Area
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159320741;

-- Ashmore and Cartier Islands
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159320353;

-- Clipperton Island
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159320635;

-- Coral Sea Islands
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159320359;

-- Dhekelia Cantonment
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159320709;

-- Gaza Strip
update ne_10m_admin_0_countries_tlc set featurecla = 'Admin-0 dependency' where ne_id = 1159320901;

-- Somaliland
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159321259;

-- Svalbard
update ne_10m_admin_0_countries_tlc set featurecla = 'Admin-0 dependency' where ne_id = 1159321119;

-- Turkish Republic of Northern Cyprus
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159320531;

-- West Bank
update ne_10m_admin_0_countries_tlc set featurecla = 'Admin-0 dependency' where ne_id = 1159320903;


-- Fix Saint Helena wikidata id for this build. Remove once NE is updated
update ne_10m_admin_0_countries_iso set wikidataid = 'Q192184' where ne_id = 1159320733;


-- Fixes to country labels for some languages to shorten or match local expectations

--Update Bahamas name
update ne_10m_admin_0_countries_iso set name_ru = 'Багамы' where ne_id = 1159320415;

--Update Central Africa Republic name
update ne_10m_admin_0_countries_iso set name_fr = 'Centrafrique' where ne_id = 1159320463;
update ne_10m_admin_0_countries_iso set name_zh = '中非' where ne_id = 1159320463;
update ne_10m_admin_0_countries_iso set name_zht = '中非' where ne_id = 1159320463;

--Update China name
update ne_10m_admin_0_countries_iso set name_de = 'China' where ne_id = 1159320471;
update ne_10m_admin_0_countries_iso set name_en = 'China' where ne_id = 1159320471;
update ne_10m_admin_0_countries_iso set name_fr = 'Chine' where ne_id = 1159320471;
update ne_10m_admin_0_countries_iso set name_ko = '중국' where ne_id = 1159320471;
update ne_10m_admin_0_countries_iso set name_zh = '中国' where ne_id = 1159320471;
update ne_10m_admin_0_countries_iso set name_zht = '中国' where ne_id = 1159320471;

--Update Cocos (Keeling) Island
update ne_10m_admin_0_countries_iso set name_ar = 'جزر كوكوس (كيلينغ)' where ne_id = 1159320367;
update ne_10m_admin_0_countries_iso set name_en = 'Cocos (Keeling) Islands' where ne_id = 1159320367;
update ne_10m_admin_0_countries_iso set name_es = 'Islas Cocos (Keeling)' where ne_id = 1159320367;
update ne_10m_admin_0_countries_iso set name_ja = 'ココス[キーリング]諸島' where ne_id = 1159320367;
update ne_10m_admin_0_countries_iso set name_ru = 'Кокосовые (Килинг) острова' where ne_id = 1159320367;

--Update Cyprus name
update ne_10m_admin_0_countries_iso set name_de = 'Zypern' where ne_id = 1159320533;

--Update Czechia name
update ne_10m_admin_0_countries_iso set name_en = 'Czechia' where ne_id = 1159320535;
update ne_10m_admin_0_countries_iso set name_es = 'Chequia' where ne_id = 1159320535;
update ne_10m_admin_0_countries_iso set name_zht = '捷克' where ne_id = 1159320535;

--Update Dominica name
update ne_10m_admin_0_countries_iso set name_ko = '도미니카' where ne_id = 1159320543;

--Update Falklands Islands name
update ne_10m_admin_0_countries_iso set name_en = 'Falkland Islands (Islas Malvinas)' where ne_id = 1159320711;
update ne_10m_admin_0_countries_iso set name_fr = 'Îles Malouines (Îles Falkland)' where ne_id = 1159320711;
update ne_10m_admin_0_countries_iso set name_ja = 'フォークランド諸島 (マルビナス諸島)' where ne_id = 1159320711;
update ne_10m_admin_0_countries_iso set name_ko = '포클랜드 제도 (말비나스 군도)' where ne_id = 1159320711;

--Update Israel name
update ne_10m_admin_0_countries_iso set name_ar = 'فلسطين' where ne_id = 1159320895;
update ne_10m_admin_0_countries_iso set name_id = 'Palestina' where ne_id = 1159320895;
update ne_10m_admin_0_countries_iso set name_ur = 'فلسطین' where ne_id = 1159320895;

--Update Haiti name
update ne_10m_admin_0_countries_iso set name_ru = 'Гаити' where ne_id = 1159320839;

--Update Ireland name
update ne_10m_admin_0_countries_iso set name_ar = 'أيرلندا' where ne_id = 1159320877;
update ne_10m_admin_0_countries_iso set name_pt = 'Irlanda' where ne_id = 1159320877;

--Update Kosovo name
update ne_10m_admin_0_countries_tlc set name_ja = 'コソボ' where ne_id = 1159321007;
update ne_10m_admin_0_countries_tlc set name_ru = 'Косово' where ne_id = 1159321007;

--Update Mali name
update ne_10m_admin_0_countries_iso set name_ja = 'マリ' where ne_id = 1159321063;
update ne_10m_admin_0_countries_iso set name_zht = '馬利' where ne_id = 1159321063;

--Update Moldova name
update ne_10m_admin_0_countries_iso set name_de = 'Moldawien' where ne_id = 1159321045;

--Update Myanmar name
update ne_10m_admin_0_countries_iso set name_es = 'Myanmar' where ne_id = 1159321067;

--Update North Korea name
update ne_10m_admin_0_countries_iso set name_zh = '朝鲜' where ne_id = 1159321181;
update ne_10m_admin_0_countries_iso set name_zht = '北韓' where ne_id = 1159321181;

--Update Oman name
update ne_10m_admin_0_countries_iso set name_ar = 'عمان' where ne_id = 1159321151;

--Update Saint Barthélemy name
update ne_10m_admin_0_countries_iso set name_pt = 'São Bartolomeu' where ne_id = 1159320633;
update ne_10m_admin_0_countries_iso set name_zht = '聖巴多祿繆島' where ne_id = 1159320633;

--Update Saint Helena, Ascension and Tristan da Cunha name
update ne_10m_admin_0_countries_iso set name_ar = 'سانت هيلينا، أسينسيون وتريستان دا كونها' where ne_id = 1159320733;
update ne_10m_admin_0_countries_iso set name_de = 'St. Helena, Ascension und Tristan da Cunha' where ne_id = 1159320733;
update ne_10m_admin_0_countries_iso set name_en = 'Saint Helena, Ascension and Tristan da Cunha' where ne_id = 1159320733;
update ne_10m_admin_0_countries_iso set name_es = 'Santa Elena, Ascensión y Tristán de Acuña' where ne_id = 1159320733;
update ne_10m_admin_0_countries_iso set name_fr = 'Sainte-Hélène, Ascension et Tristan da Cunha' where ne_id = 1159320733;
update ne_10m_admin_0_countries_iso set name_pt = 'Santa Helena, Ascensão e Tristão da Cunha' where ne_id = 1159320733;
update ne_10m_admin_0_countries_iso set name_ru = 'Острова Святой Елены, Вознесения и Тристан-да-Кунья' where ne_id = 1159320733;
update ne_10m_admin_0_countries_iso set name_zh= '圣赫勒拿、阿森松和特里斯坦-达库尼亚' where ne_id = 1159320733;
update ne_10m_admin_0_countries_iso set name_zht = '圣赫勒拿、阿森松和特里斯坦-达库尼亚' where ne_id = 1159320733;

--Update Saint Kitts and Nevis
update ne_10m_admin_0_countries_iso set name_zht = '圣基茨和尼维斯' where ne_id = 1159320983;

--Update South Africa name
update ne_10m_admin_0_countries_iso set name_ja = '南アフリカ' where ne_id = 1159321431;
update ne_10m_admin_0_countries_iso set name_ko = '남아프리카' where ne_id = 1159321431;

--Update South Korea name
update ne_10m_admin_0_countries_iso set name_zh = '韩国' where ne_id = 1159320985;
update ne_10m_admin_0_countries_iso set name_zht = '南韓' where ne_id = 1159320985;

--Update Taiwan name
update ne_10m_admin_0_countries_iso set name_de = 'Taiwan' where ne_id = 1159321335;
update ne_10m_admin_0_countries_iso set name_es = 'Taiwán' where ne_id = 1159321335;
update ne_10m_admin_0_countries_iso set name_ja = '台湾' where ne_id = 1159321335;
update ne_10m_admin_0_countries_iso set name_ko = '타이완' where ne_id = 1159321335;
update ne_10m_admin_0_countries_iso set name_zh = '台湾' where ne_id = 1159321335;
update ne_10m_admin_0_countries_iso set name_zht = '臺灣' where ne_id = 1159321335;

--Update Turks and Caicos Island
update ne_10m_admin_0_countries_iso set name_zht = '特克斯和凱科斯群島' where ne_id = 1159320737;

--Update United States name
update ne_10m_admin_0_countries_iso set name_en = 'United States' where ne_id = 1159321369;
