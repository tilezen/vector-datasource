-- we look up min_label, max_label by wikidata ID.
CREATE INDEX ne_10m_admin_0_countries_wikidata_index ON ne_10m_admin_0_countries(wikidataid);
