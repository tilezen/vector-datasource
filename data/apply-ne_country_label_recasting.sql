-- Recasts a few rows in the ne_10m_admin_0_countries_iso and ne_10m_admin_0_countries_tlc
-- tables to either show or hide certain labels


-- Akrotiri Sovereign Base Area
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159320741;

-- Aland
update ne_10m_admin_0_countries_iso set fclass_iso = 'unrecognized' where ne_id = 1159320621;
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159320621;

-- Antarctica
update ne_10m_admin_0_countries_iso set fclass_iso = 'unrecognized' where ne_id = 1159320335;
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159320335;

-- Ashmore and Cartier Islands
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159320353;

-- Clipperton Island
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159320635;

-- Coral Sea Islands
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159320359;

-- Dhekelia Cantonment
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159320709;

-- Gaza Strip
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'Admin-0 country' where ne_id = 1159320901;

-- Palestine
update ne_10m_admin_0_countries_iso set fclass_iso = 'unrecognized' where ne_id = 1159320899;

-- Somaliland
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159321259;

-- Turkish Republic of Northern Cyprus
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'unrecognized' where ne_id = 1159320531;

-- West Bank
update ne_10m_admin_0_countries_tlc set fclass_tlc = 'Admin-0 country' where ne_id = 1159320903;
