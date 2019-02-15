-- ladder the rest of the polygon queries
CREATE INDEX
  planet_osm_polygon_geom_min_zoom_9_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_boundary_min_zoom < 9 OR
    mz_building_min_zoom < 9 OR
    mz_earth_min_zoom < 9 OR
    mz_landuse_min_zoom < 9 OR
    mz_poi_min_zoom < 9 OR
    mz_transit_level < 9 OR
    mz_water_min_zoom < 9;
