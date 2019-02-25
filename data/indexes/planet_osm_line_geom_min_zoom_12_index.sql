CREATE INDEX
  planet_osm_line_geom_min_zoom_12_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom < 12 OR
    mz_landuse_min_zoom < 12 OR
    mz_road_level < 12 OR
    mz_transit_level < 12 OR
    mz_water_min_zoom < 12;
