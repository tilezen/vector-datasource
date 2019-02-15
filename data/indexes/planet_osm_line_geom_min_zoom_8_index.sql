-- only these 2 columns are relevant in lower zoom queries
CREATE INDEX
  planet_osm_line_geom_min_zoom_8_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_landuse_min_zoom < 8 OR
    mz_transit_level < 8;
