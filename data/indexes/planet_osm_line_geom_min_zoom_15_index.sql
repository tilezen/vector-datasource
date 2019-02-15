CREATE INDEX
  planet_osm_line_geom_min_zoom_15_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom < 15 OR
    mz_landuse_min_zoom < 15 OR
    mz_road_level < 15 OR
    mz_transit_level < 15 OR
    mz_water_min_zoom < 15;
