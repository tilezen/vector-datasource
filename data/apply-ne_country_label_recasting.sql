-- Recasts a few rows in the ne_10m_admin_0_countries_iso and ne_10m_admin_0_countries_tlc
-- tables to either show or hide certain labels

-- sets featurcla to equal fclass_tlc values. We can then further modify the values while keeping the fclass intact.
-- featurecla has a shorter varchar length and needs altering first
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
update ne_10m_admin_0_countries_tlc set featurecla = 'Admin-0 country' where ne_id = 1159320901;

-- Somaliland
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159321259;

-- Turkish Republic of Northern Cyprus
update ne_10m_admin_0_countries_tlc set featurecla = 'unrecognized' where ne_id = 1159320531;

-- West Bank
update ne_10m_admin_0_countries_tlc set featurecla = 'Admin-0 country' where ne_id = 1159320903;


-- Fix Saint Helena wikidata id for this build. Remove once NE is updated
update ne_10m_admin_0_countries_iso set wikidataid = 'Q192184' where ne_id = 1159320733;
