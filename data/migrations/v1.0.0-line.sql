UPDATE planet_osm_line SET mz_label_placement = ST_PointOnSurface(way) WHERE mz_label_placement IS NULL;
