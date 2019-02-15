CREATE INDEX
  planet_osm_line_geom_min_zoom_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom IS NOT NULL OR
    mz_landuse_min_zoom IS NOT NULL OR
    mz_road_level IS NOT NULL OR
    mz_transit_level IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;
